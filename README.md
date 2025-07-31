# 📤 Archive.org Auto Uploader (Termux Compatible)

This script automatically uploads video and image files from your **Documents** folder (in Termux) to [Archive.org](https://archive.org).

---

## 📦 Features

- Automatically scans `Documents/` folder
- Supports video & image formats
- Auto-generates clean identifier
- Logs uploaded links with status
- Archive.org API key/secret stored via `.env`

---

## 📁 Supported File Types

- 🎥 `.mp4`, `.mkv`, `.mov`, `.avi`, `.webm`
- 🖼️ `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.webp`

---

## ⚙️ Setup Instructions

### 1. 📥 Clone or Download

```bash
git clone https://github.com/Piyash-ORG/archive-uploader.git
cd archive-uploader

2. 🐍 Install Requirements

pip install internetarchive python-dotenv

3. 🗝️ Create .env File

Create a .env file in the project root folder with your Archive.org credentials:

ACCESS_KEY=your_archive_access_key
SECRET_KEY=your_archive_secret_key

Replace with your real keys from: https://archive.org/account/s3.php

4. 📂 Allow Storage Access (for Termux only)

termux-setup-storage

Make sure your files are in:

/data/data/com.termux/files/home/storage/documents/


---

🚀 Run the Script

python upload.py

You’ll see live upload status and get the Archive.org links printed and saved to:

Documents/archive_upload_log.txt


---

📝 Log Example

🕒 Upload Session: 2025-07-31 17:22:50
----------------------------------------------------------
✅ myvideo.mp4
🔗 https://archive.org/download/myvideo-auto/myvideo.mp4


---

👨‍💻 Made for Developers & Archivists

Fast way to archive your files directly from your phone or PC using the power of Python and Internet Archive API.


---

🔒 Security Note

Never share your .env file publicly.
