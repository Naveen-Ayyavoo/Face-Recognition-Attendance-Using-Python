<div align="center">

# 🎯 Face Recognition Attendance System

*An intelligent, automated attendance tracking solution powered by AI*

[![Python](https://img.shields.io/badge/Python-3.7+-3776ab?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/downloads/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.11+-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)](https://opencv.org/)
[![Platform](https://img.shields.io/badge/Platform-Windows-0078d4?style=for-the-badge&logo=windows&logoColor=white)]()

[🚀 Quick Start](#-installation) • [📖 Documentation](#-table-of-contents) • [🤝 Contributing](#-contributing)

</div>

---

## 🌟 Overview

Transform your attendance management with cutting-edge facial recognition technology! This system automatically identifies students through webcam feeds, logs attendance in real-time, and generates professional PDF reports—all while maintaining high accuracy and ease of use.

> **⚠️ Platform Notice**  
> Currently optimized for **Windows environments**. Cross-platform support for Linux and macOS coming soon!

<!-- 
<div align="center">
  <img src="./assets/demo.gif" alt="System Demo" width="700" style="border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);" />
  <p><em>Real-time face recognition in action</em></p>
</div>
-->

## 📋 Table of Contents

<details>
<summary>Click to expand</summary>

- [🌟 Overview](#-overview)
- [✨ Key Features](#-key-features)
- [🏗️ Project Architecture](#️-project-architecture)
- [🔧 Prerequisites](#-prerequisites)
- [🚀 Installation](#-installation)
- [💻 Usage Guide](#-usage-guide)
  - [Running the System](#running-the-system)
  - [Generating Reports](#generating-reports)
- [⚙️ Configuration](#️-configuration)
- [📁 Core Components](#-core-components)
- [🔍 Troubleshooting](#-troubleshooting)
- [📄 License](#-license)
- [🤝 Contributing](#-contributing)

</details>

## ✨ Key Features

<table>
<tr>
<td width="50%">

### 🎥 **Real-time Recognition**
- Advanced facial detection & recognition
- Live webcam integration
- High-accuracy confidence thresholds
- Multi-threaded processing

</td>
<td width="50%">

### 📅 **Smart Scheduling**
- Automated session management
- Configurable class timings
- Daily attendance tracking
- Flexible time slots

</td>
</tr>
<tr>
<td width="50%">

### 📊 **Data Management**
- Excel-based logging system
- Structured student directories
- Automated file organization
- Data integrity validation

</td>
<td width="50%">

### 📄 **Professional Reports**
- PDF report generation
- Customizable templates
- Attendance analytics
- Export capabilities

</td>
</tr>
</table>

## 🏗️ Project Architecture

```
📁 face_recognition/
├── 📄 README.md                    # You are here!
├── 🐍 main.py                      # Core recognition engine
├── 📊 report_generator.py          # PDF report generator
├── 📋 requirements.txt             # Dependencies
├── 👥 student_faces/               # Student image database
│   └── 📁 RegNo_Course_Name/       # Individual student folders
│       ├── 🖼️ photo1.jpg
│       └── 🖼️ photo2.png
└── 📈 attendance_reports/          # Generated PDF reports
```


## 🔧 Prerequisites

### System Requirements

| Component | Requirement | Purpose |
|-----------|-------------|----------|
| **Python** | 3.7+ (3.9+ recommended) | Core runtime |
| **CMake** | Latest version | Building dlib library |
| **C++ Compiler** | Visual Studio Build Tools | Compiling dependencies |
| **wkhtmltopdf** | Latest version | PDF generation |

## ⚙️ Windows Setup


1. **Visual Studio Build Tools**
   ```plaintext
   Download from: https://visualstudio.microsoft.com/downloads/
   
   Install "Desktop development with C++" workload

2. **CMake**
   ```plaintext
   Download from: https://cmake.org/download/

   Add to system PATH during installation
   ```

3. **wkhtmltopdf**
   ```plaintext
   Download from: https://wkhtmltopdf.org/downloads.html

   Default path: C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe
   ```

## 🚀 Installation

### Quick Setup

```bash
# 1. Clone or download the project
git clone https://github.com/Naveen-Ayyavoo/Face-Recognition-Attendance-Using-Python.git

cd face_recognition

# 2. Create virtual environment (recommended)
python -m venv .venv

# 3. Activate virtual environment
# Windows:
.venv\Scripts\activate

# 4. Install dependencies
pip install -r requirements.txt
```

### Student Database Setup

1. **Create student folders** in `student_faces/` :

```plaintext
Format: RegNo_Course_Name
Example: S101_CSE_AliceSmith
```
2. Add student photos :

  - Use clear, frontal face images
  - Supported formats: `.jpg` , `.png` , `.jpeg`
  - Multiple images per student improve accuracy

## 💻 Usage Guide

### Running the System

```bash
# Start the attendance system
python main.py
```
**What happens next:**

1. ⌛ System waits for the scheduled time to start

2. 🔄 System initializes and loads student faces

3. 📹 Webcam activates for live recognition

4. ✅ Attendance is automatically marked based on schedule

5. 📊 Daily Excel file is created/updated


### Generating Reports
```bash
# Generate PDF report from Excel data
python report_generator.py
```

**Output:** ✅ PDF report saved to `attendance_reports/`

## ⚙️ Configuration

### 📅 Class Schedule Setup

```python
# Edit main.py
class_schedule = {
    "Morning Session": {"start": time(9, 0), "end": time(10, 30)},
    "Afternoon Session": {"start": time(14, 0), "end": time(15, 30)},
    # Add your custom sessions here
}
```
### 📊 Report Configuration

```python
# Edit report_generator.py
XLSX_INPUT_FILE = "IT_Attendance_2024-01-15.xlsx"  # Source file
PDF_OUTPUT_FILE = "attendance_report_2024-01-15.pdf"  # Output file

# Windows wkhtmltopdf path (update for other OS)
config = Configuration(
    wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"
)
```

## 📁 Core Components

| File | Purpose | Key Functions |
|------|---------|---------------|
| `main.py` | 🧠 Core engine | Face detection, recognition, Excel logging |
| `report_generator.py` | 📄 Report system | PDF generation, data formatting |
| `requirements.txt` | 📦 Dependencies | All required Python packages |

## 🔍 Troubleshooting
🚨 **Common Issues & Solutions**

### Installation Problems

❌ **dlib installation fails**

```bash
# Solution: Ensure CMake and C++ compiler are installed
pip install cmake
pip install dlib
```
❌ **Face recognition accuracy is low**

- ✅ Use high-quality, well-lit photos
- ✅ Add multiple images per student
- ✅ Ensure proper webcam positioning
- ✅ Check lighting conditions

❌ **PDF generation fails**

```python
# Check wkhtmltopdf path in report_generator.py
config = Configuration(wkhtmltopdf="/path/to/wkhtmltopdf")
```

❌ **Student folder format errors**

```plaintext
❌ Wrong: John_Doe, 123-CS-John
✅ Correct: 123_CS_JohnDoe
```
🔧 **Advanced Troubleshooting**

### Performance Optimization
- Reduce image resolution for faster processing
- Adjust confidence thresholds in main.py
- Use SSD storage for better I/O performance

### System Requirements
- **RAM:** Minimum 4GB, 8GB recommended
- **CPU:** Multi-core processor recommended
- **Webcam:** 720p or higher resolution

## 🪪 License

This project is licensed under the [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) license.  
It is free to use for **educational and personal purposes**.  
**Commercial use is strictly prohibited** without written permission.


## 🤝 Contributing

<div align="center" style="font-size: 1.5rem;">

**We welcome contributions! 🎉**

</div>

### How to Contribute

1. 🍴 Fork the repository
2. 🌿 Create a feature branch

```bash
git checkout -b feature/AmazingFeature
```

3. 📝 Make your changes

4. 🚀 Commit your changes

```bash
git commit -m 'Add some AmazingFeature'
```

5. 📤 Push to the branch

```bash
git push origin feature/AmazingFeature
```

6. 📣 Open a pull request 
<br>

### Development Roadmap

- 🌐 Cross-platform compatibility (Linux, macOS)

- 🎨 Web-based dashboard

- 📱 Mobile app integration

- 🔒 Enhanced security features

- 📊 Advanced analytics

- ☁️ Cloud storage integration
<br>

<div align="center" style="font-size: 1.5rem;">

**Made with ❤️ for educational institutions**

*Star ⭐ this repo if you found it helpful!*

</div>
