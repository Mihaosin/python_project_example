from model.contact import Contact
from data.add_group import random_string
import os.path
import json
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


testdata = [Contact(firstname="", lastname="")] + [
            Contact(firstname=random_string("firstname"+str(i), 10), lastname=random_string("lastname", 20))
            for i in range(n)
]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../", f)


with open(file, "w") as out:
    out.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))