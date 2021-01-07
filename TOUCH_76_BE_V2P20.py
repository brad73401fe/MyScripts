#!/usr/bin/env python
#Author:   BEVERSON
#DateTime: 2020/11/11 21:25:01 PST
#Notes:    Default path for bash is "/bin/bash". Optional path for bash is "/usr/local/bin/bash".
#Notes:    Default path for python is "/usr/bin/python". Optional path for python is "/usr/local/bin/python".

REVISION_STATUS="2020/11/11";

import time, os, commands, sys, shutil, random; #Define python modules.

FILE_NAME_HEADER="TOUCH_76_BE_V2P20.py";
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
CmdLineInput_01=commands.getoutput("python -V"); #python -V, python --version.
if   ( SEL_PYTHON_VER == 1 ):
	print("%-16s = %d.%d.%d.%s.%d" % ("PYTHON_VERSION", sys.version_info[0], sys.version_info[1], sys.version_info[2], sys.version_info[3], sys.version_info[4]));
elif ( SEL_PYTHON_VER == 2 ):
	print("%-16s = %d.%d.%d.%s.%d" % ("PYTHON_VERSION", sys.version_info.major, sys.version_info.minor, sys.version_info.micro, sys.version_info.releaselevel, sys.version_info.serial));
elif ( SEL_PYTHON_VER == 3 ):
	print("");
	print("%-16s = %s"     % ("PYTHON_VERSION", CmdLineInput_01));
else:
	print("%-16s = %b%s%b" % ("PYTHON_VERSION", "\x1b[31m", "**ERROR**", "\x1b[0m"));
#print(""); #END IF STATEMENT.
###### END - Get python version. ####

#### START - Get revision status. ####
print("%-16s = %s" % ("REVISION_STATUS", REVISION_STATUS));
###### END - Get revision status. ####

print("\n%s%s%s---------------------------------------------------------------------------%s" % (HEADER_ATTRIB, HEADER_FGCOLR, HEADER_BGCOLR, HEADER_RSTALL));

#### Argument to select the device in use option. ####
ARGA=str(sys.argv);           #This puts all arguments into an array. (0-n).
Set_AQC100_B10_V1P10_Flag=0;  #Set flag to default (0). AQC100-B10 (Atlantic).
Set_AQC107_B10_V1P16_Flag=0;  #Set flag to default (0). AQC107-B10 (Jamaica).
Set_AQC111C_B01_V0P25_Flag=0; #Set flag to default (0). AQC111C-B01 (Bermuda).
Set_BBIC5_B1_R09A_Flag=0;     #Set flag to default (0). QT10GA-B1,QT10GS-B1,QT10GT-B1,QT10GU-B1 (BBIC5).
Set_BBIC5_B1_R10_Flag=0;      #Set flag to default (0). QT10GA-B1,QT10GS-B1,QT10GT-B1,QT10GU-B1 (BBIC5).
Set_BBIC5_B1_R11_Flag=0;      #Set flag to default (0). QT10GA-B1,QT10GS-B1,QT10GT-B1,QT10GU-B1 (BBIC5).
Set_BBIC5_B1_R12_Flag=0;      #Set flag to default (0). QT10GA-B1,QT10GS-B1,QT10GT-B1,QT10GU-B1 (BBIC5).
Set_BBIC5_B1_WS_R01_Flag=0;   #Set flag to default (0). QT10GA-B1,QT10GS-B1,QT10GT-B1,QT10GU-B1 (BBIC5).
Set_BBIC5_C0_R07_Flag=0;      #Set flag to default (0). QT10GA-C0,QT10GS-C0,QT10GT-C0,QT10GU-C0 (BBIC5).
Set_BBIC5_D0_R01A_Flag=0;     #Set flag to default (0). QT10GA-D0,QT10GS-D0,QT10GT-D0,QT10GU-D0 (BBIC5).
Set_BBIC6_A0_R01_Flag=0;      #Set flag to default (0). QT10GA-AX2,QT10GS-AX2,QT10GT-AX2,QT10GU-AX2 (BBIC6).
Set_PMIC_A4_R01_Flag=0;       #Set flag to default (0). PMIC-A4 (PMIC).
Set_PMIC_C0_R01_Flag=0;       #Set flag to default (0). PMIC-C0 (PMIC).
Set_PMIC_C1_R01_Flag=0;       #Set flag to default (0). PMIC-C1 (PMIC).
Set_X550A_B0_V1P80_Flag=0;    #Set flag to default (0). X550-AT2-B00 (Sageville 17mm).
Set_REL_X550A_B0_Flag=0;      #Set flag to default (0). Released X550-AT2-B00.
Set_DEBUG_Flag=0;             #Set flag to default (0).
Set_Touch_All_Flag=0;         #Set flag to default (0).
ExitStatus0=0;                #Set flag to default (0).
i=0;
j=len(sys.argv);
while (i < len(sys.argv)):
	#CASE STATEMENT: Filter through arguments to decide which flags to enable.
	if   (sys.argv[i] == "-aqc100_b10_v1p10"):    Set_AQC100_B10_V1P10_Flag=1;
	elif (sys.argv[i] == "-aqc107_b10_v1p16"):    Set_AQC107_B10_V1P16_Flag=1;
	elif (sys.argv[i] == "-aqc111c_b01_v0p25"):   Set_AQC111C_B01_V0P25_Flag=1;
	elif (sys.argv[i] == "-bbic5_b1_r09a"):       Set_BBIC5_B1_R09A_Flag=1;
	elif (sys.argv[i] == "-bbic5_b1_r10"):        Set_BBIC5_B1_R10_Flag=1;
	elif (sys.argv[i] == "-bbic5_b1_r11"):        Set_BBIC5_B1_R11_Flag=1;
	elif (sys.argv[i] == "-bbic5_b1_r12"):        Set_BBIC5_B1_R12_Flag=1;
	elif (sys.argv[i] == "-bbic5_b1_ws_r01"):     Set_BBIC5_B1_WS_R01_Flag=1;
	elif (sys.argv[i] == "-bbic5_c0_r07"):        Set_BBIC5_C0_R07_Flag=1;
	elif (sys.argv[i] == "-bbic5_d0_r01a"):       Set_BBIC5_D0_R01A_Flag=1;
	elif (sys.argv[i] == "-bbic6_a0_r01"):        Set_BBIC6_A0_R01_Flag=1;
	elif (sys.argv[i] == "-pmic_a4_r01"):         Set_PMIC_A4_R01_Flag=1;
	elif (sys.argv[i] == "-pmic_c0_r01"):         Set_PMIC_C0_R01_Flag=1;
	elif (sys.argv[i] == "-pmic_c1_r01"):         Set_PMIC_C1_R01_Flag=1;
	elif (sys.argv[i] == "-x550a_b0_v1p80"):      Set_X550A_B0_V1P80_Flag=1;
	elif (sys.argv[i] == "-rel_x550a_b0"):        Set_REL_X550A_B0_Flag=1;
	elif (sys.argv[i] == "-debug"):               Set_DEBUG_Flag=1;
	elif (sys.argv[i] == "-touch_all"):           Set_Touch_All_Flag=1;
	elif (sys.argv[i] == "-h"):                   ExitStatus0=1;
	elif (sys.argv[i] == "-help"):                ExitStatus0=1;
	#else:                                        print("NO OPTIONS SELECTED."); #DEBUG ONLY. REMOVE WHEN FINISHED.
	#print(""); #END IF STATEMENT.
	i=( i + 1 );
#print(""); #END WHILE STATEMENT.

DoDebugArg0="NO"; #(YES/NO)
if (Set_DEBUG_Flag == 1) or (DoDebugArg0 == "YES"):
	ExitStatus0=1; #Want to stop at exit status section.
	print("#### START: Debug. ################################");
	print("Argument List:  %s" % (str(sys.argv))); #DEBUG ONLY. REMOVE WHEN FINISHED.
	print("Argument Flags: %s" % (sys.argv[1:]));  #DEBUG ONLY. REMOVE WHEN FINISHED.
	print("Argument Count: %d" % (len(sys.argv))); #DEBUG ONLY. REMOVE WHEN FINISHED.
	
	i_debug=0;
	while (i_debug < len(sys.argv)):
		#ARGA_LC[${i}]=`printf "%s" ${ARGA[$i]} | tr '[:upper:]' '[:lower:]'`; #Change all uppercase to lowercase.
		print("ARGA[%02d]    = %s" % (i_debug, sys.argv[i_debug]));
		i_debug=( i_debug + 1 );
	#print(""); #END WHILE STATEMENT.
	print("#### END  : Debug. ################################");
	print("\n%s%s%s---------------------------------------------------------------------------%s" % (HEADER_ATTRIB, HEADER_FGCOLR, HEADER_BGCOLR, HEADER_RSTALL));
#print(""); #END IF STATEMENT.

#### Check file name header. ####
# FILE_NAME_HEADER.replace(".py", ".sh")
if ( sys.argv[0].replace("./", "") == FILE_NAME_HEADER ):
	if (Set_DEBUG_Flag == 1):
		print("%s# INFO: File name header matches.%s" % ("\x1b[32m", "\x1b[0m"));
		print("%s%s <=> %s%s"                         % ("\x1b[32m", sys.argv[0].replace("./", ""), FILE_NAME_HEADER, "\x1b[0m"));
		print("\n%s%s%s---------------------------------------------------------------------------%s" % (HEADER_ATTRIB, HEADER_FGCOLR, HEADER_BGCOLR, HEADER_RSTALL));
	#print(""); #END IF STATEMENT.
else:
	print("%s# ERROR: File name header does not match.%s" % ("\x1b[31m", "\x1b[0m"));
	print("%s%s <=> %s%s"                                 % ("\x1b[31m", sys.argv[0].replace("./", ""), FILE_NAME_HEADER, "\x1b[0m"));
	print("\n%s%s%s---------------------------------------------------------------------------%s" % (HEADER_ATTRIB, HEADER_FGCOLR, HEADER_BGCOLR, HEADER_RSTALL));
	ExitStatus0=1;
#print(""); #END IF STATEMENT.

