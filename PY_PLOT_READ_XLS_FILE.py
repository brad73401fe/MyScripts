#!/usr/bin/python3
#Author:   BEVERSON
#DateTime: 2021/02/14 23:59:01 PST
#Notes:    Default path for bash is "/bin/bash". Optional path for bash is "/usr/local/bin/bash".
#Notes:    Default path for python is "/usr/bin/python". Optional path for python is "/usr/local/bin/python".

REVISION_STATUS="2021/02/14";

#import time, os,   commands, sys, shutil, random; #Define python modules.
import  time, os, subprocess, sys, shutil, random; #Define python modules.

FILE_NAME_HEADER="PY_PLOT_CHARTS.py";
HEADER_ATTRIB="\x1b[4m";	#(1,2,4,5,7,8).
HEADER_FGCOLR="\x1b[34m";	#(39,30,31,32,33,34,35,36,37).
HEADER_BGCOLR="\x1b[49m";	#(49,40,41,42,43,44,45,46,47).
HEADER_RSTALL="\x1b[0m";	#(0,21,22,24,25,27,28);
print("%s%s%s#### START - %-53s ########%s" % (HEADER_ATTRIB, HEADER_FGCOLR, HEADER_BGCOLR, FILE_NAME_HEADER,    HEADER_RSTALL));
print("%s%s%s# Time SOF : %-53s ########%s" % (HEADER_ATTRIB, HEADER_FGCOLR, HEADER_BGCOLR, time.strftime("%c"), HEADER_RSTALL));
print("");

#### Define Date and Time variables. ####
DATE_STANDARD=time.strftime("%c");
DATE_YYYYmmdd=time.strftime("%Y/%m/%d");
TIME_HHMMSS=time.strftime("%H:%M:%S");
ZONE_ZZ=time.strftime("%Z");

#### START - Select the Date and Time output type. ####
SEL_DATE_TIME=2; #Default is 2.
if   (SEL_DATE_TIME == 1):
	#### Option 1. ####
	print("%-16s = %s"       % ("DateTime", DATE_STANDARD));
elif (SEL_DATE_TIME == 2):
	#### Option 2. ####
	print("%-16s = %s %s %s" % ("DateTime", DATE_YYYYmmdd, TIME_HHMMSS, ZONE_ZZ));
else:
	print("%-16s = %s%s%s"   % ("DateTime", "\x1b[31m", "**ERROR**", "\x1b[0m"));
#print(""); #END IF STATEMENT.
###### END - Select the Date and Time output type. ####

#### START - Basic environmental variables information. ####
USER=os.environ["USER"];         print("%-16s = %s" % ("USER",     USER));
HOME=os.environ["HOME"];         print("%-16s = %s" % ("HOME",     HOME));
HOSTNAME=os.environ["HOSTNAME"]; print("%-16s = %s" % ("HOSTNAME", HOSTNAME));
###### END - Basic environmental variables information. ####

#### START - Get python version. ####
SEL_PYTHON_VER=1; #Default is 1.
#CmdLineInput_01=subprocess.call(["python","-V"]); #python -V, python --version.
if   ( SEL_PYTHON_VER == 1 ):
	print("%-16s = %d.%d.%d.%s.%d" % ("PYTHON_VERSION", sys.version_info[0], sys.version_info[1], sys.version_info[2], sys.version_info[3], sys.version_info[4]));
elif ( SEL_PYTHON_VER == 2 ):
	print("%-16s = %d.%d.%d.%s.%d" % ("PYTHON_VERSION", sys.version_info.major, sys.version_info.minor, sys.version_info.micro, sys.version_info.releaselevel, sys.version_info.serial));
#elif ( SEL_PYTHON_VER == 3 ):
#	print("");
#	print("%-16s = %s"     % ("PYTHON_VERSION", CmdLineInput_01));
else:
	print("%-16s = %b%s%b" % ("PYTHON_VERSION", "\x1b[31m", "**ERROR**", "\x1b[0m"));
#print(""); #END IF STATEMENT.
###### END - Get python version. ####

#### START - Get revision status. ####
print("%-16s = %s" % ("REVISION_STATUS", REVISION_STATUS));
###### END - Get revision status. ####

print("\n%s%s%s---------------------------------------------------------------------------%s" % (HEADER_ATTRIB, HEADER_FGCOLR, HEADER_BGCOLR, HEADER_RSTALL));

import matplotlib, numpy, pandas;

import matplotlib.pyplot as plt;
import numpy as np;
import pandas as pd;

print("%-16s = %s"     % ("matplotlib", matplotlib.__version__));
print("%-16s = %s"     % (     "numpy", numpy.__version__));
print("%-16s = %s"     % (    "pandas", pandas.__version__));
print("\n%s%s%s---------------------------------------------------------------------------%s" % (HEADER_ATTRIB, HEADER_FGCOLR, HEADER_BGCOLR, HEADER_RSTALL));


