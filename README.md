# Xbox Restore Button Combo Calculator
The original Xbox has an undocumented feature allowing the user to factory reset the console by inputting a special button combo. This button combo is unique to each system and is derived from the system's unique HDD key stored in EEPROM.
Microsoft support would give this code to users. This is the only official way to factory reset the console, and it bypasses parental controls or any other considerations which would otherwise prevent it.

This script will calculate your console-unique factory reset code given the HDD Key. Methods for deriving the HDD Key are beyond the scope of this project.

## How to use

Python 3+ is required.

Download code_gen.py and run it in Python. Type or paste your HDD Key when prompted. The program will print your reset code to the console.
