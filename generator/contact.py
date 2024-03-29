from model.contact import Contact
import random
import string
import os.path
import json
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts","file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)


n = 5
f = "data/contacts.json"


for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + " "*2
    # + string.punctuation
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", lastname="")] + [
            Contact(firstname=random_string("firstname"+str(i), 10), lastname=random_string("lastname", 20))
            for i in range(n)
]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../", f)


with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))