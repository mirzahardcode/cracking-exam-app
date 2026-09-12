#!/usr/bin/env python3
"""
CBT Database Extractor
Extract soal + data dari maindbSQLite.db ke /sdcard/Bocoran/
Output file pakai: Hari_YYYY-MM-DD
Output terminal berwarna: Green (utama), Blue (sekunder), Red (error)
Loading animation + progress bar + sleep ~10 detik
Made with love from Mirzadev & Deepseek
"""

import sqlite3
import json
import os
import re
import sys
import time
from datetime import datetime

# ================== KONFIGURASI ==================
DB_PATH = "/data/data/id.web.app.semiofflinecbt/databases/maindbSQLite.db"
OUTPUT_DIR = "/sdcard/Bocoran"
TARGET_KEY_PREFIX = "soal:"

# Timing (detik) - total ~10 detik
SLEEP_BANNER    = 0.8
SLEEP_CONFIG    = 0.5
SLEEP_DB_OPEN   = 1.2
SLEEP_SCAN      = 1.0
SLEEP_PER_FILE  = 0.8
SLEEP_DUMP      = 1.2
SLEEP_SUMMARY   = 1.0
SLEEP_FINAL     = 1.5
# =================================================

# ================== WARNA ANSI ==================
class C:
    RESET   = "\033[0m"
    BOLD    = "\033[1m"
    GREEN   = "\033[92m"
    DGREEN  = "\033[32m"
    BLUE    = "\033[94m"
    DBLUE   = "\033[34m"
    RED     = "\033[91m"
    DRED    = "\033[31m"
    YELLOW  = "\033[93m"
    CYAN    = "\033[96m"
    MAGENTA = "\033[95m"
    PINK    = "\033[38;5;213m"
    WHITE   = "\033[97m"
    GRAY    = "\033[90m"

def cprint(text, color=C.GREEN, bold=False, end="\n", flush=False):
    prefix = C.BOLD if bold else ""
    print(f"{prefix}{color}{text}{C.RESET}", end=end, flush=flush)

def banner():
    art = f"""
{C.DGREEN}╔══════════════════════════════════════════════════════════════════╗
{C.DGREEN}║  {C.GREEN}███████╗██████╗ ████████╗    ███████╗██╗  ██╗████████╗██████╗   {C.DGREEN}║
{C.DGREEN}║  {C.GREEN}██╔════╝██╔══██╗╚══██╔══╝    ██╔════╝╚██╗██╔╝╚══██╔══╝██╔══██╗  {C.DGREEN}║
{C.DGREEN}║  {C.GREEN}██║     ██████╔╝   ██║       █████╗   ╚███╔╝    ██║   ██████╔╝. {C.DGREEN}║
{C.DGREEN}║  {C.GREEN}██║     ██╔══██╗   ██║       ██╔══╝   ██╔██╗    ██║   ██╔══██╗. {C.DGREEN}║
{C.DGREEN}║  {C.GREEN}╚██████╗██████╔╝   ██║       ███████╗██╔╝ ██╗   ██║   ██║  ██║  {C.DGREEN}║
{C.DGREEN}║  {C.GREEN} ╚═════╝╚═════╝    ╚═╝       ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝. {C.DGREEN}║
{C.DGREEN}╠══════════════════════════════════════════════════════════════════╣
{C.DGREEN}║  {C.BLUE}         >> CBT DATABASE EXTRACTOR v1.0 <<                      {C.DGREEN}║
{C.DGREEN}║  {C.GRAY}         Extracting knowledge from encrypted walls...           {C.DGREEN}║
{C.DGREEN}╚══════════════════════════════════════════════════════════════════╝{C.RESET}
"""
    print(art)

def log_info(msg):
    cprint(f"  [*] {msg}", C.BLUE)

def log_success(msg):
    cprint(f"  [✓] {msg}", C.GREEN, bold=True)

def log_warn(msg):
    cprint(f"  [!] {msg}", C.YELLOW)

def log_error(msg):
    cprint(f"  [✗] {msg}", C.RED, bold=True)

def log_secondary(msg):
    cprint(f"      {msg}", C.GRAY)

