import os,re,shutil
amerPatterm=re.compile(r"""
^(.*?)
([0-1]?\d)
(-)
([0-3]?\d)
(-)
(19|20\d{2})
(.*?)$
""",re.VERBOSE)

os.chdir("C:\\Users\\zouch")

for file in os.listdir("C:\\Users\\zouch"):
    mo=amerPatterm.search(file)
    if mo==None:
        continue
    beforeDate=mo.group(1)
    dateMonth=mo.group(2)
    dateDay=mo.group(4)
    dateYear=mo.group(6)
    afterYear=mo.group(7)
    euroPattern=beforeDate+dateDay+'-'+dateMonth+'-'+dateYear+afterYear
    shutil.move(file,euroPattern)