#### Exit status. ####
if (ExitStatus0 == 1):
	print("#### List of arguments and settings: ####");
	print("%caqc100_b10_v1p10)    Set_AQC100_B10_V1P10_Flag=1;    %s" % ("-", "#(AQ TE AQC100-B10 [Atlantic Version 1.10])"));
	print("%caqc107_b10_v1p16)    Set_AQC107_B10_V1P16_Flag=1;    %s" % ("-", "#(AQ TE AQC107-B10 [Jamaica Version 1.16])"));
	print("%caqc111c_b01_v0p25)   Set_AQC111C_B01_V0P25_Flag=1;   %s" % ("-", "#(AQ TE AQC111C-B01 [Bermuda Version 0.25])"));
	print("%cbbic5_b1_r09a)       Set_BBIC5_B1_R09A_Flag=1;       %s" % ("-", "#(QT TE QT10GA-B1 [BBIC5 FT Release 09A])"));
	print("%cbbic5_b1_r10)        Set_BBIC5_B1_R10_Flag=1;        %s" % ("-", "#(QT TE QT10GA-B1 [BBIC5 FT Release 10])"));
	print("%cbbic5_b1_r11)        Set_BBIC5_B1_R11_Flag=1;        %s" % ("-", "#(QT TE QT10GA-B1 [BBIC5 FT Release 11])"));
	print("%cbbic5_b1_r12)        Set_BBIC5_B1_R12_Flag=1;        %s" % ("-", "#(QT TE QT10GA-B1 [BBIC5 FT Release 12])"));
	print("%cbbic5_b1_ws_r01)     Set_BBIC5_B1_WS_R01_Flag=1;     %s" % ("-", "#(QT TE QT10GA-B1 [BBIC5 WS Release 01])"));
	print("%cbbic5_c0_r07)        Set_BBIC5_C0_R07_Flag=1;        %s" % ("-", "#(QT TE QT10GA-C0 [BBIC5 FT Release 07])"));
	print("%cbbic5_d0_r01a)       Set_BBIC5_D0_R01A_Flag=1;       %s" % ("-", "#(QT TE QT10GA-D0 [BBIC5 FT Release 01A])"));
	print("%cbbic6_a0_r01)        Set_BBIC6_A0_R01_Flag=1;        %s" % ("-", "#(QT TE QT10GA-AX2 [BBIC6 FT Release 01])"));
	print("%cpmic_a4_r01)         Set_PMIC_A4_R01_Flag=1;         %s" % ("-", "#(QT TE PMIC-A4 [PMIC FT Release 01])"));
	print("%cpmic_c0_r01)         Set_PMIC_C0_R01_Flag=1;         %s" % ("-", "#(QT TE PMIC-C0 [PMIC FT Release 01])"));
	print("%cpmic_c1_r01)         Set_PMIC_C1_R01_Flag=1;         %s" % ("-", "#(QT TE PMIC-C1 [PMIC FT Release 01])"));
	print("%cx550a_b0_v1p80)      Set_X550A_B0_V1P80_Flag=1;      %s" % ("-", "#(AQ TE X550-AT2-B00 [Sageville 17mm Version 1.80])"));
	print("%crel_x550a_b0)        Set_REL_X550A_B0_Flag=1;        %s" % ("-", "#(Released to Amkor/PE X550-AT2-B00)"));
	print("%cdebug)               Set_DEBUG_Flag=1;"                  % ("-"));
	print("%ctouch_all)           Set_Touch_All_Flag=1;"              % ("-"));
	print("%ch)                   ExitStatus0=1;"                     % ("-"));
	print("%chelp)                ExitStatus0=1;"                     % ("-"));
	print("%c)                    ;"                                  % ("*"));
	
	print("");
	print("%s%s%s# Time EOF : %-53s ########%s" % (HEADER_ATTRIB, HEADER_FGCOLR, HEADER_BGCOLR, time.strftime("%c"), HEADER_RSTALL));
	print("%s%s%s###### END - %-53s ########%s" % (HEADER_ATTRIB, HEADER_FGCOLR, HEADER_BGCOLR, FILE_NAME_HEADER,    HEADER_RSTALL));
	sys.exit(); #(0=Success, 1=Failure).
#print(""); #END IF STATEMENT.

