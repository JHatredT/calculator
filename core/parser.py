from core.const import const_table
from core.context import ParserContext
from core.func import Function, func_table
from core.op import Operator, unary_op_table, binary_op_table


class Parser:
    def parse(self, expr: str) -> float:
        context = ParserContext(0, 'unary', [], [])

        while context.ptr < len(expr):
            char = expr[context.ptr]

            if char.isdigit() or char == '.':
                self._parse_num(expr, context)
            elif char in const_table:
                context.output.append(const_table[char])
                context.state = 'binary'
            elif char in unary_op_table | binary_op_table:
                self._parse_op(char, context)
            elif char == '(':
                context.stack.append(char)
                context.state = 'unary'
                context.ptr += 1
            elif char == ')':
                self._consume_stack(context)
                context.state = 'binary'
                context.ptr += 1
            elif char.isalpha():
                self._parse_func(expr, context)

        self._consume_stack(context)

        if len(context.output) != 1 or context.stack:
            raise ValueError
        
        return context.output[0]
                
    def _parse_num(self, expr: str, context: ParserContext):
        if context.state != 'unary':
            raise ValueError
        
        base = context.ptr

        while context.ptr < len(expr):
            char = expr[context.ptr]

            if not (char.isdigit() or char == '.'):
                break

            context.ptr += 1

        if expr[base:context.ptr].count('.') > 1:
            raise ValueError
        
        context.output.append(float(expr[base:context.ptr]))
        context.state = 'binary'
        
    def _parse_op(self, char: str, context: ParserContext):
        if char in unary_op_table and context.state == 'unary':
            op = unary_op_table[char]
            context.state = 'unary'
        elif char in binary_op_table and context.state == 'binary':
            op = binary_op_table[char]
            context.state = 'unary'
        else:
            raise ValueError
        
        while context.stack:
            top = context.stack[-1]

            if type(top) == Function:
                pass
            elif type(top) != Operator or not (
                (op.prec <= top.prec and op.assoc == 'left') or
                (op.prec < top.prec and op.assoc == 'right')
            ):
                break
            
            self._apply_func(context)

        context.stack.append(op)
        context.ptr += 1

    def _parse_func(self, expr: str, context: ParserContext):
        if context.state != 'unary':
            raise ValueError
        
        base = context.ptr

        while context.ptr < len(expr):
            char = expr[context.ptr]

            if not char.isalpha():
                break

            context.ptr += 1

        if expr[base:context.ptr] not in func_table:
            raise ValueError
        
        context.stack.append(func_table[expr[base:context.ptr]])
        context.state = 'unary'

    def _apply_func(self, context: ParserContext):
        func = context.stack.pop()
        values = []

        if len(context.output) < func.arity:
            raise ValueError
        
        for _ in range(func.arity):
            values.append(context.output.pop())

        context.output.append(func(values[::-1]))

    def _consume_stack(self, context: ParserContext):
        while context.stack:
            top = context.stack[-1]

            if top == '(':
                context.stack.pop()
                break

            self._apply_func(context)