import sys
from cx_Freeze import setup, Executable

build_exe_options = {'packages': ['os'], 'excludes': ['tkinter']}

base = None
if sys.platform == 'win32':
    base = 'win32GUI'

setup(
    name='guifoo',
    version='0.1',
    description='My GUI Application',
    options={'build_exe': build_exe_options},
    executables=[Executable('main.py', base=base)]
)

# 取消签名