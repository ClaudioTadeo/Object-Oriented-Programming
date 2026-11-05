import os
import tkinter as tk
from tkinter import messagebox

class RegisterView:

    def __init__(self, root):
        self.ventana = tk.Toplevel(root)

        self.ventana.title("REGISTER USER")
        self.ventana.geometry("1080x720")
        self.ventana.configure(bg="#00A8E8")  # Fondo Azul Celeste
        self.ventana.resizable(False, False)

        self.ventana.transient(root)
        self.ventana.grab_set()

        self.titulo = tk.Label(
            self.ventana,
            text="CREATE ACCOUNT",
            font=("Gill Sans", 20, "bold"),
            bg="#00A8E8",                  # Fondo Azul Celeste
            fg="#FF6B35"                   # Texto del Título Naranja
        )
        self.titulo.pack(pady=18)

        self.lbl_nombre = tk.Label(
            self.ventana,
            text="Full name:",
            bg="#00A8E8",                  # Fondo Azul Celeste
            font=("Gill Sans", 12)
        )
        self.lbl_nombre.pack()

        self.entry_nombre = tk.Entry(
            self.ventana,
            width=30,
            font=("Gill Sans", 12)
        )
        self.entry_nombre.pack(pady=4)

        self.lbl_email = tk.Label(
            self.ventana,
            text="Email:",
            bg="#00A8E8",                  # Fondo Azul Celeste
            font=("Gill Sans", 12)
        )
        self.lbl_email.pack()

        self.entry_email = tk.Entry(
            self.ventana,
            width=30,
            font=("Gill Sans", 12)
        )
        self.entry_email.pack(pady=4)

        self.lbl_password = tk.Label(
            self.ventana,
            text="Password:",
            bg="#00A8E8",                  # Fondo Azul Celeste
            font=("Gill Sans", 12)
        )
        self.lbl_password.pack()

        self.entry_password = tk.Entry(
            self.ventana,
            width=30,
            show="*",
            font=("Gill Sans", 12)
        )
        self.entry_password.pack(pady=4)

        self.lbl_confirmar = tk.Label(
            self.ventana,
            text="Confirm password:",
            bg="#00A8E8",                  # Fondo Azul Celeste
            font=("Gill Sans", 12)
        )
        self.lbl_confirmar.pack()

        self.entry_confirmar = tk.Entry(
            self.ventana,
            width=30,
            show="*",
            font=("Gill Sans", 12)
        )
        self.entry_confirmar.pack(pady=4)

        self.btn_guardar = tk.Button(
            self.ventana,
            text="Register user",
            width=22,
            bg="#FF6B35",                  # Botón Naranja
            fg="white",
            font=("Gill Sans", 12, "bold"),
            cursor="hand2"
        )
        self.btn_guardar.pack(pady=12)

        self.btn_cancelar = tk.Button(
            self.ventana,
            text="Cancel",
            width=25,
            bg="#AC27AE",
            command=self.cerrar,
            cursor="hand2"
        )
        self.btn_cancelar.pack()

        self.entry_nombre.focus_set()

    def obtener_datos(self):
        nombre = self.entry_nombre.get().strip()
        email = self.entry_email.get().strip()
        password = self.entry_password.get()
        confirmar = self.entry_confirmar.get()

        return nombre, email, password, confirmar

    def mostrar_mensaje(self, titulo, mensaje, tipo="info"):
        if tipo == "error":
            messagebox.showerror(
                titulo,
                mensaje,
                parent=self.ventana
            )
        else:
            messagebox.showinfo(
                titulo,
                mensaje,
                parent=self.ventana
            )

    def cerrar(self):
        self.ventana.destroy()
