#!/usr/bin/env python
#Author:   BEVERSON
#DateTime: 2021/01/19 00:55:01 PST
#Notes:    Default path for bash is "/bin/bash". Optional path for bash is "/usr/local/bin/bash".
#Notes:    Default path for python is "/usr/bin/python". Optional path for python is "/usr/local/bin/python".

REVISION_STATUS="2021/01/19";

import time, os, commands, sys, shutil, random; #Define python modules.

FILE_NAME_HEADER="RESISTOR_COLOR_CODE.py";
HEADER_ATTRIB="\x1b[4m";	#(1,2,4,5,7,8).
HEADER_FGCOLR="\x1b[34m";	#(39,30,31,32,33,34,35,36,37).
HEADER_BGCOLR="\x1b[49m";	#(49,40,41,42,43,44,45,46,47).
HEADER_RSTALL="\x1b[0m";	#(0,21,22,24,25,27,28);
print("%s%s%s#### START - %-53s ########%s" % (HEADER_ATTRIB, HEADER_FGCOLR, HEADER_BGCOLR, FILE_NAME_HEADER,    HEADER_RSTALL));
print("%s%s%s# Time SOF : %-53s ########%s" % (HEADER_ATTRIB, HEADER_FGCOLR, HEADER_BGCOLR, time.strftime("%c"), HEADER_RSTALL));
print("");

NUMB_BAND_INPUT = raw_input("Select number of color bands (4/5): ");
print("");

if   (NUMB_BAND_INPUT == "4"):
	import RESISTOR_COLOR_CODE_4B_FUNC;
	RESISTOR_COLOR_CODE_4B_FUNC.LEGEND_4B();
	RESISTOR_COLOR_CODE_4B_FUNC.RUN_MAIN_4B(FILE_NAME_HEADER,HEADER_ATTRIB,HEADER_FGCOLR,HEADER_BGCOLR,HEADER_RSTALL);
elif (NUMB_BAND_INPUT == "5"):
	import RESISTOR_COLOR_CODE_5B_FUNC;
	RESISTOR_COLOR_CODE_5B_FUNC.LEGEND_5B();
	RESISTOR_COLOR_CODE_5B_FUNC.RUN_MAIN_5B(FILE_NAME_HEADER,HEADER_ATTRIB,HEADER_FGCOLR,HEADER_BGCOLR,HEADER_RSTALL)
else:
	print("%-16s = %s (%s%s%s)" % ("NUMB_BAND_INPUT", NUMB_BAND_INPUT, "\x1b[31m", "ERROR: Incorrect number.", "\x1b[0m"));
#print(""); #END IF STATEMENT.

print("");
print("%s%s%s# Time EOF : %-53s ########%s" % (HEADER_ATTRIB, HEADER_FGCOLR, HEADER_BGCOLR, time.strftime("%c"), HEADER_RSTALL));
print("%s%s%s###### END - %-53s ########%s" % (HEADER_ATTRIB, HEADER_FGCOLR, HEADER_BGCOLR, FILE_NAME_HEADER,    HEADER_RSTALL));
