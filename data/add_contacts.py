from model.contact import Contact
import random
import string



constant = [
    Contact(firstname="firstname1", lastname="lastname1", homephone="homephone1", mobilephone="mobilephone1", secondaryphone="secondaryphone1", workphone="workphone1"),
    Contact(firstname="firstname2", lastname="lastname2", homephone="homephone2", mobilephone="mobilephone2", secondaryphone="secondaryphone2", workphone="workphone2")
]





def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])



testdata = [Contact(firstname="", lastname="", homephone="", mobilephone="", workphone="")] + [
    Contact(firstname=random_string("firstname", 10),lastname=random_string("lastname", 20),homephone=("homephone", 20), mobilephone=("mobilephone",20),workphone=("workphone", 20),secondaryphone=("secondaryphone,20"))
    for i in range(2)
]