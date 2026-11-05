import os
import tkinter as tk
from tkinter import messagebox

class LoginView:

    def __init__(self, root):
        self.root = root

        self.root.title("Login")
        self.root.geometry("1080x720")
        self.root.configure(bg="#00A8E8")  # Fondo Azul Celeste
        self.root.resizable(False, False)

        self.titulo = tk.Label(
            root,
            text="LOGIN",
            font=("Gill Sans", 24, "bold"),
            bg="#00A8E8",                  # Fondo Azul Celeste
            fg="#151A60"
        )
        self.titulo.pack(pady=20)

        self.lbl_email = tk.Label(
            root,
            text="Email:",
            font=("Gill Sans", 12),
            bg="#00A8E8"                  # Fondo Azul Celeste
        )
        self.lbl_email.pack()

        self.entry_email = tk.Entry(
            root,
            width=35,
            font=("Gill Sans", 12)
        )
        self.entry_email.pack(pady=5)

        self.lbl_password = tk.Label(
            root,
            text="Password:",
            font=("Gill Sans", 12),
            bg="#00A8E8"                  # Fondo Azul Celeste
        )
        self.lbl_password.pack()

        self.entry_password = tk.Entry(
            root,
            width=35,
            font=("Gill Sans", 12),
            show="*"
        )
        self.entry_password.pack(pady=5)

        self.btn_login = tk.Button(
            root,
            text="Enter",
            width=20,
            bg="#151A60",
            fg="white",
            font=("Gill Sans", 12, "bold"),
            cursor="hand2"
        )
        self.btn_login.pack(pady=15)

        self.btn_register = tk.Button(
            root,
            text="Create account",
            width=20,
            bg="#FF6B35",                  # Botón Naranja
            fg="white",
            font=("Gill Sans", 11),
            cursor="hand2"
        )
        self.btn_register.pack()

    def obtener_datos(self):
        email = self.entry_email.get().strip()
        password = self.entry_password.get()
        return email, password

    def limpiar_campos(self):
        self.entry_email.delete(0, tk.END)
        self.entry_password.delete(0, tk.END)

    def mostrar_mensaje(self, titulo, mensaje, tipo="info"):
        if tipo == "error":
            messagebox.showerror(titulo, mensaje, parent=self.root)
        else:
            messagebox.showinfo(titulo, mensaje, parent=self.root)
