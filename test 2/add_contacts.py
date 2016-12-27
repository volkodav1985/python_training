# -*- coding: utf-8 -*-

from model.contact import Contact






def test_add_contacts(app, json_contacts):
    contact = json_contacts
    old_contacts = app.group.get_contact_list()
    app.group.create(contact)
    assert len(old_contacts) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_groups, key=Contact.id_or_max)


