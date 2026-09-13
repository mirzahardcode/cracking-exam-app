# Changelog

All notable changes to this APK modification project will be documented in this file.

Format based on [Keep a Changelog](https://keepachangelog.com/).
APK version tracks upstream app version. Patch version tracks our modifications.

---

## [v8.3] - 2026-09-14

Full re-audit against CBT Exam Browser v8.3. Previous patches re-applied and extended.

### ✅ Bypassed / Modified
- Screen pinning (lock task mode) — `ExamActivity.x()` hard-returned
- FLAG_SECURE removed (screenshot allowed)
- Ban detection (15-minute system) — DeviceStatus override
- Ads removed — AdMob, IronSource, Facebook AN, Unity, Vungle, Yandex (6 networks)
- PairIP license check — Application class swapped to `MyApplication`
- DeviceStatus check bypass — all 12 `is*Ok` flags forced true via `Lo/xc1;->a()`
- Copy-paste restriction removed — native long-press + WebView `user-select` re-enabled
- Branding toast injected
- Bluetooth / camera / notification permission dialogs neutralized

### 🔧 Technical Changes
- Manifest: pruned all ad SDK activities, services, providers
- Manifest: `android:name` swapped from `com.pairip.application.Application` → `com.cbt.exam.browser.MyApplication`
- Smali: `Lo/x3;->b()`, `Lo/x3;->c()` → `return-void`
- Smali: `Lo/ia2;->a()` → `return-void`
- Smali: `Lo/yc2;->b()` → `return-void`
- Smali: `Lo/yt1;->a()` → `return-void`
- Smali: `Lo/tb1;->onLongClick()` → returns `false`
- Smali: `ExamActivity.onCreate` — copy-paste gate inverted (`if-nez` → `goto`)
- Smali: `ExamActivity.onCreate` — JS injection post-`loadUrl()` for CSS `user-select: text`
- Smali: `Lo/xc1;->a()` — field override block inserted before `return-object`

### 📦 Build Info
- Base APK: `com.cbt.exam.browser` v8.3
- Toolchain: apktool + jadx + VSCode Copilot + apksigner
- Sign: custom keystore
- Test device: personal Android device, isolated environment

### ⚠️ Notes
- Publish only for educational / security research purposes
- Do not install on devices under exam invigilation
- No warranty, no liability

---

## [v6.6] - 2026-08-19

### ✅ Bypassed / Modified
- Screen pinning disabled
- FLAG_SECURE removed (screenshot allowed)
- Ban bypassed
- Ads removed
- Branding toast injected

---

## [v1.0] - 2020-12-04

### ✅ Released
- Initial release on Play Store
