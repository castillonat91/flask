from flask import Flask,  request, render_template, redirect, url_for, flash
import mysql.connector

#creamos una instancia de la clase flask

app = Flask(__name__)

#configurar la conexion
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="AGENDA2024"
)
cursor = db.cursor()

#definir rutas
@app.route('/')
def lista():
    cursor = db.cursor()
    cursor.execute('SELECT * FROM personas')
    personas = cursor.fetchall()
    return render_template('index.html',personas=personas)

@app.route('/registrar', methods=['POST'])
def registrar_usuarios():
    NOMBRE = request.form['nombre'],
    APELLIDO = request.form['apellido'],
    EMAIL = request.form['correo'],
    DIRECCION = request.form['direccion'],
    TELEFONO = request.form['telefono'],
    USUARIO = request.form['usuario'],
    CONTRASEÑA = request.form['contraseña'],
    
    #insertar datos a la tlaba personas
    
    cursor.execute("INSERT INTO personas(nombreper,apellidoper,emailper,dirper,telper,usuarioper,contraper)VALUES(%s,%s,%s,%s,%s,%s,%s)",(NOMBRE,APELLIDO,EMAIL,DIRECCION,TELEFONO,USUARIO,CONTRASEÑA))
    
    db.commit()
    flash('usuario creado correctament','success')
    return redirect(url_for('registrar.html'))
  
# para ejecutar la aplicacion
if __name__ == '__main__':
    app.add_url_rule('/',view_func=lista)
    app.run(debug=True,port=5005)