import tkinter as tk
from tkinter import ttk, messagebox, filedialog

class ProductView:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de productos e inventario")
        self.root.geometry("600x400")
        self.root.configure(bg="#00A8E8")  # Fondo Azul Celeste

        frame_export = tk.LabelFrame(
            self.root, 
            text="Exportar Inventario", 
            font=("Gill Sans", 11, "bold"),
            bg="#00A8E8",                  # Fondo Azul Celeste
            fg="#151A60" 
        )
        frame_export.pack(fill="x", padx=15, pady=10)

        tk.Label(
            frame_export, 
            text="Formato:", 
            bg="#00A8E8",                  # Fondo Azul Celeste
            font=("Gill Sans", 10)
        ).pack(side="left", padx=5, pady=5)

        self.combo_format = ttk.Combobox(
            frame_export,
            values=["CSV", "TXT", "JSON", "PDF"],
            state="readonly",
            width=10,
        )
        self.combo_format.set("CSV")
        self.combo_format.pack(side="left", padx=5)

        self.btn_export = tk.Button(
            frame_export,
            text="Exportar Reporte",
            bg="#FF6B35",                  # Botón Naranja
            fg="white",
            font=("Gill Sans", 10, "bold")
        )
        self.btn_export.pack(side="left", padx=10)

    def obtener_formato_seleccionado(self):
        return self.combo_format.get()

    def solicitar_ruta_guardado(self, extension):
        filepath = filedialog.asksaveasfilename(
            defaultextension=f".{extension.lower()}",
            filetypes=[(f"Archivos {extension}", f"*.{extension.lower()}")]
        )
        return filepath

    def mostrar_mensaje(self, titulo, mensaje, tipo="info"):
        if tipo == "error":
            messagebox.showerror(titulo, mensaje, parent=self.root)
        else:
            messagebox.showinfo(titulo, mensaje, parent=self.root)
