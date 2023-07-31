import click
from blkpy.util import run_lsblk

# 1. Allow the verbose flag to be an environment variable
# 2. Add a new option that allows setting the level of verbosity, 
# from 1 to 4 with a default


@click.command()
@click.option('--verbose', '-v', is_flag=True)
@click.option('--debug-level', '-d', envvar='BLKPY_DEBUG_LEVEL', type=int, default=1, help='Set the debug optionally with an environment variable')
@click.argument('device')
def main(device, verbose, debug_level):
    print(f"Device: {device}")
    print(f"Verbose: {verbose}")
    print(f"Debug level: {debug_level}")
    #print(f"{run_lsblk(device)}")
