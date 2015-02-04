import re
import sys


def get_count (regex, str):
	m=regex.search(line)
	if not m:
		return 0
	return int(m.group(1))


display_sha=True


commits=0
insertions=0
deletions=0

cregex=re.compile("^commit ([a-f0-9]+)")
regex=re.compile("^ [0-9]")
iregex=re.compile("([0-9]+) insert")
dregex=re.compile("([0-9]+) delet")
for line in sys.stdin:
		
	c=cregex.match(line)
	if c:
		commits+=1
		if display_sha:
			print c.group(1)
	if regex.match(line):
		i=get_count(iregex,line)
		insertions+=i
		d=get_count(dregex,line)
		deletions+=d

print "Commits: {0}".format(commits)
print "Insertions: {0}".format(insertions)
print "Deletions: {0}".format(deletions)
