from pool import Pool
import os

class Menu:
    """
    Classe que abstrai as ativides do menu do sistema.
    Deve ser instanciada passando um objeto do tipo Pool.
    Para iniciar o menu, chame o método run().
    Exemplo:
    >>> pool = Pool()
    >>> menu = Menu(pool)
    >>> menu.run()
    """
    def __init__(self, pool: Pool):
        self._pool = pool
        pass

    def show_options(self):
        print("1 - Criar processo")
        print("2 - Executar próximo")
        print("3 - Executar processo específico")
        print("4 - Salvar estado em arquivo")
        print("5 - Carregar de arquivo")
        print("0 - Sair")

    def get_option(self) -> int:
        """
        Retorna a opção escolhida pelo usuário através do input.
        Se a opção não puder ser convertida para inteiro, retorna -1.
        """
        try:
            option = int(input("Digite a opção desejada: "))
            return option
        except ValueError:
            return -1

    def get_process_type(self) -> str:
        """
        Retorna o tipo de processo escolhido pelo usuário através do input.
        Se a opção não for válida, exibe uma mensagem de erro e pede novamente.
        """
        process_types = ["ComputingProcess", "WritingProcess", "PrintingProcess", "ReadingProcess"]
        print("Tipos de processos disponíveis:")
        for i, process_type in enumerate(process_types):
            print(f"{i+1} - {process_type}")
        selected_type = self.get_option() - 1
        if selected_type in [0, 1, 2, 3]:
            return process_types[selected_type]
        else:
            print("Tipo de processo inválido. Tente novamente.")
            return self.get_process_type()


    def exec_option(self, option: int):
        match option:
            case 1:
                process_type: str = self.get_process_type()
                
                # Se o processo for de cálculo ou escrita, pede a expressão
                if process_type in ["ComputingProcess", "WritingProcess"]:
                    expression = input("Digite a expressão do processo: ")
                    self._pool.new_process(process_type, expression)
                else:
                    self._pool.new_process(process_type)

                self.clear_terminal()
                print("Processo criado e adicionado à fila com sucesso.")

            case 2:
                self._pool.run_next()

            case 3:
                selected_pid = int(input("Insira o PID do processo que deseja executar: "))
                self._pool.run_process(selected_pid)

            case 4:
                self._pool.save_state()
                print("Estado salvo com sucesso em state.csv.")

            case 5:
                self._pool.load_state()
                print("Estado carregado com sucesso de state.csv.")

            case _: 
                print("Opção inválida. Tente novamente.")

    def run(self):
        while True:
            self.show_options()
            option = self.get_option()
            self.clear_terminal()
            if option == 0:
                print("Saindo...")
                break
            elif option == -1:
                print("Apenas inteiros são aceitos. Tente novamente.")
            else:
                self.exec_option(option)
                print('')

    def clear_terminal(self):
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')


