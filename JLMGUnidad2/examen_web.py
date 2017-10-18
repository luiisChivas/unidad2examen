from flask import Flask, render_template, request, redirect
from examen_modulo import funcionfuerza

app = Flask(__name__)

@app.route('/')
def hello() -> '302':
    return redirect('/entry')

@app.route('/entry')
def entry_page()-> 'html':
    return render_template('entry.html', the_title='Examén Unidad 2')

@app.route('/fuerza', methods=['GET', 'POST'])
def execute()->'html':
    L = float(request.form['L'])
    M = float(request.form['M'])
    T = float(request.form['T'])
    tittle = 'El resultado de la fuerza es: '
    result = funcionfuerza(L,M,T)
    return render_template('results.html',
                           this_tittle = tittle,
                           the_l = L,
                           the_m = M,
                           the_t = T,
                           the_result = result)

if __name__ == '__main__':
    app.run(port=5001)