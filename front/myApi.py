from flask import Flask

app = Flask(__name__)

# Members API Route
@app.route('/api/get_elements')
def get_elements():
    elements = ['элемент1', 'элемент2', 'элемент3']
    return jsonify(elements)

if __name__ == '__main__':
    app.run()