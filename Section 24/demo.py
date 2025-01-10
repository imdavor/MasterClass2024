from fpdf import FPDF


# customiziramo i overridamo header
class PDF(FPDF):
    def header(self):
        self.image("images/logo.png", 10, 8, 33)
        self.set_font("helvetica", "B", 16)
        self.cell(80)
        self.cell(40, 10, "Hello World!", border=1, align="C")
        self.ln(40)

    def footer(self):
        self.set_y(-15)
        self.set_font("helvetica", "I", 16)
        self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", align="C")


# da bi koristio feature instaliranog paketa, moram kreirati objekt
pdf = PDF()

# osnovne postavke pagea
pdf.add_page()
pdf.set_font("helvetica", "B", 16)
for i in range(1, 41):
    pdf.cell(0, 10, f"Printing line number {i}", new_x="LMARGIN", new_y="NEXT")

pdf.output("pdf/sample.pdf")
