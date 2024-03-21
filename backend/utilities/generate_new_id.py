import uuid as id
import random as r

def generate_new_id_by_firstname_lastname(attributes):
    new_id = id.uuid4(
        id.NAMESPACE_DNS,
        '{0}{1}{2}'.format(attributes["Lastname"],attributes["Firstname"], r.randint(0,1000))
    )
    return new_id

def generate_new_id_by_username_lastname(attributes):
    new_id = id.uuid4(
        id.NAMESPACE_DNS,
        '{0}{1}{2}'.format(attributes["Username"],attributes["Lastname"], r.randint(0,1000))
    )
    return new_id