
import os
from flask import Flask, request, redirect, url_for, send_from_directory
from werkzeug import secure_filename
import json

UPLOAD_FOLDER = 'uploads'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def update_json(filename):
    print(filename)
    file='uploads/lista.json'
    with open(file) as fp:
    	c=fp.read()
    try:
	 v=json.loads(c)
	 print(v)   
	 #v.append(filename)
	# sorted(set(v))
#	 dict(zip(v, v)).keys()
         l = []
	 a=v
	 b=[]
 	 b.append(filename)
	 for elemento in a:
    		l.append(elemento)

	 for elemento in b:
    		if elemento not in l:
       			l.append(elemento)
	
	 print(l)
   	 with open(file,'wb') as fp:
    	 	json.dump(l,fp)
    except:
	pass

# http://flask.pocoo.org/docs/patterns/fileuploads/
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            print '**found file', file.filename
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

	    update_json(filename)

            
            return url_for('uploaded_file',
                                    filename=filename)
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

if __name__ == '__main__':
	app.run(debug=True)
