# linqsh
I don't know why this should exist, but I made this.

# usage
## example file item_group
```
group	list
-------|------
00000	a.lst
00001	b.lst
00002	c.lst
00003	b.lst
```

## example
```bash
$ export FS='\t'
$ export RS='\n'
$ cat item_group | tail -n+3 | from_stdin | filter x 'grep -e item1 -f $x2' | foreach 'echo $1'
00001
00002
```
