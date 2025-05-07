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

def mostrar_estudiantes_alfabeticamente(estudiantes):
    copia = []
    for e in estudiantes:
        copia.append(e)
    
    for i in range(len(copia)):
        for j in range(i + 1, len(copia)):
            if copia[i]['nombre'] > copia[j]['nombre']:
                temporal = copia[i]
                copia[i] = copia[j]
                copia[j] = temporal
    
    max_longitud = 6
    for e in copia:
        if len(e['nombre']) > max_longitud:
            max_longitud = len(e['nombre'])
    
    linea = '-' * (max_longitud + 10)
    
    print("|NOMBRE".ljust(max_longitud + 1) + "| NOTA" + " |")
    print(linea)
    
    for e in copia:
        nombre = e['nombre'].ljust(max_longitud)
        nota = str(e['nota']).rjust(4)
        print("|" + nombre + "| " + nota + " |")

estudiantes = cargar_estudiantes('estudiantes.csv')
mostrar_estudiantes_alfabeticamente(estudiantes)