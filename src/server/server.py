# flask web server

from flask import Flask

# local
from freq_analyzer.mapper import mapper
from freq_analyzer.reducer import reducer
from freq_analyzer.mapReduce import MapReduce
from freq_analyzer.stemming import merge_stems


app = Flask(__name__, static_url_path='', static_folder='../../public')

@app.route("/")
def root():
  return app.send_static_file('index.html')


if __name__ == "__main__":
  app.run(debug=True)
