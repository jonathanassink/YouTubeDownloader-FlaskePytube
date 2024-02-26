from flask import Flask, render_template, request, redirect, url_for
from pytube import YouTube

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    url = request.form['url']
    download_type = request.form['download_type']

    try:
        yt = YouTube(url)

        if download_type == 'audio':
            audio_stream = yt.streams.filter(only_audio=True).first()
            audio_stream.download('downloads')
        elif download_type == 'video':
            video_stream = yt.streams.filter(file_extension='mp4').first()
            video_stream.download('downloads')

        return redirect(url_for('index'))
    except Exception as e:
        return render_template('error.html', error=str(e))

if __name__ == '__main__':
    app.run(debug=True)
