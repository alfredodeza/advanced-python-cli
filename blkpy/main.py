import click
from blkpy.util import run_lsblk

# Example usage:
# blkpy vda1

# Requirement
# blkpy info vda1


@click.group()
@click.option('--verbose', '-v', is_flag=True)
def main(verbose):
    print(f"Verbose: {verbose}")
    pass


@main.command()
@click.argument('device')
def info(device):
    print(f"Device: {device}")
    print(f"{run_lsblk(device)}")


@main.command()
@click.argument('device')
def nice(device):
    print(f"Device: {device}")
    print(f"{run_lsblk(device, nice=True)}")