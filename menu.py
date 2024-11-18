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
        pass

    def get_option(self) -> int:
        return 0

    def exec_option(self, option: int):
        match option:
            case _:
                pass

    def run(self):
        while True:
            self.show_options()
            option = self.get_option()
            if option == 0:
                print("Saindo...")
                break
            self.exec_option(option)

    @staticmethod
    def clear_terminal():
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')


