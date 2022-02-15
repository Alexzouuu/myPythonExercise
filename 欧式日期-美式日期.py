import re,shutil,os
#TODO:创建正则表达式
dataPattern=re.compile(r"""
^(.*?)
(1?\d)
(-)
(\d\d)
(-)
(\d\d\d\d)
(.*?)$#不能加括号，这样就会多运行一次
""",re.VERBOSE)
#TODO:找出工作目录的所有文件
os.chdir('C:\\Users\\zouch')
for amerFilename in os.listdir('C:\\Users\\zouch'):
    mo=dataPattern.search(amerFilename)
#TODO:如果没有日期，则跳过
    if mo==None:
        continue#break语句是直接跳出循坏，但continue只是结束本次循坏
    beforeDate=mo.group(1)
    dateMonth=mo.group(2)
    dateDay=mo.group(4)
    dateYear=mo.group(6)
    afterDate=mo.group(7)
#TODO:循坏遍历所有文件，检查是否包含日期
    euroFilename=beforeDate+dateDay+'-'+dateMonth+'-'+dateYear+afterDate
#TODO:用shutil.move进行改名
    shutil.move(amerFilename,euroFilename)
