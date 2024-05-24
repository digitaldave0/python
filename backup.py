import os
import shutil
import zipfile
import argparse
from datetime import datetime



def backup_folder(source_folder, backup_folder):
   print("Source Folder:", source_folder)
   print("Backup Folder:", backup_folder)



   # Get the current date and time with microsecond precision
   current_datetime = datetime.now().strftime("Backup_%Y-%m-%d_%H-%M-%S-%f")



   # Create the backup folder inside the destination folder
   backup_folder_path = os.path.join(backup_folder, current_datetime)



   print("Backup Folder Path:", backup_folder_path)



   try:
       os.makedirs(backup_folder_path)
   except FileExistsError:
       print(f"Backup folder '{backup_folder_path}' already exists. Skipping backup operation.")
       return



   # Copy all files from source to destination
   for root, dirs, files in os.walk(source_folder):
       for file in files:
           source_file_path = os.path.join(root, file)
           dest_file_path = os.path.join(backup_folder_path, os.path.relpath(source_file_path, source_folder))
           os.makedirs(os.path.dirname(dest_file_path), exist_ok=True)
           shutil.copy(source_file_path, dest_file_path)



   # Zip the copied files
   backup_zip_file = os.path.join(backup_folder, current_datetime + ".zip")
   with zipfile.ZipFile(backup_zip_file, 'w') as zipf:
       for root, dirs, files in os.walk(backup_folder_path):
           for file in files:
               file_path = os.path.join(root, file)
               zipf.write(file_path, os.path.relpath(file_path, backup_folder_path))



   print("Backup completed successfully.")



if __name__ == "__main__":
   # Parse command-line arguments
   parser = argparse.ArgumentParser(description="Backup folder and subfolders and zip them.")
   parser.add_argument("source_folder", help="Path to the source folder to be backed up")
   parser.add_argument("backup_folder", help="Path to the backup folder where the backup will be stored")
   args = parser.parse_args()



   # Perform backup
   backup_folder(args.source_folder, args.backup_folder)