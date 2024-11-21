"""
Arthur Martins Zimmermann
Gabriel Jardim Nascimento
"""
from process import Process

class WritingProcess(Process):
    """
    Escreve a expressão recebida por parametro no arquivo computation.txt.
    """
    def __init__(self, pid: int, expression: str):
        """
        expression é o calculo que será escrito no arquivo
        Ex: '2+2'
        """
        super().__init__(pid)
        self._expression = expression

    @property
    def expression(self):
        return self._expression

    def execute(self):
        with open('computation.txt', 'a') as f:
            f.write(self._expression + '\n')
        print(f'Escrito em computation.txt: {self._expression}')

    def __str__(self):
        return f'{super().pid} | WritingProcess | {self.expression}'
