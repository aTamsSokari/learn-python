from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

in_file = open(from_file)

# when you use open(from_file).read(), you don't need to close the file again

indata = in_file.read()

print "The input file is %d bytes long"% len(indata)

print "Does the output file exist? %r"% exists(to_file)
print "Ready? Hit RETURN to continue. Not ready? Hit CTRL-C(^C) to abort."
raw_input()

out_file = open(to_file, "w")
out_file.write(indata)

print "Alright! All done."

out_file.close()
in_file.close()
