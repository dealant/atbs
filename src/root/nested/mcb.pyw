#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

# TODO: Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'del':
    if sys.argv[2] in mcbShelf:
        del mcbShelf[sys.argv[2]]
    elif len(sys.argv) == 3:
        print(str(sys.argv[1])+' is not in the database') 
elif len(sys.argv) == 2:
    #list key words or retrieve data
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(dict(mcbShelf.items())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

# TODO: List keywords and load content.

mcbShelf.close()