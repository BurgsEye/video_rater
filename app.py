from flask import Flask, send_from_directory, request, render_template, redirect

from urllib.parse import unquote

import os
import shutil

app = Flask(__name__)


# serve CSS files from the static/css directory
@app.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory('static', path)

@app.route("/move_video", methods=["POST"])
def move_video():
    rating = request.form["rating"]
    current_video = request.form["current_video"]
    filename =unquote(current_video.split('/')[-1])

    dest_dir = "rated/" + rating

    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)


    source = 'videos/'+filename
    dest = dest_dir+'/'+filename
    
    print(source,'current_video')
    print(dest,'dest')
    
    shutil.move(source,dest)
    return redirect("/")

@app.route("/videos/<path:path>")
def serve_videos(path):
    video_path = os.path.join("videos", path)
    if not os.path.exists(video_path):
        return "Video not found", 404
    return send_from_directory("videos", path)


@app.route("/purge_videos", methods=["POST"])
def purge_videos():
    directory = 'rated/D'
    # iterate over files in
    # that directory
    counter = 0
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        # checking if it is a file
        if os.path.isfile(f):
            os.remove(f)
            counter =+ 1
    ##return redirect("/?counter=" + str(counter))
    return str(counter)


@app.route("/")
def index():
    videos = []
    for filename in os.listdir("videos"):
        if filename.endswith(".mp4"):
            videos.append(filename)
    if len(videos) > 0:
        next_video = videos[0]
        videos = videos[1:]
    else:
        next_video = None
        message = "No videos found in the videos folder."
        return render_template("index.html", next_video=next_video, videos=videos,no_videos = len(videos), message=message)
    return render_template("index.html", next_video=next_video, videos=videos, no_videos = len(videos) +1 )

if __name__ == "__main__":
    app.run(debug=True)