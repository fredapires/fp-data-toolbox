def schedule_task(path: str, schedule: str) -> None:
    """
    A function that creates a scheduled task using the Windows Task Scheduler. 
    The task will run the specified script at the specified schedule.

    Includes .py scripts, but could also be .bat scripts

    Parameters:
    path (str): The full file path to the script that should be run as the scheduled task.
    schedule (str): The schedule for the task to run. This should be in the format understood by the Windows Task Scheduler. Examples include "daily" or "monthly".

    Returns:
    None
    """
    import subprocess

    subprocess.run(['schtasks', '/create', '/tn',
                   'MyTask', '/tr', path, '/sc', schedule])
