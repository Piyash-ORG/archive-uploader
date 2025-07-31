# 📤 Archive.org Auto Uploader (Termux Compatible)

A Python script that automatically uploads video and image files from your Documents folder (in Termux) to Archive.org.

---

## 🚀 Features

- Scans your Documents/ folder for media files  
- Supports common video and image formats  
- Generates clean, auto-based Archive.org identifiers  
- Logs upload status and shareable links  
- Uses `.env` file to store API credentials securely  

---

## 📁 Supported File Types

- 🎥 Video: `.mp4`, `.mkv`, `.mov`, `.avi`, `.webm`  
- 🖼️ Image: `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.webp`  

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Piyash-ORG/archive-uploader.git
cd archive-uploader

2️⃣ Install Dependencies

pip install internetarchive python-dotenv

3️⃣ Create .env File

In the project root folder, create a .env file to store your Archive.org credentials:

nano .env

Paste the following content and save:

ACCESS_KEY=your_archive_access_key
SECRET_KEY=your_archive_secret_key

➡️ Get your credentials from: https://archive.org/account/s3.php


---

4️⃣ Enable Storage Access (Termux Only)

termux-setup-storage

Then place your media files in:

~/sdcard/Documents


---

▶️ Run the Script

python upload.py

You'll see live upload status in the terminal. Uploaded links are also saved to:

Documents/archive_upload_log.txt


---

📝 Upload Log Example

🕒 Upload Session: 2025-07-31 17:22:50
----------------------------------------------------------
✅ myvideo.mp4
🔗 https://archive.org/download/myvideo-auto/myvideo.mp4


---

👨‍💻 Made for Developers & Archivists

Quick and simple way to archive your media files directly from your Android phone (Termux) or PC using Python and the Internet Archive API.


---

🔐 Security Note

Never share your .env file publicly.
Add .env to your .gitignore file to prevent accidental uploads.


---

🔧 Need help?

Open an issue on GitHub or reach out for support.
/\
