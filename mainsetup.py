from cx_Freeze import *
import sys
includefiles = ['icon.ico']
base = None
if sys.platform == "win32":
    base = "Win32GUI"

shortcut_table = [
    ("DesktopShortcut",  # Shortcut
     "DesktopFolder",  # Directory
     "Typing Speed Incraser -Tanish",  # Name
     "TARGETDIR",  # Component
     "[TARGETDIR]\main.exe",  # Target
     None,  # Arguments
     None,  # Description
     None,  # hotkey
     None,  # icon
     None,  # iconindex
     None,  # showcmd
     "TARGETDIR",  # WKdIR
     )
]
msi_data = {"shortcut": shortcut_table}
bdist_msi_options = {'data': msi_data}
setup(
    version="0.1",
    description="Typing Speed Increase",
    author="Tanish Gupta",
    name="Typing Speed Increase - By Tanish",
    options={'build_exe': {'include_files': includefiles}, "bdist_msi": bdist_msi_options, },
    executables=[
        Executable(
            script="main.py",
            base=base,
            icon='icon.ico',

        )
    ]
)
