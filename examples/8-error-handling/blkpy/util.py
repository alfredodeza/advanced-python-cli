import subprocess
import shlex
import json
import logging
from json.decoder import JSONDecodeError

log = logging.getLogger(__name__)

# create a function that runs suprocess and returns the output
def run_command(command):
    log.debug(f'Running command: {command}')
    cmd = shlex.split(command)
    output = subprocess.check_output(cmd)
    return output

def run_lsblk(device):
    """
    Runs lsblk command and produces JSON output:

    lsblk -J -o NAME,SIZE,TYPE,MOUNTPOINT
    {
    "blockdevices": [
        {"name": "vda", "size": "59.6G", "type": "disk", "mountpoint": null,
            "children": [
                {"name": "vda1", "size": "59.6G", "type": "part", "mountpoint": "/etc/hosts"}
            ]
        }
    ]
    }
    """
    command = f'lsblk -J -o NAME,SIZE,TYPE,MOUNTPOINT'
    output = run_command(command)
    try:
        devices = json.loads(output)['blockdevices']
    except JSONDecodeError as e:
        log.exception("Error decoding JSON output from lsblk")
        devices = []
    for parent in devices:
        if parent['name'] == device:
            return parent
        for child in parent.get('children', []):
            if child['name'] == device:
                return child

