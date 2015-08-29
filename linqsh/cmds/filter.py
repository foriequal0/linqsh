import sys
import subprocess
import argparse
import linqsh.env as env
import linqsh.utils.split as split

__author__ = 'foriequal0'


COMMAND='filter'


def add_arguments(parser: argparse.ArgumentParser):
    parser.add_argument('command',
                       help='ex: [ $1 == "asdf" ]')
    pass


def cmd_main(args):
    for record in split.iter_stream(sys.stdin):
        fields = split.field_split(record)

        p = subprocess.Popen([env.SHELL, '-c', args.command, record])
        if p.returncode == 0:
            print(record)
        else:
            continue