#### Information on OS release. ####
GET_LSB_RELEASE="lsb_release -a";                               #Get Linux Standard Base Release Information.
GET_SMARTEST_VER="/opt/hp93000/soc/prod_env/bin/HPSmarTest -V"; #Get Smartest Version Information.
#### System76 Machine. ####
if   (HOSTNAME == "Bradley-Lemur"       ): print("%s" % (commands.getoutput(GET_LSB_RELEASE))); SYSTEM_TYPE="System76_Lemur (" + commands.getoutput("lsb_release -sd") + ")";    #(7.5.2.02)
elif (HOSTNAME == "system76-pc"         ): print("%s" % (commands.getoutput(GET_LSB_RELEASE))); SYSTEM_TYPE="System76_LemurPro (" + commands.getoutput("lsb_release -sd") + ")"; #(7.5.2.02)
#### Systems at QT HQ. ####
elif (HOSTNAME == "SJ-OPS-BEVERSON"     ): print("%s" % (commands.getoutput(GET_LSB_RELEASE))); SYSTEM_TYPE="Windows_10 (" + commands.getoutput("lsb_release -sd") + ")"; #(7.4.0.02). (IP: 10.10.21.66)
elif (HOSTNAME == "zbjcxm-l1"           ): print("%s" % (commands.getoutput(GET_LSB_RELEASE))); SYSTEM_TYPE="Windows_10 (" + commands.getoutput("lsb_release -sd") + ")"; #(7.4.0.02). (IP: 10.10.21.66)
elif (HOSTNAME == "93koffline01"        ): print("%s" % (commands.getoutput(GET_LSB_RELEASE))); SYSTEM_TYPE="V93K_Offline\n" + commands.getoutput(GET_SMARTEST_VER); #(7.4.0.02). (IP: 10.10.21.17)
elif (HOSTNAME == "93koffline02"        ): print("%s" % (commands.getoutput(GET_LSB_RELEASE))); SYSTEM_TYPE="V93K_Offline\n" + commands.getoutput(GET_SMARTEST_VER); #(7.4.0.02). (IP: 10.10.21.18)
elif (HOSTNAME == "93koffline03"        ): print("%s" % (commands.getoutput(GET_LSB_RELEASE))); SYSTEM_TYPE="V93K_Offline\n" + commands.getoutput(GET_SMARTEST_VER); #(7.4.0.02). (IP: 10.10.21.13)
elif (HOSTNAME == "fm-ops01"            ): print("%s" % (commands.getoutput(GET_LSB_RELEASE))); SYSTEM_TYPE="V93K_Offline\n" + commands.getoutput(GET_SMARTEST_VER); #(7.3.2.10). (IP: 10.10.5.116)
#### Systems at AQ HQ. ####
elif (HOSTNAME == "93K_TESTER_AQ01"     ): print("%s" % (commands.getoutput(GET_LSB_RELEASE))); SYSTEM_TYPE="V93K_Online\n" + commands.getoutput(GET_SMARTEST_VER);  #(7.3.2.10). (IP: 10.10.14.24)
elif (HOSTNAME == "93K_TESTER_HYPR"     ): print("%s" % (commands.getoutput(GET_LSB_RELEASE))); SYSTEM_TYPE="V93K_Online\n" + commands.getoutput(GET_SMARTEST_VER);  #(7.3.2.10). (IP: 10.10.14.6)
elif (HOSTNAME == "93K_OFFLINE_AQ01"    ): print("%s" % (commands.getoutput(GET_LSB_RELEASE))); SYSTEM_TYPE="V93K_Offline\n" + commands.getoutput(GET_SMARTEST_VER); #(7.3.2.10). (IP: 10.10.14.23)
elif (HOSTNAME == "93K_OFFLINE_HYPR"    ): print("%s" % (commands.getoutput(GET_LSB_RELEASE))); SYSTEM_TYPE="V93K_Offline\n" + commands.getoutput(GET_SMARTEST_VER); #(7.3.2.10). (IP: 10.10.14.5)
elif (HOSTNAME == "advantest-vm1"       ): print("%s" % (commands.getoutput(GET_LSB_RELEASE))); SYSTEM_TYPE="V93K_Offline\n" + commands.getoutput(GET_SMARTEST_VER); #(7.3.2.10). (IP: 10.10.14.174)(Server: ops-esxi-01)
elif (HOSTNAME == "advantest-vm2"       ): print("%s" % (commands.getoutput(GET_LSB_RELEASE))); SYSTEM_TYPE="V93K_Offline\n" + commands.getoutput(GET_SMARTEST_VER); #(7.3.2.10). (IP: 10.10.14.172)(Server: ops-esxi-01)
elif (HOSTNAME == "advantest-vm3"       ): print("%s" % (commands.getoutput(GET_LSB_RELEASE))); SYSTEM_TYPE="V93K_Offline\n" + commands.getoutput(GET_SMARTEST_VER); #(7.3.2.10). (IP: 10.10.14.179)(Server: ops-esxi-01)
elif (HOSTNAME == "advantest-vm4"       ): print("%s" % (commands.getoutput(GET_LSB_RELEASE))); SYSTEM_TYPE="V93K_Offline\n" + commands.getoutput(GET_SMARTEST_VER); #(7.3.2.10). (IP: 10.10.14.181)(Server: ops-esxi-01)
elif (HOSTNAME == "advantest-vm5"       ): print("%s" % (commands.getoutput(GET_LSB_RELEASE))); SYSTEM_TYPE="V93K_Offline\n" + commands.getoutput(GET_SMARTEST_VER); #(7.3.2.10). (IP: 10.10.14.8)  (Server: ops-esxi-01)
elif (HOSTNAME == "advantest-vm6"       ): print("%s" % (commands.getoutput(GET_LSB_RELEASE))); SYSTEM_TYPE="V93K_Offline\n" + commands.getoutput(GET_SMARTEST_VER); #(7.3.2.10). (IP: 10.10.14.210)(Server: ops-esxi-01)
elif (HOSTNAME == "linux4.aquantia.com" ): print("%s" % (commands.getoutput(GET_LSB_RELEASE))); SYSTEM_TYPE="V93K_Offline\n" + commands.getoutput(GET_SMARTEST_VER); #(7.1.4.7)
elif (HOSTNAME == "linux15.aquantia.com"): print("%s" % (commands.getoutput(GET_LSB_RELEASE))); SYSTEM_TYPE="V93K_Offline\n" + commands.getoutput(GET_SMARTEST_VER); #(6.3.4.X)
elif (HOSTNAME == "linux19.aquantia.com"): print("%s" % (commands.getoutput(GET_LSB_RELEASE))); SYSTEM_TYPE="V93K_Offline\n" + commands.getoutput(GET_SMARTEST_VER); #(6.5.4.13)
elif (HOSTNAME == "linux60.aquantia.com"): print("%s" % (commands.getoutput(GET_LSB_RELEASE))); SYSTEM_TYPE="VTRAN";
elif (HOSTNAME == "suns1"               ): print("%s" % (commands.getoutput("cat /etc/release"))); SYSTEM_TYPE="Galaxy_Admin";
#### V93K online systems at ISE Labs. ####
elif (HOSTNAME == "PS1"                 ): print("%s" % (commands.getoutput(GET_LSB_RELEASE))); SYSTEM_TYPE="V93K_Online\n" + commands.getoutput(GET_SMARTEST_VER); #(6.5.4.18)
elif (HOSTNAME == "PS1-64"              ): print("%s" % (commands.getoutput(GET_LSB_RELEASE))); SYSTEM_TYPE="V93K_Online\n" + commands.getoutput(GET_SMARTEST_VER); #(7.1.4.X)
elif (HOSTNAME == "PS2"                 ): print("%s" % (commands.getoutput(GET_LSB_RELEASE))); SYSTEM_TYPE="V93K_Online\n" + commands.getoutput(GET_SMARTEST_VER); #(6.5.4.18)
elif (HOSTNAME == "PS2-64"              ): print("%s" % (commands.getoutput(GET_LSB_RELEASE))); SYSTEM_TYPE="V93K_Online\n" + commands.getoutput(GET_SMARTEST_VER); #(7.1.4.X)
elif (HOSTNAME == "PS31"                ): print("%s" % (commands.getoutput(GET_LSB_RELEASE))); SYSTEM_TYPE="V93K_Online\n" + commands.getoutput(GET_SMARTEST_VER); #(6.5.4.18)
elif (HOSTNAME == "PS3"                 ): print("%s" % (commands.getoutput(GET_LSB_RELEASE))); SYSTEM_TYPE="V93K_Online\n" + commands.getoutput(GET_SMARTEST_VER); #(7.1.4.X)
elif (HOSTNAME == "ps4-64"              ): print("%s" % (commands.getoutput(GET_LSB_RELEASE))); SYSTEM_TYPE="V93K_Online\n" + commands.getoutput(GET_SMARTEST_VER); #(7.4.0.02)
elif (HOSTNAME == "ps5-64"              ): print("%s" % (commands.getoutput(GET_LSB_RELEASE))); SYSTEM_TYPE="V93K_Online\n" + commands.getoutput(GET_SMARTEST_VER); #(7.4.0.02)
elif (HOSTNAME == "PS7-64"              ): print("%s" % (commands.getoutput(GET_LSB_RELEASE))); SYSTEM_TYPE="V93K_Online\n" + commands.getoutput(GET_SMARTEST_VER); #(7.4.0.02)
elif (HOSTNAME == "ps10-64"             ): print("%s" % (commands.getoutput(GET_LSB_RELEASE))); SYSTEM_TYPE="V93K_Online\n" + commands.getoutput(GET_SMARTEST_VER); #(7.4.0.02)
elif (HOSTNAME == "PS12-64"             ): print("%s" % (commands.getoutput(GET_LSB_RELEASE))); SYSTEM_TYPE="V93K_Online\n" + commands.getoutput(GET_SMARTEST_VER); #(7.4.0.02)
elif (HOSTNAME == "PS15"                ): print("%s" % (commands.getoutput(GET_LSB_RELEASE))); SYSTEM_TYPE="V93K_Online\n" + commands.getoutput(GET_SMARTEST_VER); #(6.5.4.18)
elif (HOSTNAME == "ps15-64"             ): print("%s" % (commands.getoutput(GET_LSB_RELEASE))); SYSTEM_TYPE="V93K_Online\n" + commands.getoutput(GET_SMARTEST_VER); #(7.4.0.02)
elif (HOSTNAME == "ps16-64"             ): print("%s" % (commands.getoutput(GET_LSB_RELEASE))); SYSTEM_TYPE="V93K_Online\n" + commands.getoutput(GET_SMARTEST_VER); #(7.4.0.02)
#### V93K offline systems at ISE Labs. ####
elif (HOSTNAME == "hp108"               ): print("%s" % (commands.getoutput(GET_LSB_RELEASE))); SYSTEM_TYPE="V93K_Offline\n" + commands.getoutput(GET_SMARTEST_VER); #(6.5.4.18)
elif (HOSTNAME == "hp109"               ): print("%s" % (commands.getoutput(GET_LSB_RELEASE))); SYSTEM_TYPE="V93K_Offline\n" + commands.getoutput(GET_SMARTEST_VER); #(6.5.4.18)
elif (HOSTNAME == "hp110"               ): print("%s" % (commands.getoutput(GET_LSB_RELEASE))); SYSTEM_TYPE="V93K_Offline\n" + commands.getoutput(GET_SMARTEST_VER); #(6.5.4.18)
elif (HOSTNAME == "hp117"               ): print("%s" % (commands.getoutput(GET_LSB_RELEASE))); SYSTEM_TYPE="V93K_Offline\n" + commands.getoutput(GET_SMARTEST_VER); #(6.3.5.X)
elif (HOSTNAME == "hp118"               ): print("%s" % (commands.getoutput(GET_LSB_RELEASE))); SYSTEM_TYPE="V93K_Offline\n" + commands.getoutput(GET_SMARTEST_VER); #(6.5.4.18)
elif (HOSTNAME == "hp207"               ): print("%s" % (commands.getoutput(GET_LSB_RELEASE))); SYSTEM_TYPE="V93K_Offline\n" + commands.getoutput(GET_SMARTEST_VER); #(7.4.0.02)
elif (HOSTNAME == "hp208"               ): print("%s" % (commands.getoutput(GET_LSB_RELEASE))); SYSTEM_TYPE="V93K_Offline\n" + commands.getoutput(GET_SMARTEST_VER); #(7.4.0.02)
elif (HOSTNAME == "hp209"               ): print("%s" % (commands.getoutput(GET_LSB_RELEASE))); SYSTEM_TYPE="V93K_Offline\n" + commands.getoutput(GET_SMARTEST_VER); #(7.4.0.02)
elif (HOSTNAME == "hp210"               ): print("%s" % (commands.getoutput(GET_LSB_RELEASE))); SYSTEM_TYPE="V93K_Offline\n" + commands.getoutput(GET_SMARTEST_VER); #(7.4.0.02)
elif (HOSTNAME == "hp224"               ): print("%s" % (commands.getoutput(GET_LSB_RELEASE))); SYSTEM_TYPE="V93K_Offline\n" + commands.getoutput(GET_SMARTEST_VER); #(7.4.0.02)
elif (HOSTNAME == "hp225"               ): print("%s" % (commands.getoutput(GET_LSB_RELEASE))); SYSTEM_TYPE="V93K_Offline\n" + commands.getoutput(GET_SMARTEST_VER); #(7.4.0.02)
elif (HOSTNAME == "hp226"               ): print("%s" % (commands.getoutput(GET_LSB_RELEASE))); SYSTEM_TYPE="V93K_Offline\n" + commands.getoutput(GET_SMARTEST_VER); #(7.4.0.02)
elif (HOSTNAME == "hp230"               ): print("%s" % (commands.getoutput(GET_LSB_RELEASE))); SYSTEM_TYPE="V93K_Offline\n" + commands.getoutput(GET_SMARTEST_VER); #(7.1.4.X)
elif (HOSTNAME == "hp231"               ): print("%s" % (commands.getoutput(GET_LSB_RELEASE))); SYSTEM_TYPE="V93K_Offline\n" + commands.getoutput(GET_SMARTEST_VER); #(7.1.4.X)
elif (HOSTNAME == "hp233"               ): print("%s" % (commands.getoutput(GET_LSB_RELEASE))); SYSTEM_TYPE="V93K_Offline\n" + commands.getoutput(GET_SMARTEST_VER); #(7.1.4.X)
elif (HOSTNAME == "hp234"               ): print("%s" % (commands.getoutput(GET_LSB_RELEASE))); SYSTEM_TYPE="V93K_Offline\n" + commands.getoutput(GET_SMARTEST_VER); #(7.4.0.02)
elif (HOSTNAME == "hp236"               ): print("%s" % (commands.getoutput(GET_LSB_RELEASE))); SYSTEM_TYPE="V93K_Offline\n" + commands.getoutput(GET_SMARTEST_VER); #(7.4.0.02)
elif (HOSTNAME == "hp240"               ): print("%s" % (commands.getoutput(GET_LSB_RELEASE))); SYSTEM_TYPE="V93K_Offline\n" + commands.getoutput(GET_SMARTEST_VER); #(7.3.2.5)(RHEL 5.8)
elif (HOSTNAME == "hp240-aquantia"      ): print("%s" % (commands.getoutput(GET_LSB_RELEASE))); SYSTEM_TYPE="V93K_Offline\n" + commands.getoutput(GET_SMARTEST_VER); #(7.3.2.5)(RHEL 5.6)
#### V93K online/offline systems at iTest Inc. ####
elif (HOSTNAME == "smartscale01"        ): print("%s" % (commands.getoutput(GET_LSB_RELEASE))); SYSTEM_TYPE="V93K_Online\n" + commands.getoutput(GET_SMARTEST_VER);  #(7.4.0.02)
elif (HOSTNAME == "smartscale02"        ): print("%s" % (commands.getoutput(GET_LSB_RELEASE))); SYSTEM_TYPE="V93K_Online\n" + commands.getoutput(GET_SMARTEST_VER);  #(7.4.0.02)
elif (HOSTNAME == "smartscale03"        ): print("%s" % (commands.getoutput(GET_LSB_RELEASE))); SYSTEM_TYPE="V93K_Online\n" + commands.getoutput(GET_SMARTEST_VER);  #(7.4.0.02)
elif (HOSTNAME == "smartscale04"        ): print("%s" % (commands.getoutput(GET_LSB_RELEASE))); SYSTEM_TYPE="V93K_Online\n" + commands.getoutput(GET_SMARTEST_VER);  #(7.4.0.02)
elif (HOSTNAME == "smartscale05"        ): print("%s" % (commands.getoutput(GET_LSB_RELEASE))); SYSTEM_TYPE="V93K_Online\n" + commands.getoutput(GET_SMARTEST_VER);  #(7.4.0.02)
elif (HOSTNAME == "smartscale06"        ): print("%s" % (commands.getoutput(GET_LSB_RELEASE))); SYSTEM_TYPE="V93K_Online\n" + commands.getoutput(GET_SMARTEST_VER);  #(7.4.0.02)
elif (HOSTNAME == "smartscale07"        ): print("%s" % (commands.getoutput(GET_LSB_RELEASE))); SYSTEM_TYPE="V93K_Online\n" + commands.getoutput(GET_SMARTEST_VER);  #(7.4.0.02)
elif (HOSTNAME == "smartscale08"        ): print("%s" % (commands.getoutput(GET_LSB_RELEASE))); SYSTEM_TYPE="V93K_Online\n" + commands.getoutput(GET_SMARTEST_VER);  #(7.4.0.02)
elif (HOSTNAME == "offline1"            ): print("%s" % (commands.getoutput(GET_LSB_RELEASE))); SYSTEM_TYPE="V93K_Offline\n" + commands.getoutput(GET_SMARTEST_VER); #(7.4.0.02)
elif (HOSTNAME == "offline2"            ): print("%s" % (commands.getoutput(GET_LSB_RELEASE))); SYSTEM_TYPE="V93K_Offline\n" + commands.getoutput(GET_SMARTEST_VER); #(7.4.0.02)
elif (HOSTNAME == "offline3"            ): print("%s" % (commands.getoutput(GET_LSB_RELEASE))); SYSTEM_TYPE="V93K_Offline\n" + commands.getoutput(GET_SMARTEST_VER); #(7.4.0.02)
elif (HOSTNAME == "offline4"            ): print("%s" % (commands.getoutput(GET_LSB_RELEASE))); SYSTEM_TYPE="V93K_Offline\n" + commands.getoutput(GET_SMARTEST_VER); #(7.4.0.02)
elif (HOSTNAME == "offline5"            ): print("%s" % (commands.getoutput(GET_LSB_RELEASE))); SYSTEM_TYPE="V93K_Offline\n" + commands.getoutput(GET_SMARTEST_VER); #(7.4.0.02)
elif (HOSTNAME == "offline10"           ): print("%s" % (commands.getoutput(GET_LSB_RELEASE))); SYSTEM_TYPE="V93K_Offline\n" + commands.getoutput(GET_SMARTEST_VER); #(7.4.0.02)
elif (HOSTNAME == "offline11"           ): print("%s" % (commands.getoutput(GET_LSB_RELEASE))); SYSTEM_TYPE="V93K_Offline\n" + commands.getoutput(GET_SMARTEST_VER); #(7.4.0.02)
elif (HOSTNAME == "offline13"           ): print("%s" % (commands.getoutput(GET_LSB_RELEASE))); SYSTEM_TYPE="V93K_Offline\n" + commands.getoutput(GET_SMARTEST_VER); #(7.4.0.02)
elif (HOSTNAME == "offline15"           ): print("%s" % (commands.getoutput(GET_LSB_RELEASE))); SYSTEM_TYPE="V93K_Offline\n" + commands.getoutput(GET_SMARTEST_VER); #(7.4.0.02)
elif (HOSTNAME == "offline16"           ): print("%s" % (commands.getoutput(GET_LSB_RELEASE))); SYSTEM_TYPE="V93K_Offline\n" + commands.getoutput(GET_SMARTEST_VER); #(7.4.0.02)
#### V93K online systems at EAG. ####
elif (HOSTNAME == "klondike"            ): print("%s" % (commands.getoutput(GET_LSB_RELEASE))); SYSTEM_TYPE="V93K_Online\n" + commands.getoutput(GET_SMARTEST_VER); #(6.5.4.18)
#### V93K offline systems at EAG. ####
elif (HOSTNAME == "linsim02"            ): print("%s" % (commands.getoutput(GET_LSB_RELEASE))); SYSTEM_TYPE="V93K_Online\n" + commands.getoutput(GET_SMARTEST_VER); #(6.5.4.18)
else:                                      print("Not available.");                             SYSTEM_TYPE="Not available.";
#print(""); #END IF STATEMENT.
print("\n%s%s%s---------------------------------------------------------------------------%s" % (HEADER_ATTRIB, HEADER_FGCOLR, HEADER_BGCOLR, HEADER_RSTALL));
print("SYSTEM_TYPE = %s" % (SYSTEM_TYPE));

