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

import matplotlib, numpy;
#matplotlib.use('Agg')

import matplotlib.pyplot as plt;
import numpy as np;

print("%-16s = %s"     % ("matplotlib", matplotlib.__version__));
print("%-16s = %s"     % (     "numpy", numpy.__version__));
print("\n%s%s%s---------------------------------------------------------------------------%s" % (HEADER_ATTRIB, HEADER_FGCOLR, HEADER_BGCOLR, HEADER_RSTALL));

###########################################################################
#Chart #1.
xpoints = np.array([1,2,3,4,5,6,7,8,9,10]);
ypoints = np.array([1,8,2,6,3,9,4,7,5,10]);

plt.plot(xpoints,ypoints,linestyle='-',marker='o',color="#000000"); #black
#plt.grid();
plt.xticks(np.arange(0,11,step=1.0));
plt.yticks(np.arange(0,11,step=1.0));
plt.title("My Kick Ass Chart!");
plt.xlabel("X-Axis");
plt.ylabel("Y-Axis");
plt.show();

###########################################################################
#Chart #2.
plot2_x1 = np.array([1,2,3,4, 5]);
plot2_y1 = np.array([5,1,7,2, 9]);
plot2_y2 = np.array([2,8,4,6,10]);

plt.plot(plot2_x1,plot2_y1,linestyle='-',marker='o',color="#008000"); #green
plt.plot(plot2_x1,plot2_y2,linestyle='-',marker='o',color="#0000ff"); #blue
#plt.grid();
plt.xticks(np.arange(0, 6,step=1.0));
plt.yticks(np.arange(0,11,step=1.0));
plt.title("My Chart #2.");
plt.xlabel("X-Axis");
plt.ylabel("Y-Axis");
plt.show();

###########################################################################
#Chart #3.
plot3_x1 = np.array([1,2,3,4, 5]);
plot3_y1 = np.array([5,1,7,2, 9]);
plot3_y2 = np.array([2,8,4,6,10]);
plot3_y3 = np.array([1,3,5,7, 9]);
plot3_y4 = np.array([8,6,4,2, 0]);

plt.subplot(2,4,1);
plt.plot(plot3_x1,plot3_y1,linestyle='-',marker='o',color="#008080"); #teal
plt.xticks(np.arange(0, 6,step=1.0));
plt.yticks(np.arange(0,11,step=1.0));
plt.title("My Chart #3-1.");
plt.xlabel("X-Axis");
plt.ylabel("Y-Axis");

plt.subplot(2,4,3);
plt.plot(plot3_x1,plot3_y2,linestyle='-',marker='o',color="#ffa500"); #orange
plt.xticks(np.arange(0, 6,step=1.0));
plt.yticks(np.arange(0,11,step=1.0));
plt.title("My Chart #3-2.");
plt.xlabel("X-Axis");
plt.ylabel("Y-Axis");

plt.subplot(2,4,6);
plt.plot(plot3_x1,plot3_y3,linestyle='-',marker='o',color="#ff0000"); #red
plt.xticks(np.arange(0, 6,step=1.0));
plt.yticks(np.arange(0,11,step=1.0));
plt.title("My Chart #3-3.");
plt.xlabel("X-Axis");
plt.ylabel("Y-Axis");

plt.subplot(2,4,8);
plt.plot(plot3_x1,plot3_y4,linestyle='-',marker='o',color="#ff00ff"); #magenta
plt.xticks(np.arange(0, 6,step=1.0));
plt.yticks(np.arange(0,11,step=1.0));
plt.title("My Chart #3-4.");
plt.xlabel("X-Axis");
plt.ylabel("Y-Axis");

plt.suptitle("My Multi-Subplots");
plt.show();

###########################################################################
#Chart #4.
y = np.array([25,20,20,5,10,20]);
mylabels = [ "Apples", "Bananas", "Cherries",   "Dates",    "Figs",  "Grapes"];
mycolors = ["#ff0000", "#ff69b4",  "#0000ff", "#008000", "#a52a2a", "#800080"]; #red,hotpink,blue,green,brown,purple

plt.pie(y, labels = mylabels, colors = mycolors);
plt.title("My Chart #4.");
plt.legend(loc="lower center",ncol=4,frameon=True,bbox_to_anchor=(0.5,-0.12)); #title="Chart #4 Legend",;
plt.show();

print("");
print("%s%s%s# Time EOF : %-53s ########%s" % (HEADER_ATTRIB, HEADER_FGCOLR, HEADER_BGCOLR, time.strftime("%c"), HEADER_RSTALL));
print("%s%s%s###### END - %-53s ########%s" % (HEADER_ATTRIB, HEADER_FGCOLR, HEADER_BGCOLR, FILE_NAME_HEADER,    HEADER_RSTALL));
