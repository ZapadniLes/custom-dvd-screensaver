# Custom dvd screensaver

With this script and a few more steps below you can create a screensaver in the style of the old dvd screensaver but with your own logo.

## Prerequisites

- Python 3.x
- Pygame library
- PyInstaller

## Installation Steps

### 1. Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/dvd-logo-screensaver.git
cd dvd-logo-screensaver
```
### 2. Install Python

### 3. Install Required Libraries
Install the necessary libraries using pip:
```bash
pip install pygame pyinstaller
```
### 4. Convert and Rename Your Image
Ensure your logo image is named **dvd_logo.bmp** and place it in the same directory as main.py.

### 5. Create the Executable
```bash
pyinstaller --onefile --add-data "dvd_logo.bmp;." -w main.py
```
### 6. Locate the Executable
Navigate to the dist folder where you will find the main.exe file:
```bash
cd dist
```
### 7. Rename the Executable
Rename main.exe to your desired screensaver name and change the file extension to .scr.

