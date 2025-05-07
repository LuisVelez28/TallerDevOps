from estudiantes.registro import cargar_estudiantes, mostrar_estudiantes_alfabeticamente, mostrar_promedio

def main():
    archivo_csv = 'estudiantes.csv'
    estudiantes = cargar_estudiantes(archivo_csv)
    
if __name__ == "__main__":
    main()