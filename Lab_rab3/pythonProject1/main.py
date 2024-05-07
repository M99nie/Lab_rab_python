from flask import Flask, render_template, request

app = Flask("Ипотечный калькулятор")


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/', methods=['post', 'get'])
def form():
    if request.method == 'POST':
        summ = int(request.form.get('num_1'))
        procent = int(request.form.get('num_2'))/12
        srok = int(request.form.get('num_3'))
    return render_template('index.html', ans=summ*(procent+((procent)/(((1+procent)**srok)-1))))


if __name__ == '__main__':
    app.run()