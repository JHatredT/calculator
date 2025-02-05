from enum import Enum
from dataclasses import dataclass
from core.op import unary_op_table, binary_op_table
from core.dlm import dlm_table
from core.const import const_table


class TokenType(Enum):
    NUMBER = 1
    OPERATOR = 2
    FUNCTION = 3
    DELIMITER = 4
    CONSTANT = 5


@dataclass
class Token:
    type: TokenType
    value: str


class TokenSequence:
    def __init__(self):
        self.ptr = 0
        self.tokens = []

    def __repr__(self):
        return str(self.tokens)


class Tokenizer:
    def tokenize(self, expr: str) -> TokenSequence:
        seq = TokenSequence()

        while seq.ptr < len(expr):
            if self._is_num_char(expr[seq.ptr]):
                self._tokenize_num(expr, seq)
            elif self._is_op_char(expr[seq.ptr]):
                self._tokenize_op(expr, seq)
            elif self._is_func_char(expr[seq.ptr]):
                self._tokenize_func(expr, seq)
            elif self._is_dlm_char(expr[seq.ptr]):
                self._tokenize_dlm(expr, seq)
            else:
                raise ValueError(f'Token not recognized: {expr[seq.ptr]}')

        return seq

    def _tokenize_num(self, expr: str, seq: TokenSequence):
        base = seq.ptr

        while seq.ptr < len(expr) and self._is_num_char(expr[seq.ptr]):
            seq.ptr += 1

        seq.tokens.append(Token(TokenType.NUMBER, expr[base:seq.ptr]))

    def _tokenize_op(self, expr: str, seq: TokenSequence):
        seq.tokens.append(Token(TokenType.OPERATOR, expr[seq.ptr]))
        seq.ptr += 1

    def _tokenize_func(self, expr: str, seq: TokenSequence):
        base = seq.ptr

        while seq.ptr < len(expr) and self._is_func_char(expr[seq.ptr]):
            seq.ptr += 1
        
        seq.tokens.append(Token(TokenType.FUNCTION, expr[base:seq.ptr]))

    def _tokenize_dlm(self, expr: str, seq: TokenSequence):
        seq.tokens.append(Token(TokenType.DELIMITER, expr[seq.ptr]))
        seq.ptr += 1

    def _tokenize_const(self, expr: str, seq: TokenSequence):
        seq.tokens.append(Token(TokenType.CONSTANT, expr[seq.ptr]))
        seq.ptr += 1

    def _is_num_char(self, char: str):
        return char.isdigit() or char == '.'
    
    def _is_op_char(self, char: str):
        return char in unary_op_table | binary_op_table
    
    def _is_func_char(self, char: str):
        return char.isalpha()

    def _is_dlm_char(self, char: str):
        return char in dlm_table.keys() | {i.pair for i in dlm_table.values()}
    
    def _is_const_char(self, char: str):
        return char in const_table