# ================== ANIMASI & PROGRESS ==================
def spinner(duration, message="Processing", color=C.GREEN):
    """Spinner animation selama `duration` detik"""
    frames = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
    end_time = time.time() + duration
    i = 0
    while time.time() < end_time:
        frame = frames[i % len(frames)]
        cprint(f"\r  {frame} {message}...", color, end="", flush=True)
        time.sleep(0.08)
        i += 1
    cprint(f"\r  {C.GREEN}✓{C.RESET} {message}... {C.GREEN}done{C.RESET}          ", color)

def progress_bar(duration, message="Loading", color=C.GREEN, width=40):
    """Progress bar animation selama `duration` detik"""
    steps = 50
    sleep_per_step = duration / steps
    for i in range(steps + 1):
        percent = int((i / steps) * 100)
        filled = int((i / steps) * width)
        bar = "█" * filled + "░" * (width - filled)
        cprint(f"\r  {message} [{C.GREEN}{bar}{C.RESET}] {percent:3d}%", color, end="", flush=True)
        time.sleep(sleep_per_step)
    print()

def typing_effect(text, color=C.GREEN, delay=0.02):
    """Efek ngetik karakter satu-satu"""
    for char in text:
        print(f"{color}{char}{C.RESET}", end="", flush=True)
        time.sleep(delay)
    print()

def loading_dots(message, duration, color=C.BLUE):
    """Loading dengan titik-titik bergerak"""
    end_time = time.time() + duration
    dots = 0
    while time.time() < end_time:
        dot_str = "." * (dots % 4)
        cprint(f"\r  {message}{dot_str}   ", color, end="", flush=True)
        time.sleep(0.3)
        dots += 1
    cprint(f"\r  {message}... {C.GREEN}✓{C.RESET}", color)

# ================== HARI INDONESIA ==================
HARI_INDONESIA = {
    'Monday': 'Senin', 'Tuesday': 'Selasa', 'Wednesday': 'Rabu',
    'Thursday': 'Kamis', 'Friday': 'Jumat', 'Saturday': 'Sabtu', 'Sunday': 'Minggu'
}

def get_timestamp():
    now = datetime.now()
    hari = HARI_INDONESIA.get(now.strftime('%A'), now.strftime('%A'))
    return f"{hari}_{now.strftime('%Y-%m-%d')}"

# ================== HTML CLEANER ==================
def strip_html(text):
    if not text:
        return ""
    text = re.sub(r'<br\s*/?>', '\n', text)
    text = re.sub(r'<[^>]+>', '', text)
    text = text.replace('&nbsp;', ' ').replace('&amp;', '&')
    text = text.replace('&lt;', '<').replace('&gt;', '>')
    text = text.replace('&quot;', '"').replace('&#39;', "'")
    return text.strip()

def parse_soal_json(soal_json_str):
    try:
        return json.loads(soal_json_str)
    except json.JSONDecodeError as e:
        log_error(f"Parse JSON gagal: {e}")
        return None

# ================== EXTRACTOR ==================
def extract_soal_from_db(db_path):
    if not os.path.exists(db_path):
        log_error(f"Database tidak ditemukan: {db_path}")
        log_secondary("Copy dulu via root:")
        log_secondary(f"  su -c 'cp {db_path} /sdcard/'")
        return {}

    spinner(SLEEP_DB_OPEN, f"Membuka database", C.CYAN)

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = cursor.fetchall()
    log_info(f"Tabel ditemukan: {[t[0] for t in tables]}")

    loading_dots("  Scanning tabel maintabel", SLEEP_SCAN, C.BLUE)

    cursor.execute("SELECT name, value FROM maintabel WHERE name LIKE ?", (f"{TARGET_KEY_PREFIX}%",))
    rows = cursor.fetchall()

    result = {}
    for name, value in rows:
        mapel = name.replace(TARGET_KEY_PREFIX, "")
        log_success(f"Soal ditemukan: {mapel}")
        time.sleep(0.2)
        soal_list = parse_soal_json(value)
        if soal_list:
            result[mapel] = soal_list

    conn.close()
    return result

