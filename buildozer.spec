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

# (str) Version number (automatically increment this for releases)
version = 0.1

# (str) Application versioning (internal)
version.regex = __version__ = ['"](.*)['"]
version.filename = %(source.dir)s/main.py

# (list) Application requirements
requirements = python3,kivy

# (str) Supported orientation (portrait, landscape, all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (list) Permissions
android.permissions = INTERNET

# (list) Android additional libraries / Java classes (optional)
#android.add_jars =

# (list) Android application meta-data to set (key=value)
#android.meta_data =

# (str) Android entry point, default is ok
#android.entrypoint = org.kivy.android.PythonActivity

# (str) Android application theme
#android.theme = '@android:style/Theme.NoTitleBar'

# (str) App icon and name
icon.filename = %(source.dir)s/icon.png

# (bool) Copy library instead of link (useful for restricted filesystems)
copy_libs = 1

# (str) Android SDK version to target
android.api = 34

# (str) Minimum API your APK will support
android.minapi = 21

# (str) Android NDK version
android.ndk = 25b

# (str) Android SDK tools version
android.sdk = 34.0.0

# (str) Application entry point (for kivy)
# (Leave as default if using main.py)
#android.entrypoint = org.kivy.android.PythonActivity

# (str) Output directory for build
build_dir = .buildozer

# (str) Output filename pattern
# (This determines the name of the generated APK)
android.arch = armeabi-v7a

# (str) APK filename pattern
android.filename = %(title)s-%(version)s.apk

# (bool) Automatically accept SDK licenses
android.accept_sdk_license = True

# (bool) Enable debug (True = debug.apk, False = release.apk)
debug = True


[buildozer]

# (str) Log level (0 = quiet, 2 = normal, 3 = verbose)
log_level = 2

# (bool) Display logcat output when running `buildozer android deploy run logcat`
logcat = True

# (bool) Automatically log in to adb devices
adb = True
