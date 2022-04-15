from flask import Flask, request, render_template, make_response, abort
import os

app = Flask(__name__)
app.config['UPLOAD_EXTENSIONS'] = ['.xml']
app.config['UPLOAD_PATH'] = 'uploads'

@app.route("/")
def index():
    return render_template("index.html")


@app.route('/', methods=['POST'])
def story():
    return render_template("story.html")


if __name__ == "__main__":
    app.run(debug=True, passthrough_errors=True)

