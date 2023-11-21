# Importa algumas funções que são necessárias para o funcionamento do projeto,
# algumas do tkinter são importados automaticamente para mmelhor funcionamento.

from tkinter import *
from tkinter.font import Font
from tkcalendar import *
import sqlite3
import webbrowser as wb
from datetime import *

# Inicia a classe meu Equilíbrio, que será exclusiva e funcionará para toda a
# a extensão do código.

class MeuEquilibrio():

    # Utiliza o método construtor para a criação de um gatilho para abrir a 
    # tela de boas vindas ou não, além da função que leva a criação das ta-
    # belas no método interligado à biblioteca sqlite3, ou seja, o banco 
    # de dados local.

    def __init__(self):

        self.gatilho = None
        self.criarBd()
        self.registrarSono()

        if self.gatilho == 1:

            self.telaPrincipal()
        else:

            self.boasVindas()

    # Essa função serve apenas para esconder uma janela que foi aberta,
    # e abrir uma outra janela topLevel, chamando o seu método que foi
    # previamente informado no parâmetro, assim como a janela antiga.

    def esconder(self, atual, nova):
        atual.withdraw()
        nova()

    # Efeito parecido a anterior, apenas com o intuito de aparecer a 
    # janela que antes havia sido escondida e ddestruindo a janela
    # aberta atualmente.

    def aparecer(self, antiga, nova):
        antiga.destroy()
        nova.update()
        nova.deiconify()

    # Tal métodp funciona de maneira diferente das demais. Ao invés
    # de esconder uma janela x, ela simplesmente destrói a janela e
    # entra em outro método, para abrir uma janela Tk.

    def destruir(self, atual, nova):
        atual.destroy()
        nova()

    # Método exclusivo para os protocols da janela topLevel, onde
    # essa função destrói a janela Tk referente à atual topLevel,
    # evitando assim que o programa continue rodando caso o usu-
    # ário feche a janela no "X".

    def sair(self, destruir):
        destruir.destroy()

    # Criação da janela de boas-vindas, a qual aparece ao usuário
    # uma única vez.

    def boasVindas(self):
        self.janelaVindas = Tk()
        self.janelaVindas.geometry("365x570+450+10")
        self.janelaVindas.resizable(False, False)
        self.janelaVindas.iconbitmap(".\\imagens\\logo.ico")
        self.janelaVindas.title("Meu Equilíbrio")
        self.janelaVindas['bg'] = '#FFFFFF'

        vindas = PhotoImage(file = '.\\imagens\\vindas.png')
        self.label(self.janelaVindas, "arial 12", '', vindas, '#FFFFFF', None, 0.2, 0, 0.6, 0.15)

        logonomus = PhotoImage(file = '.\imagens\logonomus.png')
        self.label(self.janelaVindas, "arial 12", '', logonomus, '#FFFFFF', None, 0.2, 0.15, 0.6, 0.65)
        
        entrar = PhotoImage(file = '.\imagens\entrar.png')
        self.botao(self.janelaVindas, 'Arial 12', '', entrar, '#FFFFFF', 'white', 0.075, 0.8, 0.85, 0.1, lambda: self.destruir(self.janelaVindas, self.telaPrincipal))

        self.janelaVindas.mainloop()

    # Tela principal do aplicativo é criada nesse método. É aqui
    # que essa janela serve como mãe para todas as outras, levando
    # as áreas ofertadas pelo app.  

    def telaPrincipal(self):
        self.janelaPrincipal = Tk()
        self.janelaPrincipal.geometry("365x570+450+10")
        self.janelaPrincipal.iconbitmap(".\\imagens\\logo.ico")
        self.janelaPrincipal.title("Meu Equilíbrio")
        self.janelaPrincipal.resizable(False, False)
        self.janelaPrincipal['bg'] = '#FFFFFF'

        topoTela = Frame(self.janelaPrincipal, background = '#FCD647')
        topoTela.place(relx = 0, rely = 0, relwidth = 1, relheight= 0.1)
        
        equilibrio = PhotoImage(file = ".\\imagens\\equilibrio.png")
        self.label(topoTela, "arial 12", None, equilibrio, "#FCD647", '#FCD647', 0.27, 0.15, 0.5, 0.7)

        botao1 = PhotoImage(file = '.\\imagens\\aliviar.png')
        self.botao(self.janelaPrincipal, 'Arial 12', '', botao1, 'white', 'white', 0.15, 0.2, 0.7, 0.1, lambda: self.destruir(self.janelaPrincipal, self.aliviarAnsiedade))

        botao2 = PhotoImage(file = '.\\imagens\\superar.png')
        self.botao(self.janelaPrincipal, 'Arial 12', '', botao2, 'white', 'white', 0.15, 0.35, 0.7, 0.1, lambda: self.destruir(self.janelaPrincipal, self.superarMedos))

        botao3 = PhotoImage(file = '.\\imagens\\roda.png')
        self.botao(self.janelaPrincipal, 'Arial 12', '', botao3, 'white', 'white', 0.15, 0.5, 0.7, 0.1, lambda: self.destruir(self.janelaPrincipal, self.rodaDaVida))

        botao4 = PhotoImage(file = '.\\imagens\\psico.png')
        self.botao(self.janelaPrincipal, 'Arial 12', '', botao4, 'white', 'white', 0.15, 0.65, 0.7, 0.1, lambda: self.destruir(self.janelaPrincipal, self.psicoeducacao))

        botao5 = PhotoImage(file = '.\\imagens\\dormir.png')
        self.botao(self.janelaPrincipal, 'Arial 12', '', botao5, 'white', 'white', 0.15, 0.8, 0.7, 0.1, lambda: self.destruir(self.janelaPrincipal, self.detalhesSono))

        self.janelaPrincipal.mainloop()

    # Quando apertado no botão aliviar ansiedade, o programa vem
    # para esse método que cria a janela de aliviar a ansidade com
    # novos botões que caminham a outras ramificações.

    def aliviarAnsiedade(self):
        self.janelaAliviar = Tk()
        self.janelaAliviar.geometry("365x570+450+10")
        self.janelaAliviar.iconbitmap(".\\imagens\\logo.ico")
        self.janelaAliviar.title("Meu Equilíbrio")
        self.janelaAliviar.resizable(False, False)
        self.janelaAliviar['bg'] = '#FFFFFF'

        topoTela = Frame(self.janelaAliviar, background = '#FCD647')
        topoTela.place(relx = 0, rely = 0, relwidth = 1, relheight= 0.1)

        aliviarAn = PhotoImage(file = ".\\imagens\\aliviarAnsiedade.png")
        self.label(topoTela, "arial 12", None, aliviarAn, "#FCD647", '#FCD647', 0.1, 0.15, 0.8, 0.7)

        seta = PhotoImage(file = '.\\imagens\\seta.png')
        self.botao(topoTela, 'Arial 12', None, seta, '#FCD647', '#FCD647', 0.05, 0.2, 0.08, 0.57, lambda: self.destruir(self.janelaAliviar, self.telaPrincipal))

        botao1 = PhotoImage(file = '.\\imagens\\aliviarResp.png')
        self.botao(self.janelaAliviar, 'Arial 12', '', botao1, 'white', 'white', 0.15, 0.15, 0.7, 0.1, lambda: self.destruir(self.janelaAliviar, self.respiracaoDiafrag))
        
        botao2 = PhotoImage(file = '.\\imagens\\aliviarEnfre.png')
        self.botao(self.janelaAliviar, 'Arial 12', '', botao2, 'white', 'white', 0.15, 0.3, 0.7, 0.1, lambda: self.destruir(self.janelaAliviar, self.cartõesDeEnfrentamento))

        botao3 = PhotoImage(file = '.\\imagens\\aliviarRel.png')
        self.botao(self.janelaAliviar, 'Arial 12', '', botao3, 'white', 'white', 0.15, 0.45, 0.7, 0.1, lambda: self.destruir(self.janelaAliviar, self.tecRel))

        img = PhotoImage(file = ".\\imagens\\aliviarImg.png")
        self.label(self.janelaAliviar, "arial 12", None, img, "white", '#FFFFFF', 0.2, 0.6, 0.6, 0.3)

        self.janelaAliviar.mainloop()

    # Assim que clicada na primeiro botão da janela Aliviar a Ansiedade
    # o programa segue seu curso e cria a janela de técnicas de respira-
    # ção, ensinando ao usuário como realizar a respiração diafragmática
    # de forma adequada. 

    def respiracaoDiafrag(self):
        self.janelaRes = Tk()
        self.janelaRes.geometry("365x570+450+10")
        self.janelaRes.iconbitmap(".\\imagens\\logo.ico")
        self.janelaRes.title("Meu Equilíbrio")
        self.janelaRes.resizable(False, False)
        self.janelaRes['bg'] = '#FFFFFF'

        topoTela = Frame(self.janelaRes, background = '#FCD647')
        topoTela.place(relx = 0, rely = 0, relwidth = 1, relheight= 0.1)

        res = PhotoImage(file = ".\\imagens\\respiracao.png")
        self.label(topoTela, "arial 12", None, res, "#FCD647", '#FCD647', 0.1, 0.15, 0.8, 0.7)

        seta = PhotoImage(file = '.\\imagens\\seta.png')
        self.botao(topoTela, 'Arial 12', None, seta, '#FCD647', '#FCD647', 0.05, 0.2, 0.08, 0.57, lambda: self.destruir(self.janelaRes, self.aliviarAnsiedade))

        botao1 = PhotoImage(file = '.\\imagens\\res1.png')
        self.botao(self.janelaRes, 'Arial 12', '', botao1, 'white', 'white', 0.09, 0.15, 0.8, 0.13, lambda: self.destruir(self.janelaRes, self.passoUmRes))

        botao2 = PhotoImage(file = '.\\imagens\\res2.png')
        self.botao(self.janelaRes, 'Arial 12', '', botao2, 'white', 'white', 0.1, 0.3, 0.8, 0.07, lambda: self.destruir(self.janelaRes, self.passoDoisRes))

        botao3 = PhotoImage(file = '.\\imagens\\res3.png')
        self.botao(self.janelaRes, 'Arial 12', '', botao3, 'white', 'white', 0.09, 0.4, 0.8, 0.07, lambda: self.destruir(self.janelaRes, self.passoTresRes))

        botao4 = PhotoImage(file = '.\\imagens\\res4.png')
        self.botao(self.janelaRes, 'Arial 12', '', botao4, 'white', 'white', 0.1, 0.5, 0.8, 0.1, lambda: self.destruir(self.janelaRes, self.passoQuatroRes))

        botao5 = PhotoImage(file = '.\\imagens\\res5.png')
        self.botao(self.janelaRes, 'Arial 12', '', botao5, 'white', 'white', 0.09, 0.6, 0.8, 0.1, lambda: self.destruir(self.janelaRes, self.passoCincoRes))

        obs = PhotoImage(file = ".\\imagens\\obs.png")
        self.label(self.janelaRes, "arial 12", None, obs, "white", '#FFFFFF', 0.1, 0.75, 0.8, 0.1)

        self.janelaRes.mainloop()

    # Ao clicar no passo de número 1, essa tela é criada e uma instrução
    # com imagens emerge, mostrando mais especificadamente como realizar
    # a ação proposta.

    def passoUmRes(self):
        self.janelaResUm = Tk()
        self.janelaResUm.geometry("365x570+450+10")
        self.janelaResUm.iconbitmap(".\\imagens\\logo.ico")
        self.janelaResUm.title("Meu Equilíbrio")
        self.janelaResUm.resizable(False, False)
        self.janelaResUm['bg'] = '#FFFFFF'

        topoTela = Frame(self.janelaResUm, background = '#FCD647')
        topoTela.place(relx = 0, rely = 0, relwidth = 1, relheight= 0.1)

        primeiroPasso = PhotoImage(file = ".\\imagens\\primeiroPassoRoda.png")
        self.label(topoTela, "arial 12", None, primeiroPasso, "#FCD647", '#FCD647', 0.1, 0.15, 0.8, 0.7)

        seta = PhotoImage(file = '.\\imagens\\seta.png')
        self.botao(topoTela, 'Arial 12', None, seta, '#FCD647', '#FCD647', 0.05, 0.2, 0.08, 0.57, lambda: self.destruir(self.janelaResUm, self.respiracaoDiafrag))

        seta2 = PhotoImage(file = '.\\imagens\\seta2.png')
        self.botao(topoTela, 'Arial 12', None, seta2, '#FCD647', '#FCD647', 0.87, 0.2, 0.08, 0.57, lambda: self.destruir(self.janelaResUm, self.passoDoisRes))

        passoUm = PhotoImage(file = '.\\imagens\\passoUmRes.png')
        self.label(self.janelaResUm, None, None, passoUm, 'white', None, 0.175, 0.15, 0.65, 0.15)

        imgUm = PhotoImage(file = '.\\imagens\\imgPassoUmRes.png')
        self.label(self.janelaResUm, None, None, imgUm, 'white', None, 0.175, 0.35, 0.65, 0.4)

        self.janelaResUm.mainloop()

    # Essa janela funciona da mesma forma a anterior, mostrando de forma 
    # detalhada com imagen o segundo passo.

    def passoDoisRes(self):
        self.janelaResDois = Tk()
        self.janelaResDois.geometry("365x570+450+10")
        self.janelaResDois.iconbitmap(".\\imagens\\logo.ico")
        self.janelaResDois.title("Meu Equilíbrio")
        self.janelaResDois.resizable(False, False)
        self.janelaResDois['bg'] = '#FFFFFF'

        topoTela = Frame(self.janelaResDois, background = '#FCD647')
        topoTela.place(relx = 0, rely = 0, relwidth = 1, relheight= 0.1)

        segundoPasso = PhotoImage(file = ".\\imagens\\segundoPassoRoda.png")
        self.label(topoTela, "arial 12", None, segundoPasso, "#FCD647", '#FCD647', 0.1, 0.15, 0.8, 0.7)

        seta = PhotoImage(file = '.\\imagens\\seta.png')
        self.botao(topoTela, 'Arial 12', None, seta, '#FCD647', '#FCD647', 0.05, 0.2, 0.08, 0.57, lambda: self.destruir(self.janelaResDois, self.respiracaoDiafrag))

        seta2 = PhotoImage(file = '.\\imagens\\seta2.png')
        self.botao(topoTela, 'Arial 12', None, seta2, '#FCD647', '#FCD647', 0.87, 0.2, 0.08, 0.57, lambda: self.destruir(self.janelaResDois, self.passoTresRes))

        passoDois = PhotoImage(file = '.\\imagens\\passoDoisRes.png')
        self.label(self.janelaResDois, None, None, passoDois, 'white', None, 0.1, 0.15, 0.8, 0.1)

        imgDois = PhotoImage(file = '.\\imagens\\imgPassoDoisRes.png')
        self.label(self.janelaResDois, None, None, imgDois, 'white', None, 0.05, 0.35, 0.9, 0.4)

        self.janelaResDois.mainloop()

    # Passo três criando a janela com o mesmo atributo das anteriores,
    # alterando a tela apenas com o objetivo de mostrar de forma nítida
    # a execução eficaz do passo três.

    def passoTresRes(self):
        self.janelaResTres = Tk()
        self.janelaResTres.geometry("365x570+450+10")
        self.janelaResTres.iconbitmap(".\\imagens\\logo.ico")
        self.janelaResTres.title("Meu Equilíbrio")
        self.janelaResTres.resizable(False, False)
        self.janelaResTres['bg'] = '#FFFFFF'

        topoTela = Frame(self.janelaResTres, background = '#FCD647')
        topoTela.place(relx = 0, rely = 0, relwidth = 1, relheight= 0.1)

        terceiroPasso = PhotoImage(file = ".\\imagens\\TerceiroPassoRoda.png")
        self.label(topoTela, "arial 12", None, terceiroPasso, "#FCD647", '#FCD647', 0.1, 0.15, 0.8, 0.7)

        seta = PhotoImage(file = '.\\imagens\\seta.png')
        self.botao(topoTela, 'Arial 12', None, seta, '#FCD647', '#FCD647', 0.05, 0.2, 0.08, 0.57, lambda: self.destruir(self.janelaResTres, self.respiracaoDiafrag))

        seta2 = PhotoImage(file = '.\\imagens\\seta2.png')
        self.botao(topoTela, 'Arial 12', None, seta2, '#FCD647', '#FCD647', 0.87, 0.2, 0.08, 0.57, lambda: self.destruir(self.janelaResTres, self.passoQuatroRes))

        passoTres = PhotoImage(file = '.\\imagens\\passoTresRes.png')
        self.label(self.janelaResTres, None, None, passoTres, 'white', None, 0.1, 0.15, 0.8, 0.07)

        imgTres = PhotoImage(file = '.\\imagens\\imgPassoTresRes.png')
        self.label(self.janelaResTres, None, None, imgTres, 'white', None, 0.2, 0.35, 0.6, 0.4)

        self.janelaResTres.mainloop()

    # Passo quatro funcionando de maneira bastante similar às anteriores.

    def passoQuatroRes(self):
        self.janelaResQuatro = Tk()
        self.janelaResQuatro.geometry("365x570+450+10")
        self.janelaResQuatro.iconbitmap(".\\imagens\\logo.ico")
        self.janelaResQuatro.title("Meu Equilíbrio")
        self.janelaResQuatro.resizable(False, False)
        self.janelaResQuatro['bg'] = '#FFFFFF'

        topoTela = Frame(self.janelaResQuatro, background = '#FCD647')
        topoTela.place(relx = 0, rely = 0, relwidth = 1, relheight= 0.1)

        quartoPasso = PhotoImage(file = ".\\imagens\\quartoPassoRoda.png")
        self.label(topoTela, "arial 12", None, quartoPasso, "#FCD647", '#FCD647', 0.1, 0.15, 0.8, 0.7)

        seta = PhotoImage(file = '.\\imagens\\seta.png')
        self.botao(topoTela, 'Arial 12', None, seta, '#FCD647', '#FCD647', 0.05, 0.2, 0.08, 0.57, lambda: self.destruir(self.janelaResQuatro, self.respiracaoDiafrag))

        seta2 = PhotoImage(file = '.\\imagens\\seta2.png')
        self.botao(topoTela, 'Arial 12', None, seta2, '#FCD647', '#FCD647', 0.87, 0.2, 0.08, 0.57, lambda: self.destruir(self.janelaResQuatro, self.passoCincoRes))

        passoQuatro = PhotoImage(file = '.\\imagens\\passoQuatroRes.png')
        self.label(self.janelaResQuatro, None, None, passoQuatro, 'white', None, 0.05, 0.15, 0.9, 0.1)

        imgQuatro = PhotoImage(file = '.\\imagens\\imgPassoQuatroRes.png')
        self.label(self.janelaResQuatro, None, None, imgQuatro, 'white', None, 0.05, 0.3, 0.9, 0.5)

        self.janelaResQuatro.mainloop()

    # Por fim, a explicação nitida do passo a passo termina com a criação
    # desta janela que executa a especificação do passo 5.

    def passoCincoRes(self):
        self.janelaResCinco = Tk()
        self.janelaResCinco.geometry("365x570+450+10")
        self.janelaResCinco.iconbitmap(".\\imagens\\logo.ico")
        self.janelaResCinco.title("Meu Equilíbrio")
        self.janelaResCinco.resizable(False, False)
        self.janelaResCinco['bg'] = '#FFFFFF'

        topoTela = Frame(self.janelaResCinco, background = '#FCD647')
        topoTela.place(relx = 0, rely = 0, relwidth = 1, relheight= 0.1)

        quintoPasso = PhotoImage(file = ".\\imagens\\quintoPassoRoda.png")
        self.label(topoTela, "arial 12", None, quintoPasso, "#FCD647", '#FCD647', 0.1, 0.15, 0.8, 0.7)

        seta = PhotoImage(file = '.\\imagens\\seta.png')
        self.botao(topoTela, 'Arial 12', None, seta, '#FCD647', '#FCD647', 0.05, 0.2, 0.08, 0.57, lambda: self.destruir(self.janelaResCinco, self.respiracaoDiafrag))

        passoCinco = PhotoImage(file = '.\\imagens\\passoCincoRes.png')
        self.label(self.janelaResCinco, None, None, passoCinco, 'white', None, 0.05, 0.15, 0.9, 0.1)

        imgCinco = PhotoImage(file = '.\\imagens\\imgPassoCincoRes.png')
        self.label(self.janelaResCinco, None, None, imgCinco, 'white', None, 0.05, 0.3, 0.9, 0.5)

        self.janelaResCinco.mainloop()

    # Retornando a janela do aliviar ansiedade, caso o usuário clique na
    # segunda opção,o programa redireciona a esse método que cria a ja-
    # nela dos cartões de enfrentamento, onde nela é possível registrar
    # mensagens motivacionais criadas pelo usuário e salvas em banco
    # de dados local, para não ser perdido caso o usuário saia dessa 
    # janela ou do aplicativo.

    def cartõesDeEnfrentamento(self):
        self.janelaCartoes = Tk()
        self.janelaCartoes.geometry("365x570+450+10")
        self.janelaCartoes.iconbitmap(".\\imagens\\logo.ico")
        self.janelaCartoes.title("Meu Equilíbrio")
        self.janelaCartoes.resizable(False, False)
        self.janelaCartoes['bg'] = '#FFFFFF'
        self.text= StringVar()
        contador = self.janelaCartoes.register(func=self.contcarac)

        topoTela = Frame(self.janelaCartoes, background = '#FCD647')
        topoTela.place(relx = 0, rely = 0, relwidth = 1, relheight= 0.1)

        voltar = PhotoImage(file = ".\\imagens\\seta.png")
        self.botao(topoTela, 'arial 12', '', voltar, '#FCD647', '#FCD647', 0.03, 0.2, 0.1, 0.6, lambda: self.destruir(self.janelaCartoes, self.aliviarAnsiedade))

        adicionar = PhotoImage(file = ".\\imagens\\enfrentamentoAdd.png")
        self.botao(self.janelaCartoes, 'arial 12', '', adicionar, '#FFFFFF', '#FFFFFF', 0.15, 0.25, 0.7, 0.1, self.adicionarCartão)

        digitar = PhotoImage(file = ".\\imagens\\enfrentamentoAddMedo.png")
        self.label(self.janelaCartoes, 'arial 12', '', digitar, '#FFFFFF', None, 0.1, 0.15, 0.8, 0.1)

        self.mensagemCartao = Entry(self.janelaCartoes, font="open\ Sans 15", bg= '#FFFFFF', textvar=self.text, relief=FLAT, justify= CENTER, validate='key', validatecommand=(contador, '%P'))    
        self.mensagemCartao.place(relx=0.225, rely=0.164, relwidth=0.57, relheight=0.076)

        lucida = ('Lucida Calligraphy', 12)

        self.cartaoum = Label(self.janelaCartoes,bg ="#fedadf", text = '', wraplength = 100)
        self.cartaoum.place(relx = 0.175, rely = 0.4, relwidth = 0.3, relheight = 0.2 ) 
        self.cartaoum.configure(font = lucida)

        self.cartaodois = Label(self.janelaCartoes,bg ="#b8eef3", text = '', wraplength = 100)
        self.cartaodois.place(relx = 0.525, rely = 0.4, relwidth = 0.3, relheight = 0.2 ) 
        self.cartaodois.configure(font = lucida)

        self.cartaotres = Label(self.janelaCartoes,bg ="#f7f6b1", text = '', wraplength = 100)
        self.cartaotres.place(relx = 0.175, rely = 0.65, relwidth = 0.3, relheight = 0.2 ) 
        self.cartaotres.configure(font = lucida)

        self.cartaoquatro = Label(self.janelaCartoes,bg ="#c1edb0", text = '', wraplength = 100)
        self.cartaoquatro.place(relx = 0.525, rely = 0.65, relwidth = 0.3, relheight = 0.2 ) 
        self.cartaoquatro.configure(font = lucida)

        cartaoRosa = PhotoImage(file= ".\\imagens\\lixRosa.png")
        self.botao(self.janelaCartoes, 'arial 12', '', cartaoRosa, '#fedadf', '#fedadf', 0.395, 0.553, 0.08, 0.047, lambda: self.apagarCartao(1))
        
        cartaoAzul = PhotoImage(file= ".\\imagens\\lixAzul.png")
        self.botao(self.janelaCartoes, 'arial 12', '', cartaoAzul, '#b8eef3', '#b8eef3', 0.745, 0.553, 0.08, 0.047, lambda: self.apagarCartao(2))

        cartaoAmarelo = PhotoImage(file= ".\\imagens\\lixAmarela.png")
        self.botao(self.janelaCartoes, 'arial 12', '', cartaoAmarelo, '#f7f6b1', '#f7f6b1', 0.395, 0.803, 0.08, 0.047, lambda: self.apagarCartao(3))
        
        cartaoVerde = PhotoImage(file= ".\\imagens\\lixVerde.png")
        self.botao(self.janelaCartoes, 'arial 12', '', cartaoVerde, '#c1edb0', '#c1edb0', 0.745, 0.803, 0.08, 0.047, lambda: self.apagarCartao(4))

        textoTopo = PhotoImage(file= ".\\imagens\\enfrentamento.png")
        self.label(topoTela, 'arial 12', '', textoTopo, "#FCD647", None, 0.1, 0.15, 0.8, 0.7) 

        self.janelaCartoes.bind('<Return>', self.adicionarCartão)

        self.scannerBdEnfrent()

        self.janelaCartoes.mainloop()

    # Retornando a tela principal de aliviar a ansiedade, caso a op-
    # ção escolhida pelo usuário fosse a terceira, o programa vem a 
    # essa função que cria a janela de instrução a tecnicas de rela-
    # xamento muscular progressivo. As telas a seguir de passos pos-
    # suem as mesmas funcionalidades das de passos anteriores, ape-
    # nas alterando para a instrução de técnicas de relaxamento.

    def tecRel(self):
        self.janelaRel = Tk()
        self.janelaRel.geometry("365x570+450+10")
        self.janelaRel.iconbitmap(".\\imagens\\logo.ico")
        self.janelaRel.title("Meu Equilíbrio")
        self.janelaRel.resizable(False, False)
        self.janelaRel['bg'] = '#FFFFFF'

        topoTela = Frame(self.janelaRel, background = '#FCD647')
        topoTela.place(relx = 0, rely = 0, relwidth = 1, relheight= 0.1)

        rel = PhotoImage(file = ".\\imagens\\tecRel.png")
        self.label(topoTela, "arial 12", None, rel, "#FCD647", '#FCD647', 0.1, 0.15, 0.8, 0.7)

        seta = PhotoImage(file = '.\\imagens\\seta.png')
        self.botao(topoTela, 'Arial 12', None, seta, '#FCD647', '#FCD647', 0.05, 0.2, 0.08, 0.57, lambda: self.destruir(self.janelaRel, self.aliviarAnsiedade))

        rel0 = PhotoImage(file = ".\\imagens\\rel0.png")
        self.label(self.janelaRel, "arial 12", None, rel0, "white", '#FFFFFF', 0.05, 0.1, 0.9, 0.1)

        botao1 = PhotoImage(file = '.\\imagens\\rel1.png')
        self.botao(self.janelaRel, 'Arial 12', '', botao1, 'white', 'white', 0.1, 0.2, 0.8, 0.1, lambda: self.destruir(self.janelaRel, self.passoUmRel))

        botao2 = PhotoImage(file = '.\\imagens\\rel2.png')
        self.botao(self.janelaRel, 'Arial 12', '', botao2, 'white', 'white', 0.1, 0.33, 0.8, 0.16, lambda: self.destruir(self.janelaRel, self.passoDoisRel))

        botao3 = PhotoImage(file = '.\\imagens\\rel3.png')
        self.botao(self.janelaRel, 'Arial 12', '', botao3, 'white', 'white', 0.07, 0.5, 0.8, 0.15, lambda: self.destruir(self.janelaRel, self.passoTresRel))

        botao4 = PhotoImage(file = '.\\imagens\\rel4.png')
        self.botao(self.janelaRel, 'Arial 12', '', botao4, 'white', 'white', 0.08, 0.67, 0.8, 0.11, lambda: self.destruir(self.janelaRel, self.passoQuatroRel))

        obs = PhotoImage(file = ".\\imagens\\obs.png")
        self.label(self.janelaRel, "arial 12", None, obs, "white", '#FFFFFF', 0.1, 0.83, 0.8, 0.1)

        self.janelaRel.mainloop()

    def passoUmRel(self):
        self.janelaRelUm = Tk()
        self.janelaRelUm.geometry("365x570+450+10")
        self.janelaRelUm.iconbitmap(".\\imagens\\logo.ico")
        self.janelaRelUm.title("Meu Equilíbrio")
        self.janelaRelUm.resizable(False, False)
        self.janelaRelUm['bg'] = '#FFFFFF'

        topoTela = Frame(self.janelaRelUm, background = '#FCD647')
        topoTela.place(relx = 0, rely = 0, relwidth = 1, relheight= 0.1)

        primeiroPasso = PhotoImage(file = ".\\imagens\\primeiroPassoRoda.png")
        self.label(topoTela, "arial 12", None, primeiroPasso, "#FCD647", '#FCD647', 0.1, 0.15, 0.8, 0.7)

        seta = PhotoImage(file = '.\\imagens\\seta.png')
        self.botao(topoTela, 'Arial 12', None, seta, '#FCD647', '#FCD647', 0.05, 0.2, 0.08, 0.57, lambda: self.destruir(self.janelaRelUm, self.tecRel))

        seta2 = PhotoImage(file = '.\\imagens\\seta2.png')
        self.botao(topoTela, 'Arial 12', None, seta2, '#FCD647', '#FCD647', 0.87, 0.2, 0.08, 0.57, lambda: self.destruir(self.janelaRelUm, self.passoDoisRel))

        passoUm = PhotoImage(file = '.\\imagens\\passoUmRel.png')
        self.label(self.janelaRelUm, None, None, passoUm, 'white', None, 0.175, 0.15, 0.65, 0.15)

        imgUm = PhotoImage(file = '.\\imagens\\imgPassoUmRel.png')
        self.label(self.janelaRelUm, None, None, imgUm, 'white', None, 0.175, 0.4, 0.65, 0.4)

        self.janelaRelUm.mainloop()

    def passoDoisRel(self):
        self.janelaRelDois = Tk()
        self.janelaRelDois.geometry("365x570+450+10")
        self.janelaRelDois.iconbitmap(".\\imagens\\logo.ico")
        self.janelaRelDois.title("Meu Equilíbrio")
        self.janelaRelDois.resizable(False, False)
        self.janelaRelDois['bg'] = '#FFFFFF'

        topoTela = Frame(self.janelaRelDois, background = '#FCD647')
        topoTela.place(relx = 0, rely = 0, relwidth = 1, relheight= 0.1)

        segundoPasso = PhotoImage(file = ".\\imagens\\segundoPassoRoda.png")
        self.label(topoTela, "arial 12", None, segundoPasso, "#FCD647", '#FCD647', 0.1, 0.15, 0.8, 0.7)

        seta = PhotoImage(file = '.\\imagens\\seta.png')
        self.botao(topoTela, 'Arial 12', None, seta, '#FCD647', '#FCD647', 0.05, 0.2, 0.08, 0.57, lambda: self.destruir(self.janelaRelDois, self.tecRel))

        seta2 = PhotoImage(file = '.\\imagens\\seta2.png')
        self.botao(topoTela, 'Arial 12', None, seta2, '#FCD647', '#FCD647', 0.87, 0.2, 0.08, 0.57, lambda: self.destruir(self.janelaRelDois, self.passoTresRel))

        passoDois = PhotoImage(file = '.\\imagens\\passoDoisRel.png')
        self.label(self.janelaRelDois, None, None, passoDois, 'white', None, 0.0725, 0.15, 0.85, 0.13)

        imgDois = PhotoImage(file = '.\\imagens\\imgPassoDoisRel.png')
        self.label(self.janelaRelDois, None, None, imgDois, 'white', None, 0.05, 0.35, 0.9, 0.45)

        self.janelaRelDois.mainloop()

    def passoTresRel(self):
        self.janelaRelTres = Tk()
        self.janelaRelTres.geometry("365x570+450+10")
        self.janelaRelTres.iconbitmap(".\\imagens\\logo.ico")
        self.janelaRelTres.title("Meu Equilíbrio")
        self.janelaRelTres.resizable(False, False)
        self.janelaRelTres['bg'] = '#FFFFFF'

        topoTela = Frame(self.janelaRelTres, background = '#FCD647')
        topoTela.place(relx = 0, rely = 0, relwidth = 1, relheight= 0.1)

        terceiroPasso = PhotoImage(file = ".\\imagens\\TerceiroPassoRoda.png")
        self.label(topoTela, "arial 12", None, terceiroPasso, "#FCD647", '#FCD647', 0.1, 0.15, 0.8, 0.7)

        seta = PhotoImage(file = '.\\imagens\\seta.png')
        self.botao(topoTela, 'Arial 12', None, seta, '#FCD647', '#FCD647', 0.05, 0.2, 0.08, 0.57, lambda: self.destruir(self.janelaRelTres, self.tecRel))

        seta2 = PhotoImage(file = '.\\imagens\\seta2.png')
        self.botao(topoTela, 'Arial 12', None, seta2, '#FCD647', '#FCD647', 0.87, 0.2, 0.08, 0.57, lambda: self.destruir(self.janelaRelTres, self.passoQuatroRel))

        passoTres = PhotoImage(file = '.\\imagens\\passoTresRel.png')
        self.label(self.janelaRelTres, None, None, passoTres, 'white', None, 0.1, 0.15, 0.8, 0.18)

        imgTres = PhotoImage(file = '.\\imagens\\imgPassoTresRel.png')
        self.label(self.janelaRelTres, None, None, imgTres, 'white', None, 0.2, 0.35, 0.6, 0.6)

        self.janelaRelTres.mainloop()

    def passoQuatroRel(self):
        self.janelaRelQuatro = Tk()
        self.janelaRelQuatro.geometry("365x570+450+10")
        self.janelaRelQuatro.iconbitmap(".\\imagens\\logo.ico")
        self.janelaRelQuatro.title("Meu Equilíbrio")
        self.janelaRelQuatro.resizable(False, False)
        self.janelaRelQuatro['bg'] = '#FFFFFF'

        topoTela = Frame(self.janelaRelQuatro, background = '#FCD647')
        topoTela.place(relx = 0, rely = 0, relwidth = 1, relheight= 0.1)

        quartoPasso = PhotoImage(file = ".\\imagens\\quartoPassoRoda.png")
        self.label(topoTela, "arial 12", None, quartoPasso, "#FCD647", '#FCD647', 0.1, 0.15, 0.8, 0.7)

        seta = PhotoImage(file = '.\\imagens\\seta.png')
        self.botao(topoTela, 'Arial 12', None, seta, '#FCD647', '#FCD647', 0.05, 0.2, 0.08, 0.57, lambda: self.destruir(self.janelaRelQuatro, self.tecRel))

        passoQuatro = PhotoImage(file = '.\\imagens\\passoQuatroRel.png')
        self.label(self.janelaRelQuatro, None, None, passoQuatro, 'white', None, 0.05, 0.15, 0.9, 0.15)

        imgQuatro = PhotoImage(file = '.\\imagens\\imgPassoQuatroRel.png')
        self.label(self.janelaRelQuatro, None, None, imgQuatro, 'white', None, 0.05, 0.35, 0.9, 0.5)

        self.janelaRelQuatro.mainloop()

    # Ao retornar ao tópico da tela principal, caso aperte
    # no segundo botão, entrará ao metodo e aparecerá a 
    # janela superar medos, onde ficará a disposição
    # do usuário a adição de medos que tal possuí
    # e a opção de um botão que o leve a outra janela
    # e observe seus medos.

    def superarMedos(self):
        self.janelaSuperarMedos = Tk()
        self.janelaSuperarMedos.geometry("365x570+450+10")
        self.janelaSuperarMedos.resizable(False, False)
        self.janelaSuperarMedos.iconbitmap(".\\imagens\\logo.ico")
        self.janelaSuperarMedos.title("Meu Equilíbrio")
        self.janelaSuperarMedos['bg'] = '#FFFFFF'
        self.text= StringVar()

        topoTela = Frame(self.janelaSuperarMedos, background = '#FCD647')
        topoTela.place(relx = 0, rely = 0, relwidth = 1, relheight= 0.1)

        voltar = PhotoImage(file = ".\\imagens\\seta.png")
        self.botao(topoTela, 'arial 12', '', voltar, '#FCD647', '#FCD647', 0.03, 0.3, 0.1, 0.5, lambda: self.destruir(self.janelaSuperarMedos, self.telaPrincipal))

        textoTopo = PhotoImage(file= ".\\imagens\\superarMedos.png")
        self.label(topoTela, 'arial 12', '', textoTopo, "#FCD647", None, 0.27, 0.15, 0.5, 0.7) 

        adicionar = PhotoImage(file = ".\\imagens\\superarAdd.png")
        self.botao(self.janelaSuperarMedos, 'arial 12', '', adicionar, '#FFFFFF', '#FFFFFF', 0.1, 0.25, 0.8, 0.1, self.adicionarMedo)

        superarVeja = PhotoImage(file = ".\\imagens\\superarVeja.png")
        self.botao(self.janelaSuperarMedos, 'arial 12', '', superarVeja, '#FFFFFF', '#FFFFFF', 0.1, 0.85, 0.8, 0.1, lambda: self.destruir(self.janelaSuperarMedos, self.minhaListaDeMedos))

        digitar = PhotoImage(file = ".\\imagens\\superarAddMedo.png")
        self.label(self.janelaSuperarMedos, 'arial 12', '', digitar, '#FFFFFF', None, 0.1, 0.15, 0.8, 0.1)

        rodaImg = PhotoImage(file = ".\\imagens\\superarImg.png")
        self.label(self.janelaSuperarMedos, 'arial 12', '', rodaImg, 'black', None, 0.275, 0.45, 0.45, 0.25)

        self.addMedo = Entry(self.janelaSuperarMedos, font="open\ Sans 15", bg= '#FFFFFF', textvar=self.text, relief=FLAT, justify= CENTER)    
        self.addMedo.place(relx=0.225, rely=0.164, relwidth=0.57, relheight=0.073)

        self.janelaSuperarMedos.bind('<Return>', self.adicionarMedo)

        self.janelaSuperarMedos.mainloop()

    # Com o Usuário apertando no botão citado acima, conse-
    # guirá entrar em uma janela onde terá sua lista de medos
    # e também um botão onde será possível superar tal medo,
    # levando assim a exclusão do item à lista.

    def minhaListaDeMedos(self):
        self.janelaMeusMedos = Tk()
        self.janelaMeusMedos.geometry("365x570+450+10")
        self.janelaMeusMedos.resizable(False, False)
        self.janelaMeusMedos.iconbitmap(".\\imagens\\logo.ico")
        self.janelaMeusMedos.title("Meu Equilíbrio")
        self.janelaMeusMedos.resizable(False, False)
        self.janelaMeusMedos['bg'] = '#FFFFFF'
        self.text= StringVar()

        topoTela = Frame(self.janelaMeusMedos, background = '#FCD647')
        topoTela.place(relx = 0, rely = 0, relwidth = 1, relheight= 0.1)

        voltar = PhotoImage(file = ".\\imagens\\voltarME.png")
        self.botao(topoTela, 'arial 12', '', voltar, '#FCD647', '#FCD647', 0.03, 0.3, 0.1, 0.5, lambda: self.destruir(self.janelaMeusMedos, self.superarMedos))

        self.listaMedo = Listbox(self.janelaMeusMedos, bg="#FFFFFF", fg="#328EFF", font= ("open\ Sans", 15, 'bold'), justify = "center", selectbackground = '#FFFFFF', selectforeground = '#3ad1cb', borderwidth= 0, bd = 0)       
        self.listaMedo.place(relx=0.03, rely=0.12, relwidth=0.84, relheight=0.65)

        superei = PhotoImage(file = ".\\imagens\\superei.png")
        self.botao(self.janelaMeusMedos, 'arial 12', '', superei, 'white', '#FFFFFF', 0.2, 0.87, 0.6, 0.1, self.retirarMedo)

        scrollbar = Scrollbar(self.janelaMeusMedos)
        scrollbar.place(relx=0.88, rely=0.12, relwidth=0.08, relheight=0.65)

        self.listaMedo.config(yscrollcommand = scrollbar.set) 
        scrollbar.config(command = self.listaMedo.yview)

        textoTopo = PhotoImage(file= ".\\imagens\\listaMedos.png")
        self.label(topoTela, 'arial 12', '', textoTopo, "#FCD647", None, 0.2, 0.15, 0.6, 0.7)

        self.scannerBdMedo()

        self.janelaMeusMedos.bind('<Return>', self.retirarMedo)

        self.janelaMeusMedos.mainloop()

    # Voltando a tela principal, com o usuário apertando a 
    # terceira opção, ele vem a esse método, onde é possivel
    # levar a outras ramificações da roda da vida, como saber
    # o que é, a importância de tal e como fazê-la.

    def rodaDaVida(self):
        self.janelaRodaDaVida = Tk()
        self.janelaRodaDaVida.geometry("365x570+450+10")
        self.janelaRodaDaVida.iconbitmap(".\\imagens\\logo.ico")
        self.janelaRodaDaVida.title("Meu Equilíbrio")
        self.janelaRodaDaVida.resizable(False, False)
        self.janelaRodaDaVida['bg'] = '#FFFFFF'

        topoTela = Frame(self.janelaRodaDaVida, background = '#FCD647')
        topoTela.place(relx = 0, rely = 0, relwidth = 1, relheight= 0.1)

        voltar = PhotoImage(file = ".\\imagens\\voltarME.png")
        self.botao(topoTela, 'arial 12', '', voltar, '#FCD647', '#FCD647', 0.03, 0.3, 0.1, 0.5, lambda: self.destruir(self.janelaRodaDaVida, self.telaPrincipal))

        rodaDaVida = PhotoImage(file = ".\\imagens\\oQueRoda.png")
        self.botao(self.janelaRodaDaVida, 'arial 12', '', rodaDaVida, '#FFFFFF', '#FFFFFF', 0.085, 0.2, 0.83, 0.1, lambda: self.destruir(self.janelaRodaDaVida, self.oqueERodaDaVida))

        rodaDaVida2 = PhotoImage(file = ".\\imagens\\importanciaRoda.png")
        self.botao(self.janelaRodaDaVida, 'arial 12', '', rodaDaVida2, '#FFFFFF', '#FFFFFF', 0.085, 0.33, 0.83, 0.1, lambda: self.destruir(self.janelaRodaDaVida, self.importanciaRodaDaVida))

        rodaDaVida3 = PhotoImage(file = ".\\imagens\\aprendaRoda.png")
        self.botao(self.janelaRodaDaVida, 'arial 12', '', rodaDaVida3, '#FFFFFF', '#FFFFFF', 0.085, 0.47, 0.83, 0.1,  lambda: self.destruir(self.janelaRodaDaVida, self.fazerRodaDaVida))

        rodaImg = PhotoImage(file = ".\\imagens\\imgRoda.png")
        self.botao(self.janelaRodaDaVida, 'arial 12', '', rodaImg, '#FFFFFF', '#FFFFFF', 0.15, 0.65, 0.7, 0.25, None)

        textoTopo = PhotoImage(file= ".\\imagens\\roda da vida.png")
        self.label(topoTela, 'arial 12', '', textoTopo, "#FCD647", None, 0.1, 0.15, 0.8, 0.7) 

        self.janelaRodaDaVida.mainloop()

    # Esse método, quando acionado, leva a instrução sobre
    # o que é a roda da vida, orientando o usuário a entender 
    # melhor do que se trata. 

    def oqueERodaDaVida(self):
        self.janelaOqueERodaDaVida = Tk()
        self.janelaOqueERodaDaVida.geometry("365x570+450+10")
        self.janelaOqueERodaDaVida.iconbitmap(".\\imagens\\logo.ico")
        self.janelaOqueERodaDaVida.title("Meu Equilíbrio")
        self.janelaOqueERodaDaVida.resizable(False, False)
        self.janelaOqueERodaDaVida['bg'] = '#FFFFFF'

        topoTela = Frame(self.janelaOqueERodaDaVida, background = '#FCD647')
        topoTela.place(relx = 0, rely = 0, relwidth = 1, relheight= 0.1)

        voltar = PhotoImage(file = ".\\imagens\\voltarME.png")
        self.botao(topoTela, 'arial 12', '', voltar, '#FCD647', '#FCD647', 0.03, 0.3, 0.1, 0.5, lambda: self.destruir(self.janelaOqueERodaDaVida, self.rodaDaVida))

        ideiaRodaDaVida = PhotoImage(file= ".\\imagens\\ideiaRodaDaVida.png")
        self.label(self.janelaOqueERodaDaVida, "arial 12", '', ideiaRodaDaVida, 'white', None, 0.05, 0.14, 0.2, 0.2)

        ideiaRodaDaVida2 = PhotoImage(file= ".\\imagens\\ideiaRodaDaVida2.png")
        self.label(self.janelaOqueERodaDaVida, 'arial 12', '', ideiaRodaDaVida2, "white", None, 0.05, 0.45, 0.2, 0.2)

        ideiaRodaDaVida3 = PhotoImage(file= ".\\imagens\\ideiaRodaDaVida3.png")
        self.label(self.janelaOqueERodaDaVida, 'arial 12', '', ideiaRodaDaVida3, "white", None, 0.05, 0.76, 0.2, 0.2)

        textoTopo = PhotoImage(file= ".\\imagens\\textoTopo.png")
        self.label(topoTela, 'arial 12', '', textoTopo, "#FCD647", None, 0.1, 0.15, 0.8, 0.7)

        texto = PhotoImage(file= ".\\imagens\\texto.png")
        self.label(self.janelaOqueERodaDaVida, 'arial 12', '', texto, "white", None, 0.27, 0.14, 0.65, 0.2)

        texto2 = PhotoImage(file= ".\\imagens\\texto2.png")
        self.label(self.janelaOqueERodaDaVida, 'arial 12', '', texto2, "white", None, 0.27, 0.45, 0.65, 0.25)

        texto3 = PhotoImage(file= ".\\imagens\\texto3.png")
        self.label(self.janelaOqueERodaDaVida, 'arial 12', '', texto3, "white", None, 0.27, 0.76, 0.65, 0.2)

        self.janelaOqueERodaDaVida.mainloop()

    # Esse método explica da importância da roda da vida e 
    # porquê é importante aplicá-la para maior conhecimento
    # pessoal.

    def importanciaRodaDaVida(self):
        self.janelaimporRodaDaVida = Tk()
        self.janelaimporRodaDaVida.geometry("365x570+450+10")
        self.janelaimporRodaDaVida.iconbitmap(".\\imagens\\logo.ico")
        self.janelaimporRodaDaVida.title("Meu Equilíbrio")
        self.janelaimporRodaDaVida.resizable(False, False)
        self.janelaimporRodaDaVida['bg'] = '#FFFFFF'

        topoTela = Frame(self.janelaimporRodaDaVida, background = '#FCD647')
        topoTela.place(relx = 0, rely = 0, relwidth = 1, relheight= 0.1)

        voltar = PhotoImage(file = ".\\imagens\\voltarME.png")
        self.botao(topoTela, 'arial 12', '', voltar, '#FCD647', '#FCD647', 0.03, 0.3, 0.1, 0.5, lambda: self.destruir(self.janelaimporRodaDaVida, self.rodaDaVida))

        imagemRoda = PhotoImage(file= ".\\imagens\\img1importancia.png")
        self.label(self.janelaimporRodaDaVida, 'arial 12', '', imagemRoda, "white", None, 0.3, 0.7, 0.4, 0.23)

        textoTopo = PhotoImage(file= ".\\imagens\\importanciaRoda2.png")
        self.label(topoTela, 'arial 12', '', textoTopo, "#FCD647", None, 0.13, 0.26, 0.75, 0.5)

        imporRodaDaVida = PhotoImage(file= ".\\imagens\\txt1importancia.png")
        self.label(self.janelaimporRodaDaVida, "arial 12", '', imporRodaDaVida, 'white', None, 0.15, 0.13, 0.7, 0.2)

        imporRodaDaVida2 = PhotoImage(file= ".\\imagens\\txt2importancia.png")
        self.label(self.janelaimporRodaDaVida, 'arial 12', '', imporRodaDaVida2, "white", None, 0.15, 0.36, 0.7, 0.15)

        imporRodaDaVida3 = PhotoImage(file= ".\\imagens\\txt3importancia.png")
        self.label(self.janelaimporRodaDaVida, 'arial 12', '', imporRodaDaVida3, "white", None, 0.15, 0.53, 0.7, 0.12)

        self.janelaimporRodaDaVida.mainloop()

    # Esse tópico e a sequência dos próximos mostrarão, de
    # forma nítida, sobre como realizar a construção de uma
    # roda da vida eficaz em uma folha de papel.

    def fazerRodaDaVida(self):
        self.janelafazerRodaDaVida = Tk()
        self.janelafazerRodaDaVida.geometry("365x570+450+10")
        self.janelafazerRodaDaVida.iconbitmap(".\\imagens\\logo.ico")
        self.janelafazerRodaDaVida.title("Meu Equilíbrio")
        self.janelafazerRodaDaVida.resizable(False, False)
        self.janelafazerRodaDaVida['bg'] = '#FFFFFF'

        topoTela = Frame(self.janelafazerRodaDaVida, background = '#FCD647')
        topoTela.place(relx = 0, rely = 0, relwidth = 1, relheight= 0.1)

        voltar = PhotoImage(file = ".\\imagens\\voltarME.png")
        self.botao(topoTela, 'arial 12', '', voltar, '#FCD647', '#FCD647', 0.03, 0.3, 0.1, 0.5, lambda: self.destruir(self.janelafazerRodaDaVida, self.rodaDaVida))
        
        fazerRodaDaVida = PhotoImage(file= ".\\imagens\\fazer1.png")
        self.botao(self.janelafazerRodaDaVida, "arial 12", '', fazerRodaDaVida, 'white', 'white', 0.085, 0.13, 0.83, 0.1, lambda: self.destruir(self.janelafazerRodaDaVida, self.passoUmRoda))

        fazerRodaDaVida2 = PhotoImage(file= ".\\imagens\\fazer2.png")
        self.botao(self.janelafazerRodaDaVida, "arial 12", '', fazerRodaDaVida2, 'white', 'white', 0.085, 0.23, 0.83, 0.1, lambda: self.destruir(self.janelafazerRodaDaVida, self.passoDoisRoda))

        fazerRodaDaVida3 = PhotoImage(file= ".\\imagens\\fazer3.png")
        self.botao(self.janelafazerRodaDaVida, "arial 12", '', fazerRodaDaVida3, 'white', 'white', 0.085, 0.34, 0.83, 0.1, lambda: self.destruir(self.janelafazerRodaDaVida, self.passoTresRoda))

        fazerRodaDaVida4 = PhotoImage(file= ".\\imagens\\fazer4.png")
        self.botao(self.janelafazerRodaDaVida, "arial 12", '', fazerRodaDaVida4, 'white', 'white', 0.085, 0.45, 0.83, 0.15, lambda: self.destruir(self.janelafazerRodaDaVida, self.passoQuatroRoda))

        fazerRodaDaVida5 = PhotoImage(file= ".\\imagens\\fazer5.png")
        self.botao(self.janelafazerRodaDaVida, "arial 12", '', fazerRodaDaVida5, 'white', 'white', 0.085, 0.60, 0.83, 0.1, lambda: self.destruir(self.janelafazerRodaDaVida, self.passoCincoRoda))

        fazerRodaDaVida6 = PhotoImage(file= ".\\imagens\\fazer6.png")
        self.botao(self.janelafazerRodaDaVida, "arial 12", '', fazerRodaDaVida6, 'white', 'white', 0.085, 0.71, 0.83, 0.1, lambda: self.destruir(self.janelafazerRodaDaVida, self.passoSeisRoda))

        textoTopo = PhotoImage(file= ".\\imagens\\fazerRoda.png")
        self.label(topoTela, 'arial 12', '', textoTopo, "#FCD647", None, 0.1, 0.15, 0.8, 0.7)

        textoBase = PhotoImage(file= ".\\imagens\\obser.png")
        self.label(self.janelafazerRodaDaVida, "arial 12", '', textoBase, 'white', None, 0.085, 0.85, 0.83, 0.1)

        self.janelafazerRodaDaVida.mainloop()

    def passoUmRoda(self):
        self.janelaRodaUm = Tk()
        self.janelaRodaUm.geometry("365x570+450+10")
        self.janelaRodaUm.iconbitmap(".\\imagens\\logo.ico")
        self.janelaRodaUm.title("Meu Equilíbrio")
        self.janelaRodaUm.resizable(False, False)
        self.janelaRodaUm['bg'] = '#FFFFFF'

        topoTela = Frame(self.janelaRodaUm, background = '#FCD647')
        topoTela.place(relx = 0, rely = 0, relwidth = 1, relheight= 0.1)

        primeiroPasso = PhotoImage(file = ".\\imagens\\primeiroPassoRoda.png")
        self.label(topoTela, "arial 12", None, primeiroPasso, "#FCD647", '#FCD647', 0.1, 0.15, 0.8, 0.7)

        seta = PhotoImage(file = '.\\imagens\\seta.png')
        self.botao(topoTela, 'Arial 12', None, seta, '#FCD647', '#FCD647', 0.05, 0.2, 0.08, 0.57, lambda: self.destruir(self.janelaRodaUm, self.fazerRodaDaVida))

        seta2 = PhotoImage(file = '.\\imagens\\seta2.png')
        self.botao(topoTela, 'Arial 12', None, seta2, '#FCD647', '#FCD647', 0.87, 0.2, 0.08, 0.57, lambda: self.destruir(self.janelaRodaUm, self.passoDoisRoda))

        passoUm = PhotoImage(file = '.\\imagens\\passoUmRoda.png')
        self.label(self.janelaRodaUm, None, None, passoUm, 'white', None, 0.175, 0.15, 0.65, 0.1)

        imgUm = PhotoImage(file = '.\\imagens\\imgPassoUmRoda.png')
        self.label(self.janelaRodaUm, None, None, imgUm, 'white', None, 0.175, 0.35, 0.65, 0.4)

        self.janelaRodaUm.mainloop()

    def passoDoisRoda(self):
        self.janelaRodaDois = Tk()
        self.janelaRodaDois.geometry("365x570+450+10")
        self.janelaRodaDois.iconbitmap(".\\imagens\\logo.ico")
        self.janelaRodaDois.title("Meu Equilíbrio")
        self.janelaRodaDois.resizable(False, False)
        self.janelaRodaDois['bg'] = '#FFFFFF'

        topoTela = Frame(self.janelaRodaDois, background = '#FCD647')
        topoTela.place(relx = 0, rely = 0, relwidth = 1, relheight= 0.1)

        segundoPasso = PhotoImage(file = ".\\imagens\\segundoPassoRoda.png")
        self.label(topoTela, "arial 12", None, segundoPasso, "#FCD647", '#FCD647', 0.1, 0.15, 0.8, 0.7)

        seta = PhotoImage(file = '.\\imagens\\seta.png')
        self.botao(topoTela, 'Arial 12', None, seta, '#FCD647', '#FCD647', 0.05, 0.2, 0.08, 0.57, lambda: self.destruir(self.janelaRodaDois, self.fazerRodaDaVida))

        seta2 = PhotoImage(file = '.\\imagens\\seta2.png')
        self.botao(topoTela, 'Arial 12', None, seta2, '#FCD647', '#FCD647', 0.87, 0.2, 0.08, 0.57, lambda: self.destruir(self.janelaRodaDois, self.passoTresRoda))

        passoDois = PhotoImage(file = '.\\imagens\\passoDoisRoda.png')
        self.label(self.janelaRodaDois, None, None, passoDois, 'white', None, 0.1, 0.15, 0.8, 0.1)

        imgDois = PhotoImage(file = '.\\imagens\\imgPassoDoisRoda.png')
        self.label(self.janelaRodaDois, None, None, imgDois, 'white', None, 0.05, 0.35, 0.9, 0.4)

        obsDois = PhotoImage(file = '.\\imagens\\obsPassoDoisRoda.png')
        self.label(self.janelaRodaDois, None, None, obsDois, 'white', None, 0.05, 0.85, 0.9, 0.1)

        self.janelaRodaDois.mainloop()

    # Essa função é um diferencil dos outros tópicos, pois
    # a partir do passo 3, um botão que leva a esse método
    # é acionado e, assim, essa tela mostra as cores que está
    # sendo instruído e seus respectivos significados a se-
    # rem adicionados.

    def areaRodaVida(self):
        self.janelaAreaRoda = Tk()
        self.janelaAreaRoda.geometry("365x570+450+10")
        self.janelaAreaRoda.iconbitmap(".\\imagens\\logo.ico")
        self.janelaAreaRoda.title("Meu Equilíbrio")
        self.janelaAreaRoda.resizable(False, False)
        self.janelaAreaRoda['bg'] = '#FFFFFF'

        topoTela = Frame(self.janelaAreaRoda, background = '#FCD647')
        topoTela.place(relx = 0, rely = 0, relwidth = 1, relheight= 0.1)

        areaRoda = PhotoImage(file = ".\\imagens\\areaRodaVida.png")
        self.label(topoTela, "arial 12", None, areaRoda, "#FCD647", '#FCD647', 0.1, 0.15, 0.8, 0.7)

        seta = PhotoImage(file = '.\\imagens\\seta.png')
        self.botao(topoTela, 'Arial 12', None, seta, '#FCD647', '#FCD647', 0.05, 0.2, 0.08, 0.57, lambda: self.destruir(self.janelaAreaRoda, self.fazerRodaDaVida))

        infoArea = PhotoImage(file = '.\\imagens\\txtRodaVida.png')
        self.label(self.janelaAreaRoda, None, None, infoArea, 'white', None, 0.05, 0.1, 0.8, 0.85)

        self.janelaAreaRoda.mainloop()

    def passoTresRoda(self):
        self.janelaRodaTres = Tk()
        self.janelaRodaTres.geometry("365x570+450+10")
        self.janelaRodaTres.iconbitmap(".\\imagens\\logo.ico")
        self.janelaRodaTres.title("Meu Equilíbrio")
        self.janelaRodaTres.resizable(False, False)
        self.janelaRodaTres['bg'] = '#FFFFFF'

        topoTela = Frame(self.janelaRodaTres, background = '#FCD647')
        topoTela.place(relx = 0, rely = 0, relwidth = 1, relheight= 0.1)

        terceiroPasso = PhotoImage(file = ".\\imagens\\TerceiroPassoRoda.png")
        self.label(topoTela, "arial 12", None, terceiroPasso, "#FCD647", '#FCD647', 0.1, 0.15, 0.8, 0.7)

        seta = PhotoImage(file = '.\\imagens\\seta.png')
        self.botao(topoTela, 'Arial 12', None, seta, '#FCD647', '#FCD647', 0.05, 0.2, 0.08, 0.57, lambda: self.destruir(self.janelaRodaTres, self.fazerRodaDaVida))

        seta2 = PhotoImage(file = '.\\imagens\\seta2.png')
        self.botao(topoTela, 'Arial 12', None, seta2, '#FCD647', '#FCD647', 0.87, 0.2, 0.08, 0.57, lambda: self.destruir(self.janelaRodaTres, self.passoQuatroRoda))

        passoTres = PhotoImage(file = '.\\imagens\\passoTresRoda.png')
        self.label(self.janelaRodaTres, None, None, passoTres, 'white', None, 0.05, 0.15, 0.9, 0.1)

        imgTres = PhotoImage(file = '.\\imagens\\imgPassoTresRoda.png')
        self.label(self.janelaRodaTres, None, None, imgTres, 'white', None, 0.05, 0.35, 0.9, 0.4)

        self.janelaRodaTres.mainloop()

    def passoQuatroRoda(self):
        self.janelaRodaQuatro = Tk()
        self.janelaRodaQuatro.geometry("365x570+450+10")
        self.janelaRodaQuatro.iconbitmap(".\\imagens\\logo.ico")
        self.janelaRodaQuatro.title("Meu Equilíbrio")
        self.janelaRodaQuatro.resizable(False, False)
        self.janelaRodaQuatro['bg'] = '#FFFFFF'

        topoTela = Frame(self.janelaRodaQuatro, background = '#FCD647')
        topoTela.place(relx = 0, rely = 0, relwidth = 1, relheight= 0.1)

        quartoPasso = PhotoImage(file = ".\\imagens\\quartoPassoRoda.png")
        self.label(topoTela, "arial 12", None, quartoPasso, "#FCD647", '#FCD647', 0.1, 0.15, 0.8, 0.7)

        seta = PhotoImage(file = '.\\imagens\\seta.png')
        self.botao(topoTela, 'Arial 12', None, seta, '#FCD647', '#FCD647', 0.05, 0.2, 0.08, 0.57, lambda: self.destruir(self.janelaRodaQuatro, self.fazerRodaDaVida))

        seta2 = PhotoImage(file = '.\\imagens\\seta2.png')
        self.botao(topoTela, 'Arial 12', None, seta2, '#FCD647', '#FCD647', 0.87, 0.2, 0.08, 0.57, lambda: self.destruir(self.janelaRodaQuatro, self.passoCincoRoda))

        passoQuatro = PhotoImage(file = '.\\imagens\\passoQuatroRoda.png')
        self.label(self.janelaRodaQuatro, None, None, passoQuatro, 'white', None, 0.05, 0.15, 0.9, 0.1)

        imgQuatro = PhotoImage(file = '.\\imagens\\imgPassoQuatroRoda.png')
        self.label(self.janelaRodaQuatro, None, None, imgQuatro, 'white', None, 0.05, 0.3, 0.9, 0.5)

        obsQuatro = PhotoImage(file = '.\\imagens\\btnPassoQuatroRoda.png')
        self.botao(self.janelaRodaQuatro, None, None, obsQuatro, 'white', 'white', 0.0725, 0.85, 0.85, 0.1, lambda: self.destruir(self.janelaRodaQuatro, self.areaRodaVida))

        self.janelaRodaQuatro.mainloop()

    def passoCincoRoda(self):
        self.janelaRodaCinco = Tk()
        self.janelaRodaCinco.geometry("365x570+450+10")
        self.janelaRodaCinco.iconbitmap(".\\imagens\\logo.ico")
        self.janelaRodaCinco.title("Meu Equilíbrio")
        self.janelaRodaCinco.resizable(False, False)
        self.janelaRodaCinco['bg'] = '#FFFFFF'

        topoTela = Frame(self.janelaRodaCinco, background = '#FCD647')
        topoTela.place(relx = 0, rely = 0, relwidth = 1, relheight= 0.1)

        quintoPasso = PhotoImage(file = ".\\imagens\\quintoPassoRoda.png")
        self.label(topoTela, "arial 12", None, quintoPasso, "#FCD647", '#FCD647', 0.1, 0.15, 0.8, 0.7)

        seta = PhotoImage(file = '.\\imagens\\seta.png')
        self.botao(topoTela, 'Arial 12', None, seta, '#FCD647', '#FCD647', 0.05, 0.2, 0.08, 0.57, lambda: self.destruir(self.janelaRodaCinco, self.fazerRodaDaVida))

        seta2 = PhotoImage(file = '.\\imagens\\seta2.png')
        self.botao(topoTela, 'Arial 12', None, seta2, '#FCD647', '#FCD647', 0.87, 0.2, 0.08, 0.57, lambda: self.destruir(self.janelaRodaCinco, self.passoSeisRoda))

        passoCinco = PhotoImage(file = '.\\imagens\\passoCincoRoda.png')
        self.label(self.janelaRodaCinco, None, None, passoCinco, 'white', None, 0.05, 0.15, 0.9, 0.1)

        imgCinco = PhotoImage(file = '.\\imagens\\imgPassoCincoRoda.png')
        self.label(self.janelaRodaCinco, None, None, imgCinco, 'white', None, 0.05, 0.3, 0.9, 0.5)

        obsCinco = PhotoImage(file = '.\\imagens\\btnPassoQuatroRoda.png')
        self.botao(self.janelaRodaCinco, None, None, obsCinco, 'white', 'white', 0.0725, 0.85, 0.85, 0.1, lambda: self.destruir(self.janelaRodaCinco, self.areaRodaVida))

        self.janelaRodaCinco.mainloop()

    def passoSeisRoda(self):
        self.janelaRodaSeis = Tk()
        self.janelaRodaSeis.geometry("365x570+450+10")
        self.janelaRodaSeis.iconbitmap(".\\imagens\\logo.ico")
        self.janelaRodaSeis.title("Meu Equilíbrio")
        self.janelaRodaSeis.resizable(False, False)
        self.janelaRodaSeis['bg'] = '#FFFFFF'

        topoTela = Frame(self.janelaRodaSeis, background = '#FCD647')
        topoTela.place(relx = 0, rely = 0, relwidth = 1, relheight= 0.1)

        sextoPasso = PhotoImage(file = ".\\imagens\\sextoPassoRoda.png")
        self.label(topoTela, "arial 12", None, sextoPasso, "#FCD647", '#FCD647', 0.1, 0.15, 0.8, 0.7)

        seta = PhotoImage(file = '.\\imagens\\seta.png')
        self.botao(topoTela, 'Arial 12', None, seta, '#FCD647', '#FCD647', 0.05, 0.2, 0.08, 0.57, lambda: self.destruir(self.janelaRodaSeis, self.fazerRodaDaVida))

        passoSeis = PhotoImage(file = '.\\imagens\\passoSeisRoda.png')
        self.label(self.janelaRodaSeis, None, None, passoSeis, 'white', None, 0.05, 0.15, 0.9, 0.15)

        imgSeis = PhotoImage(file = '.\\imagens\\imgPassoSeisRoda.png')
        self.label(self.janelaRodaSeis, None, None, imgSeis, 'white', None, 0.05, 0.3, 0.9, 0.5)

        obsCinco = PhotoImage(file = '.\\imagens\\btnPassoQuatroRoda.png')
        self.botao(self.janelaRodaSeis, None, None, obsCinco, 'white', 'white', 0.0725, 0.85, 0.85, 0.1, lambda: self.destruir(self.janelaRodaSeis, self.areaRodaVida))

        self.janelaRodaSeis.mainloop()

    # Voltando ao tópico da tela principal, apertando em psi-
    # coeducação é redirecionado a essa tela, que possuem três
    # ramificações de três áreas que são interessantes a serem
    # conhecidas

    def psicoeducacao(self):
        self.janelapsicoeducacao = Tk()
        self.janelapsicoeducacao.geometry("365x570+450+10")
        self.janelapsicoeducacao.iconbitmap(".\\imagens\\logo.ico")
        self.janelapsicoeducacao.title("Meu Equilíbrio")
        self.janelapsicoeducacao.resizable(False, False)
        self.janelapsicoeducacao['bg'] = '#FFFFFF'

        topoTela = Frame(self.janelapsicoeducacao, background = '#FCD647')
        topoTela.place(relx = 0, rely = 0, relwidth = 1, relheight= 0.1)

        voltar = PhotoImage(file = ".\\imagens\\voltarME.png")
        self.botao(topoTela, 'arial 12', '', voltar, '#FCD647', '#FCD647', 0.03, 0.3, 0.1, 0.5, lambda: self.destruir(self.janelapsicoeducacao, self.telaPrincipal))

        psico1 = PhotoImage(file = ".\\imagens\\psico1.png")
        self.botao(self.janelapsicoeducacao, 'arial 12', '', psico1, '#FFFFFF', '#FFFFFF', 0.075, 0.2, 0.85, 0.1, lambda: self.destruir(self.janelapsicoeducacao, self.artigosEVideos))

        psico2 = PhotoImage(file = ".\\imagens\\psico2.png")
        self.botao(self.janelapsicoeducacao, 'arial 12', '', psico2, 'white', '#FFFFFF', 0.075, 0.33, 0.85, 0.1, lambda: self.destruir(self.janelapsicoeducacao, self.bonsHabitos))

        psico3 = PhotoImage(file = ".\\imagens\\psico3.png")
        self.botao(self.janelapsicoeducacao, 'arial 12', '', psico3, 'white', '#FFFFFF', 0.075, 0.45, 0.85, 0.1, lambda: self.destruir(self.janelapsicoeducacao, self.ajuda))

        psicoImg = PhotoImage(file = ".\\imagens\\psicoImg.png")
        self.label(self.janelapsicoeducacao, 'arial 12', '', psicoImg, '#FFFFFF', None, 0.36, 0.65, 0.28, 0.2)

        textoTopo = PhotoImage(file= ".\\imagens\\textoTopo1.png")
        self.label(topoTela, 'arial 12', '', textoTopo, "#FCD647", None, 0.1, 0.15, 0.8, 0.7)

        self.janelapsicoeducacao.mainloop()

    # Apertando na primeira opção do método anterior, chega-se
    # a esse método que mostra vários artigos e videos sobre a
    # ansiedade que podem ser clicados e assim direcionado a um
    # site confiável sobre as devidas instruções. A mesma coisa
    # acontece nos dois métodos seguintes.

    def artigosEVideos(self):
        self.janelaArtigoVideo = Tk()
        self.janelaArtigoVideo.geometry("365x570+450+10")
        self.janelaArtigoVideo.iconbitmap(".\\imagens\\logo.ico")
        self.janelaArtigoVideo.title("Meu Equilíbrio")
        self.janelaArtigoVideo.resizable(False, False)
        self.janelaArtigoVideo['bg'] = '#FFFFFF'

        topoTela = Frame(self.janelaArtigoVideo, background = '#FCD647')
        topoTela.place(relx = 0, rely = 0, relwidth = 1, relheight= 0.1)

        voltar = PhotoImage(file = ".\\imagens\\voltarME.png")
        self.botao(topoTela, 'arial 12', '', voltar, '#FCD647', '#FCD647', 0.03, 0.3, 0.1, 0.5, lambda: self.destruir(self.janelaArtigoVideo, self.psicoeducacao))

        psico1 = PhotoImage(file = ".\\imagens\\informe1.png")
        self.botao(self.janelaArtigoVideo, 'arial 12', '', psico1, 'white', '#FFFFFF', 0, 0.1, 1, 0.149, lambda: wb.open_new_tab('https://www.youtube.com/watch?v=iIc97ZKxSBU'), 'hand1')

        psico2 = PhotoImage(file = ".\\imagens\\informe2.png")
        self.botao(self.janelaArtigoVideo, 'arial 12', '', psico2, 'white', '#FFFFFF', 0, 0.25, 1, 0.149, lambda: wb.open_new_tab('https://www.youtube.com/watch?v=LBF27_w_49k'), 'hand1')

        psico3 = PhotoImage(file = ".\\imagens\\informe3.png")
        self.botao(self.janelaArtigoVideo, 'arial 12', '', psico3, 'white', '#FFFFFF', 0, 0.4, 1, 0.149, lambda: wb.open_new_tab('https://www.pfizer.com.br/noticias/ultimas-noticias/saude-mental-na-pandemia-do-coronavirus-como-manter-o-bem-estar-em-tempos-de-distanciamento-social'), 'hand1')

        psico4 = PhotoImage(file = ".\\imagens\\informe4.png")
        self.botao(self.janelaArtigoVideo, 'arial 12', '', psico4, 'white', '#FFFFFF', 0, 0.55, 1, 0.149, lambda: wb.open_new_tab('https://www.youtube.com/watch?v=12YX1sozG8g'), 'hand1')

        psico5 = PhotoImage(file = ".\\imagens\\informe5.png")
        self.botao(self.janelaArtigoVideo, 'arial 12', '', psico5, 'white', '#FFFFFF', 0, 0.7, 1, 0.149, lambda: wb.open_new_tab('https://canaltech.com.br/saude/5-remedios-naturais-que-combatem-ansiedade/'), 'hand1')

        psico6 = PhotoImage(file = ".\\imagens\\informe6.png")
        self.botao(self.janelaArtigoVideo, 'arial 12', '', psico6, 'white', '#FFFFFF', 0, 0.85, 1, 0.149, lambda: wb.open_new_tab('https://noticiasconcursos.com.br/como-a-ansiedade-afeta-a-vida-profissional/'), 'hand1')

        textoTopo = PhotoImage(file= ".\\imagens\\informe.png")
        self.label(topoTela, 'arial 12', '', textoTopo, "#FCD647", None, 0.1, 0.15, 0.8, 0.7)

        self.janelaArtigoVideo.mainloop()

    def bonsHabitos(self):
        self.janelaBonsHabitos = Tk()
        self.janelaBonsHabitos.geometry("365x570+450+10")
        self.janelaBonsHabitos.iconbitmap(".\\imagens\\logo.ico")
        self.janelaBonsHabitos.title("Meu Equilíbrio")
        self.janelaBonsHabitos.resizable(False, False)
        self.janelaBonsHabitos['bg'] = '#FFFFFF'

        topoTela = Frame(self.janelaBonsHabitos, background = '#FCD647')
        topoTela.place(relx = 0, rely = 0, relwidth = 1, relheight= 0.1)

        voltar = PhotoImage(file = ".\\imagens\\voltarME.png")
        self.botao(topoTela, 'arial 12', '', voltar, '#FCD647', '#FCD647', 0.03, 0.3, 0.1, 0.5, lambda: self.destruir(self.janelaBonsHabitos, self.psicoeducacao))

        psico1 = PhotoImage(file = ".\\imagens\\bomhabito1.png")
        self.botao(self.janelaBonsHabitos, 'arial 12', '', psico1, '#FFFFFF', '#FFFFFF', 0, 0.1, 1, 0.149, lambda: wb.open_new_tab('https://www.semagro.ms.gov.br/lista-50-alimentos-saudaveis-alguns-surpreendentes/'), 'hand1')

        psico2 = PhotoImage(file = ".\\imagens\\bomhabito2.png")
        self.botao(self.janelaBonsHabitos, 'arial 12', '', psico2, '#FFFFFF', '#FFFFFF', 0, 0.25, 1, 0.149, lambda: wb.open_new_tab('https://www.conquistesuavida.com.br/noticia/alimentacao-variada-descubra-como-devemos-equilibrar-as-refeicoes-do-dia-a-dia_a4441/1'), 'hand1')

        psico3 = PhotoImage(file = ".\\imagens\\bomhabito3.png")
        self.botao(self.janelaBonsHabitos, 'arial 12', '', psico3, '#FFFFFF', '#FFFFFF', 0, 0.4, 1, 0.149, lambda: wb.open_new_tab('https://www.nutrii.com.br/blog/por-que-e-importante-hidratar-se/'), 'hand1')

        psico4 = PhotoImage(file = ".\\imagens\\bomhabito4.png")
        self.botao(self.janelaBonsHabitos, 'arial 12', '', psico4, '#FFFFFF', '#FFFFFF', 0, 0.55, 1, 0.149, lambda: wb.open_new_tab('https://www.opopular.com.br/noticias/magazine/sa%C3%BAde-%C3%A0-mesa-1.1625046/alimenta%C3%A7%C3%A3o-refrescante-no-calor-1.2319894'), 'hand1')

        psico5 = PhotoImage(file = ".\\imagens\\bomhabito5.png")
        self.botao(self.janelaBonsHabitos, 'arial 12', '', psico5, '#FFFFFF', '#FFFFFF', 0, 0.7, 1, 0.149, lambda: wb.open_new_tab('https://www.istoedinheiro.com.br/alimentacao-saudavel-previne-doencas-mentais-confira-melhores-dietas-e-alimentos/'), 'hand1')

        psico6 = PhotoImage(file = ".\\imagens\\bomhabito6.png")
        self.botao(self.janelaBonsHabitos, 'arial 12', '', psico6, '#FFFFFF', '#FFFFFF', 0, 0.85, 1, 0.149, lambda: wb.open_new_tab('https://claudia.abril.com.br/saude/alimentos-interferem-humor/'), 'hand1')


        textoTopo = PhotoImage(file= ".\\imagens\\bomhabito.png")
        self.label(topoTela, 'arial 12', '', textoTopo, "#FCD647", None, 0.1, 0.15, 0.8, 0.7)

        self.janelaBonsHabitos.mainloop()

    def ajuda(self):
        self.janelaAjuda = Tk()
        self.janelaAjuda.geometry("365x570+450+10")
        self.janelaAjuda.iconbitmap(".\\imagens\\logo.ico")
        self.janelaAjuda.title("Meu Equilíbrio")
        self.janelaAjuda.resizable(False, False)
        self.janelaAjuda['bg'] = '#FFFFFF'

        topoTela = Frame(self.janelaAjuda, background = '#FCD647')
        topoTela.place(relx = 0, rely = 0, relwidth = 1, relheight= 0.1)

        voltar = PhotoImage(file = ".\\imagens\\voltarME.png")
        self.botao(topoTela, 'arial 12', '', voltar, '#FCD647', '#FCD647', 0.03, 0.3, 0.1, 0.5, lambda: self.destruir(self.janelaAjuda, self.psicoeducacao))

        psico1 = PhotoImage(file = ".\\imagens\\procurar1.png")
        self.botao(self.janelaAjuda, 'arial 12', '', psico1, '#FFFFFF', '#FFFFFF', 0, 0.1, 1, 0.149, lambda: wb.open_new_tab('https://www.boaconsulta.com/blog/por-que-procurar-um-psicologo-entenda/'), 'hand1')

        psico2 = PhotoImage(file = ".\\imagens\\procurar2.png")
        self.botao(self.janelaAjuda, 'arial 12', '', psico2, '#FFFFFF', '#FFFFFF', 0, 0.25, 1, 0.149, lambda: wb.open_new_tab('https://conexao.segurosunimed.com.br/5-beneficios-de-fazer-acompanhamento-psicologico/'), 'hand1')

        psico3 = PhotoImage(file = ".\\imagens\\procurar3.png")
        self.botao(self.janelaAjuda, 'arial 12', '', psico3, '#FFFFFF', '#FFFFFF', 0, 0.4, 1, 0.149, lambda: wb.open_new_tab('https://psicologiaacessivel.net/2016/08/15/motivos-para-procurar-um-psicologo/'), 'hand1')

        psico4 = PhotoImage(file = ".\\imagens\\procurar4.png")
        self.botao(self.janelaAjuda, 'arial 12', '', psico4, '#FFFFFF', '#FFFFFF', 0, 0.55, 1, 0.149, lambda: wb.open_new_tab('https://www.correiodocidadao.com.br/ultimas-noticias/ponto-alto-do-estresse-quando-procurar-ajuda/'), 'hand1')

        psico5 = PhotoImage(file = ".\\imagens\\procurar5.png")
        self.botao(self.janelaAjuda, 'arial 12', '', psico5, '#FFFFFF', '#FFFFFF', 0, 0.7, 1, 0.149, lambda: wb.open_new_tab('https://www.metropoles.com/saude/aprenda-a-identificar-uma-crise-de-ansiedade-e-saiba-o-que-fazer'), 'hand1')

        psico6 = PhotoImage(file = ".\\imagens\\procurar6.png")
        self.botao(self.janelaAjuda, 'arial 12', '', psico6, '#FFFFFF', '#FFFFFF', 0, 0.85, 1, 0.149, lambda: wb.open_new_tab('https://www.opovo.com.br/noticias/especialpublicitario/geracaofamilia/2021/08/16/equilibrio-emocional-a-receita-correta-para-o-bem-viver-e-os-bons-negocios.html'), 'hand1')

        textoTopo = PhotoImage(file= ".\\imagens\\procurar.png")
        self.label(topoTela, 'arial 12', '', textoTopo, "#FCD647", None, 0.1, 0.15, 0.8, 0.7)

        self.janelaAjuda.mainloop()

    # Por final, quando aperta em hora de dormir ainda na tela 
    # Principal, o usuário é redirecionado a essa tela que mostra
    # detalhes de seu sono, e as opções de adicionar um novo dia
    # ou selecionar um dia já armazenado.

    def detalhesSono(self):
        self.janelaDetalhe = Tk()
        self.janelaDetalhe.geometry("365x570+450+10")
        self.janelaDetalhe.iconbitmap(".\\imagens\\logo.ico")
        self.janelaDetalhe.title("Meu Equilíbrio")
        self.janelaDetalhe.resizable(False, False)
        self.janelaDetalhe['bg'] = '#FFFFFF'

        topoTela = Frame(self.janelaDetalhe, background = '#FCD647')
        topoTela.place(relx = 0, rely = 0, relwidth = 1, relheight= 0.1)

        detalheSono = PhotoImage(file = ".\\imagens\\detalheSono.png")
        self.label(topoTela, "arial 12", None, detalheSono, "#FCD647", '#FCD647', 0.2, 0.15, 0.6, 0.7)

        seta = PhotoImage(file = '.\\imagens\\seta.png')
        self.botao(topoTela, 'Arial 12', None, seta, '#FCD647', '#FCD647', 0.05, 0.2, 0.08, 0.57, lambda: self.destruir(self.janelaDetalhe, self.telaPrincipal))

        selecione = PhotoImage(file = '.\\imagens\\selecione.png')
        self.botao(self.janelaDetalhe, None, None, selecione, 'white', 'white', 0.05, 0.1, 0.9, 0.1, lambda: self.esconder(self.janelaDetalhe, self.selDia))

        voceDormiu = PhotoImage(file = ".\\imagens\\voceDormiu.png")
        self.label(self.janelaDetalhe, "arial 12", None, voceDormiu, "#FFFFFF", '#FFFFFF', 0.2, 0.22, 0.6, 0.1)

        self.hora = Label(self.janelaDetalhe, text = '' , font = ('open\ Sans', 20, 'bold'), background = 'white')
        self.hora.place(relx= 0.2, rely= 0.35, relheight= 0.1, relwidth= 0.6)

        texto = PhotoImage(file = ".\\imagens\\mensagem.png")
        self.label(self.janelaDetalhe, "arial 12", None, texto, 'white', '#FFFFFF', 0.1, 0.5, 0.8, 0.2)

        self.mensagem = Label(self.janelaDetalhe, text = '', font = ('open\ Sans', 12, 'bold'), background = 'white', foreground= 'black')
        self.mensagem.place(relx= 0.17, rely= 0.58, relheight= 0.067, relwidth= 0.67)

        novoDia = PhotoImage(file = '.\\imagens\\novoDia.png')
        self.botao(self.janelaDetalhe, None, None, novoDia, 'white', 'white', 0.1, 0.8, 0.8, 0.1, lambda: self.esconder(self.janelaDetalhe, self.adicionarDia))

        self.janelaDetalhe.mainloop()

    # Nessa tela o usuário consegue facilmente selecionar um dia
    # que foi colocado em nosso banco de dados por ele e assim 
    # ver a estimativa de sono e se foi um horário bom de sono.

    def selDia(self):
        self.janelaSelDia = Toplevel()
        self.janelaSelDia.geometry("365x570+450+10")
        self.janelaSelDia.iconbitmap(".\\imagens\\logo.ico")
        self.janelaSelDia.title("Meu Equilíbrio")
        self.janelaSelDia.resizable(False, False)
        self.janelaSelDia['bg'] = '#FFFFFF'

        topoTela = Frame(self.janelaSelDia, background = '#FCD647')
        topoTela.place(relx = 0, rely = 0, relwidth = 1, relheight= 0.1)

        equilibrio = PhotoImage(file = ".\\imagens\\seldiaa.png")
        self.label(topoTela, "arial 12", None, equilibrio, "#FCD647", '#FCD647', 0.1, 0.15, 0.8, 0.7)

        seta = PhotoImage(file = '.\\imagens\\seta.png')
        self.botao(topoTela, 'Arial 12', None, seta, '#FCD647', '#FCD647', 0.05, 0.2, 0.08, 0.57, lambda: self.aparecer(self.janelaSelDia, self.janelaDetalhe))

        self.listaDia = Listbox(self.janelaSelDia, bg="#FFFFFF", fg="#328EFF", font= ("open\ Sans", 15, 'bold'), justify = "center", borderwidth= 0, bd = 0)
        self.listaDia.place(relx=0.03, rely=0.15, relwidth=0.89, relheight=0.8)

        scrollbar = Scrollbar(self.janelaSelDia)
        scrollbar.place(relx=0.88, rely=0.15, relwidth=0.08, relheight=0.8)

        self.listaDia.config(yscrollcommand = scrollbar.set) 
        scrollbar.config(command = self.listaDia.yview)

        self.listaDia.bind_all("<<ListboxSelect>>", self.calcularHoras)

        self.janelaSelDia.protocol("WM_DELETE_WINDOW", lambda: self.sair(self.janelaDetalhe))

        self.scannerBd()

        self.janelaSelDia.mainloop()

    # Aqui o usuário por fim pode adicionar um dia de sono no
    # aplicativo, informando a hora que dormiu, a que acordou 
    # e o dia.

    def adicionarDia(self):
        self.janelaAdicionar = Toplevel()
        self.janelaAdicionar.geometry("365x570+450+10")
        self.janelaAdicionar.iconbitmap(".\\imagens\\logo.ico")
        self.janelaAdicionar.title("Meu Equilíbrio")
        self.janelaAdicionar.resizable(False, False)
        self.janelaAdicionar['bg'] = '#FFFFFF'

        topoTela = Frame(self.janelaAdicionar, background = '#FCD647')
        topoTela.place(relx = 0, rely = 0, relwidth = 1, relheight= 0.1)

        equilibrio = PhotoImage(file = ".\\imagens\\adicionar.png")
        self.label(topoTela, "arial 12", None, equilibrio, "#FCD647", '#FCD647', 0.1, 0.15, 0.8, 0.7)

        seta = PhotoImage(file = '.\\imagens\\seta.png')
        self.botao(topoTela, 'Arial 12', None, seta, '#FCD647', '#FCD647', 0.05, 0.2, 0.08, 0.57, lambda: self.aparecer(self.janelaAdicionar, self.janelaDetalhe))

        mimir = PhotoImage(file = ".\\imagens\\mimir.png")
        self.label(self.janelaAdicionar, "arial 12", None, mimir, "white", '#FFFFFF', 0.05, 0.15, 0.9, 0.07)

        acorda = PhotoImage(file = ".\\imagens\\acordar.png")
        self.label(self.janelaAdicionar, "arial 12", None, acorda, "white", '#FFFFFF', 0.05, 0.25, 0.9, 0.07)

        dia = PhotoImage(file = ".\\imagens\\seldia.png")
        self.label(self.janelaAdicionar, "arial 12", None, dia, "white", '#FFFFFF', 0.05, 0.35, 0.9, 0.07)

        self.dormir = Entry(self.janelaAdicionar , font = ('open Sans', 15), background = 'white', bd = 0)
        self.dormir.place(relx= 0.45, rely= 0.1499, relheight= 0.05, relwidth= 0.4)

        self.acordar = Entry(self.janelaAdicionar , font =  ('open Sans', 15), background = 'white', bd = 0)
        self.acordar.place(relx= 0.45, rely= 0.2499, relheight= 0.05, relwidth= 0.4)

        self.dia = Button(self.janelaAdicionar , font =  ('open Sans', 15), background = 'white', bd = 0, activebackground = 'white', text = '', command = lambda: self.esconder(self.janelaAdicionar, self.calendario))
        self.dia.place(relx= 0.39, rely= 0.3499, relheight= 0.05, relwidth= 0.3)

        self.janelaAdicionar.protocol("WM_DELETE_WINDOW", lambda: self.sair(self.janelaDetalhe))

        salvar = PhotoImage(file = '.\\imagens\\salvar.png')
        self.botao(self.janelaAdicionar, None, None, salvar, 'white', 'white', 0.64, 0.45, 0.27, 0.1, self.armazenarSono)

        imgadd = PhotoImage(file = ".\\imagens\\imgAdd.png")
        self.label(self.janelaAdicionar, "arial 12", None, imgadd, "white", '#FFFFFF', 0.2, 0.54, 0.6, 0.35)

        self.janelaAdicionar.bind('<Return>', self.armazenarSono)

        self.janelaAdicionar.mainloop()

    # Método criado para a construção da janela
    # Calendário onde o usuário pode selecionar
    # uma certa data.

    def calendario(self):

        self.janelaCalendario = Toplevel()
        self.janelaCalendario.geometry("365x570+450+10")
        self.janelaCalendario.iconbitmap(".\\imagens\\logo.ico")
        self.janelaCalendario.title("Meu Equilíbrio")
        self.janelaCalendario.resizable(False, False)
        self.janelaCalendario['bg'] = '#FFFFFF'

        topoTela = Frame(self.janelaCalendario, background = '#FCD647')
        topoTela.place(relx = 0, rely = 0, relwidth = 1, relheight= 0.1)

        equilibrio = PhotoImage(file = ".\\imagens\\addDia.png")
        self.label(topoTela, "arial 12", None, equilibrio, "#FCD647", '#FCD647', 0.1, 0.15, 0.8, 0.7)

        seta = PhotoImage(file = '.\\imagens\\seta.png')
        self.botao(topoTela, 'Arial 12', None, seta, '#FCD647', '#FCD647', 0.05, 0.2, 0.08, 0.57, lambda: self.aparecer(self.janelaCalendario, self.janelaAdicionar))

        self.calendar = Calendar(self.janelaCalendario, selectmode = 'day', date_pattern ="dd-mm-yyyy")
        self.calendar.place(relx = 0.10, rely = 0.15, relwidth = 0.8, relheight = 0.5)

        add = PhotoImage(file = '.\\imagens\\addDiaBotao.png')
        self.botao(self.janelaCalendario, 'Arial 12', None, add, 'white', '#FFFFFF', 0.2, 0.7, 0.57, 0.07, self.armazenarDia)

        self.janelaCalendario.protocol("WM_DELETE_WINDOW", lambda: self.sair(self.janelaDetalhe))

        self.janelaCalendario.mainloop()



    # Finalizando o layout das telas, essa função abaixo permite
    # a construção de botões nas telas ao longo do aplicativo, 
    # sendo apenas necessário selecionar algumas informações.

    def botao(self, janela, fonte, texto, image, bg, ab, x, y, width, height, command, cursor = None):
        btn = Button(janela)
        btn["font"] = fonte
        btn["text"] = texto
        btn["image"] = image
        btn["bg"] = bg  
        btn["command"] = command
        btn['activebackground'] = ab
        btn["bd"] = 0
        btn["relief"] = GROOVE
        btn['cursor'] = cursor
        btn.place(relx=x, rely=y, relwidth=width, relheight=height)

    # Bastante pareciddo com o anterior, esse método tem como
    # a criação de labels que não serão manipuláveis ao longo 
    # das telas.

    def label(self, janela, fonte, text, image, bg, fg, x, y, width, height):
        lbl = Label(janela)
        lbl["font"] = fonte
        lbl["text"] = text
        lbl['image'] = image
        lbl['fg'] = fg
        lbl["bg"] = bg
        lbl.place(relx=x, rely=y, relwidth=width, relheight=height)


    # Essa função cria o arquivo de banco de dados quando é solicitado.
    # Caso já exista, ele apenas dá prosseguimento ao código.

    def criarBd(self):

        open('MeuEquilibrio.bd', 'a').close()

    # O método abaixo é o primeiro a ser rodado, pois ele cria
    # todas as tabelas necessárias para o pleno andamento do 
    # aplicativo. Caso as tabelas já existirem, ele abre o app
    # direto da tela principal e não mais da tela de boas vindas.

    def registrarSono(self):
        self.conector = sqlite3.connect('MeuEquilibrio.bd')
        self.cursor = self.conector.cursor()
        try:
            self.cursor.execute('''CREATE TABLE horadormir(
                            id INT AUTO_INCREMENT,
                            dormir VARCHAR(10) NOT NULL,
                            acordar VARCHAR(10) NOT NULL,
                            data DATE NOT NULL PRIMARY KEY);''')

            self.cursor.execute('''CREATE TABLE medos(
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            medo VARCHAR(100) NOT NULL);''')

            self.cursor.execute('''CREATE TABLE cartaoum(
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            frase VARCHAR(40) NOT NULL);''')

            self.cursor.execute('''CREATE TABLE cartaodois(
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            frase VARCHAR(40) NOT NULL);''')

            self.cursor.execute('''CREATE TABLE cartaotres(
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            frase VARCHAR(40) NOT NULL);''')


            self.cursor.execute('''CREATE TABLE cartaoquatro(
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            frase VARCHAR(40) NOT NULL);''')

            self.conector.commit()
        
        except:
            self.gatilho = 1
        self.conector.close()

    # Essa função é responsável por adicionar o medo no banco de
    # dados evitar que envie alguma informação vazia ao banco.

    def adicionarMedo(self, event = None):
        
        medo = self.addMedo.get()

        aviso = Label(self.janelaSuperarMedos, font = ('open\ Sans', 12, 'bold'), foreground = "#FF66A0", background = "#FFFFFF", text = '')
        aviso.place(relx = 0.075, rely = 0.75, relheight= 0.07, relwidth= 0.85)

        if medo != '':

            self.conector = sqlite3.connect('MeuEquilibrio.bd')
            self.cursor = self.conector.cursor()

            self.cursor.execute(f"INSERT INTO medos(medo) VALUES ('{medo}');")
            self.conector.commit()

            aviso['foreground'] = '#328eff'
            aviso['text'] = 'Adicionado'

            self.conector.close()

        else:

            aviso['foreground'] = '#FCD647'
            aviso['text'] = 'Não é possível adicionar valores vazios.'

        medo = self.addMedo.delete(0, END)

    # Função semelhante a citada acima, essa tem como objetivo o 
    # armazenamento das informações de datas e horas, assim como
    # eliminar todos os possíveis erros previsíveis por parte do
    # usuário, como formato de data e hora errada ou vazia, além
    # de muitos outros.

    def armazenarSono(self, event = None):
    
        acordar = self.acordar.get()
        dormir = self.dormir.get()
        dia = self.dia['text']

        aviso = Label(self.janelaAdicionar, font = ('open Sans', 12, 'bold'), foreground = "#FF66A0", background = "#FFFFFF", text = '')
        aviso.place(relx = 0.1, rely = 0.9, relheight= 0.07, relwidth= 0.8)

        if acordar == '' or dormir == '' or dia == '':

            aviso['text'] = 'Preencha todos os campos!'

        else:
            try:
                novoAcordar = acordar.split(':')
                novoDormir = dormir.split(':')
                novoDia = dia.split('-')

                numAcordar = novoAcordar[0].isnumeric()
                numAcordar1 = novoAcordar[1].isnumeric()
                numDormir = novoDormir[0].isnumeric()
                numDormir1 = novoDormir[1].isnumeric()
                numDia = novoDia[0].isnumeric()
                numDia1 = novoDia[1].isnumeric()
                numDia2 = novoDia[2].isnumeric()

                if numAcordar == True and numAcordar1 == True and numDormir == True and numDormir1 == True and numDia == True and numDia1 == True and numDia2 == True:

                    if len(novoAcordar[0]) == 2 and len(novoAcordar[1]) == 2 and len(novoDormir[0]) == 2 and len(novoDormir[1]) == 2 and len(novoDia[0]) == 2 and len(novoDia[1]) == 2 and len(novoDia[2]) == 4:

                        novoAcordar[0] = int(novoAcordar[0])
                        novoAcordar[1] = int(novoAcordar[1])
                        novoDormir[0] = int(novoDormir[0])
                        novoDormir[1] = int(novoDormir[1])
                        novoDia[0] = int(novoDia[0])
                        novoDia[1] = int(novoDia[1])
                        novoDia[2] = int(novoDia[2])
                        
                        if novoAcordar[0] >= 00 and novoAcordar[0] <= 23 and novoDormir[0] >= 00 and novoDormir[0] <= 23 and novoAcordar[1] >= 00 and novoAcordar[1] <= 59 and novoDormir[1] >= 00 and novoDormir[1] <= 59:
                            
                            try:
                                self.conector = sqlite3.connect('MeuEquilibrio.bd')
                                self.cursor = self.conector.cursor()

                                diaFinal = str(f'{novoDia[2]}-{novoDia[1]}-{novoDia[0]}')

                                self.cursor.execute(f"INSERT INTO horadormir(dormir, acordar, data) VALUES ('{dormir}', '{acordar}', '{diaFinal}');")
                                self.conector.commit()

                                aviso['foreground'] = '#328eff'
                                aviso['text'] = 'Adicionado'

                                self.conector.close()

                            except:
                                aviso['text'] = 'Essa data já foi usada,\n por favor, utilize outra.'

                        else:
                            aviso['text'] = 'O Formato das horas vai de "00:00" \n até "23:59"'
                        
                    else:
                        aviso['text'] = 'Formate as horas em "HH:MM" e \n os dias em "DD/MM/AAAA"!'
                    
                else:
                    aviso['text'] = 'Por favor, utilize os valores em números.'

            except:

                aviso['text'] = 'Formate as horas em "HH:MM".'

            self.acordar.delete(0, END)

            self.dormir.delete(0, END)

            self.dia['text'] = ''

    # Método responsável por pegar a data que está armazenada na
    # janela de calendário e levar ao botão de selecionar o dia
    # além de apagar esta tela.

    def armazenarDia(self):

        diaSel = self.calendar.get_date()

        self.dia['text'] = diaSel
        self.aparecer(self.janelaCalendario, self.janelaAdicionar)



    # Essa função funciona como um scanner da tabela do hora de
    # dormir, onde consegue pegar as informações dos dias de so-
    # non e colocar na listbox do selecionar dia.

    def scannerBd(self):

        self.conector = sqlite3.connect('MeuEquilibrio.bd')
        self.cursor = self.conector.cursor()

        self.cursor.execute(f"SELECT data FROM horadormir ORDER BY data")
            
        listaData = []
        for i in self.cursor:
            listaData.append(i[0])
        
        controle = 0

        for i in listaData:

            dia = listaData[controle]

            dia = str(dia)

            dia = dia.split('-')

            ano = dia[0]
            mes = dia[1]
            day = dia[2]

            data = day +'-'+ mes + '-' + ano

            self.listaDia.insert(END, data)
            controle += 1

        self.conector.close()

    # De maneira similar a acima, funciona do mesmo jeito, apenas
    # com a diferença de pegar as infomações da tabela de medos.

    def scannerBdMedo(self):

        self.conector = sqlite3.connect('MeuEquilibrio.bd')
        self.cursor = self.conector.cursor()

        self.cursor.execute(f"SELECT medo FROM medos ORDER BY medo")
            
        listaMedo = []
        for i in self.cursor:
            listaMedo.append(i[0])
        
        controle = 0

        for i in listaMedo:
            self.listaMedo.insert(END, listaMedo[controle])
            controle += 1

        self.conector.close()

    # Método um pouco mais complexo, utiliza a biblioteca datetime
    # para subtrair as respectivas horas disponibilizadas pelo usu-
    # ário e extraída assim as horas dormidas.

    def calcularHoras(self, event):

        self.conector = sqlite3.connect('MeuEquilibrio.bd')
        self.cursor = self.conector.cursor()

        aux = self.listaDia.curselection()
        dia = self.listaDia.get(aux[0])

        dia = dia.split('-')

        day = dia[0]
        mes = dia[1]
        ano = dia[2]

        data = ano +'-'+ mes + '-' + day

        self.aparecer(self.janelaSelDia, self.janelaDetalhe)

        self.cursor.execute(f"SELECT dormir FROM horadormir WHERE data = '{data}'")

        for i in self.cursor:
            dormir = i[0]

        self.cursor.execute(f"SELECT acordar FROM horadormir WHERE data = '{data}'")

        for i in self.cursor:
            acordar = i[0]

        format = '%H:%M'
        tempo = datetime.strptime(acordar, format) - datetime.strptime(dormir, format)
        
        tempo = str(tempo)
        tempo = tempo.replace("-1 day, ", '')
        tempo = tempo.replace(':00', '', 1)

        tempo = tempo.split(':')

        self.hora['text'] = f'{tempo[0]}h{tempo[1]}min'

        tempo[0] = int(tempo[0])
        tempo[1] = int(tempo[1])

        if tempo[0] < 8 and tempo[0] > 5:
            
            self.mensagem['foreground'] = '#FDC647'
            self.mensagem['text'] = 'Você está abaixo da média. \nDurma mais!'

        elif tempo[0] <= 5:
            
            self.mensagem['foreground'] = '#FF66A0'
            self.mensagem['text'] = 'Preocupante! Está dormindo\n muito pouco. Durma mais!'

        elif tempo[0] >= 8 and tempo[0] <= 10:
            self.mensagem['foreground'] = '#328EFF'
            self.mensagem['text'] = 'Perfeito! Seu sono está\nna margem ideal. Parabéns!'

        elif tempo[0] > 10:
            self.mensagem['foreground'] = '#3AD1CB'
            self.mensagem['text'] = 'Tudo em excesso faz mal.\nDiminua suas horas de sono!'

    # Funciona para retirar o medo do banco de dados e da listbox, 
    # a partir do momento que o usuário aperta em medo superado, na ~
    # janela de lista de medos.

    def retirarMedo(self, event = None):
        self.conector = sqlite3.connect('MeuEquilibrio.bd')
        self.cursor = self.conector.cursor()

        aviso = Label(self.janelaMeusMedos, font = ('open\ Sans', 12, 'bold'), foreground = "#FF66A0", background = "#FFFFFF", text = '')
        aviso.place(relx = 0.05, rely = 0.8, relheight= 0.07, relwidth= 0.9)

        aux = self.listaMedo.curselection()
        if aux != ():

            medoSel = self.listaMedo.get(aux[0])
        
            self.cursor.execute(f"DELETE FROM medos WHERE medo = '{medoSel}'")
            self.conector.commit()

            self.listaMedo.delete(0,END)
            self.scannerBdMedo()
            aviso['foreground'] = '#3ad1cb'
            aviso['text'] = 'Medo superado!'

        else:

            aviso['foreground'] = '#FF66A0'
            aviso['text'] = 'Escolha um medo para superar primeiro!'
        

        self.conector.close()

    # Essa função tem a utilidade de adicionar a mensagem optada pelo
    # usuário e previnir possivéis erros, até mesmo quando todos os 
    # cartões estão lotados.

    def adicionarCartão(self, event = None):

        self.msgCar = Label(self.janelaCartoes, font = ('open\ Sans', 12, 'bold'), foreground = "#FF66A0", background = "#FFFFFF", text = '')
        self.msgCar.place(relx = 0.05, rely = 0.9, relheight= 0.07, relwidth= 0.9)

        mensagem = self.mensagemCartao.get()

        if mensagem == '':

            self.msgCar['foreground'] = '#FF66A0'
            self.msgCar['text'] = 'Impossível adicionar mensagem vazia.'
        
        elif len(mensagem) > 35:
            
            self.msgCar['foreground'] = '#328eff'
            self.msgCar['text'] = 'Limite de caracteres atingido. Máximo: 35.'
        
        else:
            
            self.conector = sqlite3.connect('MeuEquilibrio.bd')
            self.cursor = self.conector.cursor()

            if self.cartaoum['text'] == '':
                
                self.cartaoum['text'] = mensagem
                self.cursor.execute(f"INSERT INTO cartaoum(frase) VALUES ('{mensagem}');")
                self.conector.commit()


            elif self.cartaodois['text'] == '':

                self.cartaodois['text'] = mensagem
                self.cursor.execute(f"INSERT INTO cartaodois(frase) VALUES ('{mensagem}');")
                self.conector.commit()

            elif self.cartaotres['text'] == '':

                self.cartaotres['text'] = mensagem
                self.cursor.execute(f"INSERT INTO cartaotres(frase) VALUES ('{mensagem}');")
                self.conector.commit()

            elif self.cartaoquatro['text'] == '':

                self.cartaoquatro['text'] = mensagem
                self.cursor.execute(f"INSERT INTO cartaoquatro(frase) VALUES ('{mensagem}');")
                self.conector.commit()

            else:

                self.msgCar['foreground'] = '#3ad1cb'
                self.msgCar['text'] = 'Cartões Lotados. Tente apagar alguns.'

            self.conector.close()

        self.mensagemCartao.delete(0, END)

    # Similar aos outros scanners, ele pega as tabelas de cada cartão
    # e coloca seus respectivos textos. Caso não haja nada, ele simples-
    # mente retorna um valor vazio.

    def scannerBdEnfrent(self):

        self.conector = sqlite3.connect('MeuEquilibrio.bd')
        self.cursor = self.conector.cursor()

        self.cursor.execute("SELECT frase FROM cartaoum ORDER BY frase")
        resultado = self.cursor.fetchall()

        if len(resultado) != 0:

            self.cursor.execute("SELECT frase FROM cartaoum ORDER BY frase")

            listaCartao = []
            for i in self.cursor:
                listaCartao.append(i[0])
        
            controle = 0

            for i in listaCartao:

                self.cartaoum['text'] = listaCartao[controle]
                controle += 1

        else:
            self.cartaoum['text'] = ''

        self.cursor.execute("SELECT frase FROM cartaodois ORDER BY frase")
        resultado = self.cursor.fetchall()


        if len(resultado) != 0:

            self.cursor.execute("SELECT frase FROM cartaodois ORDER BY frase")

            listaCartao = []
            for i in self.cursor:
                listaCartao.append(i[0])
        
            controle = 0

            for i in listaCartao:

                self.cartaodois['text'] = listaCartao[controle]
                controle += 1

        else:
            self.cartaodois['text'] = ''


        self.cursor.execute("SELECT frase FROM cartaotres ORDER BY frase")
        resultado = self.cursor.fetchall()

        if len(resultado) != 0:

            self.cursor.execute("SELECT frase FROM cartaotres ORDER BY frase")

            listaCartao = []
            for i in self.cursor:
                listaCartao.append(i[0])
        
            controle = 0

            for i in listaCartao:

                self.cartaotres['text'] = listaCartao[controle]
                controle += 1

        else:
            self.cartaotres['text'] = ''

        self.cursor.execute("SELECT frase FROM cartaoquatro ORDER BY frase")
        resultado = self.cursor.fetchall()

        if len(resultado) != 0:

            self.cursor.execute("SELECT frase FROM cartaoquatro ORDER BY frase")

            listaCartao = []
            for i in self.cursor:
                listaCartao.append(i[0])
        
            controle = 0

            for i in listaCartao:

                self.cartaoquatro['text'] = listaCartao[controle]
                controle += 1
        
        else:
            self.cartaoquatro['text'] = ''
                
        self.conector.close()

    # Essa função recebe um valor numérico para cada cartão correspondente
    # (1 para primeiro cartão, et cetera) e com base nesses valores, apaga
    # a mensagem do banco de dados e atualiza o cartão.

    def apagarCartao(self, event):
        self.conector = sqlite3.connect('MeuEquilibrio.bd')
        self.cursor = self.conector.cursor()

        if event == 1:

            fraseSel = self.cartaoum['text']
        
            if fraseSel != '':
        
                self.cursor.execute(f"DELETE FROM cartaoum WHERE frase = '{fraseSel}'")
                self.conector.commit()

                self.scannerBdEnfrent()
            
            else:
                
                self.msgCar['foreground'] = '#FF66A0'
                self.msgCar['text'] = 'Impossível apagar cartão vazio.'

        
        elif event == 2:

            fraseSel = self.cartaodois['text']

            if fraseSel != '':
        
                self.cursor.execute(f"DELETE FROM cartaodois WHERE frase = '{fraseSel}'")
                self.conector.commit()

                self.scannerBdEnfrent()
            
            else:
                
                self.msgCar['foreground'] = '#FF66A0'
                self.msgCar['text'] = 'Impossível apagar cartão vazio.'

        elif event == 3:

            fraseSel = self.cartaotres['text']

            if fraseSel != '':
        
                self.cursor.execute(f"DELETE FROM cartaotres WHERE frase = '{fraseSel}'")
                self.conector.commit()

                self.scannerBdEnfrent()
            
            else:
                
                self.msgCar['foreground'] = '#FF66A0'
                self.msgCar['text'] = 'Impossível apagar cartão vazio.'

        elif event == 4:

            fraseSel = self.cartaoquatro['text']

            if fraseSel != '':
        
                self.cursor.execute(f"DELETE FROM cartaoquatro WHERE frase = '{fraseSel}'")
                self.conector.commit()

                self.scannerBdEnfrent()
            
            else:
                
                self.msgCar['foreground'] = '#FF66A0'
                self.msgCar['text'] = 'Impossível apagar cartão vazio.'


        self.conector.close()

    # Método utilizado para contara os caracteres inseridos no cartão 
    # de enfrentamento. Quando atinge 35 caracteres, o entry bloqueia
    # adição

    def contcarac(self, p):

        aviso = Label(self.janelaCartoes, font = ('open\ Sans', 10, 'bold'), foreground = "#FF66A0", background = "#FFFFFF", text = '')
        aviso.place(relx = 0.7, rely = 0.25, relheight= 0.05, relwidth= 0.12)

        aviso['text'] = F'{str(len(p))} - 30'

        if len(p) >= 30:

            aviso['foreground'] = '#FF66A0'
            return False
        else:
            aviso['foreground'] = '#328EFF'
        return True




# Roda o app. 

if __name__ == "__main__":
    MeuEquilibrio()