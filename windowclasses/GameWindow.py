import db_control as db
import random
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from windowclasses import WindowManager as wm
from windowclasses import NameEntryWindow

class GameWindow(Screen):
    kv = Builder.load_file("stylefolder/GameWindow.kv")

    game_text = ObjectProperty(None)

    def set_game(self):
        # get all names from fake db
        fake_names_db = db.get_fake_names()
        # choose 2
        list_fake_names = []
        for player in NameEntryWindow.players:
            list_fake_names.append(NameEntryWindow.players[player])
            db.create_fake_name(NameEntryWindow.players[player], player)

        for i in range (2):
            not_unique = True
            while(not_unique):
                db_name = random.choice(fake_names_db)
                if(db_name not in list_fake_names):
                    list_fake_names.append(db_name)
                    not_unique = False

        random.shuffle(list_fake_names)
        random.shuffle(list_fake_names)

        output = ""
        for name in list_fake_names:
            output += "{}\n".format(name)
        # create list scramble names
        # display names

        self.game_text.text = output
