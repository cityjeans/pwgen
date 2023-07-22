# Python password generator

This script generates a set of passwords in your text terminal.<br>

## Installation
1. Download the latest release, or clone the repository.
2. Run `chmod a+x pwgen.py` to set execute permissions.
4. *optional: Move the file somewhere in your PATH. I recommend `/usr/local/bin/` on Linux.
5. *optional: You may also want to rename the file from `pwgen.py` to simply `pwgen`.*

### Dependencies
- `python3`
- *optional: Any bourne-compatible shell*

### Usage 
Run in your shell by calling `./pwgen.py`  
You may also run it by calling `python3 pwgen.py`  
You may add any combination of the available arguments, these are:  

      -h, --help        show this help message and exit
      -u, --uppercase   use uppercase letters in the password
      -d, --digits      use digits (numbers 0 to 9) in the password
      -s, --symbols     use special symbols in the password
      -w, --words       use english words in the password
      -l x, --length x  set the length of the password