#### Device in use setup. Define device in use file name and path. ####
DEV_USED_DEFAULT=".device_inuse_soc";                                                               #Default device inuse. All users.
DEV_USED_AQC100=".device_inuse_soc.AQC100_DEV";                                                     #AQC100-A00, AQC100-B00 (Atlantic).
DEV_USED_AQC107=".device_inuse_soc.AQC107_DEV";                                                     #AQC107-A00, AQC107-B00 (Jamaica).
DEV_USED_AQC111C=".device_inuse_soc.AQC111C_DEV";                                                   #AQC111C-A00, AQC111C-B00 (Bermuda).
DEV_USED_BBIC5=".device_inuse_soc.BBIC5_DEV";                                                       #QT10GA-B1,QT10GS-B1,QT10GT-B1,QT10GU-B1,QT10GA-C0,QT10GS-C0,QT10GT-C0,QT10GU-C0,QT10GA-D0,QT10GS-D0,QT10GT-D0,QT10GU-D0 (BBIC5).
DEV_USED_BBIC6=".device_inuse_soc.BBIC6_DEV";                                                       #QT10GA-AX2,QT10GS-AX2,QT10GT-AX2,QT10GU-AX2 (BBIC6).
DEV_USED_PMIC=".device_inuse_soc.PMIC_DEV";                                                         #PMIC-A4 (PMIC).
DEV_USED_X550A=".device_inuse_soc.X550A_DEV";                                                       #X550-AT2-B00 (Sageville 17mm).
DEV_USED_REL_X550A=".device_inuse_soc.REL_X550A_DEV";                                               #Released to Amkor/PE X550-AT2.

DEV_PATH_AQC100_B10_V1P10="projects/proj_Atlantic/AQC100_B10_V1P10/AQC100_DEV/waste";               #AQC100-B10 (Atlantic Version 1.10).
DEV_PATH_AQC107_B10_V1P16="projects/proj_Jamaica/AQC107_B10_V1P16/AQC107_DEV/waste";                #AQC107-B10 (Jamaica Version 1.16).
DEV_PATH_AQC111C_B01_V0P25="projects/proj_Bermuda/AQC111C_B01_V0P25/AQC111C_DEV/waste";             #AQC111C-B01 (Bermuda Version 0.25).
DEV_PATH_BBIC5_B1_R09A="devices/BBIC5/B1/BBIC5_B1_R09A/BBIC5_DEV/waste";                            #QT10GA-B1,QT10GS-B1,QT10GT-B1,QT10GU-B1 (BBIC5 Release 09A).
DEV_PATH_BBIC5_B1_R10="devices/BBIC5/B1/BBIC5_B1_R10/BBIC5_DEV/waste";                              #QT10GA-B1,QT10GS-B1,QT10GT-B1,QT10GU-B1 (BBIC5 Release 10).
DEV_PATH_BBIC5_B1_R11="devices/BBIC5/B1/BBIC5_B1_R11/BBIC5_DEV/waste";                              #QT10GA-B1,QT10GS-B1,QT10GT-B1,QT10GU-B1 (BBIC5 Release 11).
DEV_PATH_BBIC5_B1_R12="devices/BBIC5/B1/BBIC5_B1_R12/BBIC5_DEV/waste";                              #QT10GA-B1,QT10GS-B1,QT10GT-B1,QT10GU-B1 (BBIC5 Release 12).
DEV_PATH_BBIC5_B1_WS_R01="devices/BBIC5/B1/BBIC5_B1_WS_R01/BBIC5_DEV/waste";                        #QT10GA-B1,QT10GS-B1,QT10GT-B1,QT10GU-B1 (BBIC5 WS Release 01).
DEV_PATH_BBIC5_C0_R07="devices/BBIC5/C0/BBIC5_C0_R07/BBIC5_DEV/waste";                              #QT10GA-C0,QT10GS-C0,QT10GT-C0,QT10GU-C0 (BBIC5 Release 07).
DEV_PATH_BBIC5_D0_R01A="devices/BBIC5/D0/BBIC5_D0_R01A/BBIC5_DEV/waste";                            #QT10GA-D0,QT10GS-D0,QT10GT-D0,QT10GU-D0 (BBIC5 Release 01A).
DEV_PATH_BBIC6_A0_R01="devices/BBIC6/A0/BBIC6_A0_R01/BBIC6_DEV/waste";                              #QT10GA-AX2,QT10GS-AX2,QT10GT-AX2,QT10GU-AX2 (BBIC6 Release 01).
DEV_PATH_PMIC_A4_R01="devices/PMIC/A4/PMIC_A4_R01/PMIC_DEV/waste";                                  #PMIC-A4 (PMIC Release 01).
DEV_PATH_PMIC_C0_R01="devices/PMIC/C0/PMIC_C0_R01/PMIC_DEV/waste";                                  #PMIC-C0 (PMIC Release 01).
DEV_PATH_PMIC_C1_R01="devices/PMIC/C1/PMIC_C1_R01/PMIC_DEV/waste";                                  #PMIC-C1 (PMIC Release 01).
DEV_PATH_X550A_B0_V1P80="projects/proj_Sageville/X550A_B0_V1P80/X550A_DEV/waste";                   #X550-AT2-B00 (Sageville 17mm Version 1.80).
DEV_PATH_REL_X550A_B0="projects/proj_Sageville/REL_AMKOR/REL_X550A_TO_AMKOR_DIR";                   #Released to Amkor/PE X550-AT2-B00.

if (len(sys.argv) == 1):
	print("\n%s%s%s---------------------------------------------------------------------------%s" % (HEADER_ATTRIB, HEADER_FGCOLR, HEADER_BGCOLR, HEADER_RSTALL));
	if (os.path.isfile(DEV_USED_DEFAULT)):
		SED1LINE=commands.getoutput("sed -n '1 p' < %s" % (DEV_USED_DEFAULT));
		if (os.path.isdir(SED1LINE)):
			print("Current Path = %s   (%s%s%s)\n" % (SED1LINE, "\x1b[32m", "Exists", "\x1b[0m"));
		else:
			print("Current Path = %s   (%s%s%s)\n" % (SED1LINE, "\x1b[31m", "Doesn't exists", "\x1b[0m"));
		#print(""); #END IF STATEMENT.
	else:
		print("%s   (%s%s%s)\n" % (DEV_USED_DEFAULT, "\x1b[31m", "Doesn't exists", "\x1b[0m"));
	#print(""); #END IF STATEMENT.
elif (Set_AQC100_B10_V1P10_Flag == 1) and (len(sys.argv) == 2):
	print("\n%s%s%s---------------------------------------------------------------------------%s" % (HEADER_ATTRIB, HEADER_FGCOLR, HEADER_BGCOLR, HEADER_RSTALL));
	print("Device = %-30s %3s %s" % ("AQC100", "", "(Atlantic 7mm*11mm B10)"));
	DEV_USED_STRING=(os.environ["HOME"] + '/' + DEV_PATH_AQC100_B10_V1P10 + '\n');
	os.remove(DEV_USED_AQC100);
	FILE_DES=os.open(DEV_USED_AQC100, os.O_RDWR|os.O_CREAT);
	FILE_RET=os.write(FILE_DES, DEV_USED_STRING);
	os.close(FILE_DES);
	os.chmod(DEV_USED_AQC100, 0664);
	
	print("FILE_DES = %s" % (FILE_DES));
	print("FILE_RET = %d" % (FILE_RET));
	
	shutil.copy(DEV_USED_AQC100, DEV_USED_DEFAULT);
	shutil.copy(DEV_USED_AQC100, DEV_USED_DEFAULT+"@"+HOSTNAME);
	SED1LINE=commands.getoutput("sed -n '1 p' < %s" % (DEV_USED_DEFAULT));
	if (os.path.isdir(SED1LINE)):
		print("Current Path = %s   (%s%s%s)\n" % (SED1LINE, "\x1b[32m", "Exists", "\x1b[0m"));
	else:
		print("Current Path = %s   (%s%s%s)\n" % (SED1LINE, "\x1b[31m", "Doesn't exists", "\x1b[0m"));
	#print(""); #END IF STATEMENT.
