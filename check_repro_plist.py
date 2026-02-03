import plistlib
import os

plist_path = r'd:\source\ReproApp\ReproApp.iOS\bin\Debug\net10.0-ios\iossimulator-x64\Info.plist'

try:
    with open(plist_path, 'rb') as f:
        pl = plistlib.load(f)

    if 'CFBundleIconName' in pl:
        print(f"FOUND: CFBundleIconName = {pl['CFBundleIconName']}")
    else:
        print("MISSING: CFBundleIconName is not in the plist")

except Exception as e:
    print(f"Error: {e}")
