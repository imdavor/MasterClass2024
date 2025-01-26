from tkinter import *
import pyqrcode
from fpdf import FPDF
from tkinter import messagebox


class PDFCV(FPDF):
    def header(self):
        self.image("mywebsite.png", 10, 8, 33, title="Portfolio Site")

    def footer(self):
        pass

    def generate_cv(
        self, name, email, phone, address, skills, work_expirience, education, about_me
    ):
        self.add_page()
        self.ln(20)

        # display the name
        self.set_font("helvetica", "B", 26)
        self.cell(0, 10, name, new_x="LMARGIN", new_y="NEXT", align="C")
        # Contact info
        self.set_font("helvetica", "B", 12)
        self.cell(
            0, 10, "Contact Information", new_x="LMARGIN", new_y="NEXT", align="L"
        )
        # contact details
        self.set_font("helvetica", "", 10)
        self.cell(
            0, 5, "Email: {}".format(email), new_x="LMARGIN", new_y="NEXT", align="L"
        )
        self.cell(
            0, 5, "Phone: {}".format(phone), new_x="LMARGIN", new_y="NEXT", align="L"
        )
        self.cell(
            0,
            5,
            "Address: {}".format(address),
            new_x="LMARGIN",
            new_y="NEXT",
            align="L",
        )

        # Skills
        self.ln(10)
        self.set_font("helvetica", "B", 26)
        self.cell(0, 10, "Skills", new_x="LMARGIN", new_y="NEXT", align="L")
        # adding skills
        self.set_font("helvetica", "", 10)
        for skill in skills:
            self.cell(0, 5, "- {}".format(skill), new_x="LMARGIN", new_y="NEXT")

        # Work expirience
        self.ln(10)
        self.set_font("helvetica", "B", 26)
        self.cell(0, 10, "Work expirience", new_x="LMARGIN", new_y="NEXT", align="L")
        # adding expiriences
        self.set_font("helvetica", "", 10)
        for expirience in work_expirience:
            self.cell(
                0,
                5,
                "{}: {}".format(expirience["title"], expirience["description"]),
                new_x="LMARGIN",
                new_y="NEXT",
            )

        # Education
        self.ln(10)
        self.set_font("helvetica", "B", 26)
        self.cell(0, 10, "Education", new_x="LMARGIN", new_y="NEXT", align="L")
        # adding skills
        self.set_font("helvetica", "", 10)
        for education_item in education:
            self.cell(
                0,
                5,
                "{}: {}".format(education_item["degree"], education_item["university"]),
                new_x="LMARGIN",
                new_y="NEXT",
            )

        # About me
        self.ln(10)
        self.set_font("helvetica", "B", 26)
        self.cell(0, 10, "About me", new_x="LMARGIN", new_y="NEXT", align="L")
        # adding about me
        self.set_font("helvetica", "", 10)
        self.multi_cell(0, 5, about_me)

        self.output("cv1.pdf")


def generate_cv_pdf():
    name = entry_name.get()
    email = entry_email.get()
    phone = entry_phone.get()
    address = entry_address.get()
    website = entry_website.get()
    skills = entry_skills.get("1.0", END).strip().split("\n")

    work_expirience = []
    education = []

    work_expirience_lines = entry_work_expirience.get("1.0", END).strip().split("\n")
    for line in work_expirience_lines:
        title, description = line.split(":")
        work_expirience.append(
            {"title": title.strip(), "description": description.strip()}
        )

    education_lines = entry_education.get("1.0", END).strip().split("\n")
    for line in education_lines:
        degree, university = line.split(":")
        education.append({"degree": degree.strip(), "university": university.strip()})

    about_me = entry_about_me.get("1.0", END)

    # create QR code
    qrcode = pyqrcode.create(website)
    qrcode.png("mywebsite.png", scale=6)

    if not name or not email or not phone or not address or not skills or not education:
        messagebox.showerror("Error", "Please fill in all details")
        return

    cv = PDFCV()
    cv.generate_cv(
        name, email, phone, address, skills, work_expirience, education, about_me
    )


window = Tk()
window.title("CV Generator")

label_name = Label(
    window,
    text="Name: ",
)
label_name.pack()
entry_name = Entry(window)
entry_name.pack()

label_email = Label(
    window,
    text="Email: ",
)
label_email.pack()
entry_email = Entry(window)
entry_email.pack()

label_phone = Label(
    window,
    text="Phone: ",
)
label_phone.pack()
entry_phone = Entry(window)
entry_phone.pack()

label_address = Label(
    window,
    text="Address: ",
)
label_address.pack()
entry_address = Entry(window)
entry_address.pack()

label_website = Label(
    window,
    text="Website: ",
)
label_website.pack()
entry_website = Entry(window)
entry_website.pack()

label_skills = Label(window, text="Skills (Enter one skill per line)")
label_skills.pack()
entry_skills = Text(window, height=5)
entry_skills.pack()

label_work_expirience = Label(window, text="Work expirience (Enter one per line)")
label_work_expirience.pack()
entry_work_expirience = Text(window, height=5)
entry_work_expirience.pack()

label_education = Label(window, text="Education (Enter one per line)")
label_education.pack()
entry_education = Text(window, height=5)
entry_education.pack()

label_about_me = Label(window, text="About me")
label_about_me.pack()
entry_about_me = Text(window, height=5)
entry_about_me.pack()

button = Button(window, text="Generate CV", command=generate_cv_pdf)
button.pack()


window.mainloop()
