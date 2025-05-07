import csv

def cargar_estudiantes(archivo_csv):
    estudiantes = []
    with open(archivo_csv) as archivo:
        for nombre, nota in csv.reader(archivo):
            if nombre == 'nombre':
                continue
            try:
                nota = float(nota)
                if 0.0 <= nota <= 5.0:
                    estudiantes.append({'nombre': nombre, 'nota': nota})
                else:
                    print(f'Advertencia: Nota fuera de rango para {nombre}')
            except:
                print(f'Advertencia: Nota inválida para {nombre}')
    return estudiantes

print(cargar_estudiantes('estudiantes.csv'))