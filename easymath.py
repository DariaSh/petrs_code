from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

from math import sqrt, log, log2

class ExpressionCalculator(App):

    def solveEquation(self):
        equation = self.expression.text
        equation = equation.replace('=', '-(') + ')'
        equation = equation.replace('x', 'j')
        z = eval(equation, {'j': 1j})
        real, imag = z.real, -z.imag
        if imag:
            return real/imag
        if real:
            return "No solution"


    def getAnswer(self, event):
        output = ""
        expr = self.expression.text
        if expr.count("=") == 1 and (expr.count('>') == 0 and expr.count('<') == 0 and expr.count('x') == 0):
            expr = expr.replace("=", "==")
        elif expr.count("ln") == 1:
            expr = expr.replace("ln", "log2")
        elif expr.count("x") >= 1:
            expr = str(self.solveEquation())
        try:
            correct_result = eval(expr)
            output = "Your answer is: " + str(correct_result)
        except:
            output = "Check your expression! Something is wrong!"
        self.mathMessage.text = output

    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.7, 0.8)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}
        self.window.add_widget(Image(source="math_logo.png"))

        self.mathMessage = Label(
            text="Enter your mathematical expression or equation...",
            font_size=30,
            color="#ffffff",
            bold=True
        )
        self.window.add_widget(self.mathMessage)

        self.expression = TextInput(
            multiline=False,
            padding_y=(30, 30),
            size_hint=(1, 0.7),
            font_size=20
        )
        self.window.add_widget(self.expression)

        self.button = Button(
            text="Calculate My Math",
            size_hint=(0.5, 0.5),
            bold=True,
            font_size=30
        )
        self.button.bind(on_press=self.getAnswer)
        self.window.add_widget(self.button)

        return self.window


if __name__ == "__main__":
    ExpressionCalculator().run()
