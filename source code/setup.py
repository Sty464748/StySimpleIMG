from cx_Freeze import setup, Executable

setup(
    name='StySimpleIMG',
    version='1.0',
    description='StySimpleIMG',
    executables=[Executable('StySimpleIMG.py', base=None, icon='C:/Django/STY SIMPLE IMG/stySimpleIMG.ico')]
)
