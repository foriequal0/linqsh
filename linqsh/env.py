import os
import sys
import codecs
from unicodedata import category


def import_env_var():
    env = sys.modules[__name__]
    env.SHELL = os.getenv('SHELL', '/usr/sh')
    env.PWD = os.getenv('PWD')
    env.FS = os.getenv('FS', ' ')
    env.RS = os.getenv('RS', '\n')
    env.OFS = os.getenv('OFS', env.FS)
    env.ORS = os.getenv('ORS', env.RS)
    env.JSON = os.getenv('LINQSH_JSON', 0)


def add_arguments(parser):
    env = sys.modules[__name__]
    group = parser.add_argument_group('override environment variables')

    group.add_argument('-s', '--shell',
                       default=env.SHELL,
                       help='(default: %(default)s)')

    group.add_argument('--working-dir',
                       metavar='PWD',
                       default=env.PWD,
                       help='(default: %(default)s)')

    group.add_argument('--fs',
                       default=env.FS,
                       help='(default: {})'.format(escape(env.FS)))

    group.add_argument('--rs',
                       default=env.RS,
                       help='(default: {})'.format(escape(env.RS)))

    group.add_argument('--ofs',
                       default=env.OFS,
                       help='(default: {})'.format(escape(env.OFS)))

    group.add_argument('--ors',
                       default=env.ORS,
                       help='(default: {})'.format(escape(env.ORS)))

    group.add_argument('-j', '--json', action='store_true')


def override_from_args(args):
    env = sys.modules[__name__]
    env.SHELL = args.shell
    env.PWD = args.working_dir
    env.FS = unescape(args.fs)
    env.RS = unescape(args.rs)
    env.OFS = unescape(args.ofs)
    env.ORS = unescape(args.ors)
    env.JSON = args.json


def escape(str):
    escaped = []
    for c in str:
        if category(c) == 'Cc':
            escaped.append(c.encode('unicode-escape').decode())
        else:
            escaped.append(c)
    return "'" + ''.join(escaped) + "'"


def unescape(str):
    return codecs.decode(str, "unicode_escape")
