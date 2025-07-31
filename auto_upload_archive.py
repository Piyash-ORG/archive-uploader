import os
import re
import internetarchive
from datetime import datetime
from urllib.parse import quote
from dotenv import load_dotenv  # 👈 dotenv import

# ✅ Load environment variables from .env file
load_dotenv()
ACCESS_KEY = os.getenv("ACCESS_KEY")
SECRET_KEY = os.getenv("SECRET_KEY")

# 📁 Documents folder path (Termux specific)
doc_path = "/data/data/com.termux/files/home/storage/documents/"

# 🎯 Supported file extensions (Videos + Images)
allowed_exts = [
    '.mp4', '.mkv', '.mov', '.webm', '.avi',       # 🎥 Videos
    '.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp'  # 🖼️ Images
]

# 📜 Log file (to record uploaded links + titles)
log_file = os.path.join(doc_path, "archive_upload_log.txt")

# 🔍 Scan the folder for supported files
target_files = [f for f in os.listdir(doc_path) if os.path.splitext(f)[1].lower() in allowed_exts]

if not target_files:
    print("❌ No supported files found in Documents folder.")
    exit()

with open(log_file, "a") as log:
    log.write("\n\n🕒 Upload Session: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
    log.write("----------------------------------------------------------\n")

    for file_name in target_files:
        file_path = os.path.join(doc_path, file_name)

        # ✅ Generate a safe identifier for Archive.org
        raw_name = os.path.splitext(file_name)[0].lower()
        safe_name = re.sub(r'[^a-z0-9_.-]+', '-', raw_name)
        safe_name = re.sub(r'^[-_.]+', '', safe_name)
        identifier = safe_name[:95] + "-auto"

        # 🎯 Determine media type and collection
        ext = os.path.splitext(file_name)[1].lower()
        if ext in ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp']:
            mediatype = 'image'
            collection = 'opensource_image'
        else:
            mediatype = 'movies'
            collection = 'opensource_movies'

        metadata = {
            'title': file_name,
            'mediatype': mediatype,
            'collection': collection
        }

        print(f"\n🚀 Uploading: {file_name} as [{identifier}] ...")

        try:
            r = internetarchive.upload(
                identifier,
                files=[file_path],
                metadata=metadata,
                access_key=ACCESS_KEY,
                secret_key=SECRET_KEY,
                verbose=True
            )

            if r[0].status_code == 200:
                encoded_name = quote(file_name)
                direct_link = f"https://archive.org/download/{identifier}/{encoded_name}"
                print(f"✅ Upload successful!\n🔗 {direct_link}")
                log.write(f"✅ {file_name}\n🔗 {direct_link}\n\n")
            else:
                print(f"❌ Upload failed for {file_name} | Status: {r[0].status_code}")
                log.write(f"❌ {file_name} - Failed (Status: {r[0].status_code})\n\n")

        except Exception as e:
            print(f"⚠️ Error uploading {file_name} → {e}")
            log.write(f"⚠️ {file_name} - Error: {str(e)}\n\n")        # ✅ Generate a safe identifier for Archive.org
        raw_name = os.path.splitext(file_name)[0].lower()
        safe_name = re.sub(r'[^a-z0-9_.-]+', '-', raw_name)     # Keep only safe characters
        safe_name = re.sub(r'^[-_.]+', '', safe_name)           # Remove leading special chars
        identifier = safe_name[:95] + "-auto"                   # Limit length to 100 characters

        # 🎯 Determine media type and collection
        ext = os.path.splitext(file_name)[1].lower()
        if ext in ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp']:
            mediatype = 'image'
            collection = 'opensource_image'
        else:
            mediatype = 'movies'
            collection = 'opensource_movies'

        metadata = {
            'title': file_name,
            'mediatype': mediatype,
            'collection': collection
        }

        print(f"\n🚀 Uploading: {file_name} as [{identifier}] ...")

        try:
            r = internetarchive.upload(
                identifier,
                files=[file_path],
                metadata=metadata,
                access_key=ACCESS_KEY,
                secret_key=SECRET_KEY,
                verbose=True
            )

            if r[0].status_code == 200:
                encoded_name = quote(file_name)
                direct_link = f"https://archive.org/download/{identifier}/{encoded_name}"
                print(f"✅ Upload successful!\n🔗 {direct_link}")
                log.write(f"✅ {file_name}\n🔗 {direct_link}\n\n")
            else:
                print(f"❌ Upload failed for {file_name} | Status: {r[0].status_code}")
                log.write(f"❌ {file_name} - Failed (Status: {r[0].status_code})\n\n")

        except Exception as e:
            print(f"⚠️ Error uploading {file_name} → {e}")
            log.write(f"⚠️ {file_name} - Error: {str(e)}\n\n")
