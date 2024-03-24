
def clean(i: str) -> str:
    o = remove_spaces(i)
    return o

def remove_spaces(i: str) -> str:
    return " ".join(i.split())

if __name__ == '__main__':
    s = 'Công ty CP Đầu tư Xây dựng số 9 Hà Nội\n                    '
    print(clean(s))