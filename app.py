import streamlit as st
import os

# Import functions ที่เราเขียนไว้ใน src/
from src.download_video import download_video
from src.preprocess import extract_and_save_frames_and_metadata

def main():
    st.title("🎬 YouTube Video Downloader & Frame Extractor")

    youtube_url = st.text_input("📎 ใส่ลิงก์ YouTube ที่ต้องการดาวน์โหลด", placeholder="https://youtube.com/watch?v=xxxx")
    download_path = './shared_data/videos/'  # ที่เก็บไฟล์วิดีโอ
    extracted_frames_path = os.path.join(download_path, "extracted_frame")

    if st.button("🚀 ดาวน์โหลดและแยกเฟรม"):
        if youtube_url:
            with st.spinner('🚀 กำลังดาวน์โหลดวิดีโอ และซับไตเติ้ล...'):
                video_filepath, subtitle_filepath = download_video(youtube_url, path=download_path)

            if video_filepath:
                st.success(f"✅ ดาวน์โหลดวิดีโอสำเร็จ: `{video_filepath}`")
                st.video(video_filepath)

                if subtitle_filepath:
                    st.info(f"📝 พบไฟล์ซับไตเติ้ล: `{subtitle_filepath}`")
                else:
                    st.warning("⚠️ ไม่พบซับไตเติ้ล (.vtt) ใช้เฉพาะเฟรมโดยไม่มีข้อความ")

                with st.spinner('🖼 กำลังแยกเฟรมจากวิดีโอ...'):
                    metadatas = extract_and_save_frames_and_metadata(
                        video_filepath=video_filepath,
                        transcript_filepath=subtitle_filepath,
                        extracted_frames_path=extracted_frames_path,
                        output_dir=download_path,
                        frame_interval_sec=5  # ปรับตรงนี้ได้ เช่น 1 วินาที/เฟรม
                    )

                st.success(f"✅ ดึงเฟรมสำเร็จทั้งหมด {len(metadatas)} รูป")
                st.info("📦 Metadata บันทึกในไฟล์ metadata.json เรียบร้อยแล้ว")

            else:
                st.error("❌ ดาวน์โหลดวิดีโอไม่สำเร็จ กรุณาตรวจสอบลิงก์ YouTube")
        else:
            st.warning("⚠️ กรุณากรอกลิงก์ YouTube ก่อน")

if __name__ == "__main__":
    main()
