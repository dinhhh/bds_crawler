import json

class Contact():
    name: str
    mobile: str
    email: str
    user_id: str

    def __init__(self):
        self.name = None
        self.mobile = None
        self.email = None
        self.user_id = None

    def reprJSON(self):
        return dict(name=self.name, mobile=self.mobile, email=self.email, user_id=self.user_id)

class Price():
    # Thong tin gia tien
    total_amt: str
    amt_per_m: str

    def __init__(self):
        self.total_amt = None
        self.amt_per_m = None

    def reprJSON(self):
        return dict(total_amt=self.total_amt, amt_per_m=self.amt_per_m)

class Project():
    # Thong tin du an
    name: str
    desc: str
    investor: str
    status: str

    def __init__(self):
        self.name = None
        self.desc = None
        self.investor = None
        self.status = None

    def reprJSON(self):
        return dict(name=self.name, desc=self.desc, investor=self.investor, status=self.status)

class Address():
    # Thong tin dia chi
    full_add: str
    # TODO: delete comment for parsed fields
    # province_add: str
    # district_add: str
    # ward_add: str
    # street_add: str
    # num_add: str
    # longitude: float
    # latitude: float

    def __init__(self):
        self.full_add = None
        self.province_add = None
        self.district_add = None
        self.ward_add = None
        self.street_add = None
        self.num_add = None
        self.longitude = None
        self.latitude = None

    def reprJSON(self):
        return dict(full_add=self.full_add
                    #, province_add=self.province_add, district_add=self.district_add, ward_add=self.ward_add,
                    # street_add=self.street_add, num_add=self.num_add, longitude=self.longitude, latitude=self.latitude
        )

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
    id: str
    link: str
    title: str
    desc: str
    price: Price
    project: Project
    cus_attr: list[dict]
    contact: Contact
    address: Address
    created_date: str
    expire_date: str
    post_category: str
    post_id: str

    # calculate fields
    total_price: str
    price_per_m2: str

    def __init__(self):
        self.id = None
        self.link = None
        self.title = None
        self.desc = None
        self.price = None
        self.project = None
        self.cus_attr = None
        self.contact = None
        self.address = None
        self.created_date = None
        self.expire_date = None
        self.post_category = None
        self.post_id = None

        self.total_price = None
        self.price_per_m2 = None

    def reprJSON(self):
        js = dict(id=self.id, link=self.link, title=self.title, desc=self.desc, price=self.price,
                    project=self.project, contact=self.contact, address=self.address,
                    created_date=self.created_date, expire_date=self.expire_date, post_category=self.post_category,
                    total_price=self.total_price, price_per_m2=self.price_per_m2)
        for cus_att in self.cus_attr:
            for key in cus_att.keys():
                js[key] = cus_att[key]
        return js

class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj, 'reprJSON'):
            return obj.reprJSON()
        else:
            return json.JSONEncoder.default(self, obj)

if __name__ == '__main__':
    bds = Bds()
    bds.id = 'test'
    cus_attrs = [{"Hướng nhà":"Nam"}, {"Số toilet":"1 phòng"}]
    bds.cus_attr = cus_attrs
    print(bds.reprJSON())
