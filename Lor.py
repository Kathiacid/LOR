###LOR

def print_calificacion(calificacion, puntuacion):
    print("════════════════════════════════════════════════════════════════")
    print(f"🎮✨ CALIFICACIÓN DE PARTIDA ✨🎮")
    print("════════════════════════════════════════════════════════════════")
    
    print(f"\nPuntaje Total: {puntuacion} puntos")
    
    if calificacion == 'S+':
        print(f"╔════════════════════════════════════════╗")
        print(f"║  S+ - ¡Increíble! MVP del equipo.      ║")
        print(f"╚════════════════════════════════════════╝")
    elif calificacion == 'S':
        print(f"╔════════════════════════════════════════╗")
        print(f"║  S - Sobresaliente. Muy bien hecho.    ║")
        print(f"╚════════════════════════════════════════╝")
    elif calificacion == 'A+':
        print(f"╔════════════════════════════════════════╗")
        print(f"║  A+ - Excelente desempeño. ¡Bien!      ║")
        print(f"╚════════════════════════════════════════╝")
    elif calificacion == 'A':
        print(f"╔════════════════════════════════════════╗")
        print(f"║  A - Buen desempeño, pero hay más.     ║")
        print(f"╚════════════════════════════════════════╝")
    elif calificacion == 'B+':
        print(f"╔════════════════════════════════════════╗")
        print(f"║  B+ - Bien, pero aún puedes mejorar.   ║")
        print(f"╚════════════════════════════════════════╝")
    elif calificacion == 'B':
        print(f"╔════════════════════════════════════════╗")
        print(f"║  B - Necesitas mejorar, sigue así.     ║")
        print(f"╚════════════════════════════════════════╝")
    elif calificacion == 'C+':
        print(f"╔════════════════════════════════════════════╗")
        print(f"║  C+ - Algunas fallas, ¡sigue practicando!  ║")
        print(f"╚════════════════════════════════════════════╝")
    elif calificacion == 'C':
        print(f"╔════════════════════════════════════════════╗")
        print(f"║  C - Lo intentaste, pero sigue trabajando. ║")
        print(f"╚════════════════════════════════════════════╝")
    else:
        print(f"╔════════════════════════════════════════╗")
        print(f"║  D - ¡Necesitas mejorar mucho más!     ║")
        print(f"╚════════════════════════════════════════╝")
    

    print("════════════════════════════════════════════════════════════════")


oro_posible = 30000
daño_maximo_nexo = 3000


print("══════════════════════════════════════════════════════════════")
print("🎮✨ BIENVENIDO A LEAGUE OF RANGE ✨🎮")
print("══════════════════════════════════════════════════════════════")


n_kills = int(input('Ingrese numero de kills en partida=\t'))
asistencia = int(input('Ingrese numero de asistencias en partida=\t'))
muertes = int(input('Ingrese numero de muertes en partida=\t'))
daño_final = int(input('Ingrese daño final realizado=\t'))
daño_nexo = int(input('Ingrese daño realizado al nexo en partida=\t'))
if daño_nexo > daño_maximo_nexo:
    daño_nexo = daño_maximo_nexo
    print(f"Daño al Nexo ajustado a {daño_maximo_nexo} para no exceder el máximo.")
    
objetivos = int(input('Ingrese objetivos realizados=\t'))
total_objetivos = int(input('Ingrese cantidad de objetivos realizados por el equipo=\t'))
oro = int(input('Ingrese total de oro obtenido=\t'))
if oro > oro_posible:
    oro = oro_posible
    print(f"El oro ganado se ha ajustado a {oro_posible} para no exceder el máximo.")

    


if muertes == 0:
    KDA = (n_kills + asistencia) * 100  
else:
    KDA = (n_kills + asistencia) / muertes * 100

if total_objetivos == 0:
    participacion = 0  
else:
    participacion = (objetivos / total_objetivos) * 100

if daño_final == 0:
    daño_nexo = 0 
else:
    daño_nexo = (daño_nexo / daño_final) * 100

oro_ganado = (oro / oro_posible) * 100  

Formula_rango = (KDA * 0.3) + (participacion * 0.2) + (daño_nexo * 0.2) + (oro_ganado * 0.3)



if Formula_rango >= 1500:
    calificacion = 'S+'
elif Formula_rango >= 1300:
    calificacion = 'S'
elif Formula_rango >= 1100:
    calificacion = 'A+'
elif Formula_rango >= 900:
    calificacion = 'A'
elif Formula_rango >= 700:
    calificacion = 'B+'
elif Formula_rango >= 500:
    calificacion = 'B'
elif Formula_rango >= 300:
    calificacion = 'C+'
elif Formula_rango >= 100:
    calificacion = 'C'
else:
    calificacion = 'D'

print_calificacion(calificacion, Formula_rango)



