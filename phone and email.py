import re,pyperclip
selectPhone=re.compile(r"""
(\d{3}|\(\d{3}\))?
(\s|-|\.)?
(\d{3})
(\s|-|\.)?
(\d{3})?
(\s|-|\.)?
(\d{4})
""",re.VERBOSE|re.IGNORECASE)

selectEmail=re.compile(r"""
(\w+)
(@)
(qq|outlook|foxmail|123|129|gmail)
(\.com|\.cn|\.vip)
""",re.VERBOSE|re.I)

text=str(pyperclip.paste())
matches=[]

for i in selectPhone.findall(text):
    if i[6].isdecimal():
        phoneNum='-'.join([i[0],i[2],i[4],i[6]])
        matches.append(phoneNum)
    else:
        phoneNum='-'.join([i[0],i[2],i[4]])
        matches.append(phoneNum)
for i in selectEmail.findall(text):
    emailNum=''.join(i)
    matches.append(emailNum)

print('\n'.join(matches))







