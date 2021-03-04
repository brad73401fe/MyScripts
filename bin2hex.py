#!/usr/bin/env python
#Author:   BEVERSON
#DateTime: 2021/02/24 23:37:01 PST
#Notes:    Default path for bash is "/bin/bash". Optional path for bash is "/usr/local/bin/bash".
#Notes:    Default path for python is "/usr/bin/python". Optional path for python is "/usr/local/bin/python".

REVISION_STATUS="2021/02/24";

import time, os, commands, sys, shutil, random; #Define python modules.

FILE_NAME_HEADER="bin2hex.py";
HEADER_ATTRIB="\x1b[4m";	#(1,2,4,5,7,8).
HEADER_FGCOLR="\x1b[34m";	#(39,30,31,32,33,34,35,36,37).
HEADER_BGCOLR="\x1b[49m";	#(49,40,41,42,43,44,45,46,47).
HEADER_RSTALL="\x1b[0m";	#(0,21,22,24,25,27,28);
print("%s%s%s#### START - %-53s ########%s" % (HEADER_ATTRIB, HEADER_FGCOLR, HEADER_BGCOLR, FILE_NAME_HEADER,    HEADER_RSTALL));
print("%s%s%s# Time SOF : %-53s ########%s" % (HEADER_ATTRIB, HEADER_FGCOLR, HEADER_BGCOLR, time.strftime("%c"), HEADER_RSTALL));
print("");

import binascii, struct;

TIME_STAMP=time.strftime("%y%m%d");


FILE_NAME_INPUT="arcshell_bbic6_a0_210212.bin";
#FILE_NAME_INPUT="arcshell_bbic6_a0_210216.bin";
FILE_NAME_OUTPUT="temp_bin2hex_output_" + TIME_STAMP + ".txt";

with open(FILE_NAME_INPUT, 'rb') as binary_file:
	os.remove(FILE_NAME_OUTPUT);                                #This will remove files.
	FILE_DES=os.open(FILE_NAME_OUTPUT, os.O_RDWR|os.O_CREAT);   #This creates the files.
	data_byte=binary_file.read(4);
	LineCount=( 0 );
	while data_byte:
		LoopBeg=( 0 );
		LoopEnd=( 4 );
		for ZAn in xrange(LoopBeg, LoopEnd, 1):
			if (ZAn == LoopBeg):
				FILE_RET=os.write(FILE_DES, "0x" + format(LineCount, '08x') + ":  ");   #This writes to the files.
				LineCount += 1;
			#print(""); #END IF STATEMENT.
			#print(binascii.hexlify(data_byte));   #NOT REQUIRED.
			FILE_RET=os.write(FILE_DES, binascii.hexlify(data_byte)[::-1]);   #This writes to the files.
			data_byte=binary_file.read(4);
			FILE_RET=os.write(FILE_DES, " ");                                 #This writes to the files.
			if (ZAn == (LoopEnd - 1)):
				FILE_RET=os.write(FILE_DES, "#\n");                       #This writes to the files.
			#print(""); #END IF STATEMENT.
		#print(""); #END FOR STATEMENT.
	#print(""); #END WHILE STATEMENT.
#print(""); #END WITH STATEMENT.
os.close(FILE_DES);
os.chmod(FILE_NAME_OUTPUT, 0644);



print("");
print("%s%s%s# Time EOF : %-53s ########%s" % (HEADER_ATTRIB, HEADER_FGCOLR, HEADER_BGCOLR, time.strftime("%c"), HEADER_RSTALL));
print("%s%s%s###### END - %-53s ########%s" % (HEADER_ATTRIB, HEADER_FGCOLR, HEADER_BGCOLR, FILE_NAME_HEADER,    HEADER_RSTALL));
