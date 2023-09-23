from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

Window.clearcolor = (14/215, 61/215, 76/215, 1)

class Comp(BoxLayout):
    def __init__(self, **kwargs):
        super(Comp, self).__init__(**kwargs)

        self.orientation = 'vertical'
        self.padding = 20

        label1 = Label(
            text='Insira o preço e o peso em gramas dos produtos',
            font_size=14,
        )

        self.add_widget(label1)

        # Produto 1
        box1 = BoxLayout()
        label2 = Label(text='Produto 1')
        label3 = Label(text='Kg ou L')
        label4 = Label(text='', width=0)
        box1.add_widget(label2)
        box1.add_widget(label3)
        box1.add_widget(label4)
        self.add_widget(box1)

        box2 = BoxLayout(spacing=10)
        self.pr1 = TextInput(multiline=False, input_filter='float')
        self.ps1 = TextInput(multiline=False, input_filter='float')
        self.p1 = Label(font_size=20)
        box2.add_widget(self.pr1)
        box2.add_widget(self.ps1)
        box2.add_widget(self.p1)
        self.add_widget(box2)

        # Produto 2
        box3 = BoxLayout()
        label5 = Label(text='Produto 2')
        label6 = Label(text='Kg ou L')
        label7 = Label(text='', width=0)
        box3.add_widget(label5)
        box3.add_widget(label6)
        box3.add_widget(label7)
        self.add_widget(box3)

        box4 = BoxLayout(spacing=10)
        self.pr2 = TextInput(multiline=False, input_filter='float')
        self.ps2 = TextInput(multiline=False, input_filter='float')
        self.p2 = Label(font_size=20)
        box4.add_widget(self.pr2)
        box4.add_widget(self.ps2)
        box4.add_widget(self.p2)
        self.add_widget(box4)

        box5 = BoxLayout(spacing=10)
        label8 = Label(text='Diferença:', font_size=20)
        self.dif = Label(font_size=20)
        box5.add_widget(label8)
        box5.add_widget(self.dif)
        self.add_widget(box5)

        button = Button(text='Comparar')
        button.bind(on_release=self.calc)
        self.add_widget(button)

    def calc(self, instance):
        if self.pr1.text == "" or \
                self.ps1.text == "" or \
                self.pr2.text == "" or \
                self.ps2.text == "":
            self.alerta()
        else:
            pr1 = float(self.pr1.text)
            ps1 = float(self.ps1.text)
            pr2 = float(self.pr2.text)
            ps2 = float(self.ps2.text)

            self.p1.text = str("{:.2f}".format(pr1 / ps1 * 1000))
            self.p2.text = str("{:.2f}".format(pr2 / ps2 * 1000))

            self.dif.text = str("{:.2f}".format((pr1 / ps1) / (pr2 / ps2) * 100)) + ' %'

    def alerta(self):
        layout = BoxLayout(orientation='vertical', padding=10)
        label = Label(text="Preencha todas os campos.")
        ok_button = Button(text="OK")

        layout.add_widget(label)
        layout.add_widget(ok_button)

        popup = Popup(title="Alerta", content=layout, size_hint=(None, None), size=(300, 200))
        ok_button.bind(on_press=popup.dismiss)
        popup.open()

class ComparadorApp(App):
    def build(self):
        return Comp()

ComparadorApp().run()
