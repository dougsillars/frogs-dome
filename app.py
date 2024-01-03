from flask import Flask, send_from_directory
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, this is a simple web server!'

@app.route('/photos/<filename>')
def send_photo(filename):
    return send_from_directory('photos', secure_filename(filename))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)


#comment
#comment 2