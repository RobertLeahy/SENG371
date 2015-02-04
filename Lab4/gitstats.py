import re
import sys


class GitStats:

	def __get_count (self, regex, str):
		m=regex.search(str)
		if not m:
			return 0
		return int(m.group(1))
	
	def __init__ (self, file):
		self.commits=0
		self.insertions=0
		self.deletions=0
		self.last=""
		cregex=re.compile("^commit ([a-f0-9]+)")
		regex=re.compile("^ [0-9]")
		iregex=re.compile("([0-9]+) insert")
		dregex=re.compile("([0-9]+) delet")
		last=""
		for line in file:
			c=cregex.match(line)
			if c:
				self.commits+=1
				self.last=c.group(1)
			if regex.match(line):
				i=self.__get_count(iregex,line)
				self.insertions+=i
				d=self.__get_count(dregex,line)
				self.deletions+=d


if len(sys.argv)>1:
	with open(sys.argv[1]) as f:
		stats=GitStats(f)
else:
	stats=GitStats(sys.stdin)


print "Last commit processed: {0}".format(stats.last)
print "Commits: {0}".format(stats.commits)
print "Insertions: {0}".format(stats.insertions)
print "Deletions: {0}".format(stats.deletions)
