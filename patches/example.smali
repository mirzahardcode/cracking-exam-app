# ============================================================
# EXAMPLE SMALI PATCH TEMPLATE
# ============================================================
# 
# This is a generic example of how smali patches work.
# DO NOT use this directly — adapt it to your target APK.
# 
# Key concepts:
#   - .method / .end method : Define a method
#   - invoke-* : Call a method
#   - return-void : Return nothing (void)
#   - const/4 : Store a constant value in a register
#   - if-eqz : Branch if condition is zero
#   - move-result : Store return value
#   - check-cast : Type casting
#
# ============================================================

# --- EXAMPLE 1: NEUTRALIZING A METHOD ---
#
# Original method that performs a verification check:
#   .method private checkLicense()Z
#       ... complex logic ...
#       return v0  # returns true if valid, false if not
#   .end method
#
# To bypass, we simply return true always:

.method private checkLicense()Z
    .locals 1
    const/4 v0, 0x1
    return v0
.end method


# --- EXAMPLE 2: MAKING A METHOD DO NOTHING ---
#
# Original method that triggers a ban or restriction:
#   .method private triggerBan()V
#       ... complex logic ...
#   .end method
#
# To bypass, we replace all logic with empty body:

.method private triggerBan()V
    .locals 0
    return-void
.end method


# --- EXAMPLE 3: COMMENTING OUT A METHOD CALL ---
#
# Original call inside onCreate:
#   invoke-virtual {p0}, Lcom/app/ExamActivity;->startLockTask()V
#
# To bypass, comment it out:
#   # invoke-virtual {p0}, Lcom/app/ExamActivity;->startLockTask()V


# --- EXAMPLE 4: OVERRIDING A CONDITIONAL CHECK ---
#
# Original conditional check:
#   if-eqz v0, :cond_ban
#   ... logic ...
#   :cond_ban
#       invoke-virtual {p0}, Lcom/app/ExamActivity;->banUser()V
#
# To bypass, force the condition to always fail:
#   const/4 v0, 0x0
#   if-eqz v0, :cond_ban  # will always skip
#   ... logic ...
#   :cond_ban
#       # invoke-virtual {p0}, Lcom/app/ExamActivity;->banUser()V


# --- EXAMPLE 5: INJECTING A TOAST MESSAGE ---
#
# To show a custom toast when app opens:
#   const-string v0, "Your custom message"
#   const/4 v1, 0x1
#   invoke-static {p0, v0, v1}, Landroid/widget/Toast;->makeText(Landroid/content/Context;Ljava/lang/CharSequence;I)Landroid/widget/Toast;
#   move-result-object v0
#   invoke-virtual {v0}, Landroid/widget/Toast;->show()V


# ============================================================
# HOW TO USE THIS TEMPLATE
# ============================================================
# 
# 1. Decompile your target APK using apktool or MT Manager
# 2. Find the target .smali file (e.g., MainActivity.smali)
# 3. Locate the method you want to modify
# 4. Replace the method body with a patched version
# 5. Rebuild, sign, and test
#
# REMEMBER: Always backup original files before patching!
#
# ============================================================
# CREDITS: Mirzadev
# ============================================================
