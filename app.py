from flask import Flask, request, render_template, make_response, abort, os

app = Flask(__name__)
app.config['UPLOAD_EXTENSIONS'] = ['.xml']
app.config['UPLOAD_PATH'] = 'uploads'

@app.route("/")
@app.route("/home")
def index():
    return render_template("index.html")


@app.route("/story")
def btcgold():
    return render_template("story.html")


@app.route('/readstory', methods=['POST'])
def upload_files():
    uploaded_file = request.files['file']
    filename = uploaded_file.filename
    if filename != '':
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in app.config['UPLOAD_EXTENSIONS']:
            abort(400)
        uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], filename))
    return render_template("story.html")


if __name__ == "__main__":

    app.run(debug=True, passthrough_errors=True)
