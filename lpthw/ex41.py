import random
import sys
from urllib import urlopen

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
    "class %%%(%%%):": "make a class named %%% that is-a %%%.",
    "class %%%(object):\n\tdef __init__(self, ***)":
    "class %%% has-a __init__ that takes self and *** parameters",
    "class %%%(object):\n\tdef ***(self, @@@)":
    "class %%% has-a function named *** that takes self and @@@ parameters",
    "*** = %%%()": "set *** to an instance of %%%",
    "***.***(@@@)":
    "from *** get the *** function, and call it with the parameters: self and @@@.",
    "***.*** = '***'": "From *** get the *** attribute and set it to '***'"
}

print PHRASES