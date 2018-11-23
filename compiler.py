#!/usr/bin/python3
import sys
if len(sys.argv) < 2:
    print("Syntax: python FASTcompiler.py filename.FAST")
elif sys.argv[1][-5:] != ".FAST":
    print("Can only compile files that end in .FAST")
else:
    codefile = open(sys.argv[1],'r')
    code = codefile.read()
    codefile.close()
    filetext = ''
    fileext = '.py'
    if code == '':
        filetext = '#!/usr/bin/python3\nprint("Hello, world!")'
    elif code[0] == 'J':
        filetext = code[1:]
        filename = 'FAST.java'
    elif code[0] == '2':
        filetext = '#!/usr/bin/python2\n{}'.format(code[1:])
    elif code[0] == '3':
        filetext = '#!/usr/bin/python3\n{}'.format(code[1:])
    else:
        filetext = '#!/usr/bin/python3\nprint("{}")'.format(code)
    file = open(sys.argv[1][:-5]+fileext,'w')
    file.write(filetext)
    file.close()
