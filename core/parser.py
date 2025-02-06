from core.tokenizer import TokenType, Token, TokenSequence
from core.op import Operator, unary_op_table, binary_op_table
from core.func import Function, func_table
from core.dlm import dlm_table, Delimiter
from core.const import const_table


class ParseTree:
    def __init__(self):
        self.state = 'u'
        self.nodes = []

    def __repr__(self):
        return str(self.nodes)


class Parser:
    def parse(self, seq: TokenSequence) -> ParseTree:
        stack = []
        tree = ParseTree()

        for token in seq.tokens:
            if token.type == TokenType.NUMBER:
                self._parse_num(token, tree)
            elif token.type == TokenType.OPERATOR:
                self._parse_op(token, tree, stack)
            elif token.type == TokenType.FUNCTION:
                self._parse_func(token, tree, stack)
            elif token.type == TokenType.DELIMITER:
                self._parse_dlm(token, tree, stack)
            elif token.type == TokenType.CONSTANT:
                self._parse_const(token, tree)

        while stack:
            if type(stack[-1]) == Delimiter:
                raise ValueError(f'Delimiter not closed')

            tree.nodes.append(stack.pop())

        return tree

    def _parse_num(self, token: Token, tree: ParseTree):
        if tree.state != 'u':
            raise ValueError('Number unexpected')
        
        tree.nodes.append(float(token.value))
        tree.state = 'b'

    def _parse_op(self, token: Token, tree: ParseTree, stack: list[Token]):
        if token.value in unary_op_table and tree.state == 'u':
            op = unary_op_table[token.value]
        elif token.value in binary_op_table and tree.state == 'b':
            op = binary_op_table[token.value]
            tree.state = 'u'
        else:
            raise ValueError('Operator unexpected')
        
        while stack and (type(stack[-1]) == Function or (
            type(stack[-1]) == Operator and (
                (op.prec <= stack[-1].prec and op.assoc == 'left') or
                (op.prec < stack[-1].prec and op.assoc == 'right')
            )
        )):
            tree.nodes.append(stack.pop())

        stack.append(op)

    def _parse_func(self, token: Token, tree: ParseTree, stack: Token):
        if tree.state != 'u':
            raise ValueError('Function unexpected')
        
        stack.append(func_table[token.value])

    def _parse_dlm(self, token: Token, tree: ParseTree, stack: Token):
        if token.value in dlm_table and tree.state == 'u':
            stack.append(dlm_table[token.value])
        elif tree.state == 'b':
            while stack and type(stack[-1]) != Delimiter:
                tree.nodes.append(stack.pop())

            if not stack or stack[-1].pair != token.value:
                raise ValueError('Delimiter not opened')
            
            if stack[-1].mod:
                tree.nodes.append(stack[-1].mod)

            stack.pop()
        else:
            raise ValueError

    def _parse_const(self, token: Token, tree: ParseTree):
        if tree.state != 'u':
            raise ValueError('Constant unexpected')
        
        tree.nodes.append(const_table[token.value])
        tree.state = 'b'