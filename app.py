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
from flask import Flask, request, jsonify
import yt_dlp
import os

app = Flask(__name__)

DOWNLOAD_DIR = "downloads"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

@app.route('/download', methods=['POST'])
def download_video():
    data = request.get_json()
    video_url = data.get('url')

    if not video_url:
        return jsonify({"error": "No URL provided"}), 400

    ydl_opts = {
        'format': 'best',
        'outtmpl': os.path.join(DOWNLOAD_DIR, '%(title)s.%(ext)s')
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_url, download=True)
            return jsonify({
                "title": info.get('title'),
                "filename": ydl.prepare_filename(info),
                "status": "Downloaded successfully"
            })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
