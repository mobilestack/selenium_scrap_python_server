from pyvirtualdisplay import Display
from selenium import webdriver
import time


def selenium_render(url):
    """
    打开使用模拟浏览器打开一个网页，尤其是需要大量js的网页
    :param url: 网址 
    :return: 网页端的html字符串
    """
    display = Display(visible=0, size=(1024, 768))
    display.start()

    driver = webdriver.Firefox(executable_path="/home/tony/lib/geckodriver")
    driver.get(url)

    # 为了让浏览器加载
    time.sleep(5)

    html = driver.page_source
    print('html is {}'.format(html[:10]))
    
    # todo, 似乎close没有关闭彻底, quite也不能，经常有网页打开后，firefox没有正常关闭，导致大量内存占用
    driver.close()
    #driver.quit()

    display.stop()

    return html


