from flask import Flask, jsonify

# Para comenzar, creamos una instancia de la aplicación Flask usando la sintaxis app = Flask(_name_)

app = Flask(_name_)

#Después, creamos una lista de nombres de personas. Esta lista puede ser generada dinámicamente, aunque en este caso la definiremos estáticamente.
#la definimos nosotros mismos

personas = ["Carlos", "Alexandra", "Alberto", "Lucia"]

#A continuación, establecemos la ruta del punto final (endpoint) que usaremos para manejar las solicitudes.


@app.route('/personas', methods=['GET'])
def obtener_personas():

#Aquí convertimos la lista de nombres al formato JSON para que sea legible tanto en nuestro navegador como en otras aplicaciones.

    return jsonify(personas)

#Ejecutar la aplicacion Flask

if _name_ == '_main_':
    app.run(debug=True)