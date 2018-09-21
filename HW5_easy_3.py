import sys
import shutil

current_script = sys.argv[0]

shutil.copy2(current_script, '{} - copy.py'.format(current_script[0:-3]))