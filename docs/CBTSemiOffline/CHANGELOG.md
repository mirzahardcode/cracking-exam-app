# Changelog — CBT Semioffline

## [v1.2-stable] - 2026-07-18

### Final Patches & Bypasses
- ✅ **Screen Pinning** — completely disabled (startLockTask bypassed)
- ✅ **FLAG_SECURE (0x2000)** — removed (screenshots & screen recording allowed)
- ✅ **15-Minute Ban** — neutralized (onPause, onResume, onTrimMemory penalty removed)
- ✅ **OnPause Receiver Crash** — fixed (unregisterReceiver error resolved)
- ✅ **Exit Button** — fixed (closes activity properly)
- ✅ **Iklan** — removed (all ad SDKs disabled)
- ✅ **Statistik** — disabled (no more data sent to server)
- ✅ **Branding Toast** — injected ("Made With ❤ From Mirzadev")

### APK Info
- **Version Code**: 2
- **Version Name**: 1.2-stable

### Test Status
- ✅ Screen pinning — **disabled**
- ✅ Screenshot — **allowed**
- ✅ Exit/Re-enter — **no reload/restart**
- ✅ Exit button — **working**
- ✅ 15-min ban — **disabled**
- ✅ Crash — **fixed**

---

## [v1.1-beta] - 2026-07-15

###  Development Patches (In Progress)
-  Screen pinning — partially disabled (still some triggers)
-  FLAG_SECURE — removed
-  Ban detection — partially bypassed (onPause still active)
-  Exit button — not working
-  Crash on pause — still present

### APK Info
- **Version Code**: 1
- **Version Name**: 1.1-beta

### Notes
- Initial patching phase
- Still need to fix onPause crash
- Exit button still not functional
- Ads partially removed

---

## [v1.0] - 2026-06-19

### Initial Release (Original APK)

### APK Info
- **Version Code**: 1
- **Version Name**: 1.0

### Original Protections (Active)
- ❌ Screen pinning — **active**
- ❌ FLAG_SECURE (0x2000) — **active** (no screenshot)
- ❌ 15-Minute Ban — **active**
- ❌ OnPause crash — **active**
- ❌ Iklan — **present** (Vungle, IronSource, Google Ads)
- ❌ Statistik — **sending data**
- ❌ Exit button — **not working**
