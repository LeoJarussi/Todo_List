import PySimpleGUI as sg

#layout
def criar_nova_janela():
    sg.theme('DarkBlue4')
    linha = [
    [sg.Checkbox(''), sg.Input('')]
    ]

    layout = [
        [sg.Frame('Tafefas', layout= linha , key='container')],
        [sg.Button('Nova Tarefa'), sg.Button('Resetar')]
    ]

    return sg.Window('Todo List', layout=layout, finalize=True)
    

#Criar a janela
janela = criar_nova_janela()

# regras
while True: 
    event , values = janela.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Nova Tarefa':
        janela.extend_layout(janela['container'], [[sg.Checkbox(''), sg.Input('')]])

    elif event == 'Resetar':
        janela.close()
        janela = criar_nova_janela()    