from model.contact import Contact
import random
import string
import os.path
import json
import getopt
import sys



try:
    opts, args = getopt.getopt(sys.argv[1:],  "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.ext(2)


n = 5
f = "data/contacts/json"



for o , a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a







def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])



testdata = [Contact(firstname="", lastname="", homephone="", mobilephone="", workphone="")] + [
    Contact(firstname=random_string("firstname", 10),lastname=random_string("lastname", 20),homephone=("homephone", 20), mobilephone=("mobilephone",20),workphone=("workphone", 20),secondaryphone=("secondaryphone,20"))
    for i in range(2)
]



file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file, "..", f)



with open(file, "w") as out:
    out.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))