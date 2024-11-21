"""
Arthur Martins Zimmermann
Gabriel Jardim Nascimento
"""
from process import Process
from computingProcess import ComputingProcess
from pool import Pool

class ReadingProcess(Process):
    def __init__(self, pid: int, pool: Pool):
        super().__init__(pid)
        self._pool = pool
                              
    def execute(self):
        with open('computation.txt', 'w+') as f:
            for line in f.readlines():
                expression = line
                pid = len(self._pool.queue)
                self._pool.add_process(ComputingProcess(pid, expression))
            # Limpa o arquivo
            f.write('')
        print('Leitura de computation.txt concluída')

    def __str__(self):
        return f'{super().pid} | ReadingProcess'
