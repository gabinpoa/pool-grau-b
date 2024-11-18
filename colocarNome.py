import os

def get_files():
    return [file for file in os.listdir() if file.endswith('.py')]

def add_author(file):
    with open(file, 'w+') as f:
        lines = f.readlines()
        if not "Arthur Martins Zimmermann" in f.read():
            f.write(f'"""\nArthur Martins Zimmermann\nGabriel Jardim Nascimento\n"""\n')
            f.writelines(lines)

def main():
    files = get_files()
    for file in files:
        add_author(file)

if __name__ == '__main__':
    main()
