from fpdf import FPDF


# customiziramo header
class PDF(FPDF):
    def header(self):
        self.image("images/logo.png", 100, 8, 75)
        self.set_font("helvetica", "B", 16)
        self.cell(80)
        self.cell(40, 10, "Hello World!")


# da bi koristio feature instaliranog paketa, moram kreirati objekt
pdf = PDF()

# osnovne postavke pagea
pdf.add_page()

pdf.output("pdf/sample.pdf")
