from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class App_Grid(GridLayout):

    def __init__(self,**kwargs):
        super(App_Grid, self).__init__(**kwargs)

        self.cols = 2

        self.add_widget(Label(text="Name : "))
        self.name = TextInput()
        self.add_widget(self.name)

        self.add_widget(Label(text="Roll no. : "))
        self.roll = TextInput()
        self.add_widget(self.roll)

        self.add_widget(Label(text="Branch"))
        self.branch = TextInput()
        self.add_widget(self.branch)

        self.press = Button(text="Click Me!")
        self.press.bind(on_press=self.Click_Me)
        self.add_widget(self.press)

    def Click_Me(self,instance):
        print("Name of student : "+self.name.text)
        print("Roll no. of student : "+self.roll.text)
        print("Branch of student : "+self.branch.text)

class FirstApp(App):

    def build(self):
        return App_Grid()

if __name__ == "__main__":
    FirstApp().run()