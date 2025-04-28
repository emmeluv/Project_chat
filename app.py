import streamlit as st
from src.download_video import download_video

def main():
    st.title("🎬 YouTube Video Downloader (.mp4)")

    youtube_url = st.text_input("📎 ใส่ลิงก์ YouTube ที่ต้องการดาวน์โหลด", placeholder="https://youtube.com/watch?v=xxxx")
    download_path = 'datas/videos/'

    if st.button("🚀 ดาวน์โหลดวิดีโอ (MP4)"):
        if youtube_url:
            with st.spinner('กำลังดาวน์โหลด... กรุณารอสักครู่'):
                filepath = download_video(youtube_url, path=download_path)

            if filepath:
                st.success(f"✅ ดาวน์โหลดสำเร็จ: `{filepath}`")
                st.video(filepath)
            else:
                st.error("❌ ดาวน์โหลดไม่สำเร็จ กรุณาตรวจสอบลิงก์หรือเชื่อมต่อเน็ต")
        else:
            st.warning("⚠️ กรุณากรอกลิงก์ YouTube ก่อน")

if __name__ == "__main__":
    main()
