from flask import Flask,render_template,request,flash,redirect,url_for
from werkzeug.utils import secure_filename
import os
import objdetection

UPLOAD_FOLDER = 'static\\files'
# uploadfolder="C:\\Users\\kathi\\PycharmProjects\\objdetect\\images\\uploads"
ALLOWED_EXTENSIONS = {'JPG', 'JPEG', 'PNG', 'jpg', 'jpeg', 'png'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = 'super secret key'


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def index():
    return render_template("/index.html")

# @app.route("/post", methods = ['GET', 'POST'])
# def post():
#     if request.method == 'POST':
#         detectedobjects = request.form['value']
#         print(detectedobjects)
#     return detectedobjects

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   result=""
   imagename=""
   image_name=""
   detectedobjects=''
   finaldetectedobjects=''
   if request.method == 'POST':
       file = request.files['pic']
       message=''
       if file.filename == '':
           message="Please select a file"
           flash(message,'error')
           # return redirect(request.url)
       elif not allowed_file(file.filename):
           message="Only images files are allowed"
           flash(message, 'error')
       else :
           file.save(os.path.join(app.config['UPLOAD_FOLDER'],'image.jpg'))
           message="File uploaded and analysed successfully"
           image_name = "static/files/image.jpg"
           flash(message, 'result')
           finaldetectedobjects=objdetection.detectobj()
           print(finaldetectedobjects)
   # if request.method == 'GET':
   #     detectedobjects = request.args.get('value','')
   #     print(detectedobjects)
   #     message="Analyse Completed"
   #     flash(message, 'result')


   return render_template('upload.html', imagename=image_name, result=finaldetectedobjects)
       # return redirect(url_for('index'))



   # f = request.files['pic']
   # f.save(os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(f.filename)))
   # return 'file uploaded successfully'



if __name__ == "__main__":
    app.run(
        debug='true',
        threaded=False
    )

