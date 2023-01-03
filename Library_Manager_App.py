from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

class lib_grid(GridLayout):
    def __init__(self, **kwargs):
        super(lib_grid, self).__init__()
        self.cols = 2

        self.add_widget(Label(text="Student's Name : "))
        self.name = TextInput()
        self.add_widget(self.name)

        self.add_widget(Label(text="Book's Name : "))
        self.book = TextInput()
        self.add_widget(self.book)

        self.add_widget(Label(text="Issue Date Of Book : "))
        self.issue = TextInput()
        self.add_widget(self.issue)

        self.add_widget(Label(text="Return Date Of Book : "))
        self.ret = TextInput()
        self.add_widget(self.ret)

        self.add_widget(Label(text="Fine (If Any) : "))
        self.fine = TextInput()
        self.add_widget(self.fine)

        self.print_button = Button(text="Clik Here To Print Info")
        self.print_button.bind(on_press=self.click_button)
        self.add_widget(self.print_button)

        self.button_clear = Button(text='CLEAR')

        def label_clear(instance):
            self.add_widget(Label(text=" "))
        self.button_clear.bind(on_press=label_clear)
        self.add_widget(self.button_clear)

    def click_button(self, instance):
        print("     Name of student : " + self.name.text)
        print("     Name of book : " + self.book.text)
        print("     Issue date : " + self.issue.text)
        print("     Return date : " + self.ret.text)
        print("     Fine on book : " + self.fine.text)
        print("-------------------------------------------------")

class Library_App(App):
    def build(self):
        return lib_grid()

if __name__ == "__main__":
    Library_App().run()