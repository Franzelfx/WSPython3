"""07 · Dictionaries

Key-Value Paare. Zugriff via key statt Index.

Übung: Dict mit deinen Kontaktdaten.
"""

person = {'name': 'Ben', 'age': 30}
print(person['name'])
person['city'] = 'Berlin'

# Übung: Dict mit deinen Kontaktdaten
contact = {'name': 'Fabian', 'email': 'fabian@example.com', 'phone': '123456789'}
print(contact['name'])
contact['address'] = 'Musterstraße 1'
print(contact['address'])
print(contact)