import os
from pathlib import Path
import shutil

FilesExtension = {
    "wav": "Music/wav",
    "mp4": "Videos/mp4",
    "jpg": "Photos/jpg",
    "jpeg": "Photos/jpeg",
    "svg": "Photos/svg",
    "pdf": "Documents/pdf",
    "ppt": "Powerpoints",
    "pptx": "Powerpoints",
    "zip": "Compressed/zips",
    "rar": "Compressed/rar",
    "mp3": "Music/mp3",
    "exe": "Programs",
    "txt": "Text Files",    
    "csv": "Documents",     
    "xlsx": "Spreadsheets", 
    "png": "Photos",        
    "gif": "Photos",        
    "html": "Web Pages",    
    "json": "Data",
    "cdr": "Corel Draw",
    "sql": "Server Query Language",
    "drawio": "Diagrams",
    "cs": "CSharp",
    "torrent": "Miscilanious",
    "py": "Python"
}

sign = "-"
sepreator = '\n' + sign * 150 + '\n'

Current_Working_Directory = os.getcwd()

def scan_directory():
    print("Scanning Directory...", end=sepreator)
    Files = [entry.name for entry in os.scandir(Current_Working_Directory) if entry.is_file()]
    return Files

print("Are you sure you want to organize this directory?")
print(Current_Working_Directory)
print("Write Yes or No")
flag = input().strip().lower() in ["yes", "y", "1"]

if flag:
    moved_files_count = 0
    while True:
        Files = scan_directory()
        print("Files found:", Files, end=sepreator)
        
        if len(Files) == 0:
            print("No files found. Operation aborted.")
            break
        else:
            Extensions = set([file.split('.')[-1] for file in Files if '.' in file])
            print("File Extensions Found:", Extensions, end=sepreator)
            
            for ext in Extensions:
                if ext in FilesExtension:
                    os.makedirs(FilesExtension[ext], exist_ok=True)
                else:
                    print(f"Warning: No folder category defined for the '{ext}' extension.")
            
            for File in Files:
                exet = File.split('.')[-1]
                destination_folder = FilesExtension.get(exet, "Miscilanious")

                if destination_folder != "Miscilanious":
                    os.makedirs(destination_folder, exist_ok=True)

                source_path = os.path.join(Current_Working_Directory, File)
                destination_path = os.path.join(Current_Working_Directory, destination_folder, File)

                shutil.move(source_path, destination_path)
                print(f"Moved: {File} -> {destination_folder}")
                moved_files_count += 1

            print(f"\nTotal files moved: {moved_files_count}")
            break

else:
    print("Aborting operation, terminating the operation.")
    input("Press any key to exit the operation.")
