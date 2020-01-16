@echo off

for %%f in (E:\youershuo\video\*.mp4) do (
    @echo %%f
    set "FILE_NAME=%%~nf"
    D:\tools\ffmpeg-4.2.1-win64-static\bin\ffmpeg.exe -i E:\youershuo\video\test.mp4 E:\youershuo\mp3\%%~nf.mp3
)
pause