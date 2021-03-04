#!/usr/bin/env python
#Author:   BEVERSON
#DateTime: 2021/01/19 00:55:01 PST
#Notes:    Default path for bash is "/bin/bash". Optional path for bash is "/usr/local/bin/bash".
#Notes:    Default path for python is "/usr/bin/python". Optional path for python is "/usr/local/bin/python".

#Python Functions:
def LEGEND_4B():
	#ANSI Formatting Color Codes.
	BLACK__BGCOLR="\x1b[40m";
	BROWN__BGCOLR="\x1b[49m";  #No color to match. Set to default.
	RED____BGCOLR="\x1b[41m";
	ORANGE_BGCOLR="\x1b[101m"; #Set to light red to get close to orange color.
	GREEN__BGCOLR="\x1b[42m";
	YELLOW_BGCOLR="\x1b[103m";
	BLUE___BGCOLR="\x1b[44m";
	VIOLET_BGCOLR="\x1b[45m";
	GREY___BGCOLR="\x1b[100m";
	WHITE__BGCOLR="\x1b[107m";
	GOLD___BGCOLR="\x1b[43m";
	SILVER_BGCOLR="\x1b[47m";
	HEADER_RSTALL="\x1b[0m";
	
	#Print Legend Reference.
	print("%s%s%-8s | %s | %s | %4s%s | %-8s%s" % (BLACK__BGCOLR, "\x1b[39m",  "Black", "0", "0",    "1", u"\u03A9",      "n/a", HEADER_RSTALL));
	print("%s%s%-8s | %s | %s | %4s%s | %-8s%s" % (BROWN__BGCOLR, "\x1b[39m",  "Brown", "1", "1",   "10", u"\u03A9",     "+/-1", HEADER_RSTALL));
	print("%s%s%-8s | %s | %s | %4s%s | %-8s%s" % (RED____BGCOLR, "\x1b[39m",    "Red", "2", "2",  "100", u"\u03A9",     "+/-2", HEADER_RSTALL));
	print("%s%s%-8s | %s | %s | %4s%s | %-8s%s" % (ORANGE_BGCOLR, "\x1b[39m", "Orange", "3", "3",   "1K", u"\u03A9",      "n/a", HEADER_RSTALL));
	print("%s%s%-8s | %s | %s | %4s%s | %-8s%s" % (YELLOW_BGCOLR, "\x1b[30m", "Yellow", "4", "4",  "10K", u"\u03A9",      "n/a", HEADER_RSTALL));
	print("%s%s%-8s | %s | %s | %4s%s | %-8s%s" % (GREEN__BGCOLR, "\x1b[30m",  "Green", "5", "5", "100K", u"\u03A9", "+/-0.50%", HEADER_RSTALL));
	print("%s%s%-8s | %s | %s | %4s%s | %-8s%s" % (BLUE___BGCOLR, "\x1b[30m",   "Blue", "6", "6",   "1M", u"\u03A9", "+/-0.25%", HEADER_RSTALL));
	print("%s%s%-8s | %s | %s | %4s%s | %-8s%s" % (VIOLET_BGCOLR, "\x1b[30m", "Violet", "7", "7",  "10M", u"\u03A9", "+/-0.10%", HEADER_RSTALL));
	print("%s%s%-8s | %s | %s | %4s%s | %-8s%s" % (GREY___BGCOLR, "\x1b[39m",   "Grey", "8", "8", "100M", u"\u03A9", "+/-0.05%", HEADER_RSTALL));
	print("%s%s%-8s | %s | %s | %4s%s | %-8s%s" % (WHITE__BGCOLR, "\x1b[30m",  "White", "9", "9",   "1G", u"\u03A9",      "n/a", HEADER_RSTALL));
	print("%s%s%-8s | %s | %s | %4s%s | %-8s%s" % (GOLD___BGCOLR, "\x1b[30m",   "Gold", " ", " ",  "0.1", u"\u03A9",    "+/-5%", HEADER_RSTALL));
	print("%s%s%-8s | %s | %s | %4s%s | %-8s%s" % (SILVER_BGCOLR, "\x1b[30m", "Silver", " ", " ", "0.01", u"\u03A9",   "+/-10%", HEADER_RSTALL));
	print("");
#END LEGEND_4B();

