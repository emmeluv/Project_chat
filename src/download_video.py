import os
import yt_dlp

def download_video(video_url, path='shared_data/videos/'):
    try:
        if not os.path.exists(path):
            os.makedirs(path)

        ydl_opts = {
            'outtmpl': os.path.join(path, '%(title)s.%(ext)s'),
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4',
            'merge_output_format': 'mp4',
            'quiet': False,
            'noprogress': False,
            'subtitleslangs': ['en'],
            'subtitlesformat': 'vtt',
            'writesubtitles': True,
            'writeautomaticsub': True,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_url, download=True)

        video_filename = ydl.prepare_filename(info)
        video_filepath = os.path.splitext(video_filename)[0] + '.mp4'
        subtitle_filepath = os.path.splitext(video_filename)[0] + '.en.vtt'

        if not os.path.exists(subtitle_filepath):
            subtitle_filepath = None

        return video_filepath, subtitle_filepath

    except Exception as e:
        print(f"เกิดข้อผิดพลาด: {e}")
        return None, None
