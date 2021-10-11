# Hodor - cheat online voting contests
This project use techniques to test online voting contests
## Requirements
 - MAC os Catalina 10.15.7
 - Selenium (https://www.selenium.dev/)
 - Gecko webdriver for Firefox (https://github.com/mozilla/geckodriver/releases)
 - Homebrew
## Instalation
$ `brew install selenium`
## Usage
### Level 0
$ `python3 ./testlauncher.py`
That will insert 1024 votes for code 3360 into http://158.69.76.135/level0.php


## Known Issues
If used with default python version 2.7.16 for MAC the selenium module could not be found

Update gecko webdriver using Brew to avoid OSError: [Errno 86] Bad CPU type in executable: 'geckodriver'
