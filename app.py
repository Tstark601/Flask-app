from flask import Flask, jsonify, request

# Crear una instancia de la aplicación Flask
app = Flask(__name__)

# Lista de personas con información detallada
personas = [
    {"id": 1, "nombre": "Andres", "apellido": "Perez", "edad": 25, "ciudad": "Bogota"},
    {"id": 2, "nombre": "Laura", "apellido": "Gomez", "edad": 30, "ciudad": "Medellin"},
    {"id": 3, "nombre": "Camilo", "apellido": "Torres", "edad": 28, "ciudad": "Cali"},
    {"id": 4, "nombre": "Sofia", "apellido": "Ramirez", "edad": 35, "ciudad": "Barranquilla"},
    {"id": 5, "nombre": "Mateo", "apellido": "Jimenez", "edad": 27, "ciudad": "Cartagena"},
    {"id": 6, "nombre": "Valentina", "apellido": "Herrera", "edad": 32, "ciudad": "Pereira"},
    {"id": 7, "nombre": "Carlos", "apellido": "Lopez", "edad": 40, "ciudad": "Bogota"},
    {"id": 8, "nombre": "Fernanda", "apellido": "Martinez", "edad": 28, "ciudad": "Cali"},
    {"id": 9, "nombre": "Jorge", "apellido": "Rios", "edad": 30, "ciudad": "Medellin"},
    {"id": 10, "nombre": "Daniela", "apellido": "Castaño", "edad": 25, "ciudad": "Bogota"},
    {"id": 11, "nombre": "Alejandro", "apellido": "Mendoza", "edad": 35, "ciudad": "Barranquilla"},
    {"id": 12, "nombre": "Natalia", "apellido": "Fernandez", "edad": 32, "ciudad": "Pereira"},
    {"id": 13, "nombre": "Sebastian", "apellido": "Castro", "edad": 27, "ciudad": "Cartagena"},
    {"id": 14, "nombre": "Andrea", "apellido": "Ortega", "edad": 40, "ciudad": "Medellin"},
    {"id": 15, "nombre": "Mariana", "apellido": "Gutierrez", "edad": 28, "ciudad": "Cali"}
]

@app.route('/personas', methods=['GET'])
def obtener_personas():
    """
    Función de vista que devuelve una lista de objetos con información detallada de las personas en formato JSON.
    Permite filtrar por cualquier atributo (nombre, apellido, ciudad, edad, etc.) usando parámetros de consulta.

    Returns:
        Response: Objeto de respuesta JSON con la lista de personas filtrada.
    """
    filtro = request.args
    resultado = []

    # Filtrar por cada parámetro proporcionado en la solicitud
    for persona in personas:
        coincide = True
        for clave, valor in filtro.items():
            if str(persona.get(clave, '')).lower() != valor.lower():
                coincide = False
                break
        if coincide:
            resultado.append(persona)

    return jsonify(resultado)

# Punto de entrada para ejecutar la aplicación Flask
if __name__ == '__main__':
    # Ejecutar la aplicación en modo debug para facilitar el desarrollo
    app.run(debug=True)
