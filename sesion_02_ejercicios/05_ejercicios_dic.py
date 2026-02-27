"""
Diccionarios en Python

"""

tasas = {
    "2022" : 2.8,
    "2023" : -0.4,
    "2024" : 3.5,
    "2025" : 3.4,
    "2026" : 3.2
        }

print(tasas["2024"])

for anho, tasa in tasas.items():
    print(f"En el año {anho} la tasa de crecimiento fue de {tasa}%")

