from object.objs import Address

def parse(address: str) -> Address:
    add = Address()
    add.full_add = address
    return add