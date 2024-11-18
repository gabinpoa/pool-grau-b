"""
Arthur Martins Zimmermann
Gabriel Jardim Nascimento
"""
from process import Process

class Pool:
    def __init__(self, queue: list[Process]):
        self._queue = queue

    def add_process(self, process: Process):
        self._queue.append(process)

    def exec_next(self):
        self._queue.pop(0).execute()

    def exec_process(self, pid: int):
        process_index = None

        for index, process in enumerate(self._queue):
            if process.pid == pid:
                process_index = index
                break

        if process_index is not None:
            self._queue.pop(process_index).execute()

     
