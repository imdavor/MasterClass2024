from fpdf import FPDF

pdf = FPDF()

pdf.add_page()
pdf.set_font("helvetica", size=20)
pdf.write(5, "To find out what's new in tutorial, click")
pdf.set_font(style="U")
link = pdf.add_link(page=2)
pdf.write(5, " here", link)

# add second page
pdf.add_page()
pdf.image("images/logo.png", 10, 10, 20, 0, "", "https://www.google.com")
# adding html
pdf.set_left_margin(60)
pdf.set_font_size(18)
pdf.write_html("<b>Ovo je boldani html text.</b>")

pdf.write_html(
    """ Mozemo dodavati blo koji kod u htmlu i to u vise redova
    <dl>
      <dt>Description title</dt>
      <dd>Description Detail</dd>
    </dl>
    <h1>Big title</h1>
    <section>
        <h2>Section title</h2>
        <p><b>Hello</b> world. <u>I am</u> <i>tired</i>.</p>
        <p><a href="https://github.com/py-pdf/fpdf2">py-pdf/fpdf2 GitHub repo</a></p>
        <p align="right">right aligned text</p>
        <p>i am a paragraph <br>in two parts.</p>
        <font color="#00ff00"><p>hello in green</p></font>
        <font size="7"><p>hello small</p></font>
        <font face="helvetica"><p>hello helvetica</p></font>
        <font face="times"><p>hello times</p></font>
    </section>
    <section>
        <h2>Other section title</h2>
        <ul type="circle">
        <li>unordered</li>
        <li>list</li>
        <li>items</li>
        </ul>
        <ol start="3" type="i">
        <li>ordered</li>
        <li>list</li>
        <li>items</li>
        </ol>
        <br>
        <br>
        <pre>i am preformatted text.</pre>
        <br>
        <blockquote>hello blockquote</blockquote>
        <table width="50%">
        <thead>
            <tr>
            <th width="30%">ID</th>
            <th width="70%">Name</th>
            </tr>
        </thead>
        <tbody>
            <tr>
            <td>1</td>
            <td>Alice</td>
            </tr>
            <tr>
            <td>2</td>
            <td>Bob</td>
            </tr>
        </tbody>
        </table>
    </section>

"""
)

pdf.output("pdf/link.pdf")
