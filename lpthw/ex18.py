def print_two(*args):
    arg1, arg2 = args
    print "Arg1: %r, Arg2: %r." % (arg1, arg2)

def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r." % (arg1, arg2)

def print_one(arg):
    print "arg: %r." % arg

def print_none():
    print "I got nothin'."

print_two("Tams", "Sokari")
print_two_again("Thelma", "Nsofor")
print_one("Andela")
print_none()