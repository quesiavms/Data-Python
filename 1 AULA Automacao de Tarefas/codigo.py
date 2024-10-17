# Passo 1: Entrar no sistema da empresa: https://dlp.hashtagtreinamentos.com/python/intensivao/login
import pyautogui
import time
#pack pyautogui funciona como mouse e teclado do seu computador
#pyautogui.write -> escreve um texto
#pyautogui.click -> clicar com o mouse
#pyautogui.press -> apertar uma tecla
#pyautogui.hotkey -> apertar um atalho de teclado (ctrl, c)

#pausa porque se nao ele faz tudo de uma vez e nada aconteceBOHA000251
#pausa de 0.3 para tudo carregar e ele pausar em cada comando do pyautogui
pyautogui.PAUSE = 0.5
#abrir o navegador
#apertar a tecla win    
pyautogui.press('win')
#escreve edge (pesquisando)
pyautogui.write('edge')
#aperta enter para entrar no edge   Camisa  2   25.0    
pyautogui.press('enter')
#entrar no browser e escrever link
link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
pyautogui.write(link)
#enter para entrar no site
pyautogui.press('enter')

#pausa para um momento especifico, talvez por problemas de internet ou algo do tipo, prevenção de dar erro e o codigo nao se atropelar
time.sleep(3) #3 segundos de pausa

# Passo 2: Fazer login no sistema
#click é o click do mouse11.0   Conferir estoque    
pyautogui.click(x=620, y=495) #com clicks(3), daria 3 clicks seguidos
pyautogui.write('quesia@gmail.com')
#passar para proximo campo
pyautogui.press('tab')
pyautogui.write('senha123')
#apertar botao de login
pyautogui.click(x=921, y=694) #tambem seria possivel com um tab enter
#sempre que acessar algo relacionado a internet, recomendavel essa pausa, por lack de internet
time.sleep(2)

# Passo 3: Importar base de dados
import pandas

tabela = pandas.read_csv('produtos.csv')

# Passo 4: Cadastrar 1 produto


#inserindo nos campos
# Passo 5: Repetir o processo de cadastro até acabar os produtos
#para cada linha da minha tabela execute o comando
for linha in tabela.index: 
    #clicando no primeiro campo para preencher
    pyautogui.click(x=764, y=345)
    #str, tranformando em texto para o codigo escrever
    #codigo
    codigo = tabela.loc[linha,'codigo']
    pyautogui.write(str(codigo))
    pyautogui.press('tab')

    #marca
    marca = tabela.loc[linha, 'marca']
    pyautogui.write(str(marca))
    pyautogui.press('tab')

    #tipo
    tipo = tabela.loc[linha, 'tipo']
    pyautogui.write(str(tipo))
    pyautogui.press('tab')

    #categoria
    categoria = tabela.loc[linha, 'categoria']
    pyautogui.write(str(categoria))
    pyautogui.press('tab')

    #preço unitario
    preco = tabela.loc[linha, 'preco_unitario']
    pyautogui.write(str(preco))
    pyautogui.press('tab')

    #custo do produto
    custo = tabela.loc[linha, 'custo']
    pyautogui.write(str(custo))
    pyautogui.press('tab')

    #observação
    #nan = not a number = vazio
    obs = tabela.loc[linha, 'obs']
    if not pandas.isna(obs): #se nao tiver vazia, escreve
        pyautogui.write(str(obs))
    pyautogui.press('tab')

    #clicar no botao enviar
    pyautogui.press('enter')
    #scroll pra voltar pro inicio
    pyautogui.scroll(2000)
