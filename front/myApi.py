from flask import Flask

app = Flask(__name__)

# Members API Route
@app.route('/all_cpus')
def get_all_cpus():
    return

if __name__ == '__main__':
    app.run()