#!/usr/bin/env python3
import os
import sys
import re

def patch_smali(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Patch: return-void on license check
    content = re.sub(
        r'(\.method.*?checkLicense.*?\n)',
        r'\1    const/4 v0, 0x1\n    return v0\n',
        content,
        flags=re.DOTALL
    )
    
    with open(file_path, 'w') as f:
        f.write(content)
    print(f" Patched: {file_path}")

if __name__ == "__main__":
    print(" Auto-Patcher for Exam App")
    patch_smali("smali/com/pairip/licensecheck/LicenseCheck.smali")
    print(" Done ")
