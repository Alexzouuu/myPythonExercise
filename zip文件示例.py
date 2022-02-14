import zipfile,os
os.chdir("C:\\desktop2")
exampleZip=zipfile.ZipFile("《基于Python的金融分析与风险管理》.zip")
print(exampleZip.namelist())
spaminfo=exampleZip.getinfo('密码链接说明.txt')
print(spaminfo.file_size)#原来文件大小
print(spaminfo.compress_size)#压缩后文件大小
print("Compressed file is %sx smaller."%(round(spaminfo.file_size/spaminfo.compress_size,5)))#原来文件大小除以压缩后文件大小，保留五位小数
