import argparse
import sys
import os.path
import linqsh.env as env
import linqsh.cmds
import importlib
import linqsh.utils.split
from asq.initiators import query
from asq.selectors import identity

__author__ = 'foriequal0'


def add_common_arguments(parser):
    pass


def main():
    basename = os.path.basename(sys.argv[0])
    if basename in ['linqsh', 'linqsh.py']:
        symbolic=False
    else:
        symbolic=True
        symbolic_cmd = basename

    env.import_env_var()

    parser = argparse.ArgumentParser()
    if symbolic:
        module = importlib.import_module('linqsh.cmds.' + symbolic_cmd)

        env.add_arguments(parser)
        add_common_arguments(parser)
        module.add_arguments(parser)

        args = parser.parse_args()
        env.override_from_args(args)
        module.cmd_main(args)

    else:
        module_dict = query(linqsh.cmds.__all__)\
            .to_dictionary(identity,
                           lambda x: importlib.import_module('linqsh.cmds.' + x, ))

        subparsers = parser.add_subparsers(dest='cmd')
        for cmd in module_dict:
            subparser = subparsers.add_parser(cmd)

            add_common_arguments(subparser)
            env.add_arguments(subparser)
            module_dict[cmd].add_arguments(subparser)

        args = parser.parse_args()
        env.override_from_args(args)
        module_dict[args.cmd].cmd_main(args)


if __name__ == "__main__":
    main()
