import sys
import linqsh.env as env
import linqsh.utils.split as split


__author__ = 'foriequal0'


COMMAND='from_line'


def add_arguments(parser):
    pass


def cmd_main(args):
    for record in split.iter_stream(sys.stdin):
        fields = split.field_split(record)

        print(env.OFS.join(fields), end=env.ORS)