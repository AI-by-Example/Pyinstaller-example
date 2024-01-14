# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['Sheeba_main.py'],
             pathex=['C:\\Users\\danan\\Git\\Spring_Vision_App\\Spring_Vision_App', 'C:\\Users\\danan\\AppData\\Local\\Programs\\Python\\Python36\\Lib\\site-packages\\SimpleITK-1.2.0rc2.dev1167+gd4cf2-py3.6-win-amd64.egg\\SimpleITK'],
             binaries=[],
             datas=[('spring_logo.ico', '.'), ('SimpleITK/SimpleITK.py', '.'), ('SimpleITK/_SimpleITK.py', '.'), ('SimpleITK/__init__.py', '.')],
             hiddenimports=["pywt","pywt._extensions._cwt",'SimpleITK._SimpleITK','SimpleITK', 'SimpleITK.SimpleITK'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='Spring_Vision_App',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False , icon='spring_logo.ico')
