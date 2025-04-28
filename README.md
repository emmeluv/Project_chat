# Project: YouTube Video Downloader (Streamlit + yt-dlp)

ระบบเว็บแอปพลิเคชันที่ใช้สำหรับดาวน์โหลดวิดีโอจาก YouTube เป็นไฟล์ `.mp4`
รองรับทั้งลิงก์ประเภท:
- ปกติ (https://www.youtube.com/watch?v=xxx)
- Shorts (https://youtube.com/shorts/xxx)
- Embed (https://www.youtube.com/embed/xxx)
- และ youtu.be link (https://youtu.be/xxx)

---

## 🚀 วิธีติดตั้งและใช้งาน

### 1. เตรียมสภาพแวดล้อม Python
```bash
python -m venv .venv
.\.venv\Scripts\activate   # สำหรับ Windows
```

ติดตั้งไลบรารีที่จำเป็น:
```bash
pip install -r requirements.txt
```

(ใน `requirements.txt` ควรมี)
```plaintext
streamlit
yt-dlp
tqdm
```

---

### 2. ติดตั้ง ffmpeg

**จำเป็นต้องติดตั้ง `ffmpeg` เพื่อให้ระบบรวมวิดีโอะเสียงเป็น `.mp4` ได้สำเร็จ**

วิธีติดตั้ง:
- เปิด PowerShell (Run as Administrator)
- ติดตั้ง Chocolatey (ครั้งเดียวเท่านั้น):

```powershell
Set-ExecutionPolicy Bypass -Scope Process -Force; `
[System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; `
iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
```

- ติดตั้ง ffmpeg:

```powershell
choco install ffmpeg
```

เสร็จแล้วให้ปิดและเปิด PowerShell ใหม่ หรือ Terminal เพื่อให้ Windows รู้จำ PATH ใหม่

ทดสอบว่า ffmpeg ใช้ได้ไม่
```bash
ffmpeg -version
```

---

### 3. รันแอป Streamlit

```bash
streamlit run app.py
```

ระบบจะเปิดเบราว์เซอร์สเอ็ปมาที่ `http://localhost:8501`

---

## 📦 โครงสร้างโปรเจกต์
```plaintext
Project_chat/
🔍
├👉 app.py                 # ไฟล์หลัก Streamlit
├👉 src/
│   └👉 download_video.py   # ฟังก์ชั่นโหลดวิดีโอด้วย yt-dlp
├👉 datas/
│   └👉 videos/             # โฟลเดอร์เก็บวิดีโอ
├👉 .venv/                  # (Virtual Environment)
├👉 requirements.txt        # รายการไลบรารี
└👉 README.md               # (ไฟล์นี้)
```

---

## ✅ หมายเหตุพิเศษ
- ถ้าไม่มีการติดตั้ง ffmpeg จะไม่สามารถวมวิดีโอะเสียงเป็น mp4 ได้
- yt-dlp รองรับการดาวน์โหลดทุกประเภท YouTube รวมถึง Shorts และ Embeds ได้
- ไฟล์ที่ดาวน์โหลดสำเร็จจะถึงไปในโฟลเดอร์ `datas/videos/`

---

## ✨ ฟีเจอร์ที่กำลังพัฒนาหรือ
- เลือกความละเอียดวิดีโอ (360p / 720p / 1080p)
- เลือกดาวน์โหลดเฉพะ Audio (.ฟาย .mp3)
- รองรับการดาวน์โหลดหลายวิดีโอพร้อมกัน (Batch download)

---

