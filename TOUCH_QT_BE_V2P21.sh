#!/bin/bash
#Author:   BEVERSON
#DateTime: 2021/01/12 20:19:01 PST
#Notes:    Default path for bash is "/bin/bash". Optional path for bash is "/usr/local/bin/bash".
#Notes:    Default path for python is "/usr/bin/python". Optional path for python is "/usr/local/bin/python".

REVISION_STATUS="2021/01/12";

#source filename [arguments]; EXIT_STATUS=$?; printf "EXIT_STATUS: %s\n" ${EXIT_STATUS}; if [ ${EXIT_STATUS} == 1 ]; then exit 0; fi #(0=Success, 1=Failure).

FILE_NAME_HEADER=TOUCH_QT_BE_V2P21.sh;
HEADER_ATTRIB="\e[4m";		#(1,2,4,5,7,8).
HEADER_FGCOLR="\e[34m";		#(39,30,31,32,33,34,35,36,37).
HEADER_BGCOLR="\e[49m";		#(49,40,41,42,43,44,45,46,47).
HEADER_RSTALL="\e[0m";		#(0,21,22,24,25,27,28);
printf "%b%b%b#### START - %-53s ########%b\n" ${HEADER_ATTRIB} ${HEADER_FGCOLR} ${HEADER_BGCOLR} ${FILE_NAME_HEADER} ${HEADER_RSTALL};
printf "%b%b%b# Time SOF : %-53s ########%b\n" ${HEADER_ATTRIB} ${HEADER_FGCOLR} ${HEADER_BGCOLR} "$(date)"           ${HEADER_RSTALL};
printf "\n";

#### Define Date and Time variables. ####
DATE_STANDARD=$(date);
DATE_YYYYmmdd=$(date +%Y/%m/%d);
TIME_HHMMSS=$(date +%H:%M:%S);
ZONE_ZZ=$(date +%Z);

#### START - Select the Date and Time output type. ####
SEL_DATE_TIME=2; #Default is 2.
if   [ ${SEL_DATE_TIME} == 1 ]; then
	#### Option 1. ####
	printf "%-16s = %s\n"       "DateTime" "${DATE_STANDARD}";
elif [ ${SEL_DATE_TIME} == 2 ]; then
	#### Option 2. ####
	printf "%-16s = %s %s %s\n" "DateTime" ${DATE_YYYYmmdd} ${TIME_HHMMSS} ${ZONE_ZZ};
else
	printf "%-16s = %b%s%b\n"   "DateTime" "\e[31m" "**ERROR**" "\e[0m";
fi
###### END - Select the Date and Time output type. ####

#### START - Basic environmental variables information. ####
printf "%-16s = %s\n" "USER"     $USER;
printf "%-16s = %s\n" "HOME"     $HOME;
printf "%-16s = %s\n" "HOSTNAME" $HOSTNAME;
###### END - Basic environmental variables information. ####

#### START - Get bash version. ####
SEL_BASH_VER=1; #Default is 1.
CmdLineInput_01=$(bash --version); #bash --version.
if   [ ${SEL_BASH_VER} == 1 ]; then
	printf "%-16s = %s\n"     "BASH_VERSION" "${BASH_VERSION}";
elif [ ${SEL_BASH_VER} == 2 ]; then
	printf "%-16s = %s\n"     "BASH_VERSION" "$(bash --version | sed -n '1 p')"; #bash --version, 1st line only.
elif [ ${SEL_BASH_VER} == 3 ]; then
	printf "\n";
	printf "%-16s = \n%s\n"   "BASH_VERSION" "${CmdLineInput_01}"; #bash --version.
else
	printf "%-16s = %b%s%b\n" "BASH_VERSION" "\e[31m" "**ERROR**" "\e[0m";
fi
###### END - Get bash version. ####

#### START - Get revision status. ####
printf "%-16s = %s\n" "REVISION_STATUS" "${REVISION_STATUS}";
###### END - Get revision status. ####

printf "\n%b%b%b---------------------------------------------------------------------------%b\n" ${HEADER_ATTRIB} ${HEADER_FGCOLR} ${HEADER_BGCOLR} ${HEADER_RSTALL};

#### Argument to select the device in use option. ####
ARGA=($@);                    #This puts all arguments into an array. (1-n).
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
i=$(( 0 ));
j=$(( $# ));
while [ ${i} -lt ${j} ]; do
	case "${ARGA[${i}]}" in
		"-aqc100_b10_v1p10")    Set_AQC100_B10_V1P10_Flag=1;;
		"-aqc107_b10_v1p16")    Set_AQC107_B10_V1P16_Flag=1;;
		"-aqc111c_b01_v0p25")   Set_AQC111C_B01_V0P25_Flag=1;;
		"-bbic5_b1_r09a")       Set_BBIC5_B1_R09A_Flag=1;;
		"-bbic5_b1_r10")        Set_BBIC5_B1_R10_Flag=1;;
		"-bbic5_b1_r11")        Set_BBIC5_B1_R11_Flag=1;;
		"-bbic5_b1_r12")        Set_BBIC5_B1_R12_Flag=1;;
		"-bbic5_b1_ws_r01")     Set_BBIC5_B1_WS_R01_Flag=1;;
		"-bbic5_c0_r07")        Set_BBIC5_C0_R07_Flag=1;;
		"-bbic5_d0_r01a")       Set_BBIC5_D0_R01A_Flag=1;;
		"-bbic6_a0_r01")        Set_BBIC6_A0_R01_Flag=1;;
		"-pmic_a4_r01")         Set_PMIC_A4_R01_Flag=1;;
		"-pmic_c0_r01")         Set_PMIC_C0_R01_Flag=1;;
		"-pmic_c1_r01")         Set_PMIC_C1_R01_Flag=1;;
		"-x550a_b0_v1p80")      Set_X550A_B0_V1P80_Flag=1;;
		"-rel_x550a_b0")        Set_REL_X550A_B0_Flag=1;;
		"-debug")               Set_DEBUG_Flag=1;;
		"-touch_all")           Set_Touch_All_Flag=1;;
		"-h")                   ExitStatus0=1;;
		"-help")                ExitStatus0=1;;
		*)                      ;;
	esac
	i=$(( i + 1 ));
done

DoDebugArg0="NO"; #(YES/NO)
if [ ${Set_DEBUG_Flag} == 1 ] || [ ${DoDebugArg0} == "YES" ]; then
	ExitStatus0=1; #Want to stop at exit status section.
	printf "#### START: Debug. ################################\n";
	printf "File Name     : %s\n" $0;
	printf "Argument Flags: %s\n" "${ARGA[*]}";
	printf "Argument Count: %s\n" $#;
	
	i_debug_V=$(( 0 ));
	while [ ${i_debug_V} -lt ${j} ]; do
	#	ARGA_LC[${i}]=`printf "%s" ${ARGA[$i]} | tr '[:upper:]' '[:lower:]'`; #Change all uppercase to lowercase.
		printf "ARGA[%02d]    = %s\n" ${i_debug_V} ${ARGA[${i_debug_V}]};
		i_debug_V=$(( i_debug_V + 1 ));
	done
	printf "#### END  : Debug. ################################\n";
	printf "\n%b%b%b---------------------------------------------------------------------------%b\n" ${HEADER_ATTRIB} ${HEADER_FGCOLR} ${HEADER_BGCOLR} ${HEADER_RSTALL};
fi