elif (Set_AQC107_B10_V1P16_Flag == 1) and (len(sys.argv) == 2):
	print("\n%s%s%s---------------------------------------------------------------------------%s" % (HEADER_ATTRIB, HEADER_FGCOLR, HEADER_BGCOLR, HEADER_RSTALL));
	print("Device = %-30s %3s %s" % ("AQC107", "", "(Jamaica 12mm*14mm B10)"));
	DEV_USED_STRING=(os.environ["HOME"] + '/' + DEV_PATH_AQC107_B10_V1P16 + '\n');
	os.remove(DEV_USED_AQC107);
	FILE_DES=os.open(DEV_USED_AQC107, os.O_RDWR|os.O_CREAT);
	FILE_RET=os.write(FILE_DES, DEV_USED_STRING);
	os.close(FILE_DES);
	os.chmod(DEV_USED_AQC107, 0664);
	
	print("FILE_DES = %s" % (FILE_DES));
	print("FILE_RET = %d" % (FILE_RET));
	
	shutil.copy(DEV_USED_AQC107, DEV_USED_DEFAULT);
	shutil.copy(DEV_USED_AQC107, DEV_USED_DEFAULT+"@"+HOSTNAME);
	SED1LINE=commands.getoutput("sed -n '1 p' < %s" % (DEV_USED_DEFAULT));
	if (os.path.isdir(SED1LINE)):
		print("Current Path = %s   (%s%s%s)\n" % (SED1LINE, "\x1b[32m", "Exists", "\x1b[0m"));
	else:
		print("Current Path = %s   (%s%s%s)\n" % (SED1LINE, "\x1b[31m", "Doesn't exists", "\x1b[0m"));
	#print(""); #END IF STATEMENT.
elif (Set_AQC111C_B01_V0P25_Flag == 1) and (len(sys.argv) == 2):
	print("\n%s%s%s---------------------------------------------------------------------------%s" % (HEADER_ATTRIB, HEADER_FGCOLR, HEADER_BGCOLR, HEADER_RSTALL));
	print("Device = %-30s %3s %s" % ("AQC111C", "", "(Bermuda 9mm*9mm B01)"));
	DEV_USED_STRING=(os.environ["HOME"] + '/' + DEV_PATH_AQC111C_B01_V0P25 + '\n');
	os.remove(DEV_USED_AQC111C);
	FILE_DES=os.open(DEV_USED_AQC111C, os.O_RDWR|os.O_CREAT);
	FILE_RET=os.write(FILE_DES, DEV_USED_STRING);
	os.close(FILE_DES);
	os.chmod(DEV_USED_AQC111C, 0664);
	
	print("FILE_DES = %s" % (FILE_DES));
	print("FILE_RET = %d" % (FILE_RET));
	
	shutil.copy(DEV_USED_AQC111C, DEV_USED_DEFAULT);
	shutil.copy(DEV_USED_AQC111C, DEV_USED_DEFAULT+"@"+HOSTNAME);
	SED1LINE=commands.getoutput("sed -n '1 p' < %s" % (DEV_USED_DEFAULT));
	if (os.path.isdir(SED1LINE)):
		print("Current Path = %s   (%s%s%s)\n" % (SED1LINE, "\x1b[32m", "Exists", "\x1b[0m"));
	else:
		print("Current Path = %s   (%s%s%s)\n" % (SED1LINE, "\x1b[31m", "Doesn't exists", "\x1b[0m"));
	#print(""); #END IF STATEMENT.
elif (Set_BBIC5_B1_R09A_Flag == 1) and (len(sys.argv) == 2):
	print("\n%s%s%s---------------------------------------------------------------------------%s" % (HEADER_ATTRIB, HEADER_FGCOLR, HEADER_BGCOLR, HEADER_RSTALL));
	print("Device = %-30s %3s %s" % ("QT10GA", "", "(BBIC5 17mm X 17mm B1)"));
	DEV_USED_STRING=(os.environ["HOME"] + '/' + DEV_PATH_BBIC5_B1_R09A + '\n');
	os.remove(DEV_USED_BBIC5);
	FILE_DES=os.open(DEV_USED_BBIC5, os.O_RDWR|os.O_CREAT);
	FILE_RET=os.write(FILE_DES, DEV_USED_STRING);
	os.close(FILE_DES);
	os.chmod(DEV_USED_BBIC5, 0664);
	
	print("FILE_DES = %s" % (FILE_DES));
	print("FILE_RET = %d" % (FILE_RET));
	
	shutil.copy(DEV_USED_BBIC5, DEV_USED_DEFAULT);
	shutil.copy(DEV_USED_BBIC5, DEV_USED_DEFAULT+"@"+HOSTNAME);
	SED1LINE=commands.getoutput("sed -n '1 p' < %s" % (DEV_USED_DEFAULT));
	if (os.path.isdir(SED1LINE)):
		print("Current Path = %s   (%s%s%s)\n" % (SED1LINE, "\x1b[32m", "Exists", "\x1b[0m"));
	else:
		print("Current Path = %s   (%s%s%s)\n" % (SED1LINE, "\x1b[31m", "Doesn't exists", "\x1b[0m"));
	#print(""); #END IF STATEMENT.
elif (Set_BBIC5_B1_R10_Flag == 1) and (len(sys.argv) == 2):
	print("\n%s%s%s---------------------------------------------------------------------------%s" % (HEADER_ATTRIB, HEADER_FGCOLR, HEADER_BGCOLR, HEADER_RSTALL));
	print("Device = %-30s %3s %s" % ("QT10GA", "", "(BBIC5 17mm X 17mm B1)"));
	DEV_USED_STRING=(os.environ["HOME"] + '/' + DEV_PATH_BBIC5_B1_R10 + '\n');
	os.remove(DEV_USED_BBIC5);
	FILE_DES=os.open(DEV_USED_BBIC5, os.O_RDWR|os.O_CREAT);
	FILE_RET=os.write(FILE_DES, DEV_USED_STRING);
	os.close(FILE_DES);
	os.chmod(DEV_USED_BBIC5, 0664);
	
	print("FILE_DES = %s" % (FILE_DES));
	print("FILE_RET = %d" % (FILE_RET));
	
	shutil.copy(DEV_USED_BBIC5, DEV_USED_DEFAULT);
	shutil.copy(DEV_USED_BBIC5, DEV_USED_DEFAULT+"@"+HOSTNAME);
	SED1LINE=commands.getoutput("sed -n '1 p' < %s" % (DEV_USED_DEFAULT));
	if (os.path.isdir(SED1LINE)):
		print("Current Path = %s   (%s%s%s)\n" % (SED1LINE, "\x1b[32m", "Exists", "\x1b[0m"));
	else:
		print("Current Path = %s   (%s%s%s)\n" % (SED1LINE, "\x1b[31m", "Doesn't exists", "\x1b[0m"));
	#print(""); #END IF STATEMENT.
elif (Set_BBIC5_B1_R11_Flag == 1) and (len(sys.argv) == 2):
	print("\n%s%s%s---------------------------------------------------------------------------%s" % (HEADER_ATTRIB, HEADER_FGCOLR, HEADER_BGCOLR, HEADER_RSTALL));
	print("Device = %-30s %3s %s" % ("QT10GA", "", "(BBIC5 17mm X 17mm B1)"));
	DEV_USED_STRING=(os.environ["HOME"] + '/' + DEV_PATH_BBIC5_B1_R11 + '\n');
	os.remove(DEV_USED_BBIC5);
	FILE_DES=os.open(DEV_USED_BBIC5, os.O_RDWR|os.O_CREAT);
	FILE_RET=os.write(FILE_DES, DEV_USED_STRING);
	os.close(FILE_DES);
	os.chmod(DEV_USED_BBIC5, 0664);
	
	print("FILE_DES = %s" % (FILE_DES));
	print("FILE_RET = %d" % (FILE_RET));
	
	shutil.copy(DEV_USED_BBIC5, DEV_USED_DEFAULT);
	shutil.copy(DEV_USED_BBIC5, DEV_USED_DEFAULT+"@"+HOSTNAME);
	SED1LINE=commands.getoutput("sed -n '1 p' < %s" % (DEV_USED_DEFAULT));
	if (os.path.isdir(SED1LINE)):
		print("Current Path = %s   (%s%s%s)\n" % (SED1LINE, "\x1b[32m", "Exists", "\x1b[0m"));
	else:
		print("Current Path = %s   (%s%s%s)\n" % (SED1LINE, "\x1b[31m", "Doesn't exists", "\x1b[0m"));
	#print(""); #END IF STATEMENT.
elif (Set_BBIC5_B1_R12_Flag == 1) and (len(sys.argv) == 2):
	print("\n%s%s%s---------------------------------------------------------------------------%s" % (HEADER_ATTRIB, HEADER_FGCOLR, HEADER_BGCOLR, HEADER_RSTALL));
	print("Device = %-30s %3s %s" % ("QT10GA", "", "(BBIC5 17mm X 17mm B1)"));
	DEV_USED_STRING=(os.environ["HOME"] + '/' + DEV_PATH_BBIC5_B1_R12 + '\n');
	os.remove(DEV_USED_BBIC5);
	FILE_DES=os.open(DEV_USED_BBIC5, os.O_RDWR|os.O_CREAT);
	FILE_RET=os.write(FILE_DES, DEV_USED_STRING);
	os.close(FILE_DES);
	os.chmod(DEV_USED_BBIC5, 0664);
	
	print("FILE_DES = %s" % (FILE_DES));
	print("FILE_RET = %d" % (FILE_RET));
	
	shutil.copy(DEV_USED_BBIC5, DEV_USED_DEFAULT);
	shutil.copy(DEV_USED_BBIC5, DEV_USED_DEFAULT+"@"+HOSTNAME);
	SED1LINE=commands.getoutput("sed -n '1 p' < %s" % (DEV_USED_DEFAULT));
	if (os.path.isdir(SED1LINE)):
		print("Current Path = %s   (%s%s%s)\n" % (SED1LINE, "\x1b[32m", "Exists", "\x1b[0m"));
	else:
		print("Current Path = %s   (%s%s%s)\n" % (SED1LINE, "\x1b[31m", "Doesn't exists", "\x1b[0m"));
	#print(""); #END IF STATEMENT.
elif (Set_BBIC5_B1_WS_R01_Flag == 1) and (len(sys.argv) == 2):
	print("\n%s%s%s---------------------------------------------------------------------------%s" % (HEADER_ATTRIB, HEADER_FGCOLR, HEADER_BGCOLR, HEADER_RSTALL));
	print("Device = %-30s %3s %s" % ("BBIC5", "", "(BBIC5 17mm X 17mm B1 Wafer-Sort)"));
	DEV_USED_STRING=(os.environ["HOME"] + '/' + DEV_PATH_BBIC5_B1_WS_R01 + '\n');
	os.remove(DEV_USED_BBIC5);
	FILE_DES=os.open(DEV_USED_BBIC5, os.O_RDWR|os.O_CREAT);
	FILE_RET=os.write(FILE_DES, DEV_USED_STRING);
	os.close(FILE_DES);
	os.chmod(DEV_USED_BBIC5, 0664);
	
	print("FILE_DES = %s" % (FILE_DES));
	print("FILE_RET = %d" % (FILE_RET));
	
	shutil.copy(DEV_USED_BBIC5, DEV_USED_DEFAULT);
	shutil.copy(DEV_USED_BBIC5, DEV_USED_DEFAULT+"@"+HOSTNAME);
	SED1LINE=commands.getoutput("sed -n '1 p' < %s" % (DEV_USED_DEFAULT));
	if (os.path.isdir(SED1LINE)):
		print("Current Path = %s   (%s%s%s)\n" % (SED1LINE, "\x1b[32m", "Exists", "\x1b[0m"));
	else:
		print("Current Path = %s   (%s%s%s)\n" % (SED1LINE, "\x1b[31m", "Doesn't exists", "\x1b[0m"));
	#print(""); #END IF STATEMENT.
