#your main Pyhton application file

from kivy.app import App  # This imports the App class form kivy. Every Kivy application must have a class that inherits from App.
from kivy.uix.screenmanager import ScreenManager, Screen #This lets us switch between different screens in the app.
from kivy.lang import Builder #Builder loads the .kv file which defines how the UI looks.
import os # os if a Python modules that helps with file path manipulations


# Load the login UI from login.kv file
Builder.load_file("login.kv")

# Create a screen for login
class LoginScreen(Screen):
    def do_login(self):
        # Get the values entered by the user
        username = self.ids.username.text
        password = self.ids.password.text
        
        # for now, we check againts hardcoded credentials
        if username == "admin" and password == "1234":
            print("Login successful!")
            # later: Switch to payment screen
        
        else:
            print("Incorred username or password")
            
# Create a screen manager to manage different screens
class MyScreenManager(ScreenManager):
    pass

# Create the main application class
class PaymentApp(App):
    def build(self):
            return MyScreenManager()
        
# Run the application
if __name__ == "__main__":
    PaymentApp().run()
    
        