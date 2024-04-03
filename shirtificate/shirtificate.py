from fpdf import FPDF

def main():
    student = input("Enter your name: ")
    shirtificate = FPDF('Portrait','mm', 'A4')
    shirtificate.add_page()
    shirtificate.set_xy(0, 10)
    shirtificate.set_font("Arial", 'B', 16)
    shirtificate.cell(210, 10, txt="CS50 Shirtificate", ln=True, align='C')
    shirtificate.ln(20)  # Move down 20mm
    shirtificate.set_font("Arial", 'B', 14)
    shirtificate.cell(210, 10, txt=student, ln=True, align='C', fill=True)
    shirtificate.image("shirtificate.png", x=55, y=65, w=100)
    shirtificate.output("shirtificate.pdf")

if __name__ == "__main__":
    main()
