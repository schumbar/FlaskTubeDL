from pytube import YouTube
import os
DOWNLOAD_VIDEO_CLI = "pytube"


class video_downloader:
    def __init__(self, url, audio_only=False, include_subtitles=False):
        self._url = url
        self._audio_only = audio_only
        self._include_subtitles = include_subtitles
        self._download_yt_vid_command = ['pytube']

    def create_download_video_command(self):
        self._download_yt_vid_command.append(self._url)
        if self._audio_only:
            self._download_yt_vid_command.append('-a')
        elif self._include_subtitles:
            self._download_yt_vid_command.append("-c en")
        print(self._download_yt_vid_command)
        command_to_execute = ' '.join(self._download_yt_vid_command)
        return command_to_execute
