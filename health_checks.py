#!/usr/bin/env python3

import shutil
import psutil

def check_disk_usage(disk):
    """Checks the amount of free space on the disk. 
    Returns True if free space is > 20.
    
    Args: 
        disk. A path passed in as an argument."""
    du = shutil.disk_usage(disk)
    free = du.free/du.total * 100

    return free > 20

def check_cpu_usage():
    """Checks the amount of workload on a CPU.
    Returns True if usage is less than 75 percent."""
    usage = psutil.cpu_percent(1)
    return usage < 75

if not check_disk_usage('/'):
    print("System is running low on space.")
elif not check_cpu_usage():
    print('The CPU is being overloaded.')
elif not check_disk_usage and not check_cpu_usage():
    print("System is running low on space and the CPU is being overloaded.")
else:
    print("Everything is OK!")