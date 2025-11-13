# TeraBox Direct Download Link Generator

A beautiful, fast, and user-friendly command-line tool to generate **direct download links** and file info for TeraBox shared files.  
Powered by the excellent [`terabox-downloader`](https://github.com/mhoe1/terabox-downloader) library and enhanced with a colorful [Rich](https://github.com/Textualize/rich) interface.

Say goodbye to slow web redirects and hello to **instant direct links**!

---

## Features

- Generate direct download links for TeraBox shared files
- Display file name and size
- Friendly, colorful CLI interface (Rich)
- Persistent session via saved cookie
- Handles errors and invalid links gracefully

---
## Preview

![TeraBox CLI Preview](preview.png)

## Prerequisites

- Python 3.7+
- TeraBox account and a valid session cookie

---

## Installation

1. **Clone or Download this Repository**

    ```bash
    git clone https://github.com/zerosocialcode/TeraLinked.git
    cd TeraLinked
    ```

2. **Install Required Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

## Configuration

- **COOKIE**:  
  Replace the value of `COOKIE` in the script with your own TeraBox session cookie string.

    ```
    COOKIE = "lang=en; ndus=YOUR_NDUS_COOKIE_VALUE"
    ```

    You can obtain your cookie from your browser's developer tools after logging into TeraBox.

---

## Usage

Run the script from your terminal:

```bash
python main.py
```

You will be prompted to enter a TeraBox shared link.  
Type `exit` to quit the program.

**Example interaction:**
```
📦 TeraBox Direct Download Link Generator

Enter TeraBox shared link (or type 'exit' to quit): https://terabox.com/s/1abcXYZ...

✅ File Info:
📁 File Name: MyVideo.mp4
📦 File Size: 800 MB

🔗 Direct Download Link:
https://download-link-generated-by-teraboxdl.com/abc123...
```

---

## Notes

- Your TeraBox cookie is required for authentication.  
- The script suppresses the TeraboxDL banner for a cleaner output.
- If you encounter errors, check that your cookie is valid and not expired.

---

## License

MIT License (or your license here)
