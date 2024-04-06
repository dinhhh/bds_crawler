import argparse
import run

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--one_page', action='store_true', help='flag to indicate crawl 1 page only')
    parser.add_argument('--url', help='crawl this URL only')
    parser.add_argument('--more_pages', action='store_true', help='flag to indicate crawl many pages')
    parser.add_argument('--start_page', help='start index page')
    parser.add_argument('--end_page', help='end index page')

    args = parser.parse_args()
    if args.one_page and args.url is not None:
        run.crawl_page(args.url)

    if args.more_pages and args.start_page is not None and args.end_page is not None:
        run.crawl_pages(int(args.start_page), int(args.end_page))
