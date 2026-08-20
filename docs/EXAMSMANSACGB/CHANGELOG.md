# Changelog — Exam SMAN 1 Cigombong

## [v1.2-stable] - 2026-07-22

###  Final Patches & Bypasses
- ✅ **Screen Pinning** — completely disabled (startLockTask bypassed)
- ✅ **FLAG_SECURE (0x2000)** — removed (screenshots & screen recording allowed)
- ✅ **15-Minute Ban** — neutralized (onPause, onResume, onTrimMemory penalty removed)
- ✅ **OnPause Receiver Crash** — fixed (unregisterReceiver error resolved)
- ✅ **Exit Button** — fixed (closes activity properly)
- ✅ **Branding Toast** — injected ("Made With ❤ From Mirzadev")

###  APK Info
- **Version Code**: 2
- **Version Name**: 1.2-stable

###  Test Status
- ✅ Screen pinning — **disabled**
- ✅ Screenshot — **allowed**
- ✅ Exit/Re-enter — **no reload/restart**
- ✅ 15-min ban — **disabled**
- ✅ Crash — **fixed**

---

## [v1.1-beta] - 2026-07-21

###  Development Patches (In Progress)
-  Screen pinning — partially disabled (still some triggers)
-  FLAG_SECURE — removed
-  Ban detection — partially bypassed (onPause still active)
-  Crash on pause — still present

### Important Discovery
- **App Type**: Found out this is a **Compose App**, not Cordova!
- **Implication**: Different patching approach required (no JS/plugins.js, only smali)

### APK Info
- **Version Code**: 1
- **Version Name**: 1.1-beta

### Notes
- Initial patching phase
- Discovered app uses Jetpack Compose (not WebView-based)
- Need to handle lifecycle differently

---

## [v1.0] - 2025-11-21

### initial Release (Original APK)

### APK Info
- **Version Code**: 1
- **Version Name**: 1.0

### Original Protections (Active)
- ❌ Screen pinning — **active**
- ❌ FLAG_SECURE (0x2000) — **active** (no screenshot)
- ❌ 15-Minute Ban — **active**
- ❌ OnPause crash — **active**

---

## Notes

- **Compose App** — This app uses Jetpack Compose (not Cordova/WebView)
- **Patches applied to smali only** (no JavaScript/plugins.js modifications)
- **Lifecycle-based protections** handled via smali patching
- **No assets/public/ folder** — confirms non-Cordova architecture
