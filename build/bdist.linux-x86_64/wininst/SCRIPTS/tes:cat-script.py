#!python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'tes==1.0','console_scripts','tes:cat'
__requires__ = 'tes==1.0'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('tes==1.0', 'console_scripts', 'tes:cat')()
    )
