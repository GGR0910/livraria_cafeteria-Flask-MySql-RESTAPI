from flask import Flask,render_template,redirect,session,url_for

app = Flask(__name__)

@app.route('/')
def index():
    if 'usuario_logado' in session or session != None:
        return render_template('menu.html')
    else:
        return redirect(url_for('login'))

#mesas
@app.route('/mesas')
def mesas_atendimento():
    if 'usuario_logado' in session or session != None:
        return render_template('mesas.html')
    else:
        return redirect(url_for('login'))

@app.route('/mesa/<int:mesaid>')
def mesa_detalhes():
    if 'usuario_logado' in session or session != None:
        return render_template('mesa_detaljes.html')
    else:
        return redirect(url_for('login'))

#caixa
@app.route('/caixa')
def caixa():
    if 'usuario_logado' in session or session != None:
        return render_template('mesa_detaljes.html')
    else:
        return redirect(url_for('login'))

#usuarios
@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/autenticar')
def autenticar():
    pass

if __name__ == '__main__':
    app.run(debug=True)