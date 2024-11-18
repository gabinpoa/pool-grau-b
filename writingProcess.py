"""
Arthur Martins Zimmermann
Gabriel Jardim Nascimento
"""
from process import Process
from computingProcess import ComputingProcess

class WritingProcess(Process):
    def __init__(self, pid: int, processes_pool: list[Process], expression: str):
        super().__init__(pid)
        self._processes_pool = processes_pool
        self._expression = expression

    def execute(self):
        with open('computation.txt', 'a') as f:
            f.writelines([self._expression])
        pid = len(self._processes_pool)
        self._processes_pool.append(ComputingProcess(pid, self._expression))