elif (Set_BBIC5_C0_R07_Flag == 1) and (len(sys.argv) == 2):
	print("\n%s%s%s---------------------------------------------------------------------------%s" % (HEADER_ATTRIB, HEADER_FGCOLR, HEADER_BGCOLR, HEADER_RSTALL));
	print("Device = %-30s %3s %s" % ("QT10GA", "", "(BBIC5 17mm X 17mm C0)"));
	DEV_USED_STRING=(os.environ["HOME"] + '/' + DEV_PATH_BBIC5_C0_R07 + '\n');
	os.remove(DEV_USED_BBIC5);
	FILE_DES=os.open(DEV_USED_BBIC5, os.O_RDWR|os.O_CREAT);
	FILE_RET=os.write(FILE_DES, DEV_USED_STRING);
	os.close(FILE_DES);
	os.chmod(DEV_USED_BBIC5, 0664);
	
	print("FILE_DES = %s" % (FILE_DES));
	print("FILE_RET = %d" % (FILE_RET));
	
	shutil.copy(DEV_USED_BBIC5, DEV_USED_DEFAULT);
	shutil.copy(DEV_USED_BBIC5, DEV_USED_DEFAULT+"@"+HOSTNAME);
	SED1LINE=commands.getoutput("sed -n '1 p' < %s" % (DEV_USED_DEFAULT));
	if (os.path.isdir(SED1LINE)):
		print("Current Path = %s   (%s%s%s)\n" % (SED1LINE, "\x1b[32m", "Exists", "\x1b[0m"));
	else:
		print("Current Path = %s   (%s%s%s)\n" % (SED1LINE, "\x1b[31m", "Doesn't exists", "\x1b[0m"));
	#print(""); #END IF STATEMENT.
elif (Set_BBIC5_D0_R01A_Flag == 1) and (len(sys.argv) == 2):
	print("\n%s%s%s---------------------------------------------------------------------------%s" % (HEADER_ATTRIB, HEADER_FGCOLR, HEADER_BGCOLR, HEADER_RSTALL));
	print("Device = %-30s %3s %s" % ("QT10GA/QT10GS/QT10GT/QT10GU", "", "(BBIC5 17mm X 17mm D0)"));
	DEV_USED_STRING=(os.environ["HOME"] + '/' + DEV_PATH_BBIC5_D0_R01A + '\n');
	os.remove(DEV_USED_BBIC5);
	FILE_DES=os.open(DEV_USED_BBIC5, os.O_RDWR|os.O_CREAT);
	FILE_RET=os.write(FILE_DES, DEV_USED_STRING);
	os.close(FILE_DES);
	os.chmod(DEV_USED_BBIC5, 0664);
	
	print("FILE_DES = %s" % (FILE_DES));
	print("FILE_RET = %d" % (FILE_RET));
	
	shutil.copy(DEV_USED_BBIC5, DEV_USED_DEFAULT);
	shutil.copy(DEV_USED_BBIC5, DEV_USED_DEFAULT+"@"+HOSTNAME);
	SED1LINE=commands.getoutput("sed -n '1 p' < %s" % (DEV_USED_DEFAULT));
	if (os.path.isdir(SED1LINE)):
		print("Current Path = %s   (%s%s%s)\n" % (SED1LINE, "\x1b[32m", "Exists", "\x1b[0m"));
	else:
		print("Current Path = %s   (%s%s%s)\n" % (SED1LINE, "\x1b[31m", "Doesn't exists", "\x1b[0m"));
	#print(""); #END IF STATEMENT.
elif (Set_BBIC6_A0_R01_Flag == 1) and (len(sys.argv) == 2):
	print("\n%s%s%s---------------------------------------------------------------------------%s" % (HEADER_ATTRIB, HEADER_FGCOLR, HEADER_BGCOLR, HEADER_RSTALL));
	print("Device = %-30s %3s %s" % ("QT10GA-AX2/QT10GS-AX2/QT10GT-AX2/QT10GU-AX2", "", "(BBIC6 17mm X 17mm A0)"));
	DEV_USED_STRING=(os.environ["HOME"] + '/' + DEV_PATH_BBIC6_A0_R01 + '\n');
	os.remove(DEV_USED_BBIC6);
	FILE_DES=os.open(DEV_USED_BBIC6, os.O_RDWR|os.O_CREAT);
	FILE_RET=os.write(FILE_DES, DEV_USED_STRING);
	os.close(FILE_DES);
	os.chmod(DEV_USED_BBIC6, 0664);
	
	print("FILE_DES = %s" % (FILE_DES));
	print("FILE_RET = %d" % (FILE_RET));
	
	shutil.copy(DEV_USED_BBIC6, DEV_USED_DEFAULT);
	shutil.copy(DEV_USED_BBIC6, DEV_USED_DEFAULT+"@"+HOSTNAME);
	SED1LINE=commands.getoutput("sed -n '1 p' < %s" % (DEV_USED_DEFAULT));
	if (os.path.isdir(SED1LINE)):
		print("Current Path = %s   (%s%s%s)\n" % (SED1LINE, "\x1b[32m", "Exists", "\x1b[0m"));
	else:
		print("Current Path = %s   (%s%s%s)\n" % (SED1LINE, "\x1b[31m", "Doesn't exists", "\x1b[0m"));
	#print(""); #END IF STATEMENT.
elif (Set_PMIC_A4_R01_Flag == 1) and (len(sys.argv) == 2):
	print("\n%s%s%s---------------------------------------------------------------------------%s" % (HEADER_ATTRIB, HEADER_FGCOLR, HEADER_BGCOLR, HEADER_RSTALL));
	print("Device = %-30s %3s %s" % ("PMIC", "", "(PMIC 7mm X 6mm A4)"));
	DEV_USED_STRING=(os.environ["HOME"] + '/' + DEV_PATH_PMIC_A4_R01 + '\n');
	os.remove(DEV_USED_PMIC);
	FILE_DES=os.open(DEV_USED_PMIC, os.O_RDWR|os.O_CREAT);
	FILE_RET=os.write(FILE_DES, DEV_USED_STRING);
	os.close(FILE_DES);
	os.chmod(DEV_USED_PMIC, 0664);
	
	print("FILE_DES = %s" % (FILE_DES));
	print("FILE_RET = %d" % (FILE_RET));
	
	shutil.copy(DEV_USED_PMIC, DEV_USED_DEFAULT);
	shutil.copy(DEV_USED_PMIC, DEV_USED_DEFAULT+"@"+HOSTNAME);
	SED1LINE=commands.getoutput("sed -n '1 p' < %s" % (DEV_USED_DEFAULT));
	if (os.path.isdir(SED1LINE)):
		print("Current Path = %s   (%s%s%s)\n" % (SED1LINE, "\x1b[32m", "Exists", "\x1b[0m"));
	else:
		print("Current Path = %s   (%s%s%s)\n" % (SED1LINE, "\x1b[31m", "Doesn't exists", "\x1b[0m"));
	#print(""); #END IF STATEMENT.
elif (Set_PMIC_C0_R01_Flag == 1) and (len(sys.argv) == 2):
	print("\n%s%s%s---------------------------------------------------------------------------%s" % (HEADER_ATTRIB, HEADER_FGCOLR, HEADER_BGCOLR, HEADER_RSTALL));
	print("Device = %-30s %3s %s" % ("PMIC", "", "(PMIC 7mm X 6mm C0)"));
	DEV_USED_STRING=(os.environ["HOME"] + '/' + DEV_PATH_PMIC_C0_R01 + '\n');
	os.remove(DEV_USED_PMIC);
	FILE_DES=os.open(DEV_USED_PMIC, os.O_RDWR|os.O_CREAT);
	FILE_RET=os.write(FILE_DES, DEV_USED_STRING);
	os.close(FILE_DES);
	os.chmod(DEV_USED_PMIC, 0664);
	
	print("FILE_DES = %s" % (FILE_DES));
	print("FILE_RET = %d" % (FILE_RET));
	
	shutil.copy(DEV_USED_PMIC, DEV_USED_DEFAULT);
	shutil.copy(DEV_USED_PMIC, DEV_USED_DEFAULT+"@"+HOSTNAME);
	SED1LINE=commands.getoutput("sed -n '1 p' < %s" % (DEV_USED_DEFAULT));
	if (os.path.isdir(SED1LINE)):
		print("Current Path = %s   (%s%s%s)\n" % (SED1LINE, "\x1b[32m", "Exists", "\x1b[0m"));
	else:
		print("Current Path = %s   (%s%s%s)\n" % (SED1LINE, "\x1b[31m", "Doesn't exists", "\x1b[0m"));
	#print(""); #END IF STATEMENT.
elif (Set_PMIC_C1_R01_Flag == 1) and (len(sys.argv) == 2):
	print("\n%s%s%s---------------------------------------------------------------------------%s" % (HEADER_ATTRIB, HEADER_FGCOLR, HEADER_BGCOLR, HEADER_RSTALL));
	print("Device = %-30s %3s %s" % ("PMIC", "", "(PMIC 7mm X 6mm C1)"));
	DEV_USED_STRING=(os.environ["HOME"] + '/' + DEV_PATH_PMIC_C1_R01 + '\n');
	os.remove(DEV_USED_PMIC);
	FILE_DES=os.open(DEV_USED_PMIC, os.O_RDWR|os.O_CREAT);
	FILE_RET=os.write(FILE_DES, DEV_USED_STRING);
	os.close(FILE_DES);
	os.chmod(DEV_USED_PMIC, 0664);
	
	print("FILE_DES = %s" % (FILE_DES));
	print("FILE_RET = %d" % (FILE_RET));
	
	shutil.copy(DEV_USED_PMIC, DEV_USED_DEFAULT);
	shutil.copy(DEV_USED_PMIC, DEV_USED_DEFAULT+"@"+HOSTNAME);
	SED1LINE=commands.getoutput("sed -n '1 p' < %s" % (DEV_USED_DEFAULT));
	if (os.path.isdir(SED1LINE)):
		print("Current Path = %s   (%s%s%s)\n" % (SED1LINE, "\x1b[32m", "Exists", "\x1b[0m"));
	else:
		print("Current Path = %s   (%s%s%s)\n" % (SED1LINE, "\x1b[31m", "Doesn't exists", "\x1b[0m"));
	#print(""); #END IF STATEMENT.
