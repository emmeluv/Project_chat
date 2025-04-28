import os
import yt_dlp

def download_video(video_url, path='datas/videos/'):
    """
    Download a YouTube video as MP4 using yt-dlp
    """
    try:
        if not os.path.exists(path):
            os.makedirs(path)

        ydl_opts = {
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4',
            'merge_output_format': 'mp4',
            'outtmpl': os.path.join(path, '%(title)s.%(ext)s'),
            'quiet': False,
            'noprogress': False,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_url, download=True)
            filename = ydl.prepare_filename(info)

        print(f"✅ ดาวน์โหลดเสร็จ: {filename}")
        return filename

    except Exception as e:
        print(f"เกิดข้อผิดพลาด: {e}")
        return None
