[app]

# (str) Title of your application
title = InHand

# (str) Package name
package.name = inhand

# (str) Package domain (unique reverse domain)
package.domain = org.lokesh

# (str) Source code directory
source.dir = .

# (str) Main .py file to launch the app
source.main = main.py

# (list) Files to include
source.include_exts = py,png,jpg,kv,atlas

# (str) Version will be extracted automatically from your main.py
version.regex = __version__ = ['"](.*)['"]

version.filename = main.py

# (list) Application requirements
requirements = python3,kivy

# (str) Supported orientation
orientation = portrait

# (bool) Fullscreen mode
fullscreen = 1

# (list) Permissions
android.permissions = INTERNET

# (str) Application icon
icon.filename = %(source.dir)s/icon.png

# (bool) Copy library instead of link (for restricted systems)
copy_libs = 1

# (str) Android SDK/NDK/API versions
android.api = 34
android.minapi = 21
android.ndk = 25b
android.sdk = 34.0.0

# (str) Output directory for builds
build_dir = .buildozer

# (str) Output APK filename (✅ fixed here)
android.filename = %(title)s.apk

# (bool) Automatically accept SDK licenses
android.accept_sdk_license = True

# (bool) Build debug version (True = debug.apk, False = release.apk)
debug = True


[buildozer]

# (str) Log level (0 = quiet, 2 = normal, 3 = verbose)
log_level = 2

# (bool) Display logcat output when running `buildozer android deploy run logcat`
logcat = True

# (bool) Automatically log in to adb devices
adb = True



