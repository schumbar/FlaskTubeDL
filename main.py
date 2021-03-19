from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, World!"


@app.route("/shawn")
def salvador():
    return "Hello, Shawn"


@app.route("/download")
def about():
    return render_template("download.html")


@app.route('/download', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = text.upper()
    return processed_text


if __name__ == "__main__":
    app.run(debug=True)
