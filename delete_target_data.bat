@echo off
rem Script to clear the current target data including database, logfile, and all media files

rem List of files and directories to be deleted
set items="instamon.log" "target.db" "target"

rem Loop through and delete each item
for %%i in (%items%) do (
    if exist %%i (
        echo Deleting: %%i
        if exist %%i\ (
            rmdir /s /q %%i
        ) else (
            del /q %%i
        )
    ) else (
        echo Not found: %%i
    )
)

echo Deletion complete.
