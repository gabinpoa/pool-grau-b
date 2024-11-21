"""
Arthur Martins Zimmermann
Gabriel Jardim Nascimento
"""
from process import Process
from computingProcess import ComputingProcess


class ReadingProcess(Process):
    """
    Lê o arquivo computation.txt e adiciona os processos de cálculo no pool.
    """

    def __init__(self, pid: int, pool: Pool):
        """
        pool é uma referencia ao objeto Pool que contém a fila de processos.
        """
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
