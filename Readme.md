# File Organizer 🚀📂

Welcome to the File Organizer! 🎉

I was inspired by a paid software (Internet Download Manager) that automatically organizes files for you. But I thought, why pay when I can build my own? So, here’s my very own File Organizer that sorts your files automatically into neat folders based on file types! 😎

## Features ✨

- Automatically organizes your files into predefined folders like Music, Documents, Photos, Compressed, etc. 📁
- If a file doesn’t have a specific category, it gets moved to **Miscellaneous**. 🤷‍♂️
- Simple command-line tool that scans your directory and moves the files around like magic! 🔮
- Scans your current working directory and moves files to respective folders based on their extension (e.g., `.jpg` → Photos, `.mp4` → Videos, etc.).
- Automatically creates necessary folders if they don’t exist yet. 💥
- Supports multiple file types, including audio, video, documents, compressed files, photos, and more! 🖼️🎶📄

## Supported File Extensions 📂

Here’s a quick look at the supported file extensions and their corresponding folders:

- **Audio/Video:** `.wav`, `.mp3`, `.mp4`, `.mpg`, `.avi` → _Music, Videos_
- **Photos:** `.jpg`, `.jpeg`, `.png`, `.gif`, `.svg` → _Photos_
- **Documents:** `.pdf`, `.txt`, `.csv`, `.xlsx`, `.pptx` → _Documents, Text Files, Spreadsheets_
- **Compressed:** `.zip`, `.rar`, `.tar` → _Compressed_
- **Miscellaneous:** Files with unknown extensions or no extension will be moved to **Miscellaneous**. 🔀

## How it Works ⚙️

1. **Scan:** Run the script and it will scan your current directory. 🕵️‍♂️
2. **Identify:** It identifies file extensions (like `.mp4`, `.jpg`, `.txt`, etc.).
3. **Organize:** Based on the file extension, the file is moved into a corresponding folder (e.g., `.mp4` files go into the Videos folder). 🎥
4. **Fallback:** Files without a defined extension category go to **Miscellaneous**. 🗂️

## 🧑‍💻 Installation

- Clone this repository or download the Python script. 🔽
- Make sure you have Python installed on your machine. 💻
- Run the script in the terminal or command prompt:

```bash
  python file_organizer.py
```

## Usage 🏃‍♀️

Once you run the script, it’ll ask you if you want to organize your current directory. You just need to type Yes or No to confirm, and it’ll do the rest for you! 💪

**Sample Output:**

```bash
Files found: file1.mp4, image.jpg, notes.txt
File Extensions Found: mp4, jpg, txt
Files moved to: Videos/mp4, Photos/jpg, Text Files/txt
```

## Next Goal 🚀

I’m planning to convert this script into a GUI (Graphical User Interface) app for better usability! Stay tuned. 🖥️✨

## License 📄

This project is open source. Feel free to contribute, use, or adapt the code! 🙌

Enjoy organizing your files! 🎉 Let me know if you have any suggestions or fun ideas for the next version! 😄
