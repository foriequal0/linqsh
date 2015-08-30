import sys
import subprocess
import argparse
import linqsh.env as env
import linqsh.utils.split as split


def add_arguments(parser: argparse.ArgumentParser):
    parser.add_argument('variable')
    parser.add_argument('command')
    pass


def cmd_main(args):
    for record in split.iter_stream(sys.stdin):
        fields = split.field_split(record)

        processArgs = [env.SHELL, '-c', args.command]

        varPack = dict([(args.variable, record)])

        for index, val in enumerate(fields):
            varPack[args.variable+str(index)] = val

        p = subprocess.Popen(processArgs, env=varPack)

        if p.returncode == 0:
            print(record)
        else:
            continue