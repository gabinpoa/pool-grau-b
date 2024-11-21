"""
Arthur Martins Zimmermann
Gabriel Jardim Nascimento
"""
from menu import Menu
from pool import Pool

def main():
    pool = Pool()
    menu = Menu(pool)
    menu.run()

if __name__ == "__main__":
    main()
