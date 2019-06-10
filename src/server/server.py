# flask web server

from flask import Flask

# local
from freq_analyzer.main import analyze


app = Flask(__name__, static_url_path='', static_folder='../../public')

@app.route("/")
def root():
  return app.send_static_file('index.html')


if __name__ == "__main__":
  app.run(debug=True)
