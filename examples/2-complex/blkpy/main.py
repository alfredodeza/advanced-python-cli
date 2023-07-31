import click
from blkpy.util import run_lsblk


# 1. Make the verbose flag global using context
# 2. Add flags with types associated with them
# 3. Use the special context object to pass data between commands

@click.group()
@click.option('--verbose', '-v', is_flag=True)
@click.option('--debug-level', '-d', type=float, default=1)
@click.pass_context
def main(ctx, verbose, debug_level):
    ctx.ensure_object(dict)
    ctx.obj.update(locals())
    if type(debug_level) == int:
        print("Debug level is 100")
    else:
        print(f"the type of debug level is {type(debug_level)}")
    print(f"Verbose: {verbose}")
    pass


@main.command()
@click.argument('device')
@click.pass_context
def info(ctx, device):
    verbose = ctx.obj['verbose']
    if verbose:
        print(f"Device: {device}")
        print(f"{str(ctx.obj)}")
    print(f"{run_lsblk(device)}")
    
