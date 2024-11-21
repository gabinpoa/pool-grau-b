"""
Arthur Martins Zimmermann
Gabriel Jardim Nascimento
"""
from process import Process

class PrintingProcess(Process):
    """
    Imprime as informações de todos os processos no pool.
    """
    def __init__(self, pid: int, processes_pool: list[Process]):
        """
        processes_pool é a lista de processos que serão impressos
        """
        super().__init__(pid)
        self._processes_pool = processes_pool

    def execute(self):
        print('\nPID | Tipo | [Expressão]')
        for process in self._processes_pool:
            print(process.__str__())

    def __str__(self):
        return f'{super().pid} | PrintingProcess'
