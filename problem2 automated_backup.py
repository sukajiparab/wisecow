import shutil
import os
from datetime import datetime


SOURCE_DIR = '/home/rahulpolubothu/hiapp/source'

DEST_DIR = '/home/rahulpolubothu/hiapp/destination'


def backup_directory():
    backup_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_dir = os.path.join(DEST_DIR, f"backup_{backup_time}")

    try:
        shutil.copytree(SOURCE_DIR, backup_dir)
        print("Backup successful.")
    except Exception as e:
        print(f"Backup failed: {e}")

if __name__ == "__main__":
    backup_directory()
