#将一个文件夹复制到zip文件中
#将文件按照数字顺序排列
import zipfile,os
def backupToZip(folder):
#将整个文件夹备份入zip中
    number=1
    while True:
        zipFileName=os.path.basename(folder)+'_'+str(number)+'.zip'#读取这个路径中最后一个文件的文件名
        if not os.path.exists(zipFileName):
            break
        number+=1
#TODO:创建一个zip文件
    print(f'创建一个zip文件：{zipFileName}')
    backupZip=zipfile.ZipFile(zipFileName,'w')
#TODO:遍历整个文件夹，将所有文件都加入压缩文件中
    for foldername,subfolders,filenames in os.walk(folder):
        print("Adding files in %s..."%(foldername))
        backupZip.write(foldername)
        for filename in filenames:
            newBase=os.path.basename(folder)+'_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue#万一folder中有zip文件，不要备份zip文件
            backupZip.write(os.path.join(foldername,filename))#用于拼接文件路径
    backupZip.close()
    print('Done')
backupToZip('C:\\delicious')

