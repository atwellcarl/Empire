import db_control as db
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from windowclasses import WindowManager as wm
from windowclasses import NameEntryWindow
from windowclasses import GameWindow

# if(db.create_user("carlatwell", "Carl", "Atwell", "carlatwell")):
#     print("Success!")
# else:
#     print("Failed to create new user")
#
# if(db.create_exercise("Push Up", "Bodyweight")):
#     print("Success!")
# else:
#     print("Failed to create new exercise")
#
# db.create_workout("HIIT", 2, 15)
# db.create_exercise_record("carlatwell", "Push Up", 10, 3, 0, 1)
# db.create_completed_exercise("Push Up", 1, 10, 3, 0)
# db.create_has_workout("carlatwell", 1, 11, 10, 2020)
# db.close()


screen_manager = wm.WindowManager()
wm.screen_manager = screen_manager
windows = []

windows.append(NameEntryWindow.NameEntryWindow(name = "name_entry_window"))
windows.append(GameWindow.GameWindow(name = "game_window"))


for window in windows:
    screen_manager.add_widget(window)

screen_manager.current = "name_entry_window"


class MyEmpireApp(App):
    def build(self):
        return screen_manager

if __name__ == "__main__":
    MyEmpireApp().run()
