from exporters import CSVExporter, TXTExporter, JSONExporter, PDFExporter

class ProductController:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

        self.exporters = {
            "CSV": CSVExporter,
            "TXT": TXTExporter,
            "JSON": JSONExporter,
            "PDF": PDFExporter
        }

        self.vista.btn_export.config(command=self.exportar_productos)

    def exportar_productos(self):
        formato = self.vista.obtener_formato_seleccionado()
        
        productos = self.modelo.obtener_productos()
        if not productos:
            self.vista.mostrar_mensaje("Sin Datos", "No hay productos disponibles para exportar.", "error")
            return

        ruta_archivo = self.vista.solicitar_ruta_guardado(formato)
        if not ruta_archivo:
            return  

        ExporterClass = self.exporters.get(formato)
        
        if ExporterClass:
            exporter = ExporterClass()
            try:
                exporter.export(productos, ruta_archivo)
                self.vista.mostrar_mensaje(
                    "Exportación Exitosa", 
                    f"El reporte se ha exportado correctamente en formato {formato}."
                )
            except Exception as e:
                self.vista.mostrar_mensaje("Error", f"Ocurrió un error al exportar: {e}", "error")