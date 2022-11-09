from flask import Flask, render_template

app = Flask(__name__)

#Crea una ruta raíz ("/") que responda con "¡Hola Mundo!"
@app.route('/')
def hola_mundo():
    return 'Hola Mundo!'


#Crea una ruta que responda con "¡Dojo!"
@app.route('/dojo')
def dojo():
    return '¡Dojo!'


#Crea una ruta que responda con "Hola" y el nombre que esté en la URL después de /say/
@app.route('/say/<nombre>')
def say(nombre):
    return f'¡Hola {nombre}!'


#Crea una ruta que responda con la palabra dada repetida tantas veces como se especifique en la URL
def repeat (numero, text):
    return render_template('index.html', cantidad=numero, palabra=text)    


#BONUS SENSEI: Asegúrate de que si el usuario escribe cualquier ruta distinta a las especificadas, 
#reciba un mensaje de error que diga "¡Lo siento! No hay respuesta. Inténtalo otra vez.”.
@app.errorhandler(404)
def not_found(e):
    return "Pagina no encontrada"


if __name__=="__main__":
    app.run(debug=True)

