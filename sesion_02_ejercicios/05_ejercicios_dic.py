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
# 
print(tasas["2024"])

for key, value in tasas.items():
    print(f"En el año {key} la tasa de crecimiento fue de {value}%")

for key in tasas.keys():
    print(f"En el año {key}")

for key in tasas:
    print(f"En el año {key}")


for value in tasas.values():
    print(f"La tasa de crecimiento fue de {value}%")