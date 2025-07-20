from flask import Flask, render_template, request, session
app = Flask(__name__)
app.config['SECRET_KEY'] = 'clave'
@app.route('/', methods=['GET', 'POST'])
def index():
        return render_template('menu.html')
@app.route('/compra', methods=['GET', 'POST'])
def ejercicio_1():
  mensaje = False
  total = total_descuento = total_a_pagar = nombre = None
  if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        cantidad = int(request.form['cantidadunidades'])
        valor = 9000
        if edad > 30:
            descuento = 0.25
        elif edad >= 18:
            descuento = 0.15
        else:
            descuento = 0
        total = int(valor * cantidad)
        total_descuento = int(total * descuento)
        total_a_pagar = int(total - total_descuento)
        mensaje = True
  return render_template('compra.html', mensaje = mensaje, total = total, total_descuento = total_descuento,total_a_pagar = total_a_pagar, nombre = nombre)
@app.route('/usuarios', methods=['GET', 'POST'])
def ejercicio_2():
    usuarios = {'juan': 'admin', 'pepe': 'user'}
    mensaje = None
    if request.method == 'POST':
        usuario = request.form['usuario']
        contrasena = request.form['contrasena']
        if usuario in usuarios and usuarios[usuario] == contrasena:
            session['usuario'] = usuario
            if usuario == 'juan':
                mensaje = 'Bienvenido Administrador Juan'
            else:
                mensaje = f'Bienvenido {usuario}'
        else:
            mensaje = 'Usuario y/o contraseña inexistente'
    return render_template('usuarios.html', mensaje = mensaje)
if __name__ == '__main__':
    app.run()