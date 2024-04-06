# Set up
- Install Chrome browser
- Install Gologin
- Install Chrome driver (need comfortable version with Chrome browser) at [reference](https://googlechromelabs.github.io/chrome-for-testing/#stable)
- Add config file (cfg.yaml) in project folder

# Docs
- [Selenium](https://selenium-python.readthedocs.io/locating-elements.html)
- [Selenium tutorial](https://www.scrapingbee.com/blog/selenium-python/#the-find_element-methods)
- [Gologin](https://github.com/gologinapp/pygologin)

# How to run
```commandline
pip install requirements.txt
```
For crawling one page
```commandline
python main.py --one_page --url='specific_url_at_batdongsan.com.vn'
```
For crawling range of page
```commandline
python main.py --more_pages --start=1 --end=10
```