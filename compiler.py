#!/usr/bin/python3
import sys
import click

# TODO: support for non-unix line endings?
# TODO: add option specifying python interpreter path?
# TODO: fix bug where you can break no-flags with """
@click.command()
@click.argument('infile')
@click.option('-i', '--ignore-prefix', is_flag=True)
@click.option('-o', '--outfile', default='')
def fast(infile, ignore_prefix, outfile):
    if infile[-5:] not in ['.FAST', '.fast']:
        print('Can only compile .FAST files', file=sys.stderr)
        sys.exit(1)

    code = ''
    try:
        code = open(infile, 'r').read()  # does this close properly?
    except (OSError, IOError):
        print('Cannot open file', file=sys.stderr)
        sys.exit(2)

    file_text = ''
    if code is '':
        file_text = '#!/usr/bin/python3\nprint(\'Hello, world!\')'
    elif ignore_prefix:
        file_text = '#!/usr/bin/python3\nprint("""{}""")'.format(code)
    elif code[0] is 'J':
        file_text = code[1:]
        if outfile is '':
            outfile = 'fast.java'
    elif code[0] is '2':
        file_text = '#!/usr/bin/python2\n{}'.format(code[1:])
    elif code[0] is '3':
        file_text = '#!/usr/bin/python3\n{}'.format(code[1:])
    else:
        file_text = '#!/usr/bin/python3\nprint("""{}""")'.format(code)
    if outfile is '':
        outfile = 'fast.py'

    file = open(outfile, 'w')
    file.write(file_text)
    file.close()

if __name__ == '__main__':
    fast()
