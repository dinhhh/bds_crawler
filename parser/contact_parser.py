from bs4 import BeautifulSoup
import re
import json
from object import objs

def parse(html: str) -> objs.Contact:
    soup = BeautifulSoup(html, "html.parser")
    scripts_tag = soup.find_all("script")
    func_info = ""
    for script in scripts_tag:
        if "callContactBox" in script.text:
            func_info = script.text
            break
    contactbox_marker = "FrontEnd.Product.Details.ContactBox("
    t = func_info[func_info.index(contactbox_marker) + len(contactbox_marker):-1]
    # remove special character
    info_str = re.sub(r'\n\s*(\S+)\s*:', r'\n"\1":', t[0:t.index(");")])
    info_str = info_str.replace("'", '"').replace("`", '"')
    # remove not valid json string
    info_str = info_str[0:info_str.index('"adbutlerConfig')]
    last_comma_index = info_str.rfind(",")
    info_str = info_str[0:last_comma_index] + info_str[last_comma_index + 1:-1]
    info_str = info_str + "}"
    info_dict = json.loads(info_str)
    contact = objs.Contact()
    contact.name = info_dict["nameSeller"]
    contact.email = info_dict["emailSeller"]
    contact.user_id = info_dict["userId"]
    contact.mobile = info_dict["mobileSeller"]
    return contact

