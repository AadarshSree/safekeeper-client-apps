from flask import Flask, send_from_directory, make_response, jsonify, request

app = Flask(__name__ ,
            static_url_path='')


@app.route('/')
def index():
    return '<h1>Hello from Geralt Server</h1>'


@app.route('/codeverify')
def getRootHash():
    # {"origin":"whatsapp.com","version":"1015251365","root_hash":"d001608791c63855dd0059a788cc68df66f2f61576f55aec57435554b201d26a","published_date":1722326107}
    jsonResponse = {"origin":"keen.csrl.info",
                    "version":"11223344",
                    "root_hash":"8bdf484ba85de6ada347805c19a25cd5874257ac892eed3ff14389cb06bf2a08",
                    "published_date":1722353508}
    response = make_response(jsonify(jsonResponse))

    # response.headers.add('Access-Control-Allow-Origin', '*')
    # response.headers.add('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
    # response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    # return jsonify({'rootHash': 'abcde12345'})
    return response

if __name__ == '__main__':
    
    app.run(host='0.0.0.0', port="8080", debug=True)