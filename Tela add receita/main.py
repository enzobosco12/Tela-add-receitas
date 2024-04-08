from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    recipe_name = request.form['recipeName']
    origin_location = request.form['originLocation']
    date = request.form['date']
    value = request.form['value']

    print('Recipe Name:', recipe_name)
    print('Origin Location:', origin_location)
    print('Date:', date)
    print('Value:', value)

    return 'Formulário enviado com sucesso!'


if __name__ == '__main__':
    app.run(debug=True)
