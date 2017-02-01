#!/usr/bin/python

import sys,getopt,json,random

file = "planets.json"
count = 10

# Parse CLI options
try:
	opts,args = getopt.getopt(sys.argv[1:],'f:c:')
except getopt.GetoptError:
	print 'generate.py -f <inputfile>'
	sys.exit(2)

for opt,arg in opts:
	if opt == '-f':
		file = arg
	if opt == '-c':
		count = int(arg)

# Read file
f = open(file,'r')
contents = f.read()
parts = json.loads(contents)

# Generate names
for i in range(count):
	middleParts = random.randint(0,2) # Number of middle parts

	name = random.choice(parts["start"])
	if(len(parts["middle"]) > 0):
		for j in range(middleParts):
			name += random.choice(parts["middle"])
	name += random.choice(parts["end"])

	print name