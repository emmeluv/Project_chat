import cv2
import os
import json
import webvtt
from pathlib import Path

def extract_and_save_frames_and_metadata(video_filepath, transcript_filepath, extracted_frames_path, output_dir, frame_interval_sec=1):
    """
    - Extract frames จากวิดีโอทุก n วินาที
    - จับคู่กับ transcript (.vtt)
    - บันทึก frame + metadata ในรูปแบบที่ custom ได้ตามที่คุณต้องการ
    """

    video_capture = cv2.VideoCapture(video_filepath)
    if not video_capture.isOpened():
        print("❌ ไม่สามารถเปิดวิดีโอได้")
        return []

    fps = video_capture.get(cv2.CAP_PROP_FPS)
    frame_interval = int(fps * frame_interval_sec)

    Path(extracted_frames_path).mkdir(parents=True, exist_ok=True)

    # โหลด subtitle
    subtitles = []
    if transcript_filepath and os.path.exists(transcript_filepath):
        for caption in webvtt.read(transcript_filepath):
            subtitles.append({
                'start': timestamp_to_seconds(caption.start),
                'end': timestamp_to_seconds(caption.end),
                'text': caption.text
            })

    frame_count = 0
    saved_count = 0
    metadatas = []

    while True:
        success, frame = video_capture.read()
        if not success:
            break

        if frame_count % frame_interval == 0:
            # เซฟ frame
            frame_filename = f"frame_{saved_count}.jpg"
            frame_path = os.path.join(extracted_frames_path, frame_filename)
            cv2.imwrite(frame_path, frame)

            video_time_sec = frame_count / fps  # เวลาที่ frame นี้อยู่
            mid_time_ms = round(video_time_sec * 1000, 1)  # mid time เป็น milliseconds

            # หา subtitle ที่ตรงช่วงเวลา
            subtitle_text = find_subtitle_for_seconds(subtitles, video_time_sec)

            # เก็บ metadata รูปแบบใหม่
            metadatas.append({
                'extracted_frame_path': str(Path(frame_path)),
                'transcript': subtitle_text,
                'video_segment_id': saved_count,
                'video_path': str(Path(video_filepath)),
                'mid_time_ms': mid_time_ms
            })

            saved_count += 1

        frame_count += 1

    video_capture.release()

    # Save JSON
    metadata_json_path = os.path.join(output_dir, "metadata.json")
    with open(metadata_json_path, 'w', encoding='utf-8') as f:
        json.dump(metadatas, f, ensure_ascii=False, indent=2)

    print(f"✅ ดึง frame และ metadata เสร็จแล้ว: {saved_count} รูป")
    return metadatas

# Helper: timestamp string --> seconds (float)
def timestamp_to_seconds(timestamp_str):
    h, m, s = timestamp_str.split(':')
    s, ms = (s.split('.') + ['0'])[:2]  # handle no milliseconds
    return int(h) * 3600 + int(m) * 60 + int(s) + int(ms) / 1000

# Helper: หา subtitle ที่ตรงกับเวลา
def find_subtitle_for_seconds(subtitles, current_sec):
    for sub in subtitles:
        if sub['start'] <= current_sec <= sub['end']:
            return sub['text']
    return ""
