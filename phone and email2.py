import re,pyperclip

phoneNum=re.compile(r"""
(\d{3}|\(\d{3}\))?
(\s|-|\.)?
(\d{3})
(\s|-|\.)
(\d{3})
(\s|-|\.)
(\d{4})
""",re.VERBOSE|re.I)

emailNum=re.compile(r"""
((0-9a-zA-Z)|\w+)#不要忘记加上+，如果不加+的话，系统会认为只能识别一个
@
(qq|outlook|foxmail|123|129|gmail)
(\.)
(com|cn|vip)
""",re.VERBOSE|re.I)
"""
re.VERBOSE是当该标志被指定时，在 RE 字符串中的空白符被忽略
"""

text=str(pyperclip.paste())
matches=[]
for i in phoneNum.findall(text):
    if i[6].isdecimal():
        phonenum='-'.join([i[0],i[2],i[4],i[6]])#join里面只能添加一个参数，或者只能整合列表，切记只能输入一个列表
        matches.append(phonenum)
    else:
        phonenum='-'.join([i[0],i[2],i[4]])
        matches.append(phonenum)

for i in emailNum.findall(text):
    emailnum=''.join(i)
    matches.append(emailnum)

print('\n'.join(matches))
