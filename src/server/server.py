# flask web server

from flask import Flask, request
from flask_api import status
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import datetime


import json

# local
from freq_analyzer.main import analyze

app = Flask(__name__, static_url_path='', static_folder='../client/dist')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app)
db = SQLAlchemy(app)


# TODO move non web-server functionalities out
class Record(db.Model):
  id = db.Column(db.Integer(), primary_key=True)
  removeStopWords =  db.Column(db.Boolean(), default=True)
  originalText = db.Column(db.Text())
  wordCounts = db.Column(db.Text()) # word counts

  def asDict(self):
    # FIXME limited the scope to we should return the original text as a downloadable 
    mDic = {
      'id': self.id,
      'removeStopWords': self.removeStopWords,
      'originalText': self.originalText[:1000],
      'wordCounts': json.loads(self.wordCounts)[:25],
    };
    # TODO complete this
    return mDic

db.create_all()


def analysisRequst(text, removeStopWords):
  # preprocess
  lines = text.split('\n')

  word_counts = analyze(lines)
  rec = Record(removeStopWords=removeStopWords,
               originalText=text, wordCounts=json.dumps(word_counts))
  # save it
  db.session.add(rec)
  db.session.commit()

  recs = Record.query.order_by(Record.id.desc()).limit(1).all()
  rec = recs[0].asDict()
  return json.dumps(rec)


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
      removeStopWords = False if request.form['removeStopWords'] == 'false' else True

      return analysisRequst(text, removeStopWords)

    return status.HTTP_400_BAD_REQUEST

@app.route('/analysis', methods=['GET'])
def fetch_history():
  recs = Record.query.order_by(Record.id.desc()).limit(10).all()
  recs = [r.asDict() for r in recs]
  return json.dumps(recs)


if __name__ == "__main__":
  app.run(debug=True)
