from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

class Calculator(App):

    def build(self):
        widget_root = BoxLayout(orientation='vertical')
        label = Label(size_hint_y=0.75, font_size=50)
        symbol_button = ('+', '1', '2', '3',
                         '-', '4', '5', '6',
                         '*', '7', '8', '9',
                         '/', '.', '0', '=')
        grid_button = GridLayout(cols=4, size_hint_y=2)
        for symbol in symbol_button:
            grid_button.add_widget(Button(text=symbol))

        button_clear = Button(text='CLEAR', size_hint_y=None, height=100)

        def text_print_button(instance):
            label.text += instance.text

        for button in grid_button.children[1:]:
            button.bind(on_press=text_print_button)

        def label_text_size(label_ob, new_height):
            label_ob.fontsize = 0.5*label_ob.height

        label.bind(height=label_text_size)

        def result(instance):
            try:
                label.text = str(eval(label.text))
            except Exception as e:
                print("Error : "+str(e))

        grid_button.children[0].bind(on_press=result)

        def label_clear(instance):
            label.text = " "
        button_clear.bind(on_press=label_clear)

        widget_root.add_widget(label)
        widget_root.add_widget(grid_button)
        widget_root.add_widget(button_clear)

        return widget_root

if __name__ == "__main__":
    Calculator().run()
