import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--one-page', action='store_true', help='crawl this page only')

    args = parser.parse_args()
    print(args)
    pass