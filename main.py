class Contacts:
    current_id = 1

    def __init__(self):
        self.contacts = []

    def list_contacts(self):
        return self.contacts

    def add_contacts(self, name, phone, email, favorite):
        self.contacts.append(
            {
                "id": Contacts.current_id,
                "name": name,
                "phone": phone,
                "email": email,
                "favorite": favorite,
            }
        )
        Contacts.current_id += 1

    def get_contact_by_id(self, id):
        for dicts in self.contacts:
            if id == dicts.get("id"):
                return dicts


con = Contacts()
con.add_contacts("Ron", "856564547", "hgfg@ghf.com", True)

print(con.list_contacts())

print(con.get_contact_by_id(5))
