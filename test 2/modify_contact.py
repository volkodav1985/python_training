from model.contact import Contact
import random

def test_modify_contact_name(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Test"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.modify_contact_by_id(contact.id)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts.remove(contact)
    assert old_contacts == new_contacts

