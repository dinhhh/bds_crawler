from dataclasses import dataclass

class Contact():
    name: str
    mobile: str
    email: str
    user_id: str

class Price():
    # Thong tin gia tien
    total_amt: str
    amt_per_m: str

class Project():
    # Thong tin du an
    name: str
    desc: str
    investor: str
    status: str

class Address():
    # Thong tin dia chi
    full_add: str
    province_add: str
    district_add: str
    ward_add: str
    street_add: str
    num_add: str
    longitude: float
    latitude: float

class BdsCustomAttribute():
    # Thong tin ve bat dong san
    # area: str
    # num_bedroom: str
    # num_wc: str
    # num_floor: str
    # house_direct: str
    # facade_length: str
    # road_length: str
    # iterator_desc: str
    key: str
    value: str


class Bds():
    link: str
    title: str
    desc: str
    price: Price
    project: Project
    cus_attr: list[dict]
    contact: Contact
    address: Address
    # TODO:
    created_date: str
    expire_date: str
    post_category: str
    post_id: str
