"""
CodeAlpha - Python Programming Internship
Task 3 (Option A): Task Automation with Python Scripts
Move all .jpg files from a source folder to a new destination folder.

Key Concepts Used: os, shutil, file handling.
"""

import os
import shutil


def move_jpg_files(source_folder, destination_folder):
    if not os.path.isdir(source_folder):
        print(f"Source folder does not exist: {source_folder}")
        return

    os.makedirs(destination_folder, exist_ok=True)

    moved_count = 0
    for filename in os.listdir(source_folder):
        if filename.lower().endswith(".jpg") or filename.lower().endswith(".jpeg"):
            src_path = os.path.join(source_folder, filename)
            dest_path = os.path.join(destination_folder, filename)

            if os.path.isfile(src_path):
                shutil.move(src_path, dest_path)
                print(f"Moved: {filename}")
                moved_count += 1

    if moved_count == 0:
        print("No .jpg files found to move.")
    else:
        print(f"\nDone! Moved {moved_count} .jpg file(s) to '{destination_folder}'.")


if __name__ == "__main__":
    print("=== Move .jpg Files ===\n")
    source = input("Enter the source folder path: ").strip()
    destination = input("Enter the destination folder path: ").strip()
    move_jpg_files(source, destination)