elif (Set_X550A_B0_V1P80_Flag == 1) and (len(sys.argv) == 2):
	print("\n%s%s%s---------------------------------------------------------------------------%s" % (HEADER_ATTRIB, HEADER_FGCOLR, HEADER_BGCOLR, HEADER_RSTALL));
	print("Device = %-30s %3s %s" % ("X550-AT2-B00", "", "(Sageville 17mm*17mm B00)"));
	DEV_USED_STRING=(os.environ["HOME"] + '/' + DEV_PATH_X550A_B0_V1P80 + '\n');
	os.remove(DEV_USED_X550A);
	FILE_DES=os.open(DEV_USED_X550A, os.O_RDWR|os.O_CREAT);
	FILE_RET=os.write(FILE_DES, DEV_USED_STRING);
	os.close(FILE_DES);
	os.chmod(DEV_USED_X550A, 0664);
	
	print("FILE_DES = %s" % (FILE_DES));
	print("FILE_RET = %d" % (FILE_RET));
	
	shutil.copy(DEV_USED_X550A, DEV_USED_DEFAULT);
	shutil.copy(DEV_USED_X550A, DEV_USED_DEFAULT+"@"+HOSTNAME);
	SED1LINE=commands.getoutput("sed -n '1 p' < %s" % (DEV_USED_DEFAULT));
	if (os.path.isdir(SED1LINE)):
		print("Current Path = %s   (%s%s%s)\n" % (SED1LINE, "\x1b[32m", "Exists", "\x1b[0m"));
	else:
		print("Current Path = %s   (%s%s%s)\n" % (SED1LINE, "\x1b[31m", "Doesn't exists", "\x1b[0m"));
	#print(""); #END IF STATEMENT.
elif (Set_REL_X550A_B0_Flag == 1) and (len(sys.argv) == 2):
	print("\n%s%s%s---------------------------------------------------------------------------%s" % (HEADER_ATTRIB, HEADER_FGCOLR, HEADER_BGCOLR, HEADER_RSTALL));
	print("Device = %-30s %3s %s" % ("REL_PE.X550-AT2-B00", "", "(Sageville 17mm*17mm B00)"));
	
	print("");
	#print("%-20s = %d.%d.%d.%s.%d" % ("PYTHON_VERSION.MAJOR", sys.version_info[0], sys.version_info[1], sys.version_info[2], sys.version_info[3], sys.version_info[4])); #DEBUG ONLY. COMMENT OUT LATER.
	
	if (sys.version_info[0] > 2):
		REL_X550A_VER_NUMB=input("(REL_X550A_VER_NUMB) - Enter the version number you want to load (VxPxx):\t(Python Version 3)\n"); #Python version 3 and higher.
	else:
		REL_X550A_VER_NUMB=raw_input("(REL_X550A_VER_NUMB) - Enter the version number you want to load (VxPxx):\t(Python Version 2)\n"); #Python version 2 and lower.
	#print(""); #END IF STATEMENT.
	
	if   ( REL_X550A_VER_NUMB == "V1P30" ):
		print("INFO  : Version 1.30 has been selected.\n\n"); DEV_VER_STRING=('/X550A_B0_V1P30/X550A_DEV/waste');
	elif ( REL_X550A_VER_NUMB == "V1P46" ):
		print("INFO  : Version 1.46 has been selected.\n\n"); DEV_VER_STRING=('/X550A_B0_V1P46/X550A_DEV/waste');
	elif ( REL_X550A_VER_NUMB == "V1P60" ):
		print("INFO  : Version 1.60 has been selected.\n\n"); DEV_VER_STRING=('/X550A_B0_V1P60/X550A_DEV/waste');
	else:
		ERROR_MSG="ERROR : Incorrect version selected.";
		print("%s%s%s\n" %("\x1b[31m", ERROR_MSG,"\x1b[0m")); DEV_VER_STRING=('/X550A_B0_VxPxx/X550A_DEV/waste');
		print("%s%s%s"   %("\x1b[31m", "INFO: These are the only available versions","\x1b[0m"));
		print("%s%s%s"   %("\x1b[31m", " 1) V1P30","\x1b[0m"));
		print("%s%s%s"   %("\x1b[31m", " 2) V1P46","\x1b[0m"));
		print("%s%s%s"   %("\x1b[31m", " 3) V1P60","\x1b[0m"));
		print("");
	#print(""); #END IF STATEMENT.
	
	#print("DEV_VER_STRING = %s" %(DEV_VER_STRING)); #DEBUG ONLY. COMMENT OUT LATER.
	
	DEV_USED_STRING=(os.environ["HOME"] + '/' + DEV_PATH_REL_X550A_B0 + DEV_VER_STRING + '\n');
	os.remove(DEV_USED_REL_X550A);
	FILE_DES=os.open(DEV_USED_REL_X550A, os.O_RDWR|os.O_CREAT);
	FILE_RET=os.write(FILE_DES, DEV_USED_STRING);
	os.close(FILE_DES);
	os.chmod(DEV_USED_REL_X550A, 0664);
	
	print("FILE_DES = %s" % (FILE_DES));
	print("FILE_RET = %d" % (FILE_RET));
	
	shutil.copy(DEV_USED_REL_X550A, DEV_USED_DEFAULT);
	shutil.copy(DEV_USED_REL_X550A, DEV_USED_DEFAULT+"@"+HOSTNAME);
	SED1LINE=commands.getoutput("sed -n '1 p' < %s" % (DEV_USED_DEFAULT));
	if (os.path.isdir(SED1LINE)):
		print("Current Path = %s   (%s%s%s)\n" % (SED1LINE, "\x1b[32m", "Exists", "\x1b[0m"));
	else:
		print("Current Path = %s   (%s%s%s)\n" % (SED1LINE, "\x1b[31m", "Doesn't exists", "\x1b[0m"));
	#print(""); #END IF STATEMENT.
elif (len(sys.argv) == 3):
	print("\n%s%s%s---------------------------------------------------------------------------%s" % (HEADER_ATTRIB, HEADER_FGCOLR, HEADER_BGCOLR, HEADER_RSTALL));
	print("%s%s%s" % ("\x1b[31m", "#WARNING - Too many arguments!", "\x1b[0m"));
	
	print("");
	print("%s%s%s# Time EOF : %-53s ########%s" % (HEADER_ATTRIB, HEADER_FGCOLR, HEADER_BGCOLR, time.strftime("%c"), HEADER_RSTALL));
	print("%s%s%s###### END - %-53s ########%s" % (HEADER_ATTRIB, HEADER_FGCOLR, HEADER_BGCOLR, FILE_NAME_HEADER,    HEADER_RSTALL));
	sys.exit(); #(0=Success, 1=Failure).
