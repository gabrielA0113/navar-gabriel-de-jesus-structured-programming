
def obtener_datos_estudiante():
    """Solicita los datos al usuario y los guarda en un diccionario."""
    student = {}
    
    student["name"] = input("Enter your name: ")
    
    # Usamos un bucle para asegurarnos de que introduzcan números válidos (1-10)
    student["programming"] = int(input("Programming skills (1-10): "))
    student["design"] = int(input("UI design skills (1-10): "))
    student["networking"] = int(input("Networking skills (1-10): "))
    
    return student


def evaluar_carrera(student):
    """Analiza las habilidades del diccionario y determina la carrera."""

    prog = student["programming"]
    des = student["design"]
    net = student["networking"]
    
    print(f"\n Resultados para {student['name']} ---")
    
   
    if prog > 8:
        print("Suggested Career: Software Developer")
    elif des > 6:
        print("Suggested Career: UI/UX Designer")
    elif net > 7:
        print("Suggested Career: Network Administrator")
    elif prog > 6 and des > 8:
        print("Multiple Career Paths Identified")
    else:
        print("General IT Specialist / Keep exploring options!")



if __name__ == "__main__":

    datos_alumno = obtener_datos_estudiante()
    
    evaluar_carrera(datos_alumno)

