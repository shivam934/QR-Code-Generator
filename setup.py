from setuptools import setup
import sys
#import sysconfig
includefiles = ['QR.ico']
base = None
if sys.platform == "win32":
    base == "win32GUI"

shortcut_table = [
    ("DesktopShortcut",
     "DesktopFolder",
     "QR Generator",
     "TARGETDIR",
     "[TARGETDIR]\QRCODE.exe",
     None,
     None,
     None,
     None,
     None,
     None,
     "TARGETDIR",
     )
]
msi_data = {"Shortcut": shortcut_table}
bdist_msi_options = {'data': msi_data}
setup(
    name='QR_CODE_GENERATOR',
    version='1.0',
    includefiles = ['QR.ico'],
    packages=[''],
    url='[TARGETDIR]\QRCODE.exe',
    license='',
    author='Shivam',
    author_email='khandelwalshivam45@gmail.com',
    description='',
    options={'build_exe': {'include_files': includefiles}, "bdist_msi": bdist_msi_options,},
    #executables=[
        #Executable(
        #    script="QRCODE.py",
       #     base=base,
      #      icon='QR.ico',
     #   )
    #]
)
