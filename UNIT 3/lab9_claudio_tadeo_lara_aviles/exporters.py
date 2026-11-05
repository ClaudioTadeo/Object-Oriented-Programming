import csv
import json
from fpdf import FPDF

class Exporter:
    
    def export(self, data, file_path):
        raise NotImplementedError("Este método debe ser implementado por la subclase.")


class CSVExporter(Exporter):

    def export(self, data, file_path):
        with open(file_path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            
            writer.writerow(["ID", "Nombre", "Precio"])

            for product in data:
                
                if isinstance(product, dict):
                    writer.writerow([product.get('id'), product.get('nombre'), product.get('precio')])
                else:
                    writer.writerow([product[0], product[1], product[2]])
        print(f"Archivo CSV generado en: {file_path}")


class TXTExporter(Exporter):

    def export(self, data, file_path):
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write("--- REPORTE DE PRODUCTOS ---\n\n")

            for product in data:

                if isinstance(product, dict):
                    file.write(f"ID: {product.get('id')} | Nombre: {product.get('nombre')} | Precio: ${product.get('precio')}\n")
                else:
                    file.write(f"ID: {product[0]} | Nombre: {product[1]} | Precio: ${product[2]}\n")

        print(f"Archivo TXT generado en: {file_path}")


class JSONExporter(Exporter):

    def export(self, data, file_path):

        with open(file_path, 'w', encoding='utf-8') as file:

            json.dump(data, file, indent=4, ensure_ascii=False)

        print(f"Archivo JSON generado en: {file_path}")


class PDFExporter(Exporter):
    def export(self, data, file_path):
        pdf = FPDF()
        pdf.add_page()
        
        pdf.set_font("Arial", 'B', 16)
        pdf.cell(200, 10, txt="Reporte de Inventario de Productos", ln=True, align='C')
        pdf.ln(10)
        
        pdf.set_font("Arial", size=12)
        for product in data:
            if isinstance(product, dict):
                line_text = f"ID: {product.get('id')} | Producto: {product.get('nombre')} - Precio: ${product.get('precio')}"
            else:
                line_text = f"ID: {product[0]} | Producto: {product[1]} - Precio: ${product[2]}"
            pdf.cell(200, 10, txt=line_text, ln=True)
            
        pdf.output(file_path)
        print(f"Archivo PDF generado en: {file_path}")