# Xbox Factory Restore Button Combo Calculator
The original Xbox has an undocumented feature allowing the user to factory reset the console by inputting a special button combo on the System Info screen. This button combo is unique to each system and is derived from the system's unique HDD key stored in EEPROM.
Microsoft support would give this code to users. This is the only official way to factory reset the console, and it bypasses parental controls or any other considerations which would otherwise prevent it.

This script will calculate your console-unique factory reset code given the HDD Key. Methods for deriving the HDD Key are beyond the scope of this project.

## How to use

Python 3+ is required.

Download code_gen.py and run it in Python. Type or paste your HDD Key when prompted. The program will print your reset code to the console.

Go to your console's dashboard and enter Settings -> System Info. Input your button combination. A prompt will appear warning you that your data will be reset. Press "yes" to factory reset your console.

## Notable button combinations

If you have a modded console and have overwritten your HDD Key with one of the following, you can use the following pre-computed button combinations:

**All zeroes (null key)**: YRLLY

**All ones**: YRLAX
