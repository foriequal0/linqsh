__author__ = 'foriequal0'

# TODO : RS split, json list split, json object k/v split < Do I need this?
import io
import re
import sys
import linqsh.env as env

def field_split(record):
    if len(env.FS) == 1:
        return record.split(env.FS)
    else:
        return re.split(env.FS, record)


def iter_stream(buffer: io.TextIOBase):
    if len(env.RS) == 1:
        generator = char_splitter(buffer, env.RS)
    else:
        generator = regex_splitter(buffer, env.RS)

    return generator


def char_splitter(buffer: io.TextIOBase, delim):
    buf = ""
    eof = False
    while True:
        chunk = buffer.readline(1024)
        if not chunk:
            eof = True

        buf += chunk
        split = buf.split(delim)
        if len(split) > 0:
            if split[-1].endswith(delim) or eof:
                for s in split:
                    yield s
                buf = ""
            else:
                for s in split[0:-1]:
                    yield s
                buf = split[-1]

        if eof:
            break


def regex_splitter(buffer: io.TextIOBase, pattern):
    buf = ""
    eof = False

    regex = re.compile(pattern)
    while True:
        chunk = buffer.readline(1024)
        if not chunk:
            eof = True

        buf += chunk
        split = regex.split(buf)
        if len(split) > 0:
            if regex.match(split[-1]) or eof:
                for s in split:
                    yield s
                buf = ""
            else:
                for s in split[0:-1]:
                    yield s
                buf = split[-1]

        if eof:
            break

