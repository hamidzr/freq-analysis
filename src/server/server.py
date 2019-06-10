# flask web server

from flask import Flask, request, redirect
from flask_sqlalchemy import SQLAlchemy
import datetime
import json

# local
from freq_analyzer.main import analyze

app = Flask(__name__, static_url_path='', static_folder='../../public')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db = SQLAlchemy(app)


class Record(db.Model):
  id = db.Column(db.Integer(), primary_key=True)
  removeStopWords =  db.Column(db.Boolean(), default=True)
  originalText = db.Column(db.Text())
  result = db.Column(db.Text())
  createdAt = db.Column(db.DateTime(), default=datetime.datetime.now())

db.create_all()


@app.route("/")
def root():
  # res = database.select_all()
  # res = database.insert('adsasd', True, 'asdff')
  print(Record.query.all()[0].result)
  return app.send_static_file('index.html')


@app.route('/analysis', methods=['GET', 'POST'])
def upload_file():
  if request.method == 'POST':
    # check if the post request has the file part
    if 'file' not in request.files:
      return redirect(request.url)
    file = request.files['file']
    # if user does not select file, browser also
    # submit an empty part without filename
    if file.filename == '':
      return redirect(request.url)

    if file and file.content_type == 'text/plain':
      text = file.read().decode('utf-8')
      lines = text.split('\n')
      word_counts = analyze(lines)
      rec = Record(removeStopWords=True, originalText=text, result=json.dumps(word_counts))
      db.session.add(rec)
      db.session.commit()
      print(word_counts[:25])
      # return word_counts[:25]
      # filename = secure_filename(file.filename)
      # file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
      # return redirect(url_for('uploaded_file',
                              # filename=filename))
  return '''
  <!doctype html>
  <title>Submit a new request</title>
  <h1>Upload new File</h1>
  <form method=post enctype=multipart/form-data>
  <input type=file name=file>
  <input type=submit value=Upload>
  </form>
  '''

if __name__ == "__main__":
  app.run(debug=True)
