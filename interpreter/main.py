from enum import Enum, auto


class Token:

    class Type(Enum):

        INTEGER = auto()
        PLUS = auto()
        MINUS = auto()
        LPAREN = auto()
        RPAREN = auto()

    def __init__(self, kind, text):
        self.kind = kind
        self.text = text

    def __str__(self):
        return f'`{self.text}`'


def lex(text):
    result = []
    i = 0
    while i < len(text):
        if text[i] == '+':
            result.append(Token(Token.Type.PLUS, text[i]))
        elif text[i] == '-':
            result.append(Token(Token.Type.MINUS, text[i]))
        elif text[i] == '(':
            result.append(Token(Token.Type.LPAREN, text[i]))
        elif text[i] == ')':
            result.append(Token(Token.Type.RPAREN, text[i]))
        else:
            digits = [text[i]]
            for j in range(i + 1, len(text)):
                if text[j].isdigit():
                    digits.append(text[j])
                    i += 1
                else:
                    break
            if digits:
                result.append(Token(Token.Type.INTEGER, ''.join(digits)))
        i += 1
    return result


class Integer:

    def __init__(self, value):
        self.value = value


class BinaryOperation:

    class Type(Enum):

        ADDITION = auto()
        SUBTRACTION = auto()

    def __init__(self, kind=None, left=None, right=None):
        self.kind = kind
        self.left = left
        self.right = right

    @property
    def value(self):
        if self.kind == self.Type.ADDITION:
            return self.left.value + self.right.value
        if self.kind == self.Type.SUBTRACTION:
            return self.left.value - self.right.value

    def __repr__(self):
        return f'{self.left} {self.kind} {self.right}'


def parse(tokens):
    op = BinaryOperation()
    has_left = False
    i = 0
    while i < len(tokens):
        if tokens[i].kind == Token.Type.INTEGER:
            integer = Integer(int(tokens[i].text))
            if not has_left:
                op.left = integer
                has_left = True
            else:
                op.right = integer
        elif tokens[i].kind == Token.Type.PLUS:
            op.kind = BinaryOperation.Type.ADDITION
        elif tokens[i].kind == Token.Type.MINUS:
            op.kind = BinaryOperation.Type.SUBTRACTION
        elif tokens[i].kind == Token.Type.LPAREN:
            j = i
            while i <= len(tokens):
                if tokens[j].kind == Token.Type.RPAREN:
                    break
                j += 1
            subop = parse(tokens[i + 1:j])
            if not has_left:
                op.left = subop
                has_left = True
            else:
                op.right = subop
            i = j
        i += 1
    return op


def calc(text):
    tokens = lex(text)
    print(' '.join(map(str, tokens)))
    parsed = parse(tokens)
    print(f'{text} = {parsed.value}')


if __name__ == "__main__":
    calc('(135-24)+(244-63)')

    # not supported
    # calc('1+2+(3-4)')
