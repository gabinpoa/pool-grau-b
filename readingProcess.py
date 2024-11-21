"""
Arthur Martins Zimmermann
Gabriel Jardim Nascimento
"""
from process import Process
from computingProcess import ComputingProcess

class ReadingProcess(Process):
    def __init__(self, pid: int, processes_pool: list[Process]):
        super().__init__(pid)
        self._processes_pool = processes_pool
                              
    def execute(self):
        with open('computation.txt', 'w+') as f:
            for line in f.readlines():
                expression = line
                pid = len(self._processes_pool)
                self._processes_pool.append(ComputingProcess(pid, expression))
            # Limpa o arquivo
            f.write('')

    def __str__(self):
        return f'{super().pid} | ReadingProcess'
