import re

def clean(i: str) -> str:
    o = remove_spaces(i)
    return o

def remove_spaces(i: str) -> str:
    return " ".join(i.split())

def get_all_num_from_str(s: str) -> list[str]:
    return re.findall(r'[-+]?(?:\d*\,*\d+)', s)


if __name__ == '__main__':
    s = 'Công ty CP Đầu tư Xây dựng số 9 Hà Nội\n                    '
    print(clean(s))