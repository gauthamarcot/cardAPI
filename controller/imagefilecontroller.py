from flask import request

import app


@app.route('/upload', methods=['POST'])
def upload_file():
    print(request.files)
    # checking if the file is present or not.
    if 'file' not in request.files:
        return "No file found"

    file = request.files['file']
    file.save("static/test.jpg")
    return "file successfully saved"
