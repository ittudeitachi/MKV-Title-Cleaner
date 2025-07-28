import os
import subprocess

# Path to mkvpropedit.exe
mkvpropedit_path = r"C:\Program Files\MKVToolNix\mkvpropedit.exe"

# Root folder to start scanning
root_dir = r"C:\Users\iirusham\Documents\1\New folder"  # <-- Change this to your target folder

def remove_title_metadata(root, tool_path):
    for dirpath, _, filenames in os.walk(root):
        for file in filenames:
            if file.lower().endswith(".mkv"):
                file_path = os.path.join(dirpath, file)
                print(f"🔄 Removing title from: {file_path}")
                try:
                    subprocess.run(
                        [tool_path, file_path, "--delete", "title"],
                        check=True,
                        stdout=subprocess.DEVNULL,
                        stderr=subprocess.DEVNULL
                    )
                except subprocess.CalledProcessError:
                    print(f"❌ Failed to process: {file_path}")

if __name__ == "__main__":
    if not os.path.exists(mkvpropedit_path):
        print("❌ mkvpropedit.exe not found. Please check the path.")
    elif not os.path.exists(root_dir):
        print("❌ root_dir does not exist. Please check the folder path.")
    else:
        remove_title_metadata(root_dir, mkvpropedit_path)
        print("✅ Done.")
