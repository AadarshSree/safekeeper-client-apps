from flask import Flask, send_from_directory, make_response, jsonify

app = Flask(__name__ ,
            static_url_path='', 
            static_folder='web/static')

HOST_NAME = "safekeeper.dev"
PORT = "8080"


@app.route('/')
def index():
    return '<h1>Hello from Server</h1>'

@app.route('/index')
def serve_index():
    response = make_response(send_from_directory('./web', 'registration.html'))
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    return response

@app.route('/codeverify')
def getRootHash():
    return jsonify({'rootHash': 'abcde12345'})


if __name__ == '__main__':
    context = ('./.SSL_KEYS/cert.pem', './.SSL_KEYS/key.pem')
    app.run(host='0.0.0.0', port=PORT, ssl_context=context)