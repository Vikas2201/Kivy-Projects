from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout

class selfie_app(App):

    def make_app(self):

        self.camera = Camera()
        self.camera.resolution = (800, 800)

        self.button = Button(text="Click Me!!")
        self.button.size_hint = (1.6, 1.3)
        self.button.pos_hint = {'x': 0.50, 'y': 50}
        self.button.bind(on_press=self.selfie_take())

        self.layout = BoxLayout()
        self.layout.add_widget(self.camera)
        self.layout.add_widget(self.button)
        return self.layout

    def selfie_take(self, *args):
        print("Selfie successfully taken by the app")
        self.camera.export_to_png('./demo.png')

if __name__ == "__main__":
    selfie_app().run()