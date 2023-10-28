import xml.etree.ElementTree as ET

import youtube_dl


def download_subtitles(video_id):
    langs = ["pt", "en"]
    ydl = youtube_dl.YoutubeDL(
        params={
            "verbose": True,
            "quiet": False,
            "no_warnings": False,
            "writesubtitles": True,
            "writeautomaticsub": True,
            "skip_download": True,
            "subtitlesformat": "srv1",
            "subtitleslangs": langs,
            "outtmpl": f"videos/{video_id}/subtitles",
            "nooverwrites": True,
        }
    )

    ydl.download([f"https://youtu.be/{video_id}"])

    for lang in langs:
        tree = ET.parse(f"videos/{video_id}/subtitles.{lang}.srv1")
        with open(f"videos/{video_id}/subtitles_{lang}.txt", "w") as f:
            for instance in tree.findall("text"):
                f.write(f"{instance.text} ")
