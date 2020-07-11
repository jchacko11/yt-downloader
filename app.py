from flask import Flask, render_template, request
from pytube import YouTube

app = Flask('app')


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/watch')
def video_info():
    url = False
    try:
        v = request.args["v"]
    except:
        try:
            url = request.args["url"]
        except:
            v = "4OnwUz-I2GI"

    try:
        if url:
            yt = YouTube(url)
        else:
            yt = YouTube("?v=" + v)
    except:
        return render_template("vid_not_found.html")

    streams = yt.streams
    title = yt.title
    thumbnail = yt.thumbnail_url
    author = yt.author
    views = yt.views

    only_audio =streams.filter(only_audio=True)
    only_video = streams.filter(only_video=True)
    progressive = streams.filter(progressive=True)

    primary = streams.get_highest_resolution()

    return render_template(
        "video.html",
        streams=streams,
        title=title,
        thumbnail=thumbnail,
        primary=primary,
        author=author,
        views=views,
        only_audio=only_audio,
        only_video=only_video,
        progressive=progressive
    )


if __name__ == '__main__':
    app.run()