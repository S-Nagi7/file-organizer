# 📂 File Organizer Automation Tool

## 📝 Overview

The **File Organizer Automation Tool** is a Python script designed to automatically clean and organize messy folders.
It scans a directory, identifies file types based on their extensions, and moves them into neatly labeled folders.
This saves time and keeps your system clean and easy to navigate.

---

##  Prerequisites

* Python **3.6 or higher**
* Uses only built-in Python libraries:

  * `os`
  * `shutil`

---

## 🚀 Installation & Usage

### **1. Download the `organizer.py` (or `file_organizer.py`) script**

### **2. Open Terminal / Command Prompt**




### **4. Run the script**

```
python organizer.py


## 📁 Supported Categories

| Category       | Extensions                                                   |
| -------------- | ------------------------------------------------------------ |
| **Images**     | .jpg, .jpeg, .png, .gif, .bmp, .svg, .tiff, .ico, .webp      |
| **Videos**     | .mp4, .mkv, .flv, .avi, .mov, .wmv, .webm                    |
| **Documents**  | .pdf, .doc, .docx, .txt, .ppt, .pptx, .xls, .xlsx, .csv, .md |
| **Music**      | .mp3, .wav, .aac, .flac, .ogg, .m4a                          |
| **Programs**   | .exe, .msi, .bat, .sh, .py, .js, .html, .css, .java, .cpp    |
| **Compressed** | .zip, .rar, .7z, .tar, .gz, .iso                             |
| **Others**     | Anything not matching a category                             |

---

## 📂 Project Folder Structure

```
file-organizer-project/
│── README.md
│── organizer.py
│── requirements.txt
└── tests/
    └── test_organizer.py
```

---

## 🖼 Example — Before Organization

```
/Downloads/
│── report.pdf
│── song.mp3
│── photo.jpg
└── installer.exe
```

## 🗂 Example — After Organization

```
/Downloads/
│── Documents/
│     └── report.pdf
│── Music/
│     └── song.mp3
│── Images/
│     └── photo.jpg
└── Programs/
      └── installer.exe