#print(""); #END IF STATEMENT.
#### List VALID_USER with specific HOSTNAME ####
if   (HOSTNAME == "Bradley-Lemur"       ): VALID_USER="bradley";  #76_BE.
elif (HOSTNAME == "system76-pc"         ): VALID_USER="bradley";  #76_BE.
elif (HOSTNAME == "SJ-OPS-BEVERSON"     ): VALID_USER="beverson"; #QT_BE.
elif (HOSTNAME == "zbjcxm-l1"           ): VALID_USER="beverson"; #QT_BE.
elif (HOSTNAME == "93koffline01"        ): VALID_USER="beverson"; #QT_BE.
elif (HOSTNAME == "93koffline02"        ): VALID_USER="beverson"; #QT_BE.
elif (HOSTNAME == "93koffline03"        ): VALID_USER="beverson"; #QT_BE.
elif (HOSTNAME == "fm-ops01"            ): VALID_USER="beverson"; #QT_BE.
elif (HOSTNAME == "smartscale01"        ): VALID_USER="nuon";     #iTest Inc.
elif (HOSTNAME == "smartscale02"        ): VALID_USER="nuon";     #iTest Inc.
elif (HOSTNAME == "smartscale03"        ): VALID_USER="nuon";     #iTest Inc.
elif (HOSTNAME == "smartscale04"        ): VALID_USER="nuon";     #iTest Inc.
elif (HOSTNAME == "smartscale05"        ): VALID_USER="nuon";     #iTest Inc.
elif (HOSTNAME == "smartscale06"        ): VALID_USER="nuon";     #iTest Inc.
elif (HOSTNAME == "smartscale07"        ): VALID_USER="nuon";     #iTest Inc.
elif (HOSTNAME == "smartscale08"        ): VALID_USER="nuon";     #iTest Inc.
elif (HOSTNAME == "offline1"            ): VALID_USER="nuon";     #iTest Inc.
elif (HOSTNAME == "offline2"            ): VALID_USER="nuon";     #iTest Inc.
elif (HOSTNAME == "offline3"            ): VALID_USER="nuon";     #iTest Inc.
elif (HOSTNAME == "offline4"            ): VALID_USER="nuon";     #iTest Inc.
elif (HOSTNAME == "offline5"            ): VALID_USER="nuon";     #iTest Inc.
elif (HOSTNAME == "offline10"           ): VALID_USER="nuon";     #iTest Inc.
elif (HOSTNAME == "offline11"           ): VALID_USER="nuon";     #iTest Inc.
elif (HOSTNAME == "offline13"           ): VALID_USER="nuon";     #iTest Inc.
elif (HOSTNAME == "offline15"           ): VALID_USER="nuon";     #iTest Inc.
elif (HOSTNAME == "offline16"           ): VALID_USER="nuon";     #iTest Inc.
elif (HOSTNAME == "PS1"                 ): VALID_USER="bevers2";  #ISE Labs.
elif (HOSTNAME == "PS2"                 ): VALID_USER="bevers2";  #ISE Labs.
elif (HOSTNAME == "ps4-64"              ): VALID_USER="bevers2";  #ISE Labs.
elif (HOSTNAME == "ps5-64"              ): VALID_USER="bevers2";  #ISE Labs.
elif (HOSTNAME == "PS7-64"              ): VALID_USER="bevers2";  #ISE Labs.
elif (HOSTNAME == "ps10-64"             ): VALID_USER="bevers2";  #ISE Labs.
elif (HOSTNAME == "PS12-64"             ): VALID_USER="bevers2";  #ISE Labs.
elif (HOSTNAME == "PS15"                ): VALID_USER="bevers2";  #ISE Labs.
elif (HOSTNAME == "ps15-64"             ): VALID_USER="bevers2";  #ISE Labs.
elif (HOSTNAME == "ps16-64"             ): VALID_USER="bevers2";  #ISE Labs.
elif (HOSTNAME == "hp207"               ): VALID_USER="bevers2";  #ISE Labs.
elif (HOSTNAME == "hp208"               ): VALID_USER="bevers2";  #ISE Labs.
elif (HOSTNAME == "hp209"               ): VALID_USER="bevers2";  #ISE Labs.
elif (HOSTNAME == "hp210"               ): VALID_USER="bevers2";  #ISE Labs.
elif (HOSTNAME == "hp224"               ): VALID_USER="bevers2";  #ISE Labs.
elif (HOSTNAME == "hp225"               ): VALID_USER="bevers2";  #ISE Labs.
elif (HOSTNAME == "hp226"               ): VALID_USER="bevers2";  #ISE Labs.
elif (HOSTNAME == "hp230"               ): VALID_USER="bevers2";  #ISE Labs.
elif (HOSTNAME == "hp231"               ): VALID_USER="bevers2";  #ISE Labs.
elif (HOSTNAME == "hp233"               ): VALID_USER="bevers2";  #ISE Labs.
elif (HOSTNAME == "hp234"               ): VALID_USER="bevers2";  #ISE Labs.
elif (HOSTNAME == "hp236"               ): VALID_USER="bevers2";  #ISE Labs.
else:                                      VALID_USER="beverson"; #QT_BE.
#print(""); #END IF STATEMENT.
if (Set_Touch_All_Flag == 1 ) and (USER == VALID_USER):
	print("\n%s%s%s---------------------------------------------------------------------------%s" % (HEADER_ATTRIB, HEADER_FGCOLR, HEADER_BGCOLR, HEADER_RSTALL));
	WaitTimeSec=3.000; #Time is in seconds.
	time.sleep(WaitTimeSec);
	#print("Set_Touch_All_Flag = %d" % (Set_Touch_All_Flag)); #DEBUG ONLY. REMOVE WHEN FINISHED.
	print("Timestamps have been updated for specified directories and files.");
	CHECK_DIR_FILE=[]; #Define array variable.
	CHECK_DIR_FILE.insert(0, "93K_EXE_DIR");
	CHECK_DIR_FILE.insert(1, "BASH_FILE_DIR");
	CHECK_DIR_FILE.insert(2, "BackUps_TarGz_DIR");
	CHECK_DIR_FILE.insert(3, "bin");
	CHECK_DIR_FILE.insert(4, "Desktop");
	CHECK_DIR_FILE.insert(5, "Documents");                                  #(Documents/My\ Documents)
	CHECK_DIR_FILE.insert(6, "Downloads");
	CHECK_DIR_FILE.insert(7, "FTP_DIR");
	CHECK_DIR_FILE.insert(8, "logs");
	CHECK_DIR_FILE.insert(9, "Mail");
	CHECK_DIR_FILE.insert(10, "Music");
	CHECK_DIR_FILE.insert(11, "Pictures");
	CHECK_DIR_FILE.insert(12, "devices");
	CHECK_DIR_FILE.insert(13, "devices/BBIC5");
	CHECK_DIR_FILE.insert(14, "devices/BBIC6");
	CHECK_DIR_FILE.insert(15, "devices/PMIC");
	CHECK_DIR_FILE.insert(16, "projects");
	CHECK_DIR_FILE.insert(17, "projects/proj_Advantest");
	CHECK_DIR_FILE.insert(18, "projects/proj_AllianceATE");
	CHECK_DIR_FILE.insert(19, "projects/proj_Atlantic");
	CHECK_DIR_FILE.insert(20, "projects/proj_Bermuda");
	CHECK_DIR_FILE.insert(21, "projects/proj_Europa");
	CHECK_DIR_FILE.insert(22, "projects/proj_Fiji");
	CHECK_DIR_FILE.insert(23, "projects/proj_GalaxyDB");
	CHECK_DIR_FILE.insert(24, "projects/proj_Hak5");
	CHECK_DIR_FILE.insert(25, "projects/proj_HTML");
	CHECK_DIR_FILE.insert(26, "projects/proj_Jamaica");
	CHECK_DIR_FILE.insert(27, "projects/proj_Python");
	CHECK_DIR_FILE.insert(28, "projects/proj_QTNA");
	CHECK_DIR_FILE.insert(29, "projects/proj_RaspberryPi");
	CHECK_DIR_FILE.insert(30, "projects/proj_Sageville");
	CHECK_DIR_FILE.insert(31, "projects/proj_VTRAN");
	CHECK_DIR_FILE.insert(32, "projects/proj_Zelda");
	CHECK_DIR_FILE.insert(33, "Public");
	CHECK_DIR_FILE.insert(34, "smarTest");
	CHECK_DIR_FILE.insert(35, "stdf");
	CHECK_DIR_FILE.insert(36, "Templates");
	CHECK_DIR_FILE.insert(37, "Videos");
	CHECK_DIR_FILE.insert(38, "workorder");
	CHECK_DIR_FILE.insert(39, "workspace");
	CHECK_DIR_FILE.insert(40, "workspace/workspace_7.3.2.X_64bit_AQC100_BE");
	CHECK_DIR_FILE.insert(41, "workspace/workspace_7.3.2.X_64bit_AQC107_BE");
	CHECK_DIR_FILE.insert(42, "workspace/workspace_7.3.2.X_64bit_AQC111C_BE");
	CHECK_DIR_FILE.insert(43, "workspace/workspace_7.3.2.X_64bit_BBIC5_BE");
	CHECK_DIR_FILE.insert(44, "workspace/workspace_7.4.0.X_64bit_BBIC5_BE");
	CHECK_DIR_FILE.insert(45, "workspace/workspace_7.4.2.X_64bit_BBIC5_BE");
	CHECK_DIR_FILE.insert(46, "workspace/workspace_7.4.3.X_64bit_BBIC6_BE");
	CHECK_DIR_FILE.insert(47, "workspace/workspace_7.5.2.X_64bit_BBIC6_BE");
	CHECK_DIR_FILE.insert(48, "workspace/workspace_7.4.3.X_64bit_PMIC_BE");
	CHECK_DIR_FILE.insert(49, "workspace/workspace_7.5.2.X_64bit_PMIC_BE");
	CHECK_DIR_FILE.insert(50, ".device_inuse_soc");
	CHECK_DIR_FILE.insert(51, ".device_inuse_soc.AQC100_DEV");
	CHECK_DIR_FILE.insert(52, ".device_inuse_soc.AQC107_DEV");
	CHECK_DIR_FILE.insert(53, ".device_inuse_soc.AQC111C_DEV");
	CHECK_DIR_FILE.insert(54, ".device_inuse_soc.BBIC5_DEV");
	CHECK_DIR_FILE.insert(55, ".device_inuse_soc.BBIC6_DEV");
	CHECK_DIR_FILE.insert(56, ".device_inuse_soc.PMIC_DEV");
	CHECK_DIR_FILE.insert(57, ".device_inuse_soc.RFIC_DEV");
	CHECK_DIR_FILE.insert(58, ".device_inuse_soc@"+HOSTNAME);
	CHECK_DIR_FILE.insert(59, ".bash_aliases");
	CHECK_DIR_FILE.insert(60, ".bash_logout");
	CHECK_DIR_FILE.insert(61, ".bash_profile");
	CHECK_DIR_FILE.insert(62, ".bashrc");
	CHECK_DIR_FILE.insert(63, ".login");
	CHECK_DIR_FILE.insert(64, ".profile");
	CHECK_DIR_FILE.insert(65, ".tcshrc");
	CHECK_DIR_FILE.insert(66, "MAKE_APT_GET_COMMAND_V2P19.sh");
	CHECK_DIR_FILE.insert(67, FILE_NAME_HEADER.replace(".py", ".sh"));
	CHECK_DIR_FILE.insert(68, FILE_NAME_HEADER);
	
	#print("\nTotal %s = %d" % ("CHECK_DIR_FILE", len(CHECK_DIR_FILE)));    #DEBUG ONLY. REMOVE WHEN FINISHED.
	
	#### Set the for-loop stop variable. ####
	LoopBeg=( 0 );                                                          #Minimum value = 0;
	LoopEnd=(len(CHECK_DIR_FILE));                                          #Maximum value = 69;
	
	TOUCH_DIR_FILE=[]; #Clear the new array.
	
	EXISTS_PASS="Exists";
	EXISTS_FAIL="Doesn't exists";
	
	DO_PRINT_COMMAND="YES"; #(YES/NO)
	DO_TOUCH_COMMAND="YES"; #(YES/NO)
	DO_CHECK_EXISTSP="YES"; #(YES/NO)
	for ZAn in xrange(LoopBeg, LoopEnd, 1):
		if (ZAn == 0): ZBn=0; #print("%s = %2d" % ("ZBn", ZBn)); #print(""); #END IF STATEMENT.
		COUTPASS="(%2d) %-50s (%s%-14s%s)" % ((ZAn + 1), CHECK_DIR_FILE[ZAn], "\x1b[32m", EXISTS_PASS, "\x1b[0m");
		COUTFAIL="(%2d) %-50s (%s%-14s%s)" % ((ZAn + 1), CHECK_DIR_FILE[ZAn], "\x1b[31m", EXISTS_FAIL, "\x1b[0m");
		if (os.path.isdir(CHECK_DIR_FILE[ZAn])):
			if (DO_PRINT_COMMAND == "YES"): print("%s%s" % (COUTPASS, "(DIR)"));  #print(""); #END IF STATEMENT.
			if (DO_TOUCH_COMMAND == "YES"): os.utime(CHECK_DIR_FILE[ZAn], None);  #print(""); #END IF STATEMENT.
			if (DO_CHECK_EXISTSP == "YES"): TOUCH_DIR_FILE.insert(ZBn, CHECK_DIR_FILE[ZAn]); ZBn+=1; #print(""); #END IF STATEMENT.
		elif (os.path.isfile(CHECK_DIR_FILE[ZAn])):
			if (DO_PRINT_COMMAND == "YES"): print("%s%s" % (COUTPASS, "(FILE)")); #print(""); #END IF STATEMENT.
			if (DO_TOUCH_COMMAND == "YES"): os.utime(CHECK_DIR_FILE[ZAn], None);  #print(""); #END IF STATEMENT.
			if (DO_CHECK_EXISTSP == "YES"): TOUCH_DIR_FILE.insert(ZBn, CHECK_DIR_FILE[ZAn]); ZBn+=1; #print(""); #END IF STATEMENT.
		else:
			if (DO_PRINT_COMMAND == "YES"):      print("%s" %(COUTFAIL));              #print(""); #END IF STATEMENT.
		#print(""); #END IF STATEMENT.
	#print(""); #END FOR STATEMENT.
	print("");
	if (DO_PRINT_COMMAND == "YES"):      print("Total (Exists) = %d" % (len(TOUCH_DIR_FILE))); #print(""); #END IF STATEMENT.
	if (DO_PRINT_COMMAND == "BYPASSED"): print("TOUCH_DIR_FILE = %s" % (" ".join(TOUCH_DIR_FILE))); #print(""); #END IF STATEMENT.
	
	#if (DO_TOUCH_COMMAND == "BYPASSED"):
	#	if(len(TOUCH_DIR_FILE) != 0): os.utime(" ".join(TOUCH_DIR_FILE), None); #print(""); #END IF STATEMENT.
	#print(""); #END IF STATEMENT.
elif (Set_Touch_All_Flag == 1 ) and (USER != VALID_USER):
	print("\n%s%s%s---------------------------------------------------------------------------%s" % (HEADER_ATTRIB, HEADER_FGCOLR, HEADER_BGCOLR, HEADER_RSTALL));
	print("USER     = %s %-6s (%s%-16s%s)\n" % (USER, "", "\x1b[31m", "NOT A VALID USER", "\x1b[0m"));
#print(""); #END IF STATEMENT.
print("");
print("%s%s%s# Time EOF : %-53s ########%s" % (HEADER_ATTRIB, HEADER_FGCOLR, HEADER_BGCOLR, time.strftime("%c"), HEADER_RSTALL));
print("%s%s%s###### END - %-53s ########%s" % (HEADER_ATTRIB, HEADER_FGCOLR, HEADER_BGCOLR, FILE_NAME_HEADER,    HEADER_RSTALL));
