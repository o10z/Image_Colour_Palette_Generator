#imports
from flask import Flask, render_template, request
from colorthief import ColorThief
from werkzeug.utils import secure_filename

app = Flask(__name__)


# route to home page
@app.route("/")
def home():
    return render_template("index.html")


# route to results
@app.route('/results', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        color_thief = ColorThief(f.filename)
        palette = color_thief.get_palette(color_count=11, quality=1)
        return render_template('results.html', colors=palette)


if __name__ == "__main__":
    app.run(debug=True)