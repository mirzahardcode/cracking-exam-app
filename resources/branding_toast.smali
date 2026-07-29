# ============================================================
# BRANDING TOAST INJECTION
# ============================================================
#
# This is a generic smali template for displaying a custom 
# toast message with HTML-formatted colored text.
#
# Features:
#   - HTML <font color> support
#   - Unicode bold characters (Mathematical Bold)
#   - Customizable message
#
# ============================================================

# --- METHOD: tampilkanBranding()V ---
# 
# This method creates and displays a toast with custom styling.
# It uses HTML formatting for colored text and Unicode symbols
# for visual appeal.

.method private tampilkanBranding()V
    .registers 4

    # --- STEP 1: Define the message with HTML tags ---
    # 
    # Format: "Text <font color='#COLOR'>BOLD_TEXT</font> More Text"
    # 
    # The \ud835\udc0c\ud835\udc08\ud835\udc11\ud835\udc19\ud835\udc13\ud835\udc07\ud835\udc00\ud835\udc17
    # characters are Unicode Mathematical Bold letters that render 
    # as 𝐌𝐈𝐑𝐙𝐓𝐇𝐀𝐗 (bold capital letters).
    #
    # You can replace "MIRZTHAX" with your own brand names.
    # Just make sure to escape single quotes in the HTML attribute.

    const-string v0, "Made With ❤ From <font color=\'#00FF00\'><b>\ud835\udc0c\ud835\udc08\ud835\udc11\ud835\udc19\ud835\udc13\ud835\udc07\ud835\udc00\ud835\udc17</b></font>"

    # --- STEP 2: Convert HTML string to Spanned text ---
    # 
    # Android's Html.fromHtml() parses HTML tags and converts them
    # into styled text (Spanned) that can be displayed in a Toast.
    # This allows us to use colors, bold, italics, etc.

    invoke-static {v0}, Landroid/text/Html;->fromHtml(Ljava/lang/String;)Landroid/text/Spanned;

    move-result-object v0

    # --- STEP 3: Create and show the Toast ---
    # 
    # Toast.LENGTH_SHORT = 1 (2 seconds)
    # Toast.LENGTH_LONG  = 0 (3.5 seconds)
    # 
    # We use LENGTH_SHORT for a quick, non-intrusive display.

    const/4 v1, 0x1

    invoke-static {p0, v0, v1}, Landroid/widget/Toast;->makeText(Landroid/content/Context;Ljava/lang/CharSequence;I)Landroid/widget/Toast;

    move-result-object v0

    # --- STEP 4: Display the Toast ---

    invoke-virtual {v0}, Landroid/widget/Toast;->show()V

    return-void
.end method


# ============================================================
# HOW TO USE
# ============================================================
# 
# 1. Copy this method into your target .smali file
#    (e.g., MainActivity.smali, LoginActivity.smali)
# 
# 2. Call the method from onCreate() or anywhere you want:
# 
#    invoke-direct {p0}, Lcom/yourpackage/YourActivity;->tampilkanBranding()V
# 
# 3. Rebuild, sign, and test
# 
# ============================================================
# CUSTOMIZATION
# ============================================================
# 
# Change the message by modifying the const-string v0 line:
# 
#   const-string v0, "Your custom message here"
# 
# Color codes (use with <font color='#XXXXXX'>):
# 
#   Green  : #00FF00
#   Red    : #FF0000
#   Blue   : #0000FF
#   Cyan   : #00FFFF
#   Gold   : #FFD700
#   Orange : #FF6B00
#   Purple : #9B59B6
# 
# ============================================================
# NOTES
# ============================================================
# 
# - The Unicode bold characters require Android API 21+ for full support
# - Some devices may not render Unicode bold correctly — fallback is plain text
# - Toast messages are not clickable or interactive (passive display only)
# 
# ============================================================
# CREDITS: Mirzadev
# ============================================================
