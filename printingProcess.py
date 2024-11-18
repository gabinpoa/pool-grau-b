"""
Arthur Martins Zimmermann
Gabriel Jardim Nascimento
"""
from process import Process

class PrintingProcess(Process):
    def __init__(self, pid: int):
        super().__init__(pid)
