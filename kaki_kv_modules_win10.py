"""
This is an example of kaki app usin kivy modules.
"""
import os


from kaki.app import App
from kivy.factory import Factory




# main app class for kaki app with kivy modules
class LiveApp(App):

    DEBUG = 1 # set this to 0 make live app not working

    # *.kv files to watch
    KV_FILES = {
        os.path.join(os.getcwd(), "kaki_kivy_module/screenmanager.kv"),
        os.path.join(os.getcwd(), "kaki_kivy_module/loginscreen.kv"),
    }

    # class to watch from *.py files
    CLASSES = {
        "MainScreenManager": "kaki_kivy_module.screenmanager",
        "LoginScreen": "kaki_kivy_module.loginscreen",
    }

    # auto reload path
    AUTORELOADER_PATHS = [
        (".", {"recursive": True}),
    ]


    def build_app(self):

        return Factory.MainScreenManager()




# finally, run the app
if __name__ == "__main__":
    LiveApp().run()