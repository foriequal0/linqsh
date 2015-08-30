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

        p = subprocess.Popen(processArgs, env={
            args.variable: record
        }, stdout=subprocess.PIPE)

        for line in p.stdout.readlines():
            print(line)