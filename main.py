from kivy.app import App
from kivy.uix.widget import Widget

class Pomodoro(Widget):
    pass

class PomodoroApp(App):
    def build(self):
        return Pomodoro()

if __name__ == '__main__':
    PomodoroApp().run()