from selenium import webdriver
from PyQt5.QtWidgets import QMessageBox, QMainWindow,QTextEdit

import time, json


class HaiWei():
    def __init__(self):
        # 默认的链接
        self.url = 'https://www.vmall.com/product/10086726905036.html'
        # 默认的按钮 因为那个按钮的类名是会变的,所以只能写child 2 用上一个不会变的a标签来定位按钮
        self.selector = '#pro-operation > a:nth-child(2)'
        self.start_kg = False

    def addLogin(self, name, window_main,ms):
        '''
        增加一个登录的cookies 就是分别 登录一下账号
        :return:
        '''
        # 创建线程
        driver = webdriver.Chrome()
        driver.get(self.url)
        QMessageBox.information(window_main, '提醒:', '请在登入好账号后点击确定', QMessageBox.Ok)
        dictCookies = driver.get_cookies()
        jsonCookies = json.dumps(dictCookies)
        # 登录完成后，将cookie保存到本地

        with open(f'cookies/{name}.json', 'w') as f:
            f.write(jsonCookies)
        ms.log_add.emit(f'账号:{name} 保存成功!')
        driver.close()
    def start(self, name, driver,ms):
        '''
        开始自动多线程抢华为mate40pro手机,因为我 没成功过,所以如果成功了请自己判断
        :param name: 账号备注
        :param driver: 浏览器
        :param ms: 信号
        :return:
        '''

        # 超时
        driver.set_page_load_timeout(5000)  # 防止页面加载个没完
        # 访问一次,不然容易设置不了cookies
        driver.get(self.url)
        # 删除第一次建立连接时的cookie
        driver.delete_all_cookies()
        # 读取登录时存储到本地的cookie
        with open(f'cookies/{name}.json', 'r', encoding='utf-8') as f:
            listCookies = json.loads(f.read())
        for cookie in listCookies:
            # driver.delete_cookie(cookie['name'])
            driver.add_cookie({
                "domain": cookie['domain'],
                "httpOnly": cookie['httpOnly'],
                "name": cookie['name'],
                "path": cookie['path'],
                "secure": cookie['secure'],
                "value": cookie['value']
            })
        driver.get(self.url)
        i=True
        while True:

            if self.start_kg == True:
                if i == True:
                    ms.log_add.emit(f'账号:{name} 现在开始,祝您好运!')
                    i = False
                try:
                    elem = driver.find_element_by_css_selector(self.selector)
                    elem.click()
                except:
                    break
            time.sleep(0.3)
        ms.log_add.emit(f'账号:{name} 点击成功!是否抢到资格请肉眼看咯!')
    def setting(self, url, selector):
        '''
        自定义抢购的链接和以及疯狂点击的按钮(css选择器文本输入方法也很简单)
        获取选择器selector文本步骤:
        1.打开你的网站然后在浏览器中找到你需要不断点击的按钮后右键,菜单选择[审核元素\检查]
        2.之后就会出来调试器,就在高亮的元素上右键菜单依次找到 Copy > Copy selector 然后点击就成功复制到文本了
        3.将文本填进去就好了(最好是懂点css的基础,或者自己找规律来改)
        :param url:自定义网址
        :param selector:css选择器文本
        :return:
        '''
        if selector != None and selector != '':
            self.url = url
        else:
            self.url ='https://www.vmall.com/product/10086726905036.html'
        if selector != None and selector != '':
            self.selector = selector
        else:
            self.selector = '#pro-operation > a:nth-child(2)'
        print(self.url ,self.selector )
