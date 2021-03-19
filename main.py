from flask import Flask, render_template, request, send_file
from pytube import YouTube
import requests
from video_downloader import video_downloader
import os

app = Flask(__name__)


yt = None
list = []
video = None


def get_youtube_video(url):
    dl = video_downloader(url)
    command_to_execute = dl.create_download_video_command()
    return command_to_execute


@app.route("/")
def about():
    return render_template("download.html")


@app.route('/', methods=['POST'])
def my_form_post():
    title = request.form['title']
    url = request.form['url']
    com = get_youtube_video(url)
    # return send_file(yt, as_attachment=True)
    current_directory = os.getcwd()
    os.system(com)
    return f"Current directory: {current_directory}, command to execute: {com}"


if __name__ == "__main__":
    app.run(debug=True)
