from flask import Flask, render_template, request, send_file
from pytube import YouTube

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
    title = request.form['title']
    url = request.form['url']
    yt = YouTube(url)

    return send_file(yt, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
