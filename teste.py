from tkinter import *


def limitar_tamanho(p):
    if len(p) > 8:
        return False
    return True


root = Tk()

# Registrando a função que faz a validação.
vcmd = root.register(func=limitar_tamanho)

entrada = Entry(root, validate='key', validatecommand=(vcmd, '%P'))

entrada.pack()

root.mainloop()