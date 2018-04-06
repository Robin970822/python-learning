import sys

script, infile = sys.argv

def print_all(f):
    print f.read()

def rewind(f):
    f.seek(0)

def print_a_line(line, f):
    print line, f.readline(),

current = open(infile)

print "First let's print the whole file:\n"

print_all(current)

print "Now let's rewind,kind of like a tape."

rewind(current)

print "Let's print three lines:"

print_a_line(1,current)
print_a_line(2,current)
print_a_line(3,current)
