#Scientific Calculator


import math
from math import e
from PySimpleGUI import PySimpleGUI as sg


class Calculator:
    def __init__(self):
        sg.theme('Reddit')

        #layout
        self.layout = [
            [sg.Button('+',size=(15,1)), sg.Button('-',size=(15,1)), sg.Button('*',size=(15,1))],
            [sg.Button('/',size=(15,1)), sg.Button('%',size=(15,1)), sg.Button('10^x',size=(15,1))],
            [sg.Button('e^x',size=(15,1)), sg.Button('x^y',size=(15,1)), sg.Button('x^3',size=(15,1))],
            [sg.Button('x^2',size=(15,1)), sg.Button('Log10',size=(15,1)), sg.Button('Ln',size=(15,1))],
            [sg.Button('x!',size=(15,1)), sg.Button('Square root 2',size=(15,1)), sg.Button('Square root 3',size=(15,1))],
            [sg.Button('x square root y',size=(15,1)), sg.Button('Sin',size=(15,1)), sg.Button('Cos',size=(15,1))],
            [sg.Button('Tan',size=(15,1)), sg.Button('Sinh',size=(15,1)), sg.Button('Cosh',size=(15,1))],
            [sg.Button('Tanh',size=(15,1))], 
            [sg.Text('Operand1',size=(8,1)), sg.Input(key='op1',size=(15,1)), sg.Text('Operand2',size=(8,1)), sg.Input(key='op2',size=(15,1))],  
            [sg.Text('Result',size=(5,1)), sg.Output(key='result',size=(45,1))],
        ]

    def sum(self):
            res=self.op1+self.op2
            print(f'{self.op1}+{self.op2}={res}')

    def sub(self):
            res=self.op1-self.op2
            print(f'{self.op1}-{self.op2}={res}')

    def mult(self):
            res=self.op1*self.op2
            print(f'{self.op1}*{self.op2}={res}')

    def div(self):
            res=self.op1/self.op2
            print(self.op1,'/',self.op2,'=',res)

    def perc(self):
            res=self.op1/100
            print(f'{self.op1}%={res}')

    def expo10(self):
            res=10**self.op1
            print(f'10^{self.op1}={res}')

    def expxy(self):
        res=self.op1**self.op2
        print(f'{self.op1}^{self.op2}')

    def expoe(self):
        res=e**self.op1
        print(f'e^{self.op1}={res}')

    def exp3(self):
        res=self.op1**3
        print(f'{self.op1}^3={res}')

    def exp2(self):
        res=self.op1**2
        print(f'{self.op1}^2={res}')         
      

    def log10(self):
        res=math.log10(self.op1)
        print(f'log10({self.op1})={res}')

    def ln_op(self):
        res=math.log(self.op1)
        print(f'ln{self.op1}={res}') 

    def facto(self):   
        try:
            self.op1=int(self.op1)
            res=math.factorial(self.op1)
            print(f'{self.op1}!={res}') 
        except ValueError:
            print('Factorial must be an integer number.')

    def square_root_two(self):
        try:
            res=int(self.op1)**(1/2)
            print(f'Square root 2 of ({self.op1})={res}')
        except ValueError:
            print('For Square root the operand1 must be an integer.')

    def square_root_three(self):
        try:
            res=int(self.op1)**(1/3)
            print(f'Square root 3 of ({self.op1})={res}')
        except ValueError:
            print('For Square root the operant1 must be an integer.')

    def square_xy(self):
        try:
            res=int(self.op1)**(1/int(self.op2))
            print(f'Square root {self.op1} of ({self.op2})={res}')
        except ValueError:
            print('For Square root the operands must be an integer')

    def trig_sin(self):
        res=math.sin(self.op1)
        print(f'sin({self.op1})={res}')
            
    def trig_cos(self):        
        res=math.cos(self.op1)
        print(f'cos({self.op1})={res}')
        
    def trig_tan(self):
        res=math.tan(self.op1)
        print(f'tan({self.op1})={res}')

    def trig_sinh(self):
        res=math.sinh(self.op1)
        print(f'sinh({self.op1})={res}')
            
    def trig_cosh(self):        
        res=math.cosh(self.op1)
        print(f'cosh({self.op1})={res}')

    def trig_tanh(self):
        res=math.tanh(self.op1)
        print(f'tanh({self.op1})={res}')

    def start(self):

        # create a window in GUI
        self.w1 = sg.Window('Scientific Calculator').layout(self.layout)

        while True:

            # obtain data
            self.event, value = self.w1.read()

            #number validation
            try:
                self.op1=float(value.get('op1'))
                if self.event=='+' or self.event=='-' or self.event=='*' or self.event=='/' or self.event=='x square root y':
                    self.op2=float(value.get('op2'))
            except ValueError:
                print('Only float and integer numbers are accepted.')

            # window closed
            if self.event == sg.WINDOW_CLOSED:            
                break
            
            # cases
            elif self.event == '+':
                c.sum()
            elif self.event=='-':
                c.sub()
            elif self.event == '*':
                c.mult()
            elif self.event=='/':
                c.div()
            elif self.event == '%':
                c.perc()
            elif self.event=='10^x':
                c.expo10()
            elif self.event == 'e^x':
                c.expxy()
            elif self.event=='x^y':
                c.expoe()
            elif self.event == 'x^3':
                c.exp3()
            elif self.event=='x^2':
                c.exp2()
            elif self.event == 'Log10':
                c.log10()
            elif self.event=='Ln':
                c.ln_op()
            elif self.event == 'x!':
                c.facto()
            elif self.event=='Square root 2':
                c.square_root_two()
            elif self.event == 'Square root 3':
                c.square_root_three()
            elif self.event=='x square root y':
                c.square_xy()
            elif self.event == 'Sin':
                c.trig_sin()
            elif self.event=='Cos':
                c.trig_cos()
            elif self.event == 'Tan':
                c.trig_tan()
            elif self.event=='Sinh':
                c.trig_sinh()
            elif self.event == 'Cosh':
                c.trig_cosh()
            elif self.event=='Tanh':
                c.trig_tanh()


c=Calculator()
c.start()