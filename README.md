# selenium_scrap_python_server

## Usage
This little project setup a minimum python web server for scraping a website url, expecially for those with heavy js interactions.


## Installation

pip install selenium
pip install pyvirtualdisplay

yum update
yum install firefox
yum install xvfb

# Install geckodriver global-wise or local-wise

# cd /tmp
# curl -SO https://github.com/mozilla/geckodriver/releases/download/v0.11.1/geckodriver-v0.11.1-linux64.tar.gz | tar zxv - -C /usr/sbin

curl -SO https://github.com/mozilla/geckodriver/releases/download/v0.11.1/geckodriver-v0.11.1-linux64.tar.gz
# untar this to the path of Firefox executable_path


## 中文介绍
本项目使用了两个文件来爬取网页，主要适用于那些使用了大量js交互的网页，无法用beautifulsoup直接读取的网页，这里使用了模拟浏览器来加载各种js资源，最终得到的页面与我们在手机或电脑端看到的网页是一致的。


