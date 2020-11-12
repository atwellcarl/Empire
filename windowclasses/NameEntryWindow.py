import db_control as db
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.properties import ObjectProperty
from windowclasses import WindowManager as wm

players = {}

class NameEntryWindow(Screen):
    kv = Builder.load_file("stylefolder/NameEntryWindow.kv")
    real_name = ObjectProperty(None)
    fake_name = ObjectProperty(None)




    def register_name(self):
        players[self.real_name.text] = self.fake_name.text

        self.pop_up( "Names Recorded!", "Send the next player \n or start the game")


    def reset_inputs(self):
        self.real_name.text = ""
        self.fake_name.text = ""


    def start_game(self):
        wm.screen_manager.current = "game_window"


    def pop_up(self, header, message):
        popup = Popup(title = header,
                      content = Label(text = message),
                      size_hint = (None, None), size = (400, 400),
                      pos_hint = {"center_x": .5, "center_y": .5 })
        popup.open()