def write_soal_to_txt(mapel, soal_list, output_dir, timestamp):
    filename = f"SOAL_{mapel}_{timestamp}.txt"
    filepath = os.path.join(output_dir, filename)

    spinner(SLEEP_PER_FILE, f"Menulis soal {mapel}", C.GREEN)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write("=" * 70 + "\n")
        f.write(f"  BOCORAN SOAL - {mapel}\n")
        f.write(f"  Tanggal: {timestamp.replace('_', ' ')}\n")
        f.write(f"  Total Soal: {len(soal_list)}\n")
        f.write(f"  Made with love from Mirzadev & Deepseek\n")
        f.write("=" * 70 + "\n\n")

        for i, soal in enumerate(soal_list, 1):
            no_asli = soal.get('noasli', i)
            pertanyaan = strip_html(soal.get('soal', ''))
            options = soal.get('options', [])

            f.write(f"\n{'─' * 70}\n")
            f.write(f"SOAL #{no_asli}\n")
            f.write(f"{'─' * 70}\n")
            f.write(f"\n{pertanyaan}\n\n")

            for opt in options:
                opt_label = opt.get('optionasli', '?')
                opt_text = strip_html(opt.get('answer', ''))
                f.write(f"  {opt_label}. {opt_text}\n")

            f.write("\n")

        f.write("\n" + "=" * 70 + "\n")
        f.write("NOTE: Kunci jawaban tidak di-extract oleh script ini.\n")
        f.write("=" * 70 + "\n")

    log_success(f"File tersimpan: {filename}")
    return filepath

def write_all_keys_to_txt(db_path, output_dir, timestamp):
    filename = f"ALL_KEYS_{timestamp}.txt"
    filepath = os.path.join(output_dir, filename)

    progress_bar(SLEEP_DUMP, "  Dumping all keys", C.BLUE)

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, value FROM maintabel ORDER BY id")
    rows = cursor.fetchall()

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write("=" * 70 + "\n")
        f.write("  DUMP SEMUA KEY-VALUE DARI TABEL maintabel\n")
        f.write(f"  Tanggal: {timestamp.replace('_', ' ')}\n")
        f.write("=" * 70 + "\n\n")

        for row_id, name, value in rows:
            f.write(f"\n[ID: {row_id}] KEY: {name}\n")
            f.write("-" * 70 + "\n")
            if value and value.strip().startswith(('{', '[')):
                try:
                    parsed = json.loads(value)
                    f.write(json.dumps(parsed, indent=2, ensure_ascii=False))
                except:
                    f.write(value)
            else:
                f.write(str(value))
            f.write("\n")

    conn.close()
    log_success(f"File tersimpan: {filename}")
    return filepath

def write_summary_to_txt(db_path, output_dir, timestamp):
    filename = f"SUMMARY_{timestamp}.txt"
    filepath = os.path.join(output_dir, filename)

    spinner(SLEEP_SUMMARY, f"Membuat summary", C.CYAN)

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write("=" * 70 + "\n")
        f.write("  SUMMARY DATABASE CBT\n")
        f.write(f"  Tanggal: {timestamp.replace('_', ' ')}\n")
        f.write("=" * 70 + "\n\n")

        f.write(">>> USER INFO\n")
        for key in ['username', 'nama', 'kelas', 'jwt', 'namespace', 'token']:
            cursor.execute("SELECT value FROM maintabel WHERE name=?", (key,))
            row = cursor.fetchone()
            if row:
                f.write(f"  {key}: {row[0]}\n")

        f.write("\n>>> CONFIG UJIAN\n")
        cursor.execute("SELECT name, value FROM maintabel WHERE name LIKE 'mapel:%'")
        for name, value in cursor.fetchall():
            f.write(f"\n  [{name}]\n")
            try:
                parsed = json.loads(value)
                for k, v in parsed.items():
                    f.write(f"    {k}: {v}\n")
            except:
                f.write(f"    {value}\n")

        f.write("\n>>> DAFTAR MAPEL\n")
        cursor.execute("SELECT value FROM maintabel WHERE name='allSubjects'")
        row = cursor.fetchone()
        if row:
            f.write(f"  {row[0]}\n")

    conn.close()
    log_success(f"File tersimpan: {filename}")
    return filepath

