import sys
import linqsh.env as env
import linqsh.utils.split as split


def add_arguments(parser):
    pass


def cmd_main(args):
    for record in split.iter_stream(sys.stdin):
        fields = split.field_split(record)

        print(env.OFS.join(fields), end=env.ORS)