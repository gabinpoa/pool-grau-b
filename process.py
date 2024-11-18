"""
Arthur Martins Zimmermann
Gabriel Jardim Nascimento
"""
class Process:
    def __init__(self, pid: int):
        self._pid = pid

    @property
    def pid(self):
        return self._pid
    @pid.setter
    def pid(self, pid: int):
        self._pid = pid

    def execute(self):
        pass
