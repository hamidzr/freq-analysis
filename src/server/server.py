# flask web server

from flask import Flask, request
from flask_api import status
from flask_sqlalchemy import SQLAlchemy
import datetime
import json

# local
from freq_analyzer.main import analyze

app = Flask(__name__, static_url_path='', static_folder='../../public')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# TODO move non web-server functionalities out
class Record(db.Model):
  id = db.Column(db.Integer(), primary_key=True)
  removeStopWords =  db.Column(db.Boolean(), default=True)
  originalText = db.Column(db.Text())
  result = db.Column(db.Text()) # word counts
  createdAt = db.Column(db.DateTime(), default=datetime.datetime.now())

  def asDict(self):
    mDic = {
      'id': self.id,
      'removeStopWords': self.removeStopWords,
    };
    # TODO complete this
    return mDic

db.create_all()


def analysisRequst(text, removeStopWords):
  # preprocess
  lines = text.split('\n')

  word_counts = analyze(lines)
  rec = Record(removeStopWords=True,
               originalText=text, result=json.dumps(word_counts))
  # save it
  db.session.add(rec)
  db.session.commit()

  top_words = [[w, c] for w,c in word_counts[:25]]
  return json.dumps(top_words)


@app.route("/")
def root():
  return app.send_static_file('index.html')


@app.route('/analysis', methods=['POST'])
def new_request():
  if request.method == 'POST':

    # check if the post request has the file part
    if 'file' not in request.files:
      return status.HTTP_400_BAD_REQUEST

    file = request.files['file']
    if file.filename == '':
      return status.HTTP_400_BAD_REQUEST

    if file.content_type == 'text/plain':
      text = file.read().decode('utf-8')

      # default to removing stopwords
      removeStopWords = False if request.form['removeStopWords'] == False else True

      return analysisRequst(text, removeStopWords)

    return status.HTTP_400_BAD_REQUEST

@app.route('/analysis', methods=['GET'])
def fetch_history():
  # TODO limit to last 10
  recs = Record.query.all()
  recs = [r.asDict() for r in recs]
  return json.dumps(recs)


if __name__ == "__main__":
  app.run(debug=True)
