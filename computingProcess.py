"""
Arthur Martins Zimmermann
Gabriel Jardim Nascimento
"""
from process import Process

class ComputingProcess(Process):

    _possible_operators = ['+', '-', '*', '/']

    def __init__(self, pid: int, expression: str):
        super().__init__(pid)
        self._expression = expression

        # identifica o operador e guarda em self.operator
        for operator in self._possible_operators:
            if operator in expression:
                self._operator = operator
                break

        # separa os operandos e guarda em self.operands como inteiros
        self._operands: list[int] = [int(operand) for operand in expression.split(self._operator)]

    @property
    def expression(self):
        return self._expression

    def execute(self):
        match self._operator:
            case '+':
                result = self._operands[0] + self._operands[1]
                print(f'{self._operands[0]} + {self._operands[1]} = {result}')
            case '-':
                result = self._operands[0] - self._operands[1]
                print(f'{self._operands[0]} - {self._operands[1]} = {result}')
            case '*':
                result = self._operands[0] * self._operands[1]
                print(f'{self._operands[0]} * {self._operands[1]} = {result}')
            case '/':
                result = self._operands[0] / self._operands[1]
                print(f'{self._operands[0]} / {self._operands[1]} = {result:.4f}')
            case _:
                print("Operador inválido")

    def __str__(self):
        return f'{super().pid} | ComputingProcess | {self.expression}'
