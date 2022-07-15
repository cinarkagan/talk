def talk(text):
    if text.startswith("talk('") or text.startswith('talk("'):
        if text.endswith("');") or text.endswith('");'):
            text = text.replace("talk('","")
            text = text.replace("');","")
            text = text.replace('talk("',"")
            text = text.replace('");',"")
            print(text)
        else:
            print('  File "<stdin>", line 1')
            print('    '+text)
            print('    '+text.replace(text,' ')+'^')
            print('SyntaxError: EOL while scanning string literal')
    else:
        if text.startswith('#'):
            pass
        else:
            print('Traceback (most recent call last):')
            print(' File "<stdin>", line 1, in <module>')
            print("NameError: name '"+text+"' is not defined")

while True:
    text = input('talk >>>')
    talk(text)
