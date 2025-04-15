from flask import Flask, send_from_directory

app = Flask(__name__, static_folder='.', static_url_path='')

@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

@app.route('/about')
def about():
    return send_from_directory('.', 'about.html')

if __name__ == '__main__':
    # Use host='0.0.0.0' and the port=8000 to make it accessible externally
    app.run(host='0.0.0.0', port=8000)
