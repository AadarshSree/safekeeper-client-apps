import os
import glob
import hashlib
import json

def generate_cv_manifest():
    build_path = "./web/static/js"
    all_files = glob.glob(os.path.join(build_path, "**/*.js"), recursive=True)

    hash_array = []
    for file in all_files:
        with open(file, 'r', encoding='utf-8') as f:
            file_content = f.read()
        file_hash = hashlib.sha256(file_content.encode('utf-8')).hexdigest()
        print("[->]", file, "-->", file_hash)
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

    final_manifest = json.dumps({
        "manifest": hash_array,
        "manifest_hashes": {
            "longtail": longtail_hash,
            "main": main_hash,
            "combined_hash": combined_hash
        }
    }, indent=4)

    print("\n")
    print(final_manifest)
    print("\n")

generate_cv_manifest()