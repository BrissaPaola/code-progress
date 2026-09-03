"""
Módulo de funciones de utilidad e ingeniería
"""

def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def calcular_promedio(lista_notas):
    if not lista_notas:
        return 0
    return sum(lista_notas) / len(lista_notas)

if __name__ == "__main__":
    print("--- Módulo de Utilidades Cargado Correctamente ---")
    notas = [95, 88, 90, 100, 85]
    print(f"Promedio de notas de muestra: {calcular_promedio(notas)}")

# Registro de optimización de módulo - versión 1.1

# Registro de optimización de módulo - versión 1.2
