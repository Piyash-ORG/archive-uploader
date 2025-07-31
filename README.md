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

