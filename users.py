import json

def generar_json(correos):
    # Crear la estructura inicial del JSON
    query = {
        "query": {
            "bool": {
                "should": [],
                "minimum_should_match": 1
            }
        }
    }
    
    # Procesar cada correo y agregarlo al JSON
    for correo in correos:
        query["query"]["bool"]["should"].append({
            "match_phrase": {
                "data.office365.UserId": correo.strip()
            }
        })
    
    return query

def main():
    print("Pega el listado completo de correos (uno por línea) y presiona Enter dos veces para generar el JSON:\n")
    # Leer el listado de correos del usuario
    correos_raw = []
    while True:
        linea = input()
        if linea.strip() == "":
            break
        correos_raw.append(linea.strip())
    
    # Generar el JSON
    resultado = generar_json(correos_raw)
    
    # Guardar el JSON en un archivo
    with open("resultado.json", "w") as file:
        json.dump(resultado, file, indent=4)
    
    print("\nJSON generado con éxito y guardado en 'resultado.json'.")

if __name__ == "__main__":
    main()
