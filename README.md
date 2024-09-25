# safekeeper-client-apps

This repository contains Flask server to host the:
* Safekeeper enabled website 
* Code verify Audit Endpoint

## Installation

Before running the web application, install python and required dependencies from requirements.txt.
    
    pip install -r requirements.txt

Now run the Flask server using the following command:

    python server.py

## Manifest Generation

To generate a manifest for your web application, access the '/generateManifest' endpoint. To learn more about manifest generation, see [generate_cv_manifest()](https://github.com/AadarshSree/safekeeper-client-apps/blob/main/server.py#L75)

  
