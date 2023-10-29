@echo off
::
:: Schedules a task to run a specified script at a given interval using the Windows Task Scheduler
::
:: Usage: schedule_task.bat path_to_script interval (minutes)
::
:: Example: schedule_task.bat "C:\my_script.py" 60
::
:: This example schedules the script "C:\my_script.py" to run every 60 minutes.
::
:: :param path: the path to the file that should be scheduled to run
:: :type path: str
:: :param schedule: the schedule on which the file should be run, formatted as a cron schedule string
:: :type schedule: str

set path=%1
set schedule=%2

schtasks /create /tn "MyTask" /tr "%path%" /sc %schedule%

rem Confirm the task has been created
schtasks /query /tn "Run Script"

echo Task Scheduled successfully!
