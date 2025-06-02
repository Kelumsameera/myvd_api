# from flask import Flask, request, jsonify
# import yt_dlp

# app = Flask(__name__)

# @app.route('/download', methods=['GET'])
# def download_video():
#     video_url = request.args.get('url')
#     if not video_url:
#         return jsonify({'error': 'No URL provided'}), 400

#     ydl_opts = {
#         'format': 'best',  # choose best quality video+audio
#         'outtmpl': 'downloads/%(title)s.%(ext)s',  # save path template
#     }

#     try:
#         with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#             info = ydl.extract_info(video_url, download=True)
#             filename = ydl.prepare_filename(info)
#         return jsonify({'status': 'success', 'filename': filename})
#     except Exception as e:
#         return jsonify({'status': 'error', 'message': str(e)}), 500

# if __name__ == '__main__':
#     app.run(debug=True)
import flask


from flask import Flask, request, jsonify
import yt_dlp

app = Flask(__name__)  # ✅ correct app initialization

@app.route('/info', methods=['GET'])
def video_info():
    video_url = request.args.get('url')
    if not video_url:
        return jsonify({'error': 'No URL provided'}), 400

    ydl_opts = {'quiet': True, 'skip_download': True}
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_url, download=False)
        return jsonify({
            'status': 'success',
            'title': info.get('title'),
            'duration': info.get('duration'),
            'uploader': info.get('uploader'),
            'thumbnail': info.get('thumbnail'),
            'webpage_url': info.get('webpage_url')
        })
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500
if __name__ == '__main__':
     app.run(debug=True)