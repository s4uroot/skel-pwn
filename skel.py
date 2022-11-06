#!/usr/bin/python3

import sys
import os

if len(sys.argv)<2:
    print("Usage: skel <binary>")
    sys.exit(0)

program = str(sys.argv[1])
current = os.getcwd()

skel = '''#!/usr/bin/env python3

from pwn import *

context.terminal = ['tmux', 'splitw', '-h']
elf = context.binary = ELF('./{}')
context.bits = 64

libc = elf.libc
rop = ROP(elf)

gs = \'\'\'
continue
\'\'\'

def start():
    if args.GDB:
        return gdb.debug(elf.path, gdbscript=gs)
    if args.REMOTE:
        return remote('127.0.0.1', 5555)
    else:
        return process(elf.path)
r = start()

#============ exploit here ================

#============= interactive ================

r.interactive()
'''.format(program, program, program)
try:
    with open('xpl.py', 'w') as f:
        f.write(skel)
        f.close()
except:
    print("Can't write xpl.py!")
