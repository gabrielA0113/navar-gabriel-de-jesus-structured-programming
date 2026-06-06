
name="name"
Lastname="Lastname"
name "Gabriel"
Lastname "Navar"

def generate_email (name,lastname):
    email=f"{name.lower ().{lastname{}}@utd.edu.mx"

"¿deseas agregar otro correo?"(S/N)



"Calculate monthly payment"

P = float(input("Loan amount: "))
annual_rate = float(input("Annual interest rate (%): "))
years = int(input("Loan term (years): "))

r = annual_rate / 12 / 100
n = years * 12

M = P * (r * (1 + r) ** n) / ((1 + r) ** n - 1)

print(f"Monthly payment: ${M:.2f}")