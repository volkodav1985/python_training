# -*- coding: utf-8 -*-

from model.contact import Contact






def test_add_contacts(app, db, json_contacts):
    contact = json_contacts
    old_contacts = db.get_contact_list()
    app.group.create(contact)
    new_groups = db.get_group_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_groups, key=Contact.id_or_max)