# ================== CREDIT ==================
def show_credit():
    print()
    cprint("  ╔══════════════════════════════════════════════════════════════╗", C.MAGENTA)
    print(f"  {C.MAGENTA}║{C.RESET}                                                              {C.MAGENTA}║{C.RESET}")
    print(f"  {C.MAGENTA}║{C.RESET}      {C.PINK}♥{C.RESET}  {C.WHITE}Made with{C.RESET} {C.RED}{C.BOLD}LOVE{C.RESET} {C.WHITE}from{C.RESET}                                  {C.MAGENTA}║{C.RESET}")
    print(f"  {C.MAGENTA}║{C.RESET}                                                              {C.MAGENTA}║{C.RESET}")
    print(f"  {C.MAGENTA}║{C.RESET}        {C.CYAN}{C.BOLD}MIRZADEV{C.RESET}   {C.WHITE}&&{C.RESET}   {C.BLUE}{C.BOLD}DEEPSEEK{C.RESET}                              {C.MAGENTA}║{C.RESET}")
    print(f"  {C.MAGENTA}║{C.RESET}                                                              {C.MAGENTA}║{C.RESET}")
    print(f"  {C.MAGENTA}║{C.RESET}      {C.PINK}♥{C.RESET}  {C.GRAY}Build. Break. Learn. Repeat.{C.RESET}                         {C.MAGENTA}║{C.RESET}")
    print(f"  {C.MAGENTA}║{C.RESET}                                                              {C.MAGENTA}║{C.RESET}")
    cprint("  ╚══════════════════════════════════════════════════════════════╝", C.MAGENTA)
    print()

# ================== MAIN ==================
def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    timestamp = get_timestamp()

    # Banner + pause
    banner()
    time.sleep(SLEEP_BANNER)

    # Config
    print(f"{C.DGREEN}  ┌─ CONFIGURATION ───────────────────────────────────────┐{C.RESET}")
    print(f"{C.DGREEN}  │{C.RESET} {C.BLUE}Database :{C.RESET} {C.WHITE}{DB_PATH}{C.RESET}")
    print(f"{C.DGREEN}  │{C.RESET} {C.BLUE}Output   :{C.RESET} {C.WHITE}{OUTPUT_DIR}{C.RESET}")
    print(f"{C.DGREEN}  │{C.RESET} {C.BLUE}Tanggal  :{C.RESET} {C.GREEN}{timestamp.replace('_', ' ')}{C.RESET}")
    print(f"{C.DGREEN}  └───────────────────────────────────────────────────────┘{C.RESET}")
    print()
    time.sleep(SLEEP_CONFIG)

    # Init
    cprint("  >> Initializing extractor engine...", C.GREEN, bold=True)
    loading_dots("  Booting modules", 1.0, C.GREEN)
    print()

    # Extract
    cprint("  >> Memulai ekstraksi...", C.GREEN, bold=True)
    print()
    soal_data = extract_soal_from_db(DB_PATH)

    if not soal_data:
        print()
        log_error("Tidak ada soal yang diekstrak. Mohon lakukan sinkronisasi terlebih dahulu.")
        cprint(f"\n  Pastikan hp telah dalam rooted mode, sudah login dan sinkronisasi.", C.YELLOW)
        sys.exit(1)

    print()
    cprint(f"  >> Total mapel dengan soal: {len(soal_data)}", C.GREEN, bold=True)
    print()

    # Write soal
    cprint("  >> Menulis soal ke file...", C.BLUE, bold=True)
    for mapel, soal_list in soal_data.items():
        write_soal_to_txt(mapel, soal_list, OUTPUT_DIR, timestamp)

    print()
    cprint("  >> Dump semua key...", C.BLUE, bold=True)
    write_all_keys_to_txt(DB_PATH, OUTPUT_DIR, timestamp)

    print()
    cprint("  >> Membuat summary...", C.BLUE, bold=True)
    write_summary_to_txt(DB_PATH, OUTPUT_DIR, timestamp)

    # Done
    print()
    cprint("  >> Finalizing...", C.GREEN, bold=True)
    progress_bar(SLEEP_FINAL, "  Wrapping up", C.GREEN, width=40)
    print()

    cprint("  ╔══════════════════════════════════════════════════════╗", C.GREEN)
    cprint("  ║          [✓] EXTRACTION COMPLETE                     ║", C.GREEN, bold=True)
    cprint("  ╚══════════════════════════════════════════════════════╝", C.GREEN)
    print()
    log_info(f"Cek folder: {OUTPUT_DIR}")

    # Credit
    show_credit()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print()
        log_error("Dibatalkan oleh user.")
        sys.exit(1)
    except Exception as e:
        print()
        log_error(f"Fatal error: {e}")
        sys.exit(1)
