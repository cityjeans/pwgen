<h1>pwgen</h1>
<h4>Python password generator</h4>

This script runs in your unix shell "natively" so long as you have installed python3.<br>
There are no third party dependencies (other than python), so you can essentially "drag and drop" the script into `/usr/local/bin` or wherever else you like putting your scripts, as long as you run `chmod a+x pwgen.py` first.<br>
I recommend renaming the file to simply `pwgen` if you are to put this script in your PATH. This is already done out of the box on the release<br>
You may of course also run the script directly with python using `python3 pwgen.py`.

<h2>Usage</h2>
Simply run it with your shell as any other executable file using `./pwgen.py`<br>
You may add any combination of the available arguments, these are:<br>

      -h, --help        show this help message and exit
      -u, --uppercase   use uppercase letters in the password
      -d, --digits      use digits (numbers 0 to 9) in the password
      -s, --symbols     use special symbols in the password
      -w, --words       use english words in the password
      -l x, --length x  set the length of the password
