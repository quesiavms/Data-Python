# Tela Inicial
    #Titulo: QueZap
    # Botao: iniciar chat
        #quando clicar no botao:
        #abrir um pop up/modal/alert
            #Titulo: Bem vindo ao QueZap
            #Caixa de texto: Escreva seu nome no chat
            #Botao entrar no chat
    #Botao entrar no chat:
        #Sumir com o titulo
        #Sumir botao de iniciar chat
            #carregar o chat
            #caregar o campo de enviar mensagem: Digite a sua mensagem
            #Botao enviar:
                #quando clicar no botao enviar
                #enviar a mensagem
                #limpar a caixa de mensagem
                
#Flet
#importar Flet
import flet as ft

#criar funcao principal pra rodar o seu aplicativo
def main(pagina):
    #titulo
    titulo = ft.Text('QueZap') 
    
    #webscoket - tunel de comunicacao entre dois usuarios
    #criando funcao do tunel
    def enviar_msg_tunel(mensagem): 
        #executar tudo o que eu quero que acontece para todos os usuarios que recerem a mensagem
        texto = ft.Text(mensagem)
        chat.controls.append(texto)
        pagina.update()
    
    #criando tunel de comunicação
    pagina.pubsub.subscribe(enviar_msg_tunel)
    
    #pegar os lugares onde enviava mensagem e jogar elas no tunel 
    
    def enviar_msg(evento):
        nome_usuario = caixa_nome.value #pegando nome do usuario
        texto_campo_mensagem = campo_enviarmsg.value #pegando o texto que o usuario escreveu
        mensagem = f'{nome_usuario}: {texto_campo_mensagem}' #concatenando tudo 
        pagina.pubsub.send_all(mensagem) #jogando as mensagem no tunel
        #limpar caixa de add mensagem
        campo_enviarmsg.value = '' 
        pagina.update() #atualizando a tela
        
    campo_enviarmsg = ft.TextField(label= 'Digite sua mensagem', on_submit=enviar_msg)
    botao_enviarmsg = ft.ElevatedButton('Enviar', on_click= enviar_msg)
    #uma linha com varios campos, os campos vao ficar um do lado do outro
    linha_enviar = ft.Row([campo_enviarmsg, botao_enviarmsg])
    #uma coluna com as mensagem que as pessoas enviarem (que nem chat mesmo, um embaixo do outro)
    chat = ft.Column()
    
    def entrar_chat(evento):
        #fechar o popup
        popup.open = False
        #sumir com o titulo
        pagina.remove(titulo)
        #sumir com o botao iniciar chat
        pagina.remove(botao)
        #carregar chat
        pagina.add(chat)
        #carregar o campo de enviar mensagem, e botao
        pagina.add(linha_enviar)
        #adicionar mensagem que usuario entrou no chat
        nome_usuario = caixa_nome.value
        mensagem = f'{nome_usuario} entrou no chat'
        pagina.pubsub.send_all(mensagem)
                
        pagina.update() #atualizar telinha para o usuario
    
    #criando pop up
    titulo_popup = ft.Text('Bem vindo ao QueZap')
    caixa_nome = ft.TextField(label= 'Digite o seu nome')
    botao_popup = ft.ElevatedButton('Entrar no chat', on_click = entrar_chat)
    popup = ft.AlertDialog(title=titulo_popup, content=caixa_nome, actions=[botao_popup]) #possivel colocar mais botoes por ser lista
    
    #botao inicial
    def abrir_popup(evento): #sempre e toda funcao com on_click é obrigatorio evento de parametro, always
        pagina.dialog = popup #toda pagina só pode ter um unico popup, onde é sempre usado o .dialog
        popup.open = True
        pagina.update() #atualiza a tela para que o usuario veja, agora com popup

    botao = ft.ElevatedButton('Iniciar Chat', on_click= abrir_popup)
    
    
    
    #adicionando os elementos na tela
    pagina.add(titulo)
    pagina.add(botao)
    
    
#executar funcao com o flet
ft.app(main, view=ft.AppView.WEB_BROWSER)
#view altera visualizacao do app view=ft.WEB_BROWSER