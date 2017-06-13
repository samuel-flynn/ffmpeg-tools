# Purpose: Concatenate multiple files into one longer one

# Documentation: https://ffmpeg.org/ffmpeg-all.html#concat-3

from ConfigReader import ConfigReader

config = ConfigReader()

SET FILTER="[0:0] [0:1] [1:0] [1:1] [2:0] [2:1] concat=n=3:v=1:a=1 [vout] [aout]"

SET MAP=-map "[vout]" -map "[aout]" "..\files\out.mp4"

SET STARTTIME= &::-ss 30
SET DURATION= &::-t 3

SET IN1=%STARTTIME% %DURATION% -i "..\files\in1.mp4"
SET IN2=%STARTTIME% %DURATION% -i "..\files\in2.mp4"
SET IN3=%STARTTIME% %DURATION% -i "..\files\in3.mp4"




..\bin\ffmpeg.exe ^
 -sn ^
 %IN1% %IN2% %IN3% ^
 -filter_complex %FILTER% ^
 %MAP%