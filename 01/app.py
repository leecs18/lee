from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():

    data = {
        'name': 'chia sheng',
        'age': 18,
        'city': 'penang'
    }


    return render_template('index.html', data=data)


if __name__ == '__main__':
    app.run()