from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup


# class ConfirmButton(Button):
#     def on_touch_down(self, touch):
#         popup = Popup(title='Test popup', content=Label(text='Hello world'),
#                       auto_dismiss=False)
#         popup.open()


# class LoginScreen(GridLayout):

#     def __init__(self, **kwargs):
#         super(LoginScreen, self).__init__(**kwargs)
#         self.cols = 2
#         self.add_widget(Label(text='User Name'))
#         self.username = TextInput(multiline=False)
#         self.add_widget(self.username)
#         self.add_widget(Label(text='password'))
#         self.password = TextInput(password=True, multiline=False)
#         self.add_widget(self.password)

#         self.confirm_btn = ConfirmButton()
#         self.add_widget(self.confirm_btn)


# class MyApp(App):

#     def build(self):
#         return LoginScreen()


# -------------------------------------------------------------------------------


class RootWidget(BoxLayout):
    pass


class MainApp(App):

    def build(self):
        self.root = root = RootWidget()
        return root


if __name__ == '__main__':
    MainApp().run()