from flask import Flask, request, send_from_directory
from pymongo import MongoClient
from colors_processing import get_dominant_colors

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')
db = client['clothingDB']

@app.route('/')
def home():
    return 'Hello, MongoDB!'

# @app.route("/")
# def serve_app():
#     return send_from_directory('client/src/', 'index.html')

# @app.route('/<path:path>')
# def serve_static_files(path):
#     return send_from_directory('client/public', path)

@app.route("/upload", methods=["POST"] )
def upload_images():

    images = request.files.getlist("images")

    for image in images:
        file_name = image.filename

        image_path = f"server/static/{file_name}"
        image.save(f"server/static/{file_name}")

        #three dominant colors in hex
        dominant_colors = dominant_colors(image_path, 3)

        #insert into database
        db.clothingDB.insert_one({
            image_path: image_path,
            dominant_colors: dominant_colors
        })






        



    
    





if __name__ == '__main__':
    app.run()