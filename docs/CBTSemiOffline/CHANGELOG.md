# Changelog — CBT Semioffline

All notable changes to this APK modification project.

---

## [v1.2_2] - 2026-09-13

**Architectural update — PairIP removal, native dex loader migration, monetization.**

This is not a simple patch version. The app's underlying protection layer was rebuilt.

### ✅ Major Changes
- **PairIP completely removed** — license check wrapper fully stripped
- **DEX migration to `libmirsecore.so`** — all dex files relocated into a custom native loader library
- **Native loading architecture** — app now boots through `libmirsecore.so` instead of standard `classes.dex`
- **Monetization enabled** — app is now a paid release (no more free distribution)

### 🔧 Technical Impact
- Standard `classes.dex` / `classes2.dex` / `classes3.dex` are no longer present in the APK root
- Dex payloads are loaded at runtime by `libmirsecore.so` via JNI
- Static analysis via apktool/jadx alone is insufficient — native `.so` analysis required (Ghidra/IDA)
- PairIP `LicenseActivity`, `LicenseClient`, `LicenseContentProvider` references removed from manifest
- `com.android.vending.CHECK_LICENSE` permission removed

### 📦 APK Info
- Version Code: 2
- Version Name: 1.2_2
- Distribution: **Paid**
- Base APK: CBT Semioffline (v1.2_2 upstream)

### ⚠️ Notes
- This version is distributed only to licensed users
- Do not redistribute the patched APK
- Native loader is custom — future patches require RE of `libmirsecore.so`
- Old patches for v1.2-stable are NOT compatible with v1.2_2

### ✅ Retained Patches (from v1.2-stable)
- Screen pinning disabled
- FLAG_SECURE removed
- 15-minute ban neutralized
- OnPause receiver crash fixed
- Exit button working
- Ads removed
- Statistik disabled
- Branding toast injected

### 🆕 Added in v1.2_2
- PairIP removal
- Native dex loader (`libmirsecore.so`)
- Paid distribution gate

---

## [v1.2-stable] - 2026-07-18

### Final Patches & Bypasses
✅ Screen Pinning — completely disabled (startLockTask bypassed)
✅ FLAG_SECURE (0x2000) — removed (screenshots & screen recording allowed)
✅ 15-Minute Ban — neutralized (onPause, onResume, onTrimMemory penalty removed)
✅ OnPause Receiver Crash — fixed (unregisterReceiver error resolved)
✅ Exit Button — fixed (closes activity properly)
✅ Iklan — removed (all ad SDKs disabled)
✅ Statistik — disabled (no more data sent to server)
✅ Branding Toast — injected ("Made With ❤ From Mirzadev")

### 📦 APK Info
- Version Code: 2
- Version Name: 1.2-stable

### ✅ Test Status
- Screen pinning — disabled
- Screenshot — allowed
- Exit/Re-enter — no reload/restart
- Exit button — working
- 15-min ban — disabled
- Crash — fixed

---

## [v1.1-beta] - 2026-07-15

### Development Patches (In Progress)
- Screen pinning — partially disabled (still some triggers)
- FLAG_SECURE — removed
- Ban detection — partially bypassed (onPause still active)
- Exit button — not working
- Crash on pause — still present

### 📦 APK Info
- Version Code: 1
- Version Name: 1.1-beta

### ⚠️ Notes
- Initial patching phase
- Still need to fix onPause crash
- Exit button still not functional
- Ads partially removed

---

## [v1.0] - 2026-06-19

### Initial Release (Original APK)

### 📦 APK Info
- Version Code: 1
- Version Name: 1.0

### Original Protections (Active)
❌ Screen pinning — active
❌ FLAG_SECURE (0x2000) — active (no screenshot)
❌ 15-Minute Ban — active
❌ OnPause crash — active
❌ Iklan — present (Vungle, IronSource, Google Ads)
❌ Statistik — sending data
❌ Exit button — not working
