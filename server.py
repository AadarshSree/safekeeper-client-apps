from flask import Flask, send_from_directory, make_response, jsonify, request
import os
import glob
import hashlib
import json

app = Flask(__name__ ,
            static_url_path='', 
            static_folder='web/static')

HOST_NAME = "safekeeper.dev"
PORT = "8080"


@app.route('/')
def index():
    return '<h1>Hello from Server</h1>'

@app.route('/login')
def serve_login_page():
    response = make_response(send_from_directory('./web', 'loginPage.html'))
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')

    # cspHeaderString = "default-src 'self' *; style-src 'self' * 'unsafe-inline' ; script-src 'self' * 'unsafe-inline';"
    cspHeaderString = "default-src 'self' ; style-src 'self' * 'unsafe-inline' ; script-src 'self' ; connect-src *;  worker-src *;"


    response.headers['content-security-policy'] =  cspHeaderString
    response.headers['content-security-policy-report-only'] =  cspHeaderString+" report-uri / ;"
    return response

@app.route('/register')
def serve_index():
    response = make_response(send_from_directory('./web', 'registration.html'))
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')

    # cspHeaderString = "default-src 'self' *; style-src 'self' * 'unsafe-inline' ; script-src 'self' * 'unsafe-inline';"
    cspHeaderString = "default-src 'self' ; style-src 'self' * 'unsafe-inline' ; script-src 'self' ; connect-src *;  worker-src *;"


    response.headers['content-security-policy'] =  cspHeaderString
    response.headers['content-security-policy-report-only'] =  cspHeaderString+" report-uri / ;"
    return response

# Add the 'X-Content-Type-Options: nosniff' header to all static files
@app.after_request
def add_header(response):
    if request.path.startswith('/js/'):
        response.headers['x-content-type-options'] = 'nosniff'
    return response

@app.route('/codeverify')
def getRootHash():
    # {"origin":"whatsapp.com","version":"1015251365","root_hash":"d001608791c63855dd0059a788cc68df66f2f61576f55aec57435554b201d26a","published_date":1722326107}
    jsonResponse = {"origin":"safekeeper.dev",
                    "version":"11223344",
                    "root_hash":"8bdf484ba85de6ada347805c19a25cd5874257ac892eed3ff14389cb06bf2a08",
                    "published_date":1722353508}
    response = make_response(jsonify(jsonResponse))

    # response.headers.add('Access-Control-Allow-Origin', '*')
    # response.headers.add('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
    # response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    
    # return jsonify({'rootHash': 'abcde12345'})
    return response


@app.route('/generateManifest')
def generate_cv_manifest():
    build_path = "./web/static/js"
    all_files = glob.glob(os.path.join(build_path, "**/*.js"), recursive=True)

    hash_array = []
    for file in all_files:
        with open(file, 'r', encoding='utf-8') as f:
            file_content = f.read()
        file_hash = hashlib.sha256(file_content.encode('utf-8')).hexdigest()
        # print("[->]", file, "-->", file_hash)
        hash_array.append(file_hash)

    # print(hash_array)
    # print(sorted(hash_array))

    hash_array = sorted(hash_array)

    mega_hash = json.dumps(hash_array)
    mega_hash = mega_hash.replace(" ", "")
    # print("[megahash]", mega_hash)

    encoded_mega_hash = mega_hash.encode('utf-8')
    main_hash = hashlib.sha256(encoded_mega_hash).hexdigest()
    longtail_hash = main_hash
    # print('[*customHash.py*] mainHash:', main_hash)

    combined_hash_input = (longtail_hash + main_hash).encode('utf-8')
    combined_hash = hashlib.sha256(combined_hash_input).hexdigest()
    # print('[**] combinedHash:', combined_hash)

    # final_manifest = json.dumps({
    #     "manifest": hash_array,
    #     "manifest_hashes": {
    #         "longtail": longtail_hash,
    #         "main": main_hash,
    #         "combined_hash": combined_hash
    #     }
    # }, indent=4)

    # print("\n")
    # print(final_manifest)
    # print("\n")

    return jsonify({
        "manifest": hash_array,
        "manifest_hashes": {
            "longtail": longtail_hash,
            "main": main_hash,
            "combined_hash": combined_hash
        }
    })


if __name__ == '__main__':
    context = ('./.SSL_KEYS/cert.pem', './.SSL_KEYS/key.pem')
    app.run(host='0.0.0.0', port=PORT, ssl_context=context, debug=True)