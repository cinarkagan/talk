import sys

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

if len(sys.argv) == 1:
    while True:
        text = input('talk >>>')
        talk(text)
elif len(sys.argv) == 2:
    input_file = sys.argv[1]
    if input_file.endswith('.talk'):
        code = open(input_file, 'r')
        for v in code:
            print(v.strip())
    else:
        raise Exception('Cannot open file, file not in supported format(.talk format).')
else:
    raise Exception("Invalid number of arguments")
