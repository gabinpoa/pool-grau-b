"""
Arthur Martins Zimmermann
Gabriel Jardim Nascimento
"""
import csv
from computingProcess import ComputingProcess
import computingProcess
from printingProcess import PrintingProcess
from process import Process
from readingProcess import ReadingProcess
from writingProcess import WritingProcess

class Pool:
    def __init__(self, queue: list[Process]):
        self._queue = queue

    def add_process(self, process: Process):
        """Adiciona um processo ao final da fila."""
        self._queue.append(process)

    def run_next(self):
        """Remove e executa o próximo processo da fila."""
        self._queue.pop(0).execute()

    def run_process(self, pid: int):
        """
        Remove e executa o processo com o PID especificado.

        Filtra a lista de processos para encontrar o processo com o PID especificado.
        Se o processo for encontrado, ele é removido da fila
        e sua função execute é chamada.
        Caso contrário, exibe uma mensagem de erro.
        """
        filtered_process: list[int] = [i for i, p in enumerate(self._queue) if p.pid == pid] 
        if len(filtered_process) == 1:
            process_index = filtered_process[0]
            self._queue.pop(process_index).execute()
        else:
            print("Processo não encontrado.")

    def save_state(self):
        """
        Salva o estado atual da fila em um arquivo CSV.
        """
        with open("state.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["pid", "tipo", "expressao"])

            for process in self._queue:
                """
                Converte o objeto Process em uma string.
                Ex: "1 | ComputingProcess | 2+2"
                Separa a string em uma lista de strings. 
                Ex: ["1", "ComputingProcess", "2+2"]
                """
                process_str = process.__str__()
                csv_line = process_str.split(" | ")
                writer.writerow(csv_line)

    def load_state(self):
        """
        Carrega o estado da fila a partir de um arquivo CSV.
        """
        with open("state.csv", "r") as file:
            data = list(csv.reader(file))[1:]

            for line in data:
                pid = line[0]
                process_type = line[1]
                match process_type:
                    case "ComputingProcess":
                        expression = line[2]
                        self.add_process(ComputingProcess(int(pid), expression))
                    case "WritingProcess":
                        expression = line[2]
                        self.add_process(WritingProcess(int(pid), expression))
                    case "PrintingProcess":
                        self.add_process(PrintingProcess(int(pid), self._queue))
                    case "ReadingProcess":
                        self.add_process(ReadingProcess(int(pid), self._queue))
                    case _:
                        print("Tipo de processo inválido: ", process_type)
