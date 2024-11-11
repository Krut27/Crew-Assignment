# Crew-Assignment
BITSkrieg Crew Project : Keylogger
## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Legal and Ethical Considerations](#legal-and-ethical-considerations)
4. [Requirements](#requirements)
5. [Installation](#installation)
6. [Usage Instructions](#usage-instructions)
7. [Configuration](#configuration)
---

## Introduction

This project is a **Keylogger Monitoring Tool** designed for **educational and authorized monitoring purposes** within a controlled school environment. Its main purpose is to demonstrate how certain monitoring software works and provide insight into system security and user activity logging. 

> **Disclaimer**: This tool must only be used on systems where monitoring has been explicitly authorized by the administration, and it must comply with all relevant privacy laws.

---

## Features

- **Keystroke Logging**: Records key presses and saves them to a text file for analysis.
- **Screenshot Capture**: Takes a screenshot every 30 seconds to provide visual records.
- **Webcam Capture**: Periodically takes images using the system’s webcam if available.
- **Startup Setup**: Configured to run automatically upon startup on Windows.

---

## Legal and Ethical Considerations

> **Warning**: Unauthorized use of this software can infringe on privacy laws and may be illegal. Ensure you have obtained all necessary permissions and approvals before deploying this tool.

- **Authorization Required**: Only use on devices where explicit administrative authorization has been granted.
- **Informed Consent**: Users should be informed of the monitoring software and its purpose, with proper consent where applicable.
- **Data Security**: Collected data should be securely stored and accessed only by authorized personnel.

---

## Requirements

- Python 3.6 or higher
- Libraries: `pynput`, `pygame`, `Pillow`, `win32com`, `winshell`
- Windows OS (for startup functionality and webcam access)

### Installation of Required Libraries

Run the following commands to install the required libraries:
```bash
pip install pynput pygame pillow pypiwin32 winshell
```
---
## Installation
 **1. Clone the repository**:
```bash
git clone https://github.com/Krut27/Crew-Assignment.git
cd Crew-Assignment
```
**2. Configure the script:**

- Open the script in an editor and specify the `file_path` where logs and images will be saved.

- Make other adjustments to the configuration as necessary.



**3. Startup Setup (Windows):**
- The script includes a function to create a shortcut in the Windows Startup folder, so it automatically launches on boot.

- Ensure this script has the required permissions if used in a restricted environment.
## Configuration

To customize this tool, you can modify certain key parameters within the script before deploying it. These parameters include file paths, intervals for screenshot and webcam capture, and keyboard shortcuts. Below are some key settings:

- `file_path` Define the directory where you want the keystroke log and screenshots to be saved.
- Screenshot Interval: Modify the interval for screenshots by adjusting `time.sleep(30)` in the take_screenshot function.
