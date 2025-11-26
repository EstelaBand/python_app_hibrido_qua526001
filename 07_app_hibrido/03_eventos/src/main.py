import flet as ft


def main(page: ft.Page):
    # função do evento
    def exibir_nome(e): # esse ezinho e é o evento que vai programar a funçao do botão
        nome_saida.value = nome.value # receber o valor informado pelo usuário
        nome_saida.update() # update recarrega o valor que o usuário inseriu, mostra na página, como se fosse um F5
    # propriedades da página
    page.title = "App de manipulação de eventos" 
    page.scroll = "adaptive" # ou seja ele se adapta ao conteúdo
    page.theme_mode = ft.ThemeMode.LIGHT # aqui estou passando para o modo claro a página, melhor para desenvolver. O padrão é escuro então se não colocar claro ele assumirá escuro.

    # declaração de variáveis antes do page add ele vai declarar as variáveis que ele quer q o usuário 
    nome = ft.TextField(label="Informe seu nome", on_submit=exibir_nome) #ft.textfield é o input da janela, como se fosse a função input que estudamos, o on submit faz o enter funcionar após digitar o nome 
    nome_saida = ft.Text() #esse é o print ft.text, como se fosse a função print q estudamos


    page.add(
        ft.SafeArea(  # é onde está escrito trabalhando com eventos
            ft.Container(
                ft.Text("Trabalhando com Eventos", size=35, weight="bold"), #bold deixa texto em negrito
                alignment=ft.alignment.center,
            ),
            expand=True,
        ),
        nome, 
        ft.ElevatedButton("Enviar", on_click=exibir_nome), # on click vai chamar a função
        nome_saida
            
    )


ft.app(main)