def RUN_MAIN_4B(FILE_NAME_HEADER,HEADER_ATTRIB,HEADER_FGCOLR,HEADER_BGCOLR,HEADER_RSTALL):
	import time, sys; #Define python modules.
	DebugEnable=0;    #Set flag to default (0).
	ExitStatus0=0;    #Set flag to default (0).
	BAND_1_DICT = {
		"black" :0,
		"brown" :1,
		"red"   :2,
		"orange":3,
		"yellow":4,
		"green" :5,
		"blue"  :6,
		"violet":7,
		"grey"  :8,
		"white" :9
	};
	BAND_2_DICT = {
		"black" :0,
		"brown" :1,
		"red"   :2,
		"orange":3,
		"yellow":4,
		"green" :5,
		"blue"  :6,
		"violet":7,
		"grey"  :8,
		"white" :9
	};
	BAND_3_DICT = {
		"black" :         1,
		"brown" :        10,
		"red"   :       100,
		"orange":      1000,
		"yellow":     10000,
		"green" :    100000,
		"blue"  :   1000000,
		"violet":  10000000,
		"grey"  : 100000000,
		"white" :1000000000,
		"gold"  :         0.1,
		"silver":         0.01
	};
	BAND_4_DICT = {
		"black" :"n/a",
		"brown" :"+/-1%",
		"red"   :"+/-2%",
		"orange":"n/a",
		"yellow":"n/a",
		"green" :"+/-0.5%",
		"blue"  :"+/-0.25%",
		"violet":"+/-0.1%",
		"grey"  :"+/-0.05%",
		"white" :"n/a",
		"gold"  :"+/-5%",
		"silver":"+/-10%",
	};
	
	BAND_1_INPUT = raw_input("Color of band #1: ");
	BAND_2_INPUT = raw_input("Color of band #2: ");
	BAND_3_INPUT = raw_input("Color of band #3: ");
	BAND_4_INPUT = raw_input("Color of band #4: ");
	print("");
	
	if (DebugEnable == 1):
		print("%-16s = %s"       % ("BAND_1_INPUT", BAND_1_INPUT));
		print("%-16s = %s"       % ("BAND_2_INPUT", BAND_2_INPUT));
		print("%-16s = %s"       % ("BAND_3_INPUT", BAND_3_INPUT));
		print("%-16s = %s"       % ("BAND_4_INPUT", BAND_4_INPUT));
		print("");
	#print(""); #END IF STATEMENT.
	
	#Check to make sure band 1 input is valid.
	try:
		print("%-16s = %s"       % ("BAND_1_NUMB", BAND_1_DICT[BAND_1_INPUT]));
	except:
		ExitStatus0=1;
		print("%-16s = %s%s%s"   % ("BAND_1_NUMB", "\x1b[31m", "Not a valid color. Try again.", "\x1b[0m"));
	#Check to make sure band 2 input is valid.
	try:
		print("%-16s = %s"       % ("BAND_2_NUMB", BAND_2_DICT[BAND_2_INPUT]));
	except:
		ExitStatus0=1;
		print("%-16s = %s%s%s"   % ("BAND_2_NUMB", "\x1b[31m", "Not a valid color. Try again.", "\x1b[0m"));
	#Check to make sure band 3 input is valid.
	try:
		print("%-16s = %s"       % ("BAND_3_NUMB", BAND_3_DICT[BAND_3_INPUT]));
	except:
		ExitStatus0=1;
		print("%-16s = %s%s%s"   % ("BAND_3_NUMB", "\x1b[31m", "Not a valid color. Try again.", "\x1b[0m"));
	#Check to make sure band 4 input is valid.
	try:
		print("%-16s = %s"       % ("BAND_4_NUMB", BAND_4_DICT[BAND_4_INPUT]));
	except:
		ExitStatus0=1;
		print("%-16s = %s%s%s"   % ("BAND_4_NUMB", "\x1b[31m", "Not a valid color. Try again.", "\x1b[0m"));
	print("");
	
	#### Exit status. ####
	if (ExitStatus0 == 1):
		print("%s%s%s"           % ("\x1b[31m", "Exit status has been issued.", "\x1b[0m"));
		print("");
		print("%s%s%s# Time EOF : %-53s ########%s" % (HEADER_ATTRIB, HEADER_FGCOLR, HEADER_BGCOLR, time.strftime("%c"), HEADER_RSTALL));
		print("%s%s%s###### END - %-53s ########%s" % (HEADER_ATTRIB, HEADER_FGCOLR, HEADER_BGCOLR, FILE_NAME_HEADER,    HEADER_RSTALL));
		sys.exit(); #(0=Success, 1=Failure).
	#print(""); #END IF STATEMENT.
	
	BAND_1_NUMB = BAND_1_DICT[BAND_1_INPUT];
	BAND_2_NUMB = BAND_2_DICT[BAND_2_INPUT];
	BAND_3_NUMB = BAND_3_DICT[BAND_3_INPUT];
	BAND_4_NUMB = BAND_4_DICT[BAND_4_INPUT];
	
	FOUR_BAND_NUMB = (((BAND_1_NUMB * 10) + BAND_2_NUMB) * BAND_3_NUMB);
	print("%-16s = %s %s  (%s)" % ("FOUR_BAND_NUMB", '{:,.2f}'.format(FOUR_BAND_NUMB), u"\u03A9", BAND_4_NUMB));
#END RUN_MAIN_4B();
