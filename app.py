from flask import Flask, render_template, request
from werkzeug import secure_filename

@app.route('/getfile', methods=['GET','POST'])
def getfile():
    if request.method == 'POST':

        # for secure filenames. Read the documentation.
        file = request.files['myfile']
        filename = secure_filename(file.filename) 

        # os.path.join is used so that paths work in every operating system
        file.save(os.path.join("wherever","you","want",filename))

        # You should use os.path.join here too.
        with open("wherever/you/want/filename") as f:
            file_content = f.read()

        return file_content     


    else:
        result = request.args.get['myfile']
    return result