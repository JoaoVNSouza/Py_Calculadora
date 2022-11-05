import PySimpleGUI as sg


def calculadora(num1, num2, operation='+'):
    ''' Objetivo: Fazer operações matemática com 2 números.

        Parameters:
            num1 (float): primeiro número da operação.
            num2 (float): segundo número da operação.
            operation (char): Símbolo da operação que será realizada, opções (+ - * /).

        Returns:
            rst (float): resultado da operação entre dois números.
    '''

    if operation == '-':
        rst = num1 - num2
    elif operation == '+':
        rst = num1 + num2
    elif operation == '/':
        rst = num1 / num2
    elif operation == '*':
        rst = num1 * num2
    else:
        print('operando inválido')
        return -1

    return rst


# Define the window's contents
layout = [[sg.Text("Número 1:")],     # Part 2 - The Layout
          [sg.Input()],
          [sg.Text("Número 2:")],
          [sg.Input()],
          [sg.Button('+'), sg.Button('-'), sg.Button('*'), sg.Button('/')],
          [sg.Text('')],
          [sg.Text('Resultado: '), sg.Text('', key='rst')],
          [sg.Button('Cancelar')]
          ]

# Create the window
window = sg.Window('Calculadora', layout)       # Part 3 - Window Defintion


# Do something with the information gathered
while True:
    # Display and interact with the Window
    # Part 4 - Event loop or Window.read call
    event, values = window.read()

    if event == 'Cancelar':
        resultado = 2222
        break
    elif event == '+':
        resultado = calculadora(int(values[0]), int(values[1]), '+')
    elif event == '-':
        resultado = calculadora(int(values[0]), int(values[1]), '-')
    elif event == '*':
        resultado = calculadora(int(values[0]), int(values[1]), '*')
    else:
        resultado = calculadora(int(values[0]), int(values[1]), '/')

    window['rst'].update(f'{resultado}')

# Finish up by removing from the screen
window.close()