#### Check file name header. ####
# ${FILE_NAME_HEADER//.sh/.py}
if [ ${0//.\//} == ${FILE_NAME_HEADER} ]; then
	if [ ${Set_DEBUG_Flag} == 1 ]; then
		printf "%b# INFO: File name header matches.%b\n" "\e[32m" "\e[0m";
		printf "%b%s <=> %s%b\n" "\e[32m" "${0//.\//}" "${FILE_NAME_HEADER}" "\e[0m";
		printf "\n%b%b%b---------------------------------------------------------------------------%b\n" ${HEADER_ATTRIB} ${HEADER_FGCOLR} ${HEADER_BGCOLR} ${HEADER_RSTALL};
	fi
else
	printf "%b# ERROR: File name header does not match.%b\n" "\e[31m" "\e[0m";
	printf "%b%s <=> %s%b\n" "\e[31m" "${0//.\//}" "${FILE_NAME_HEADER}" "\e[0m";
	printf "\n%b%b%b---------------------------------------------------------------------------%b\n" ${HEADER_ATTRIB} ${HEADER_FGCOLR} ${HEADER_BGCOLR} ${HEADER_RSTALL};
	ExitStatus0=1;
fi

#### Exit status. ####
if [ ${ExitStatus0} == 1 ]; then
	printf "#### List of arguments and settings: ####\n";
	printf "%caqc100_b10_v1p10)    Set_AQC100_B10_V1P10_Flag=1;    %s\n" "-" "#(AQ TE AQC100-B10 [Atlantic Version 1.10])";
	printf "%caqc107_b10_v1p16)    Set_AQC107_B10_V1P16_Flag=1;    %s\n" "-" "#(AQ TE AQC107-B10 [Jamaica Version 1.16])";
	printf "%caqc111c_b01_v0p25)   Set_AQC111C_B01_V0P25_Flag=1;   %s\n" "-" "#(AQ TE AQC111C-B01 [Bermuda Version 0.25])";
	printf "%cbbic5_b1_r09a)       Set_BBIC5_B1_R09A_Flag=1;       %s\n" "-" "#(QT TE QT10GA-B1 [BBIC5 FT Release 09A])";
	printf "%cbbic5_b1_r10)        Set_BBIC5_B1_R10_Flag=1;        %s\n" "-" "#(QT TE QT10GA-B1 [BBIC5 FT Release 10])";
	printf "%cbbic5_b1_r11)        Set_BBIC5_B1_R11_Flag=1;        %s\n" "-" "#(QT TE QT10GA-B1 [BBIC5 FT Release 11])";
	printf "%cbbic5_b1_r12)        Set_BBIC5_B1_R12_Flag=1;        %s\n" "-" "#(QT TE QT10GA-B1 [BBIC5 FT Release 12])";
	printf "%cbbic5_b1_ws_r01)     Set_BBIC5_B1_WS_R01_Flag=1;     %s\n" "-" "#(QT TE QT10GA-B1 [BBIC5 WS Release 01])";
	printf "%cbbic5_c0_r07)        Set_BBIC5_C0_R07_Flag=1;        %s\n" "-" "#(QT TE QT10GA-C0 [BBIC5 FT Release 07])";
	printf "%cbbic5_d0_r01a)       Set_BBIC5_D0_R01A_Flag=1;       %s\n" "-" "#(QT TE QT10GA-D0 [BBIC5 FT Release 01A])";
	printf "%cbbic6_a0_r01)        Set_BBIC6_A0_R01_Flag=1;        %s\n" "-" "#(QT TE QT10GA-AX2 [BBIC6 FT Release 01])";
	printf "%cpmic_a4_r01)         Set_PMIC_A4_R01_Flag=1;         %s\n" "-" "#(QT TE PMIC-A4 [PMIC FT Release 01])";
	printf "%cpmic_c0_r01)         Set_PMIC_C0_R01_Flag=1;         %s\n" "-" "#(QT TE PMIC-C0 [PMIC FT Release 01])";
	printf "%cpmic_c1_r01)         Set_PMIC_C1_R01_Flag=1;         %s\n" "-" "#(QT TE PMIC-C1 [PMIC FT Release 01])";
	printf "%cx550a_b0_v1p80)      Set_X550A_B0_V1P80_Flag=1;      %s\n" "-" "#(AQ TE X550-AT2-B00 [Sageville 17mm Version 1.80])";
	printf "%crel_x550a_b0)        Set_REL_X550A_B0_Flag=1;        %s\n" "-" "#(Released to Amkor/PE X550-AT2-B00)";
	printf "%cdebug)               Set_DEBUG_Flag=1;\n"                  "-";
	printf "%ctouch_all)           Set_Touch_All_Flag=1;\n"              "-";
	printf "%ch)                   ExitStatus0=1;\n"                     "-";
	printf "%chelp)                ExitStatus0=1;\n"                     "-";
	printf "%c)                    ;\n"                                  "*";
	
	printf "\n";
	printf "%b%b%b# Time EOF : %-53s ########%b\n" ${HEADER_ATTRIB} ${HEADER_FGCOLR} ${HEADER_BGCOLR} "$(date)"           ${HEADER_RSTALL};
	printf "%b%b%b###### END - %-53s ########%b\n" ${HEADER_ATTRIB} ${HEADER_FGCOLR} ${HEADER_BGCOLR} ${FILE_NAME_HEADER} ${HEADER_RSTALL};
	exit 0; #(0=Success, 1=Failure).
fi

#### Information on OS release. ####
GET_LSB_RELEASE="lsb_release -a";                               #Get Linux Standard Base Release Information.
GET_SMARTEST_VER="/opt/hp93000/soc/prod_env/bin/HPSmarTest -V"; #Get Smartest Version Information.
#### System76 Machine. ####
if   [ $HOSTNAME == "Bradley-Lemur"        ]; then printf "$(${GET_LSB_RELEASE})\n"; SYSTEM_TYPE="System76_Lemur ($(lsb_release -sd))";    #(7.5.2.02)
elif [ $HOSTNAME == "system76-pc"          ]; then printf "$(${GET_LSB_RELEASE})\n"; SYSTEM_TYPE="System76_LemurPro ($(lsb_release -sd))"; #(7.5.2.02)
#### Systems at QT HQ. ####
elif [ $HOSTNAME == "SJ-OPS-BEVERSON"      ]; then printf "$(${GET_LSB_RELEASE})\n"; SYSTEM_TYPE="Windows_10 ($(lsb_release -sd))";      #(7.4.0.02). (IP: 10.10.21.66)
elif [ $HOSTNAME == "zbjcxm-l1"            ]; then printf "$(${GET_LSB_RELEASE})\n"; SYSTEM_TYPE="Windows_10 ($(lsb_release -sd))";      #(7.4.0.02). (IP: 10.10.21.66)
elif [ $HOSTNAME == "93koffline01"         ]; then printf "$(${GET_LSB_RELEASE})\n"; SYSTEM_TYPE="V93K_Offline\n$(${GET_SMARTEST_VER})"; #(7.4.0.02). (IP: 10.10.21.17)
elif [ $HOSTNAME == "93koffline02"         ]; then printf "$(${GET_LSB_RELEASE})\n"; SYSTEM_TYPE="V93K_Offline\n$(${GET_SMARTEST_VER})"; #(7.4.0.02). (IP: 10.10.21.18)
elif [ $HOSTNAME == "93koffline03"         ]; then printf "$(${GET_LSB_RELEASE})\n"; SYSTEM_TYPE="V93K_Offline\n$(${GET_SMARTEST_VER})"; #(7.4.0.02). (IP: 10.10.21.13)
elif [ $HOSTNAME == "fm-ops01"             ]; then printf "$(${GET_LSB_RELEASE})\n"; SYSTEM_TYPE="V93K_Offline\n$(${GET_SMARTEST_VER})"; #(7.3.2.10). (IP: 10.10.5.116)
#### Systems at AQ HQ. ####
elif [ $HOSTNAME == "93K_TESTER_AQ01"      ]; then printf "$(${GET_LSB_RELEASE})\n"; SYSTEM_TYPE="V93K_Online\n$(${GET_SMARTEST_VER})";  #(7.3.2.10). (IP: 10.10.14.24)
elif [ $HOSTNAME == "93K_TESTER_HYPR"      ]; then printf "$(${GET_LSB_RELEASE})\n"; SYSTEM_TYPE="V93K_Online\n$(${GET_SMARTEST_VER})";  #(7.3.2.10). (IP: 10.10.14.6)
elif [ $HOSTNAME == "93K_OFFLINE_AQ01"     ]; then printf "$(${GET_LSB_RELEASE})\n"; SYSTEM_TYPE="V93K_Offline\n$(${GET_SMARTEST_VER})"; #(7.3.2.10). (IP: 10.10.14.23)
elif [ $HOSTNAME == "93K_OFFLINE_HYPR"     ]; then printf "$(${GET_LSB_RELEASE})\n"; SYSTEM_TYPE="V93K_Offline\n$(${GET_SMARTEST_VER})"; #(7.3.2.10). (IP: 10.10.14.5)
elif [ $HOSTNAME == "advantest-vm1"        ]; then printf "$(${GET_LSB_RELEASE})\n"; SYSTEM_TYPE="V93K_Offline\n$(${GET_SMARTEST_VER})"; #(7.3.2.10). (IP: 10.10.14.174)(Server: ops-esxi-01)
elif [ $HOSTNAME == "advantest-vm2"        ]; then printf "$(${GET_LSB_RELEASE})\n"; SYSTEM_TYPE="V93K_Offline\n$(${GET_SMARTEST_VER})"; #(7.3.2.10). (IP: 10.10.14.172)(Server: ops-esxi-01)
elif [ $HOSTNAME == "advantest-vm3"        ]; then printf "$(${GET_LSB_RELEASE})\n"; SYSTEM_TYPE="V93K_Offline\n$(${GET_SMARTEST_VER})"; #(7.3.2.10). (IP: 10.10.14.179)(Server: ops-esxi-01)
elif [ $HOSTNAME == "advantest-vm4"        ]; then printf "$(${GET_LSB_RELEASE})\n"; SYSTEM_TYPE="V93K_Offline\n$(${GET_SMARTEST_VER})"; #(7.3.2.10). (IP: 10.10.14.181)(Server: ops-esxi-01)
elif [ $HOSTNAME == "advantest-vm5"        ]; then printf "$(${GET_LSB_RELEASE})\n"; SYSTEM_TYPE="V93K_Offline\n$(${GET_SMARTEST_VER})"; #(7.3.2.10). (IP: 10.10.14.8)  (Server: ops-esxi-01)
elif [ $HOSTNAME == "advantest-vm6"        ]; then printf "$(${GET_LSB_RELEASE})\n"; SYSTEM_TYPE="V93K_Offline\n$(${GET_SMARTEST_VER})"; #(7.3.2.10). (IP: 10.10.14.210)(Server: ops-esxi-01)
elif [ $HOSTNAME == "linux4.aquantia.com"  ]; then printf "$(${GET_LSB_RELEASE})\n"; SYSTEM_TYPE="V93K_Offline\n$(${GET_SMARTEST_VER})"; #(7.1.4.7)
elif [ $HOSTNAME == "linux15.aquantia.com" ]; then printf "$(${GET_LSB_RELEASE})\n"; SYSTEM_TYPE="V93K_Offline\n$(${GET_SMARTEST_VER})"; #(6.3.4.X)
elif [ $HOSTNAME == "linux19.aquantia.com" ]; then printf "$(${GET_LSB_RELEASE})\n"; SYSTEM_TYPE="V93K_Offline\n$(${GET_SMARTEST_VER})"; #(6.5.4.13)
elif [ $HOSTNAME == "linux60.aquantia.com" ]; then printf "$(${GET_LSB_RELEASE})\n"; SYSTEM_TYPE="VTRAN";
elif [ $HOSTNAME == "suns1"                ]; then printf "$(cat /etc/release)\n";   SYSTEM_TYPE="Galaxy_Admin";
#### V93K online systems at ISE Labs. ####
elif [ $HOSTNAME == "PS1"                  ]; then printf "$(${GET_LSB_RELEASE})\n"; SYSTEM_TYPE="V93K_Online\n$(${GET_SMARTEST_VER})"; #(6.5.4.18)
elif [ $HOSTNAME == "PS1-64"               ]; then printf "$(${GET_LSB_RELEASE})\n"; SYSTEM_TYPE="V93K_Online\n$(${GET_SMARTEST_VER})"; #(7.1.4.X)
elif [ $HOSTNAME == "PS2"                  ]; then printf "$(${GET_LSB_RELEASE})\n"; SYSTEM_TYPE="V93K_Online\n$(${GET_SMARTEST_VER})"; #(6.5.4.18)
elif [ $HOSTNAME == "PS2-64"               ]; then printf "$(${GET_LSB_RELEASE})\n"; SYSTEM_TYPE="V93K_Online\n$(${GET_SMARTEST_VER})"; #(7.1.4.X)
elif [ $HOSTNAME == "PS31"                 ]; then printf "$(${GET_LSB_RELEASE})\n"; SYSTEM_TYPE="V93K_Online\n$(${GET_SMARTEST_VER})"; #(6.5.4.18)
elif [ $HOSTNAME == "PS3"                  ]; then printf "$(${GET_LSB_RELEASE})\n"; SYSTEM_TYPE="V93K_Online\n$(${GET_SMARTEST_VER})"; #(7.1.4.X)
elif [ $HOSTNAME == "ps4-64"               ]; then printf "$(${GET_LSB_RELEASE})\n"; SYSTEM_TYPE="V93K_Online\n$(${GET_SMARTEST_VER})"; #(7.4.0.02)
elif [ $HOSTNAME == "ps5-64"               ]; then printf "$(${GET_LSB_RELEASE})\n"; SYSTEM_TYPE="V93K_Online\n$(${GET_SMARTEST_VER})"; #(7.4.0.02)
elif [ $HOSTNAME == "PS7-64"               ]; then printf "$(${GET_LSB_RELEASE})\n"; SYSTEM_TYPE="V93K_Online\n$(${GET_SMARTEST_VER})"; #(7.4.0.02)
elif [ $HOSTNAME == "ps10-64"              ]; then printf "$(${GET_LSB_RELEASE})\n"; SYSTEM_TYPE="V93K_Online\n$(${GET_SMARTEST_VER})"; #(7.4.0.02)
elif [ $HOSTNAME == "PS12-64"              ]; then printf "$(${GET_LSB_RELEASE})\n"; SYSTEM_TYPE="V93K_Online\n$(${GET_SMARTEST_VER})"; #(7.4.0.02)
elif [ $HOSTNAME == "PS15"                 ]; then printf "$(${GET_LSB_RELEASE})\n"; SYSTEM_TYPE="V93K_Online\n$(${GET_SMARTEST_VER})"; #(6.5.4.18)
elif [ $HOSTNAME == "ps15-64"              ]; then printf "$(${GET_LSB_RELEASE})\n"; SYSTEM_TYPE="V93K_Online\n$(${GET_SMARTEST_VER})"; #(7.4.0.02)
elif [ $HOSTNAME == "ps16-64"              ]; then printf "$(${GET_LSB_RELEASE})\n"; SYSTEM_TYPE="V93K_Online\n$(${GET_SMARTEST_VER})"; #(7.4.0.02)
#### V93K offline systems at ISE Labs. ####
elif [ $HOSTNAME == "hp108"                ]; then printf "$(${GET_LSB_RELEASE})\n"; SYSTEM_TYPE="V93K_Offline\n$(${GET_SMARTEST_VER})"; #(6.5.4.18)
elif [ $HOSTNAME == "hp109"                ]; then printf "$(${GET_LSB_RELEASE})\n"; SYSTEM_TYPE="V93K_Offline\n$(${GET_SMARTEST_VER})"; #(6.5.4.18)
elif [ $HOSTNAME == "hp110"                ]; then printf "$(${GET_LSB_RELEASE})\n"; SYSTEM_TYPE="V93K_Offline\n$(${GET_SMARTEST_VER})"; #(6.5.4.18)
elif [ $HOSTNAME == "hp117"                ]; then printf "$(${GET_LSB_RELEASE})\n"; SYSTEM_TYPE="V93K_Offline\n$(${GET_SMARTEST_VER})"; #(6.3.5.X)
elif [ $HOSTNAME == "hp118"                ]; then printf "$(${GET_LSB_RELEASE})\n"; SYSTEM_TYPE="V93K_Offline\n$(${GET_SMARTEST_VER})"; #(6.5.4.18)
elif [ $HOSTNAME == "hp207"                ]; then printf "$(${GET_LSB_RELEASE})\n"; SYSTEM_TYPE="V93K_Offline\n$(${GET_SMARTEST_VER})"; #(7.4.0.02)
elif [ $HOSTNAME == "hp208"                ]; then printf "$(${GET_LSB_RELEASE})\n"; SYSTEM_TYPE="V93K_Offline\n$(${GET_SMARTEST_VER})"; #(7.4.0.02)
elif [ $HOSTNAME == "hp209"                ]; then printf "$(${GET_LSB_RELEASE})\n"; SYSTEM_TYPE="V93K_Offline\n$(${GET_SMARTEST_VER})"; #(7.4.0.02)
elif [ $HOSTNAME == "hp210"                ]; then printf "$(${GET_LSB_RELEASE})\n"; SYSTEM_TYPE="V93K_Offline\n$(${GET_SMARTEST_VER})"; #(7.4.0.02)
elif [ $HOSTNAME == "hp224"                ]; then printf "$(${GET_LSB_RELEASE})\n"; SYSTEM_TYPE="V93K_Offline\n$(${GET_SMARTEST_VER})"; #(7.4.0.02)
elif [ $HOSTNAME == "hp225"                ]; then printf "$(${GET_LSB_RELEASE})\n"; SYSTEM_TYPE="V93K_Offline\n$(${GET_SMARTEST_VER})"; #(7.4.0.02)
elif [ $HOSTNAME == "hp226"                ]; then printf "$(${GET_LSB_RELEASE})\n"; SYSTEM_TYPE="V93K_Offline\n$(${GET_SMARTEST_VER})"; #(7.4.0.02)
elif [ $HOSTNAME == "hp230"                ]; then printf "$(${GET_LSB_RELEASE})\n"; SYSTEM_TYPE="V93K_Offline\n$(${GET_SMARTEST_VER})"; #(7.1.4.X)
elif [ $HOSTNAME == "hp231"                ]; then printf "$(${GET_LSB_RELEASE})\n"; SYSTEM_TYPE="V93K_Offline\n$(${GET_SMARTEST_VER})"; #(7.1.4.X)
elif [ $HOSTNAME == "hp233"                ]; then printf "$(${GET_LSB_RELEASE})\n"; SYSTEM_TYPE="V93K_Offline\n$(${GET_SMARTEST_VER})"; #(7.1.4.X)
elif [ $HOSTNAME == "hp234"                ]; then printf "$(${GET_LSB_RELEASE})\n"; SYSTEM_TYPE="V93K_Offline\n$(${GET_SMARTEST_VER})"; #(7.4.0.02)
elif [ $HOSTNAME == "hp236"                ]; then printf "$(${GET_LSB_RELEASE})\n"; SYSTEM_TYPE="V93K_Offline\n$(${GET_SMARTEST_VER})"; #(7.4.0.02)
elif [ $HOSTNAME == "hp240"                ]; then printf "$(${GET_LSB_RELEASE})\n"; SYSTEM_TYPE="V93K_Offline\n$(${GET_SMARTEST_VER})"; #(7.3.2.5)(RHEL 5.8)
elif [ $HOSTNAME == "hp240-aquantia"       ]; then printf "$(${GET_LSB_RELEASE})\n"; SYSTEM_TYPE="V93K_Offline\n$(${GET_SMARTEST_VER})"; #(7.3.2.5)(RHEL 5.6)
#### V93K online/offline systems at iTest Inc. ####
elif [ $HOSTNAME == "smartscale01"         ]; then printf "$(${GET_LSB_RELEASE})\n"; SYSTEM_TYPE="V93K_Online\n$(${GET_SMARTEST_VER})";  #(7.4.0.02)
elif [ $HOSTNAME == "smartscale02"         ]; then printf "$(${GET_LSB_RELEASE})\n"; SYSTEM_TYPE="V93K_Online\n$(${GET_SMARTEST_VER})";  #(7.4.0.02)
elif [ $HOSTNAME == "smartscale03"         ]; then printf "$(${GET_LSB_RELEASE})\n"; SYSTEM_TYPE="V93K_Online\n$(${GET_SMARTEST_VER})";  #(7.4.0.02)
elif [ $HOSTNAME == "smartscale04"         ]; then printf "$(${GET_LSB_RELEASE})\n"; SYSTEM_TYPE="V93K_Online\n$(${GET_SMARTEST_VER})";  #(7.4.0.02)
elif [ $HOSTNAME == "smartscale05"         ]; then printf "$(${GET_LSB_RELEASE})\n"; SYSTEM_TYPE="V93K_Online\n$(${GET_SMARTEST_VER})";  #(7.4.0.02)
elif [ $HOSTNAME == "smartscale06"         ]; then printf "$(${GET_LSB_RELEASE})\n"; SYSTEM_TYPE="V93K_Online\n$(${GET_SMARTEST_VER})";  #(7.4.0.02)
elif [ $HOSTNAME == "smartscale07"         ]; then printf "$(${GET_LSB_RELEASE})\n"; SYSTEM_TYPE="V93K_Online\n$(${GET_SMARTEST_VER})";  #(7.4.0.02)
elif [ $HOSTNAME == "smartscale08"         ]; then printf "$(${GET_LSB_RELEASE})\n"; SYSTEM_TYPE="V93K_Online\n$(${GET_SMARTEST_VER})";  #(7.4.0.02)
elif [ $HOSTNAME == "offline1"             ]; then printf "$(${GET_LSB_RELEASE})\n"; SYSTEM_TYPE="V93K_Offline\n$(${GET_SMARTEST_VER})"; #(7.4.0.02)
elif [ $HOSTNAME == "offline2"             ]; then printf "$(${GET_LSB_RELEASE})\n"; SYSTEM_TYPE="V93K_Offline\n$(${GET_SMARTEST_VER})"; #(7.4.0.02)
elif [ $HOSTNAME == "offline3"             ]; then printf "$(${GET_LSB_RELEASE})\n"; SYSTEM_TYPE="V93K_Offline\n$(${GET_SMARTEST_VER})"; #(7.4.0.02)
elif [ $HOSTNAME == "offline4"             ]; then printf "$(${GET_LSB_RELEASE})\n"; SYSTEM_TYPE="V93K_Offline\n$(${GET_SMARTEST_VER})"; #(7.4.0.02)
elif [ $HOSTNAME == "offline5"             ]; then printf "$(${GET_LSB_RELEASE})\n"; SYSTEM_TYPE="V93K_Offline\n$(${GET_SMARTEST_VER})"; #(7.4.0.02)
elif [ $HOSTNAME == "offline10"            ]; then printf "$(${GET_LSB_RELEASE})\n"; SYSTEM_TYPE="V93K_Offline\n$(${GET_SMARTEST_VER})"; #(7.4.0.02)
elif [ $HOSTNAME == "offline11"            ]; then printf "$(${GET_LSB_RELEASE})\n"; SYSTEM_TYPE="V93K_Offline\n$(${GET_SMARTEST_VER})"; #(7.4.0.02)
elif [ $HOSTNAME == "offline13"            ]; then printf "$(${GET_LSB_RELEASE})\n"; SYSTEM_TYPE="V93K_Offline\n$(${GET_SMARTEST_VER})"; #(7.4.0.02)
elif [ $HOSTNAME == "offline15"            ]; then printf "$(${GET_LSB_RELEASE})\n"; SYSTEM_TYPE="V93K_Offline\n$(${GET_SMARTEST_VER})"; #(7.4.0.02)
elif [ $HOSTNAME == "offline16"            ]; then printf "$(${GET_LSB_RELEASE})\n"; SYSTEM_TYPE="V93K_Offline\n$(${GET_SMARTEST_VER})"; #(7.4.0.02)
#### V93K online systems at EAG. ####
elif [ $HOSTNAME == "klondike"             ]; then printf "$(${GET_LSB_RELEASE})\n"; SYSTEM_TYPE="V93K_Online\n$(${GET_SMARTEST_VER})"; #(6.5.4.18)
#### V93K offline systems at EAG. ####
elif [ $HOSTNAME == "linsim02"             ]; then printf "$(${GET_LSB_RELEASE})\n"; SYSTEM_TYPE="V93K_Online\n$(${GET_SMARTEST_VER})"; #(6.5.4.18)
else                                               printf "Not available.\n";        SYSTEM_TYPE="Not available.";
fi
printf "\n%b%b%b---------------------------------------------------------------------------%b\n" ${HEADER_ATTRIB} ${HEADER_FGCOLR} ${HEADER_BGCOLR} ${HEADER_RSTALL};
printf "SYSTEM_TYPE = ${SYSTEM_TYPE}\n";

#### Device in use setup. Define device in use file name and path. ####
DEV_USED_DEFAULT=.device_inuse_soc;                                                                 #Default device inuse. All users.
DEV_USED_AQC100=.device_inuse_soc.AQC100_DEV;                                                       #AQC100-A00, AQC100-B00 (Atlantic).
DEV_USED_AQC107=.device_inuse_soc.AQC107_DEV;                                                       #AQC107-A00, AQC107-B00 (Jamaica).
DEV_USED_AQC111C=.device_inuse_soc.AQC111C_DEV;                                                     #AQC111C-A00, AQC111C-B00 (Bermuda).
DEV_USED_BBIC5=.device_inuse_soc.BBIC5_DEV;                                                         #QT10GA-B1,QT10GS-B1,QT10GT-B1,QT10GU-B1,QT10GA-C0,QT10GS-C0,QT10GT-C0,QT10GU-C0,QT10GA-D0,QT10GS-D0,QT10GT-D0,QT10GU-D0 (BBIC5).
DEV_USED_BBIC6=.device_inuse_soc.BBIC6_DEV;                                                         #QT10GA-AX2,QT10GS-AX2,QT10GT-AX2,QT10GU-AX2 (BBIC6).
DEV_USED_PMIC=.device_inuse_soc.PMIC_DEV;                                                           #PMIC-A4 (PMIC).
DEV_USED_X550A=.device_inuse_soc.X550A_DEV;                                                         #X550-AT2-B00 (Sageville 17mm).
DEV_USED_REL_X550A=.device_inuse_soc.REL_X550A_DEV;                                                 #Released to Amkor/PE X550-AT2.

DEV_PATH_AQC100_B10_V1P10=projects/proj_Atlantic/AQC100_B10_V1P10/AQC100_DEV/waste;                 #AQC100-B10 (Atlantic Version 1.10).
DEV_PATH_AQC107_B10_V1P16=projects/proj_Jamaica/AQC107_B10_V1P16/AQC107_DEV/waste;                  #AQC107-B10 (Jamaica Version 1.16).
DEV_PATH_AQC111C_B01_V0P25=projects/proj_Bermuda/AQC111C_B01_V0P25/AQC111C_DEV/waste;               #AQC111C-B01 (Bermuda Version 0.25).
DEV_PATH_BBIC5_B1_R09A=devices/BBIC5/B1/BBIC5_B1_R09A/BBIC5_DEV/waste;                              #QT10GA-B1,QT10GS-B1,QT10GT-B1,QT10GU-B1 (BBIC5 Release 09A).
DEV_PATH_BBIC5_B1_R10=devices/BBIC5/B1/BBIC5_B1_R10/BBIC5_DEV/waste;                                #QT10GA-B1,QT10GS-B1,QT10GT-B1,QT10GU-B1 (BBIC5 Release 10).
DEV_PATH_BBIC5_B1_R11=devices/BBIC5/B1/BBIC5_B1_R11/BBIC5_DEV/waste;                                #QT10GA-B1,QT10GS-B1,QT10GT-B1,QT10GU-B1 (BBIC5 Release 11).
DEV_PATH_BBIC5_B1_R12=devices/BBIC5/B1/BBIC5_B1_R12/BBIC5_DEV/waste;                                #QT10GA-B1,QT10GS-B1,QT10GT-B1,QT10GU-B1 (BBIC5 Release 12).
DEV_PATH_BBIC5_B1_WS_R01=devices/BBIC5/B1/BBIC5_B1_WS_R01/BBIC5_DEV/waste;                          #QT10GA-B1,QT10GS-B1,QT10GT-B1,QT10GU-B1 (BBIC5 WS Release 01).
DEV_PATH_BBIC5_C0_R07=devices/BBIC5/C0/BBIC5_C0_R07/BBIC5_DEV/waste;                                #QT10GA-C0,QT10GS-C0,QT10GT-C0,QT10GU-C0 (BBIC5 Release 07).
DEV_PATH_BBIC5_D0_R01A=devices/BBIC5/D0/BBIC5_D0_R01A/BBIC5_DEV/waste;                              #QT10GA-D0,QT10GS-D0,QT10GT-D0,QT10GU-D0 (BBIC5 Release 01A).
DEV_PATH_BBIC6_A0_R01=devices/BBIC6/A0/BBIC6_A0_R01/BBIC6_DEV/waste;                                #QT10GA-AX2,QT10GS-AX2,QT10GT-AX2,QT10GU-AX2 (BBIC6 Release 01).
DEV_PATH_PMIC_A4_R01=devices/PMIC/A4/PMIC_A4_R01/PMIC_DEV/waste;                                    #PMIC-A4 (PMIC Release 01).
DEV_PATH_PMIC_C0_R01=devices/PMIC/C0/PMIC_C0_R01/PMIC_DEV/waste;                                    #PMIC-C0 (PMIC Release 01).
DEV_PATH_PMIC_C1_R01=devices/PMIC/C1/PMIC_C1_R01/PMIC_DEV/waste;                                    #PMIC-C1 (PMIC Release 01).
DEV_PATH_X550A_B0_V1P80=projects/proj_Sageville/X550A_B0_V1P80/X550A_DEV/waste;                     #X550-AT2-B00 (Sageville 17mm Version 1.80).
DEV_PATH_REL_X550A_B0=projects/proj_Sageville/REL_AMKOR/REL_X550A_TO_AMKOR_DIR;                     #Released to Amkor/PE X550-AT2-B00.

if [ $# == 0 ]; then
	printf "\n%b%b%b---------------------------------------------------------------------------%b\n" ${HEADER_ATTRIB} ${HEADER_FGCOLR} ${HEADER_BGCOLR} ${HEADER_RSTALL};
	if [ -f ${DEV_USED_DEFAULT} ]; then
		SED1LINE=$(sed -n '1 p' <${DEV_USED_DEFAULT});
		if [ -e ${SED1LINE} ]; then
			printf "Current Path = ${SED1LINE}   (%bExists%b)\n" "\e[32m" "\e[0m";
		else
			printf "Current Path = ${SED1LINE}   (%bDoesn't exists%b)\n" "\e[31m" "\e[0m";
		fi
	else
		printf "${DEV_USED_DEFAULT}   (%bDoesn't exists%b)\n" "\e[31m" "\e[0m";
	fi
elif [ ${Set_AQC100_B10_V1P10_Flag} == 1 ] && [ $# == 1 ]; then
	printf "\n%b%b%b---------------------------------------------------------------------------%b\n" ${HEADER_ATTRIB} ${HEADER_FGCOLR} ${HEADER_BGCOLR} ${HEADER_RSTALL};
	printf "Device = %-30s %3s %s\n" "AQC100" "" "(Atlantic 7mm*11mm B10)";
	rm -rf    ${DEV_USED_AQC100}
	touch     ${DEV_USED_AQC100}
	chmod 664 ${DEV_USED_AQC100}
	printf "${HOME}/${DEV_PATH_AQC100_B10_V1P10}\n" >> ${DEV_USED_AQC100};
	cp ${DEV_USED_AQC100} ${DEV_USED_DEFAULT};
	cp ${DEV_USED_AQC100} ${DEV_USED_DEFAULT}@$HOSTNAME;
	SED1LINE=$(sed -n '1 p' <${DEV_USED_DEFAULT});
	if [ -e ${SED1LINE} ]; then
		printf "Path   = ${SED1LINE}   (%bExists%b)\n" "\e[32m" "\e[0m";
	else
		printf "Path   = ${SED1LINE}   (%bDoesn't exists%b)\n" "\e[31m" "\e[0m";
	fi
elif [ ${Set_AQC107_B10_V1P16_Flag} == 1 ] && [ $# == 1 ]; then
	printf "\n%b%b%b---------------------------------------------------------------------------%b\n" ${HEADER_ATTRIB} ${HEADER_FGCOLR} ${HEADER_BGCOLR} ${HEADER_RSTALL};
	printf "Device = %-30s %3s %s\n" "AQC107" "" "(Jamaica 12mm*14mm B10)";
	rm -rf    ${DEV_USED_AQC107}
	touch     ${DEV_USED_AQC107}
	chmod 664 ${DEV_USED_AQC107}
	printf "${HOME}/${DEV_PATH_AQC107_B10_V1P16}\n" >> ${DEV_USED_AQC107};
	cp ${DEV_USED_AQC107} ${DEV_USED_DEFAULT};
	cp ${DEV_USED_AQC107} ${DEV_USED_DEFAULT}@$HOSTNAME;
	SED1LINE=$(sed -n '1 p' <${DEV_USED_DEFAULT});
	if [ -e ${SED1LINE} ]; then
		printf "Path   = ${SED1LINE}   (%bExists%b)\n" "\e[32m" "\e[0m";
	else
		printf "Path   = ${SED1LINE}   (%bDoesn't exists%b)\n" "\e[31m" "\e[0m";
	fi
elif [ ${Set_AQC111C_B01_V0P25_Flag} == 1 ] && [ $# == 1 ]; then
	printf "\n%b%b%b---------------------------------------------------------------------------%b\n" ${HEADER_ATTRIB} ${HEADER_FGCOLR} ${HEADER_BGCOLR} ${HEADER_RSTALL};
	printf "Device = %-30s %3s %s\n" "AQC111C" "" "(Bermuda 9mm*9mm B01)";
	rm -rf    ${DEV_USED_AQC111C}
	touch     ${DEV_USED_AQC111C}
	chmod 664 ${DEV_USED_AQC111C}
	printf "${HOME}/${DEV_PATH_AQC111C_B01_V0P25}\n" >> ${DEV_USED_AQC111C};
	cp ${DEV_USED_AQC111C} ${DEV_USED_DEFAULT};
	cp ${DEV_USED_AQC111C} ${DEV_USED_DEFAULT}@$HOSTNAME;
	SED1LINE=$(sed -n '1 p' <${DEV_USED_DEFAULT});
	if [ -e ${SED1LINE} ]; then
		printf "Path   = ${SED1LINE}   (%bExists%b)\n" "\e[32m" "\e[0m";
	else
		printf "Path   = ${SED1LINE}   (%bDoesn't exists%b)\n" "\e[31m" "\e[0m";
	fi
elif [ ${Set_BBIC5_B1_R09A_Flag} == 1 ] && [ $# == 1 ]; then
	printf "\n%b%b%b---------------------------------------------------------------------------%b\n" ${HEADER_ATTRIB} ${HEADER_FGCOLR} ${HEADER_BGCOLR} ${HEADER_RSTALL};
	printf "Device = %-30s %3s %s\n" "QT10GA" "" "(BBIC5 17mm X 17mm B1)";
	rm -rf    ${DEV_USED_BBIC5}
	touch     ${DEV_USED_BBIC5}
	chmod 664 ${DEV_USED_BBIC5}
	printf "${HOME}/${DEV_PATH_BBIC5_B1_R09A}\n" >> ${DEV_USED_BBIC5};
	cp ${DEV_USED_BBIC5} ${DEV_USED_DEFAULT};
	cp ${DEV_USED_BBIC5} ${DEV_USED_DEFAULT}@$HOSTNAME;
	SED1LINE=$(sed -n '1 p' <${DEV_USED_DEFAULT});
	if [ -e ${SED1LINE} ]; then
		printf "Path   = ${SED1LINE}   (%bExists%b)\n" "\e[32m" "\e[0m";
	else
		printf "Path   = ${SED1LINE}   (%bDoesn't exists%b)\n" "\e[31m" "\e[0m";
	fi
elif [ ${Set_BBIC5_B1_R10_Flag} == 1 ] && [ $# == 1 ]; then
	printf "\n%b%b%b---------------------------------------------------------------------------%b\n" ${HEADER_ATTRIB} ${HEADER_FGCOLR} ${HEADER_BGCOLR} ${HEADER_RSTALL};
	printf "Device = %-30s %3s %s\n" "QT10GA" "" "(BBIC5 17mm X 17mm B1)";
	rm -rf    ${DEV_USED_BBIC5}
	touch     ${DEV_USED_BBIC5}
	chmod 664 ${DEV_USED_BBIC5}
	printf "${HOME}/${DEV_PATH_BBIC5_B1_R10}\n" >> ${DEV_USED_BBIC5};
	cp ${DEV_USED_BBIC5} ${DEV_USED_DEFAULT};
	cp ${DEV_USED_BBIC5} ${DEV_USED_DEFAULT}@$HOSTNAME;
	SED1LINE=$(sed -n '1 p' <${DEV_USED_DEFAULT});
	if [ -e ${SED1LINE} ]; then
		printf "Path   = ${SED1LINE}   (%bExists%b)\n" "\e[32m" "\e[0m";
	else
		printf "Path   = ${SED1LINE}   (%bDoesn't exists%b)\n" "\e[31m" "\e[0m";
	fi
elif [ ${Set_BBIC5_B1_R11_Flag} == 1 ] && [ $# == 1 ]; then
	printf "\n%b%b%b---------------------------------------------------------------------------%b\n" ${HEADER_ATTRIB} ${HEADER_FGCOLR} ${HEADER_BGCOLR} ${HEADER_RSTALL};
	printf "Device = %-30s %3s %s\n" "QT10GA" "" "(BBIC5 17mm X 17mm B1)";
	rm -rf    ${DEV_USED_BBIC5}
	touch     ${DEV_USED_BBIC5}
	chmod 664 ${DEV_USED_BBIC5}
	printf "${HOME}/${DEV_PATH_BBIC5_B1_R11}\n" >> ${DEV_USED_BBIC5};
	cp ${DEV_USED_BBIC5} ${DEV_USED_DEFAULT};
	cp ${DEV_USED_BBIC5} ${DEV_USED_DEFAULT}@$HOSTNAME;
	SED1LINE=$(sed -n '1 p' <${DEV_USED_DEFAULT});
	if [ -e ${SED1LINE} ]; then
		printf "Path   = ${SED1LINE}   (%bExists%b)\n" "\e[32m" "\e[0m";
	else
		printf "Path   = ${SED1LINE}   (%bDoesn't exists%b)\n" "\e[31m" "\e[0m";
	fi
elif [ ${Set_BBIC5_B1_R12_Flag} == 1 ] && [ $# == 1 ]; then
	printf "\n%b%b%b---------------------------------------------------------------------------%b\n" ${HEADER_ATTRIB} ${HEADER_FGCOLR} ${HEADER_BGCOLR} ${HEADER_RSTALL};
	printf "Device = %-30s %3s %s\n" "QT10GA" "" "(BBIC5 17mm X 17mm B1)";
	rm -rf    ${DEV_USED_BBIC5}
	touch     ${DEV_USED_BBIC5}
	chmod 664 ${DEV_USED_BBIC5}
	printf "${HOME}/${DEV_PATH_BBIC5_B1_R12}\n" >> ${DEV_USED_BBIC5};
	cp ${DEV_USED_BBIC5} ${DEV_USED_DEFAULT};
	cp ${DEV_USED_BBIC5} ${DEV_USED_DEFAULT}@$HOSTNAME;
	SED1LINE=$(sed -n '1 p' <${DEV_USED_DEFAULT});
	if [ -e ${SED1LINE} ]; then
		printf "Path   = ${SED1LINE}   (%bExists%b)\n" "\e[32m" "\e[0m";
	else
		printf "Path   = ${SED1LINE}   (%bDoesn't exists%b)\n" "\e[31m" "\e[0m";
	fi
elif [ ${Set_BBIC5_B1_WS_R01_Flag} == 1 ] && [ $# == 1 ]; then
	printf "\n%b%b%b---------------------------------------------------------------------------%b\n" ${HEADER_ATTRIB} ${HEADER_FGCOLR} ${HEADER_BGCOLR} ${HEADER_RSTALL};
	printf "Device = %-30s %3s %s\n" "BBIC5" "" "(BBIC5 17mm X 17mm B1 Wafer-Sort)";
	rm -rf    ${DEV_USED_BBIC5}
	touch     ${DEV_USED_BBIC5}
	chmod 664 ${DEV_USED_BBIC5}
	printf "${HOME}/${DEV_PATH_BBIC5_B1_WS_R01}\n" >> ${DEV_USED_BBIC5};
	cp ${DEV_USED_BBIC5} ${DEV_USED_DEFAULT};
	cp ${DEV_USED_BBIC5} ${DEV_USED_DEFAULT}@$HOSTNAME;
	SED1LINE=$(sed -n '1 p' <${DEV_USED_DEFAULT});
	if [ -e ${SED1LINE} ]; then
		printf "Path   = ${SED1LINE}   (%bExists%b)\n" "\e[32m" "\e[0m";
	else
		printf "Path   = ${SED1LINE}   (%bDoesn't exists%b)\n" "\e[31m" "\e[0m";
	fi
elif [ ${Set_BBIC5_C0_R07_Flag} == 1 ] && [ $# == 1 ]; then
	printf "\n%b%b%b---------------------------------------------------------------------------%b\n" ${HEADER_ATTRIB} ${HEADER_FGCOLR} ${HEADER_BGCOLR} ${HEADER_RSTALL};
	printf "Device = %-30s %3s %s\n" "QT10GA" "" "(BBIC5 17mm X 17mm C0)";
	rm -rf    ${DEV_USED_BBIC5}
	touch     ${DEV_USED_BBIC5}
	chmod 664 ${DEV_USED_BBIC5}
	printf "${HOME}/${DEV_PATH_BBIC5_C0_R07}\n" >> ${DEV_USED_BBIC5};
	cp ${DEV_USED_BBIC5} ${DEV_USED_DEFAULT};
	cp ${DEV_USED_BBIC5} ${DEV_USED_DEFAULT}@$HOSTNAME;
	SED1LINE=$(sed -n '1 p' <${DEV_USED_DEFAULT});
	if [ -e ${SED1LINE} ]; then
		printf "Path   = ${SED1LINE}   (%bExists%b)\n" "\e[32m" "\e[0m";
	else
		printf "Path   = ${SED1LINE}   (%bDoesn't exists%b)\n" "\e[31m" "\e[0m";
	fi
elif [ ${Set_BBIC5_D0_R01A_Flag} == 1 ] && [ $# == 1 ]; then
	printf "\n%b%b%b---------------------------------------------------------------------------%b\n" ${HEADER_ATTRIB} ${HEADER_FGCOLR} ${HEADER_BGCOLR} ${HEADER_RSTALL};
	printf "Device = %-30s %3s %s\n" "QT10GA/QT10GS/QT10GT/QT10GU" "" "(BBIC5 17mm X 17mm D0)";
	rm -rf    ${DEV_USED_BBIC5}
	touch     ${DEV_USED_BBIC5}
	chmod 664 ${DEV_USED_BBIC5}
	printf "${HOME}/${DEV_PATH_BBIC5_D0_R01A}\n" >> ${DEV_USED_BBIC5};
	cp ${DEV_USED_BBIC5} ${DEV_USED_DEFAULT};
	cp ${DEV_USED_BBIC5} ${DEV_USED_DEFAULT}@$HOSTNAME;
	SED1LINE=$(sed -n '1 p' <${DEV_USED_DEFAULT});
	if [ -e ${SED1LINE} ]; then
		printf "Path   = ${SED1LINE}   (%bExists%b)\n" "\e[32m" "\e[0m";
	else
		printf "Path   = ${SED1LINE}   (%bDoesn't exists%b)\n" "\e[31m" "\e[0m";
	fi
elif [ ${Set_BBIC6_A0_R01_Flag} == 1 ] && [ $# == 1 ]; then
	printf "\n%b%b%b---------------------------------------------------------------------------%b\n" ${HEADER_ATTRIB} ${HEADER_FGCOLR} ${HEADER_BGCOLR} ${HEADER_RSTALL};
	printf "Device = %-30s %3s %s\n" "QT10GA-AX2/QT10GS-AX2/QT10GT-AX2/QT10GU-AX2" "" "(BBIC6 17mm X 17mm A0)";
	rm -rf    ${DEV_USED_BBIC6}
	touch     ${DEV_USED_BBIC6}
	chmod 664 ${DEV_USED_BBIC6}
	printf "${HOME}/${DEV_PATH_BBIC6_A0_R01}\n" >> ${DEV_USED_BBIC6};
	cp ${DEV_USED_BBIC6} ${DEV_USED_DEFAULT};
	cp ${DEV_USED_BBIC6} ${DEV_USED_DEFAULT}@$HOSTNAME;
	SED1LINE=$(sed -n '1 p' <${DEV_USED_DEFAULT});
	if [ -e ${SED1LINE} ]; then
		printf "Path   = ${SED1LINE}   (%bExists%b)\n" "\e[32m" "\e[0m";
	else
		printf "Path   = ${SED1LINE}   (%bDoesn't exists%b)\n" "\e[31m" "\e[0m";
	fi
elif [ ${Set_PMIC_A4_R01_Flag} == 1 ] && [ $# == 1 ]; then
	printf "\n%b%b%b---------------------------------------------------------------------------%b\n" ${HEADER_ATTRIB} ${HEADER_FGCOLR} ${HEADER_BGCOLR} ${HEADER_RSTALL};
	printf "Device = %-30s %3s %s\n" "PMIC" "" "(PMIC 7mm X 6mm A4)";
	rm -rf    ${DEV_USED_PMIC}
	touch     ${DEV_USED_PMIC}
	chmod 664 ${DEV_USED_PMIC}
	printf "${HOME}/${DEV_PATH_PMIC_A4_R01}\n" >> ${DEV_USED_PMIC};
	cp ${DEV_USED_PMIC} ${DEV_USED_DEFAULT};
	cp ${DEV_USED_PMIC} ${DEV_USED_DEFAULT}@$HOSTNAME;
	SED1LINE=$(sed -n '1 p' <${DEV_USED_DEFAULT});
	if [ -e ${SED1LINE} ]; then
		printf "Path   = ${SED1LINE}   (%bExists%b)\n" "\e[32m" "\e[0m";
	else
		printf "Path   = ${SED1LINE}   (%bDoesn't exists%b)\n" "\e[31m" "\e[0m";
	fi
elif [ ${Set_PMIC_C0_R01_Flag} == 1 ] && [ $# == 1 ]; then
	printf "\n%b%b%b---------------------------------------------------------------------------%b\n" ${HEADER_ATTRIB} ${HEADER_FGCOLR} ${HEADER_BGCOLR} ${HEADER_RSTALL};
	printf "Device = %-30s %3s %s\n" "PMIC" "" "(PMIC 7mm X 6mm C0)";
	rm -rf    ${DEV_USED_PMIC}
	touch     ${DEV_USED_PMIC}
	chmod 664 ${DEV_USED_PMIC}
	printf "${HOME}/${DEV_PATH_PMIC_C0_R01}\n" >> ${DEV_USED_PMIC};
	cp ${DEV_USED_PMIC} ${DEV_USED_DEFAULT};
	cp ${DEV_USED_PMIC} ${DEV_USED_DEFAULT}@$HOSTNAME;
	SED1LINE=$(sed -n '1 p' <${DEV_USED_DEFAULT});
	if [ -e ${SED1LINE} ]; then
		printf "Path   = ${SED1LINE}   (%bExists%b)\n" "\e[32m" "\e[0m";
	else
		printf "Path   = ${SED1LINE}   (%bDoesn't exists%b)\n" "\e[31m" "\e[0m";
	fi
elif [ ${Set_PMIC_C1_R01_Flag} == 1 ] && [ $# == 1 ]; then
	printf "\n%b%b%b---------------------------------------------------------------------------%b\n" ${HEADER_ATTRIB} ${HEADER_FGCOLR} ${HEADER_BGCOLR} ${HEADER_RSTALL};
	printf "Device = %-30s %3s %s\n" "PMIC" "" "(PMIC 7mm X 6mm C1)";
	rm -rf    ${DEV_USED_PMIC}
	touch     ${DEV_USED_PMIC}
	chmod 664 ${DEV_USED_PMIC}
	printf "${HOME}/${DEV_PATH_PMIC_C1_R01}\n" >> ${DEV_USED_PMIC};
	cp ${DEV_USED_PMIC} ${DEV_USED_DEFAULT};
	cp ${DEV_USED_PMIC} ${DEV_USED_DEFAULT}@$HOSTNAME;
	SED1LINE=$(sed -n '1 p' <${DEV_USED_DEFAULT});
	if [ -e ${SED1LINE} ]; then
		printf "Path   = ${SED1LINE}   (%bExists%b)\n" "\e[32m" "\e[0m";
	else
		printf "Path   = ${SED1LINE}   (%bDoesn't exists%b)\n" "\e[31m" "\e[0m";
	fi
elif [ ${Set_X550A_B0_V1P80_Flag} == 1 ] && [ $# == 1 ]; then
	printf "\n%b%b%b---------------------------------------------------------------------------%b\n" ${HEADER_ATTRIB} ${HEADER_FGCOLR} ${HEADER_BGCOLR} ${HEADER_RSTALL};
	printf "Device = %-30s %3s %s\n" "X550-AT2-B00" "" "(Sageville 17mm*17mm B00)";
	rm -rf    ${DEV_USED_X550A}
	touch     ${DEV_USED_X550A}
	chmod 664 ${DEV_USED_X550A}
	printf "${HOME}/${DEV_PATH_X550A_B0_V1P80}\n" >> ${DEV_USED_X550A};
	cp ${DEV_USED_X550A} ${DEV_USED_DEFAULT};
	cp ${DEV_USED_X550A} ${DEV_USED_DEFAULT}@$HOSTNAME;
	SED1LINE=$(sed -n '1 p' <${DEV_USED_DEFAULT});
	if [ -e ${SED1LINE} ]; then
		printf "Path   = ${SED1LINE}   (%bExists%b)\n" "\e[32m" "\e[0m";
	else
		printf "Path   = ${SED1LINE}   (%bDoesn't exists%b)\n" "\e[31m" "\e[0m";
	fi
elif [ ${Set_REL_X550A_B0_Flag} == 1 ] && [ $# == 1 ]; then
	printf "\n%b%b%b---------------------------------------------------------------------------%b\n" ${HEADER_ATTRIB} ${HEADER_FGCOLR} ${HEADER_BGCOLR} ${HEADER_RSTALL};
	printf "Device = %-30s %3s %s\n" "REL_PE.X550-AT2-B00" "" "(Sageville 17mm*17mm B00)";
	rm -rf    ${DEV_USED_REL_X550A}
	touch     ${DEV_USED_REL_X550A}
	chmod 664 ${DEV_USED_REL_X550A}
	
	printf "\n";
	printf "(REL_X550A_VER_NUMB) - Enter the version number you want to load (VxPxx):\n";
	read -e REL_X550A_VER_NUMB;
	
	if   [ ${REL_X550A_VER_NUMB} == "V1P30" ]; then
		printf "INFO  : Version 1.30 has been selected.\n\n"; DEV_PATH_REL_X550A_B0_VER=${DEV_PATH_REL_X550A_B0}/X550A_B0_V1P30/X550A_DEV/waste;
	elif [ ${REL_X550A_VER_NUMB} == "V1P46" ]; then
		printf "INFO  : Version 1.46 has been selected.\n\n"; DEV_PATH_REL_X550A_B0_VER=${DEV_PATH_REL_X550A_B0}/X550A_B0_V1P46/X550A_DEV/waste;
	elif [ ${REL_X550A_VER_NUMB} == "V1P60" ]; then
		printf "INFO  : Version 1.60 has been selected.\n\n"; DEV_PATH_REL_X550A_B0_VER=${DEV_PATH_REL_X550A_B0}/X550A_B0_V1P60/X550A_DEV/waste;
	else
		printf "ERROR : Incorrect version selected.\n\n";     DEV_PATH_REL_X550A_B0_VER=${DEV_PATH_REL_X550A_B0}/X550A_B0_VxPxx/X550A_DEV/waste;
		printf "INFO: These are the only available versions\n";
		printf " 1) V1P30\n";
		printf " 2) V1P46\n";
		printf " 3) V1P60\n";
		printf "\n";
	fi
	
	printf "${HOME}/${DEV_PATH_REL_X550A_B0_VER}\n" >> ${DEV_USED_REL_X550A};
	cp ${DEV_USED_REL_X550A} ${DEV_USED_DEFAULT};
	cp ${DEV_USED_REL_X550A} ${DEV_USED_DEFAULT}@$HOSTNAME;
	SED1LINE=$(sed -n '1 p' <${DEV_USED_DEFAULT});
	if [ -e ${SED1LINE} ]; then
		printf "Path   = ${SED1LINE}   (%bExists%b)\n" "\e[32m" "\e[0m";
	else
		printf "Path   = ${SED1LINE}   (%bDoesn't exists%b)\n" "\e[31m" "\e[0m";
	fi
elif [ $# == 2 ]; then
	printf "\n%b%b%b---------------------------------------------------------------------------%b\n" ${HEADER_ATTRIB} ${HEADER_FGCOLR} ${HEADER_BGCOLR} ${HEADER_RSTALL};
	printf "%b%s%b\n" "\e[31m" "#WARNING - Too many arguments!" "\e[0m";
	
	printf "\n";
	printf "%b%b%b# Time EOF : %-53s ########%b\n" ${HEADER_ATTRIB} ${HEADER_FGCOLR} ${HEADER_BGCOLR} "$(date)"           ${HEADER_RSTALL};
	printf "%b%b%b###### END - %-53s ########%b\n" ${HEADER_ATTRIB} ${HEADER_FGCOLR} ${HEADER_BGCOLR} ${FILE_NAME_HEADER} ${HEADER_RSTALL};
	exit 0; #(0=Success, 1=Failure).
fi
#### List VALID_USER with specific HOSTNAME ####
if   [ $HOSTNAME == "Bradley-Lemur"        ]; then VALID_USER="bradley";  #76_BE.
elif [ $HOSTNAME == "system76-pc"          ]; then VALID_USER="bradley";  #76_BE.
elif [ $HOSTNAME == "SJ-OPS-BEVERSON"      ]; then VALID_USER="beverson"; #QT_BE.
elif [ $HOSTNAME == "zbjcxm-l1"            ]; then VALID_USER="beverson"; #QT_BE.
elif [ $HOSTNAME == "93koffline01"         ]; then VALID_USER="beverson"; #QT_BE.
elif [ $HOSTNAME == "93koffline02"         ]; then VALID_USER="beverson"; #QT_BE.
elif [ $HOSTNAME == "93koffline03"         ]; then VALID_USER="beverson"; #QT_BE.
elif [ $HOSTNAME == "fm-ops01"             ]; then VALID_USER="beverson"; #QT_BE.
elif [ $HOSTNAME == "smartscale01"         ]; then VALID_USER="nuon";     #iTest Inc.
elif [ $HOSTNAME == "smartscale02"         ]; then VALID_USER="nuon";     #iTest Inc.
elif [ $HOSTNAME == "smartscale03"         ]; then VALID_USER="nuon";     #iTest Inc.
elif [ $HOSTNAME == "smartscale04"         ]; then VALID_USER="nuon";     #iTest Inc.
elif [ $HOSTNAME == "smartscale05"         ]; then VALID_USER="nuon";     #iTest Inc.
elif [ $HOSTNAME == "smartscale06"         ]; then VALID_USER="nuon";     #iTest Inc.
elif [ $HOSTNAME == "smartscale07"         ]; then VALID_USER="nuon";     #iTest Inc.
elif [ $HOSTNAME == "smartscale08"         ]; then VALID_USER="nuon";     #iTest Inc.
elif [ $HOSTNAME == "offline1"             ]; then VALID_USER="nuon";     #iTest Inc.
elif [ $HOSTNAME == "offline2"             ]; then VALID_USER="nuon";     #iTest Inc.
elif [ $HOSTNAME == "offline3"             ]; then VALID_USER="nuon";     #iTest Inc.
elif [ $HOSTNAME == "offline4"             ]; then VALID_USER="nuon";     #iTest Inc.
elif [ $HOSTNAME == "offline5"             ]; then VALID_USER="nuon";     #iTest Inc.
elif [ $HOSTNAME == "offline10"            ]; then VALID_USER="nuon";     #iTest Inc.
elif [ $HOSTNAME == "offline11"            ]; then VALID_USER="nuon";     #iTest Inc.
elif [ $HOSTNAME == "offline13"            ]; then VALID_USER="nuon";     #iTest Inc.
elif [ $HOSTNAME == "offline15"            ]; then VALID_USER="nuon";     #iTest Inc.
elif [ $HOSTNAME == "offline16"            ]; then VALID_USER="nuon";     #iTest Inc.
elif [ $HOSTNAME == "PS1"                  ]; then VALID_USER="bevers2";  #ISE Labs.
elif [ $HOSTNAME == "PS2"                  ]; then VALID_USER="bevers2";  #ISE Labs.
elif [ $HOSTNAME == "ps4-64"               ]; then VALID_USER="bevers2";  #ISE Labs.
elif [ $HOSTNAME == "ps5-64"               ]; then VALID_USER="bevers2";  #ISE Labs.
elif [ $HOSTNAME == "PS7-64"               ]; then VALID_USER="bevers2";  #ISE Labs.
elif [ $HOSTNAME == "ps10-64"              ]; then VALID_USER="bevers2";  #ISE Labs.
elif [ $HOSTNAME == "PS12-64"              ]; then VALID_USER="bevers2";  #ISE Labs.
elif [ $HOSTNAME == "PS15"                 ]; then VALID_USER="bevers2";  #ISE Labs.
elif [ $HOSTNAME == "ps15-64"              ]; then VALID_USER="bevers2";  #ISE Labs.
elif [ $HOSTNAME == "ps16-64"              ]; then VALID_USER="bevers2";  #ISE Labs.
elif [ $HOSTNAME == "hp207"                ]; then VALID_USER="bevers2";  #ISE Labs.
elif [ $HOSTNAME == "hp208"                ]; then VALID_USER="bevers2";  #ISE Labs.
elif [ $HOSTNAME == "hp209"                ]; then VALID_USER="bevers2";  #ISE Labs.
elif [ $HOSTNAME == "hp210"                ]; then VALID_USER="bevers2";  #ISE Labs.
elif [ $HOSTNAME == "hp224"                ]; then VALID_USER="bevers2";  #ISE Labs.
elif [ $HOSTNAME == "hp225"                ]; then VALID_USER="bevers2";  #ISE Labs.
elif [ $HOSTNAME == "hp226"                ]; then VALID_USER="bevers2";  #ISE Labs.
elif [ $HOSTNAME == "hp230"                ]; then VALID_USER="bevers2";  #ISE Labs.
elif [ $HOSTNAME == "hp231"                ]; then VALID_USER="bevers2";  #ISE Labs.
elif [ $HOSTNAME == "hp233"                ]; then VALID_USER="bevers2";  #ISE Labs.
elif [ $HOSTNAME == "hp234"                ]; then VALID_USER="bevers2";  #ISE Labs.
elif [ $HOSTNAME == "hp236"                ]; then VALID_USER="bevers2";  #ISE Labs.
else                                               VALID_USER="beverson"; #QT_BE.
fi
if [ ${Set_Touch_All_Flag} == 1 ] && [ $USER == ${VALID_USER} ]; then
	printf "\n%b%b%b---------------------------------------------------------------------------%b\n" ${HEADER_ATTRIB} ${HEADER_FGCOLR} ${HEADER_BGCOLR} ${HEADER_RSTALL};
	WaitTimeSec=3.000; #Time is in seconds.
	sleep $WaitTimeSec;
#	printf "Set_Touch_All_Flag = ${Set_Touch_All_Flag}\n";
	printf "Timestamps have been updated for specified directories and files.\n";
	CHECK_DIR_FILE=(); #Clear the new array.
	CHECK_DIR_FILE[0]=93K_EXE_DIR;
	CHECK_DIR_FILE[1]=BASH_FILE_DIR;
	CHECK_DIR_FILE[2]=BackUps_TarGz_DIR;
	CHECK_DIR_FILE[3]=bin;
	CHECK_DIR_FILE[4]=Desktop;
	CHECK_DIR_FILE[5]=Documents;                                            #(Documents/My\ Documents)
	CHECK_DIR_FILE[6]=Downloads;
	CHECK_DIR_FILE[7]=FTP_DIR;
	CHECK_DIR_FILE[8]=GIT_DIR;
	CHECK_DIR_FILE[9]=logs;
	CHECK_DIR_FILE[10]=Mail;
	CHECK_DIR_FILE[11]=Music;
	CHECK_DIR_FILE[12]=Pictures;
	CHECK_DIR_FILE[13]=devices;
	CHECK_DIR_FILE[14]=devices/BBIC5;
	CHECK_DIR_FILE[15]=devices/BBIC6;
	CHECK_DIR_FILE[16]=devices/PMIC;
	CHECK_DIR_FILE[17]=projects;
	CHECK_DIR_FILE[18]=projects/proj_Advantest;
	CHECK_DIR_FILE[19]=projects/proj_AllianceATE;
	CHECK_DIR_FILE[20]=projects/proj_Atlantic;
	CHECK_DIR_FILE[21]=projects/proj_Bermuda;
	CHECK_DIR_FILE[22]=projects/proj_Europa;
	CHECK_DIR_FILE[23]=projects/proj_Fiji;
	CHECK_DIR_FILE[24]=projects/proj_GalaxyDB;
	CHECK_DIR_FILE[25]=projects/proj_Hak5;
	CHECK_DIR_FILE[26]=projects/proj_HTML;
	CHECK_DIR_FILE[27]=projects/proj_Jamaica;
	CHECK_DIR_FILE[28]=projects/proj_Python;
	CHECK_DIR_FILE[29]=projects/proj_QTNA;
	CHECK_DIR_FILE[30]=projects/proj_RaspberryPi;
	CHECK_DIR_FILE[31]=projects/proj_Sageville;
	CHECK_DIR_FILE[32]=projects/proj_VTRAN;
	CHECK_DIR_FILE[33]=projects/proj_Zelda;
	CHECK_DIR_FILE[34]=Public;
	CHECK_DIR_FILE[35]=smarTest;
	CHECK_DIR_FILE[36]=stdf;
	CHECK_DIR_FILE[37]=Templates;
	CHECK_DIR_FILE[38]=Videos;
	CHECK_DIR_FILE[39]=workorder;
	CHECK_DIR_FILE[40]=workspace;
	CHECK_DIR_FILE[41]=workspace/workspace_7.3.2.X_64bit_AQC100_BE;
	CHECK_DIR_FILE[42]=workspace/workspace_7.3.2.X_64bit_AQC107_BE;
	CHECK_DIR_FILE[43]=workspace/workspace_7.3.2.X_64bit_AQC111C_BE;
	CHECK_DIR_FILE[44]=workspace/workspace_7.3.2.X_64bit_BBIC5_BE;
	CHECK_DIR_FILE[45]=workspace/workspace_7.4.0.X_64bit_BBIC5_BE;
	CHECK_DIR_FILE[46]=workspace/workspace_7.4.2.X_64bit_BBIC5_BE;
	CHECK_DIR_FILE[47]=workspace/workspace_7.4.3.X_64bit_BBIC6_BE;
	CHECK_DIR_FILE[48]=workspace/workspace_7.5.2.X_64bit_BBIC6_BE;
	CHECK_DIR_FILE[49]=workspace/workspace_7.4.3.X_64bit_PMIC_BE;
	CHECK_DIR_FILE[50]=workspace/workspace_7.5.2.X_64bit_PMIC_BE;
	CHECK_DIR_FILE[51]=.device_inuse_soc;
	CHECK_DIR_FILE[52]=.device_inuse_soc.AQC100_DEV;
	CHECK_DIR_FILE[53]=.device_inuse_soc.AQC107_DEV;
	CHECK_DIR_FILE[54]=.device_inuse_soc.AQC111C_DEV;
	CHECK_DIR_FILE[55]=.device_inuse_soc.BBIC5_DEV;
	CHECK_DIR_FILE[56]=.device_inuse_soc.BBIC6_DEV;
	CHECK_DIR_FILE[57]=.device_inuse_soc.PMIC_DEV;
	CHECK_DIR_FILE[58]=.device_inuse_soc.RFIC_DEV;
	CHECK_DIR_FILE[59]=.device_inuse_soc@$HOSTNAME;
	CHECK_DIR_FILE[60]=.bash_aliases;
	CHECK_DIR_FILE[61]=.bash_logout;
	CHECK_DIR_FILE[62]=.bash_profile;
	CHECK_DIR_FILE[63]=.bashrc;
	CHECK_DIR_FILE[64]=.login;
	CHECK_DIR_FILE[65]=.profile;
	CHECK_DIR_FILE[66]=.tcshrc;
	CHECK_DIR_FILE[67]=MAKE_APT_GET_COMMAND_V2P19.sh;
	CHECK_DIR_FILE[68]=${FILE_NAME_HEADER};
	CHECK_DIR_FILE[69]=${FILE_NAME_HEADER//.sh/.py};
	
	#printf "\nTotal %s = %d\n\n" "CHECK_DIR_FILE" ${#CHECK_DIR_FILE[@]};   #DEBUG ONLY. REMOVE WHEN FINISHED.
	
	#### Set the for-loop stop variable. ####
	LoopBeg=$(( 0 ));                                                       #Minimum value = 0;
	LoopEnd=$(( ${#CHECK_DIR_FILE[@]} ));                                   #Maximum value = 70;
	
	TOUCH_DIR_FILE=(); #Clear the new array.
	
	EXISTS_PASS="Exists";
	EXISTS_FAIL="Doesn't exists";
	
	DO_PRINT_COMMAND="YES"; #(YES/NO)
	DO_TOUCH_COMMAND="YES"; #(YES/NO)
	DO_CHECK_EXISTSP="YES"; #(YES/NO)
	for (( ZAn=${LoopBeg}; ZAn<${LoopEnd}; ZAn++ )); do
		if [ $ZAn = 0 ]; then ZBn=0; fi
		COUTPASS=$(printf '(%2d) %-50s (%b%-14s%b)' $(( ${ZAn} + 1 )) "${CHECK_DIR_FILE[${ZAn}]}" "\e[32m" "${EXISTS_PASS}" "\e[0m");
		COUTFAIL=$(printf '(%2d) %-50s (%b%-14s%b)' $(( ${ZAn} + 1 )) "${CHECK_DIR_FILE[${ZAn}]}" "\e[31m" "${EXISTS_FAIL}" "\e[0m");
		if   [ -d ${CHECK_DIR_FILE[${ZAn}]} ]; then
			if [ ${DO_PRINT_COMMAND} == "YES" ];      then printf "${COUTPASS}%s\n" "(DIR)"; fi
		#	if [ ${DO_TOUCH_COMMAND} == "BYPASSED" ]; then touch ${CHECK_DIR_FILE[${ZAn}]}; fi
		#	if [ ${DO_CHECK_EXISTSP} == "YES" ];      then TOUCH_DIR_FILE+=(${CHECK_DIR_FILE[${ZAn}]}); fi
			if [ ${DO_CHECK_EXISTSP} == "YES" ];      then TOUCH_DIR_FILE[${ZBn}]=${CHECK_DIR_FILE[${ZAn}]}; ZBn=$((ZBn + 1)); fi
		elif [ -f ${CHECK_DIR_FILE[${ZAn}]} ]; then
			if [ ${DO_PRINT_COMMAND} == "YES" ];      then printf "${COUTPASS}%s\n" "(FILE)"; fi
		#	if [ ${DO_TOUCH_COMMAND} == "BYPASSED" ]; then touch ${CHECK_DIR_FILE[${ZAn}]}; fi
		#	if [ ${DO_CHECK_EXISTSP} == "YES" ];      then TOUCH_DIR_FILE+=(${CHECK_DIR_FILE[${ZAn}]}); fi
			if [ ${DO_CHECK_EXISTSP} == "YES" ];      then TOUCH_DIR_FILE[${ZBn}]=${CHECK_DIR_FILE[${ZAn}]}; ZBn=$((ZBn + 1)); fi
		else
			if [ ${DO_PRINT_COMMAND} == "YES" ];      then printf "${COUTFAIL}\n"; fi
		fi
	done
	printf "\n";
	if [ ${DO_PRINT_COMMAND} == "YES" ];      then printf "Total (Exists) = %d\n" ${#TOUCH_DIR_FILE[@]};  fi
	if [ ${DO_PRINT_COMMAND} == "BYPASSED" ]; then printf "TOUCH_DIR_FILE = %s\n" "${TOUCH_DIR_FILE[*]}"; fi
	
	if [ ${DO_TOUCH_COMMAND} == "YES" ]; then
		if [ ${#TOUCH_DIR_FILE[@]} != 0 ]; then touch ${TOUCH_DIR_FILE[*]}; fi
	fi
elif [ ${Set_Touch_All_Flag} == 1 ] && [ $USER != ${VALID_USER} ]; then
	printf "\n%b%b%b---------------------------------------------------------------------------%b\n" ${HEADER_ATTRIB} ${HEADER_FGCOLR} ${HEADER_BGCOLR} ${HEADER_RSTALL};
	printf "USER     = $USER %-6s (%b%-16s%b)\n" "" "\e[31m" "NOT A VALID USER" "\e[0m";
fi
printf "\n";
printf "%b%b%b# Time EOF : %-53s ########%b\n" ${HEADER_ATTRIB} ${HEADER_FGCOLR} ${HEADER_BGCOLR} "$(date)"           ${HEADER_RSTALL};
printf "%b%b%b###### END - %-53s ########%b\n" ${HEADER_ATTRIB} ${HEADER_FGCOLR} ${HEADER_BGCOLR} ${FILE_NAME_HEADER} ${HEADER_RSTALL};
