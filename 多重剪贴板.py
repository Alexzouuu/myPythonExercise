import shelve,pyperclip,sys
#TODO:加载保存剪贴板中的内容
mcbShelf=shelve.open('mcb')
#TODO:保存剪贴板内容
if len(sys.argv)==3 and sys.argv[1].lower()=='save':
    mcbShelf[sys.argv[2]]=pyperclip.paste()
elif len(sys.argv)==2:
#TODO:列出关键词加载内容
    if sys.argv[1].lower()=='list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
mcbShelf.close()

