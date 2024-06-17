import os

db_path = "datos (1).sqlite3"

# Verificar si el archivo existe
if os.path.exists(db_path):
    print(f"El archivo de la base de datos existe en: {db_path}")
else:
    print(f"El archivo de la base de datos no existe en: {db_path}")

# Verificar permisos del archivo
try:
    with open(db_path, 'r'):
        print(f"Tienes permisos para leer el archivo: {db_path}")
except PermissionError:
    print(f"No tienes permisos para leer el archivo: {db_path}")