#datafile = pd.read_csv('');
#datafile = pd.read_excel('T8S255W1S1_30units_QT62212_A0_QA_QA1-1_20210209_134622.stdf.raw.xlsx');
datafile = pd.read_excel('T8S255W1S1_30units_QT62212_A0_QA_QA1-1_20210209_134622.stdf.raw.core.xlsx');

print(datafile.columns);
#print(datafile.to_string());     #Debug only. Comment out.

ColTestN = datafile[['Test#']];
ColValue = datafile[['Value']];   #datafile[['Test#','Value']];

#print(ColTestN.to_string());     #Debug only. Comment out.
#print(ColValue.to_string());     #Debug only. Comment out.


plt.plot(ColTestN,linestyle='-',marker='o',color="#0000ff"); #blue.
#plt.grid();
#plt.xticks(np.arange(ROW_BEG, ROW_END,step=1.0),rotation=45);
#plt.yticks(np.arange(0,21,step=1.0));
plt.title("Plot xlsx data (Test#).");
plt.xlabel("X-Axis (Test#)");
plt.ylabel("Y-Axis");
plt.show();

plt.plot(ColValue,linestyle='-',marker='o',color="#008000"); #green.
#plt.grid();
#plt.xticks(np.arange(ROW_BEG, ROW_END,step=1.0),rotation=45);
#plt.yticks(np.arange(0,21,step=1.0));
plt.title("Plot xlsx data (Values).");
plt.xlabel("X-Axis (Values)");
plt.ylabel("Y-Axis");
plt.show();



ROW_BEG=(140);
ROW_END=(160);

plt.plot(ColTestN.iloc[ROW_BEG:ROW_END],linestyle='-',marker='o',color="#0000ff"); #blue.
#plt.grid();
plt.xticks(np.arange(ROW_BEG, ROW_END,step=1.0),rotation=45);
#plt.yticks(np.arange(0,21,step=1.0));
plt.title("Plot xlsx data (Test#).");
plt.xlabel("X-Axis (Test#)");
plt.ylabel("Y-Axis");
plt.show();

plt.plot(ColValue.iloc[ROW_BEG:ROW_END],linestyle='-',marker='o',color="#008000"); #green.
#plt.grid();
plt.xticks(np.arange(ROW_BEG, ROW_END,step=1.0),rotation=45);
#plt.yticks(np.arange(0,21,step=1.0));
plt.title("Plot xlsx data (Values).");
plt.xlabel("X-Axis (Values)");
plt.ylabel("Y-Axis");
plt.show();



ROW_BEG=(160);
ROW_END=(180);

plt.plot(ColTestN.iloc[ROW_BEG:ROW_END],linestyle='-',marker='o',color="#0000ff"); #blue.
#plt.grid();
plt.xticks(np.arange(ROW_BEG, ROW_END,step=1.0),rotation=45);
#plt.yticks(np.arange(0,21,step=1.0));
plt.title("Plot xlsx data (Test#).");
plt.xlabel("X-Axis (Test#)");
plt.ylabel("Y-Axis");
plt.show();

plt.plot(ColValue.iloc[ROW_BEG:ROW_END],linestyle='-',marker='o',color="#008000"); #green.
#plt.grid();
plt.xticks(np.arange(ROW_BEG, ROW_END,step=1.0),rotation=45);
#plt.yticks(np.arange(0,21,step=1.0));
plt.title("Plot xlsx data (Values).");
plt.xlabel("X-Axis (Values)");
plt.ylabel("Y-Axis");
plt.show();



ROW_BEG=(180);
ROW_END=(200);

plt.plot(ColTestN.iloc[ROW_BEG:ROW_END],linestyle='-',marker='o',color="#0000ff"); #blue.
#plt.grid();
plt.xticks(np.arange(ROW_BEG, ROW_END,step=1.0),rotation=45);
#plt.yticks(np.arange(0,21,step=1.0));
plt.title("Plot xlsx data (Test#).");
plt.xlabel("X-Axis (Test#)");
plt.ylabel("Y-Axis");
plt.show();

plt.plot(ColValue.iloc[ROW_BEG:ROW_END],linestyle='-',marker='o',color="#008000"); #green.
#plt.grid();
plt.xticks(np.arange(ROW_BEG, ROW_END,step=1.0),rotation=45);
#plt.yticks(np.arange(0,21,step=1.0));
plt.title("Plot xlsx data (Values).");
plt.xlabel("X-Axis (Values)");
plt.ylabel("Y-Axis");
plt.show();


print("");
print("%s%s%s# Time EOF : %-53s ########%s" % (HEADER_ATTRIB, HEADER_FGCOLR, HEADER_BGCOLR, time.strftime("%c"), HEADER_RSTALL));
print("%s%s%s###### END - %-53s ########%s" % (HEADER_ATTRIB, HEADER_FGCOLR, HEADER_BGCOLR, FILE_NAME_HEADER,    HEADER_RSTALL));
