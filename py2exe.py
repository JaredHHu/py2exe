import os
import shutil

projectname = input('要编译的文件名称：')
icon = input('无则空 图标名称：')
ui = input('是否要黑色运行界面（Y/N）：')

command = '-F'
if ui == 'N':
    command += ' -w'
if icon != '':
    command += ' -i {}'.format(icon)
os.system('pyinstaller {} {}.py'.format(command, projectname))
if os.path.exists('{}.exe'.format(projectname)):
    os.remove('{}.exe'.format(projectname))
shutil.move('dist\\{}.exe'.format(projectname), './')
shutil.rmtree('__pycache__')
shutil.rmtree('build')
shutil.rmtree('dist')
os.remove('{}.spec'.format(projectname))
