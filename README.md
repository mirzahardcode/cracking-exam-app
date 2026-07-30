# 🚀 Cracking Exam App - Research & Bypass Framework

**Educational reverse engineering project — understanding Android app protection mechanisms**

[![GitHub stars](https://img.shields.io/github/stars/mirzahardcode/cracking-exam-app)](https://github.com/mirzahardcode/cracking-exam-app/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/mirzahardcode/cracking-exam-app)](https://github.com/mirzahardcode/cracking-exam-app/network)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 📌 Disclaimer

> **⚠️ FOR EDUCATIONAL & RESEARCH PURPOSES ONLY**
>
> This repository is a **case study** in Android reverse engineering and application security research.  
> All techniques documented here are meant to help developers understand vulnerabilities and **secure their applications**.
>
> **Do not use for cheating, academic dishonesty, or illegal activities.**  
> **I am not responsible for any misuse of this information.**

---

## 📖 Overview

This project is a **documentation of my journey** reverse engineering a popular exam application.  
It covers common protection layers found in modern Android apps and how to analyze them.

### Protection Layers Studied

| Layer | Type | Description |
|-------|------|-------------|
| **Layer 1** | Integrity Protection | App tampering & signature verification |
| **Layer 2** | UI Locking | Preventing users from leaving the app |
| **Layer 3** | Behavioral Detection | Detecting when user switches apps |

---

## 🔧 Tools Used

| Tool | Purpose |
|------|---------|
| **MT Manager** | APK inspection & modification |
| **Apktool** | APK decompilation & rebuilding |
| **JADX** | Java decompilation |
| **Firebase** | Backend authentication system |
| **Termux** | Mobile reverse engineering |
| **Ghidra** | C/C++ Inspection and reverse tool |

---

## 📂 Repository Structure

```

cracking-exam-app/
├── docs/
│   └── methodology.md          # High-level approach (no technical details)
├── native/
│   └── libnative.cpp           # Bypass LicenseCheck in Shared Object (C/C++)
├── patches/
│   └── example_patch.smali     # Sample smali modification template
├── resources/
│   ├── login_panel.xml         # Custom login UI
│   └── branding_toast.smali    # Custom toast injection
├── firebase/
│   ├── database_rules.json     # Firebase Realtime DB rules
│   ├── admin.js                # For Admin Uses
│   └── admin_panel.html        # Admin panel for key management
├── scripts/
│   └── auto-patcher.py         # Automated Python Patching
└── README.md

```

---

## 🧪 Approach (High-Level)

1. **Reconnaissance** — Analyze app structure & protection layers
2. **Decompilation** — Extract smali code using apktool/MT Manager
3. **Analysis** — Identify key components & verification logic
4. **Modification** — Apply targeted patches
5. **Rebuild & Test** — Sign APK, install, and verify

---

## 🔥 Custom Branding Integration

Injected a custom toast with HTML coloring:

```

Made With ❤ From Mirzadev

```

---

## 🗄️ Firebase Key System (Custom Addition)

Built a lightweight authentication layer using Firebase Realtime Database:

- **User management** — Create & manage users
- **HWID binding** — Per-device activation
- **Expiration dates** — Time-based access control
- **Ban/Unban** — Remote device blocking

**Database Structure:**
```json
{
  "users": {
    "username": {
      "password": "xxx",
      "hwid": "device_id",
      "expired": "2025-12-31",
      "banned": false
    }
  }
}
```

---

📚 How to Use (General)

1. Clone the repository
   ```bash
   git clone https://github.com/mirzahardcode/cracking-exam-app.git
   ```
2. Read the documentation in the docs/ folder
3. Apply patches to your target APK (modify as needed)
4. Rebuild & sign using apktool
5. Test on emulator or physical device

---

🚧 Future Plans

· Automated patching tool
· Support for more app types
· Web-based admin panel
· Telegram bot for key generation

---

📞 Contact & Support

· GitHub: mirzahardcode
· Telegram: @mirzthaxx
· Project Link: github.com/mirzahardcode/cracking-exam-app

---
## 👀 See the Releases Page to Download App you want?

Download the latest APK from the [Releases Page](https://github.com/mirzahardcode/cracking-exam-app/releases/).

---

⭐ Show Your Support

If you found this project useful, please give it a star ⭐!

---

📜 License

This project is licensed under the MIT License — see the LICENSE file for details.

---

Made with ❤️ From Mirzadev

