import tkinter as tk
from models.userModel import UserModel
from views.loginView import LoginView
from controllers.authenticationController import AuthenticationController

class System:
    def __init__(self):
        self.root = tk.Tk()
        self.modelo = UserModel()
        self.vista = LoginView(self.root)
        self.controlador = AuthenticationController(self.modelo, self.vista)

    def start(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = System()
    app.start()