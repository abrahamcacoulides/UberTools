# -*- mode: python -*-

block_cipher = None


a = Analysis(['UberTools.py'],
             pathex=['C:\\Users\\abraham.cacoulides\\AppData\\Local\\Programs\\Python\\Python35-32\\Lib\\site-packages\\PyQt5\\Qt\\bin', 'C:\\Users\\abraham.cacoulides\\PycharmProjects\\UberTools'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='UberTools',
          debug=False,
          strip=False,
          upx=True,
          console=False , icon='app.ico')
