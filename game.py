""""""
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

from kivy.core.window import Window

Window.size = (250, 200)
Window.clearcolor = (255/255, 186/255, 3/255, 1)
Window.title = 'Конвертор'

class MyApp(App):
    def __init__(self):
        super().__init__()
        self.label = Label(text='Конвертор')
        self.mil = Label(text='Мили')
        self.metr = Label(text='Метры')
        self.santi = Label(text='Сантиметры')
        self.int_data = TextInput(hint_text = 'Введите значение(км)', multiline = False)
        self.int_data.bind(text = self.on_text)

    def on_text(self, *args):
        data = self.int_data.text
        if data.isnumeric():
            self.mil.text = 'В милях это: ' + str(float(data)*0.62)
            self.metr.text = 'В метрах это: ' + str(float(data)*1000)
            self.santi.text = 'В сантиметрах это: ' + str(float(data) * 100000)
        else:
            self.int_data.text = ''

    def build(self):
        box = BoxLayout(orientation='vertical')
        box.add_widget(self.label)
        box.add_widget(self.int_data)
        box.add_widget(self.mil)
        box.add_widget(self.metr)
        box.add_widget(self.santi)

        return box


if __name__ == '__main__':
    MyApp().run()