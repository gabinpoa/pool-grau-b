"""
Arthur Martins Zimmermann
Gabriel Jardim Nascimento
"""
from process import Process
from computingProcess import ComputingProcess

class WritingProcess(Process):
    def __init__(self, pid: int, processes_pool: list[Process], expression: str):
        """
        processes_pool deve ser a fila original de processos do programa
        expression é o calculo que será escrito no arquivo
        Ex: '2+2'
        """
        super().__init__(pid)
        self._processes_pool = processes_pool
        self._expression = expression

    def execute(self):
        with open('computation.txt', 'a') as f:
            f.writelines([self._expression])
        pid = len(self._processes_pool) # Todo: Gerar um pid único
        self._processes_pool.append(ComputingProcess(pid, self._expression))

