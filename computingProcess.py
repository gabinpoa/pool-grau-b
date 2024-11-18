"""
Arthur Martins Zimmermann
Gabriel Jardim Nascimento
"""
from process import Process

class ComputingProcess(Process):
    def __init__(self, pid: int, expression: str):
        super().__init__(pid)

        # identifica o operador e guarda em self.operator
        for operator in self.possible_operators:
            if operator in expression:
                self.operator = operator
                break

        # separa os operandos e guarda em self.operands como inteiros
        self.operands: list[int] = [int(operand) for operand in expression.split(self.operator)]


    possible_operators = ['+', '-', '*', '/']

