from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the Flask backend!'

@app.route('/api/data')
def get_data():
    data = {'message': 'Data from the Flask backend!'}
    return data

if __name__ == '__main__':
    app.run()