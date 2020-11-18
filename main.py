import threading,sys,os
from codes.hawei import HaiWei
from PyQt5.QtWidgets import QApplication,QMainWindow,QInputDialog,QLineEdit,QMessageBox
from PyQt5.QtCore import pyqtSignal,QObject
from PyQt5.QtGui import QIcon
from ui.main import Ui_MainWindow
from selenium import webdriver
class Myignals(QObject):
    #定义一种信号,然后确定参数的类型
    log_add=pyqtSignal(str)
def init_window_main():
    window_main.setWindowTitle('华为mate40多线程抢购神器')
    window_main.setWindowIcon(QIcon('logo.ico'))
    #绑定按钮信号
    ui_main.bt_add.clicked.connect(add)
    ui_main.bt_openWeb.clicked.connect(openWeb)
    ui_main.bt_start.clicked.connect(true_or_Flase)
    window_main.closeEvent=close
def close(enent):
    #关闭所有的浏览器
    for item in driver:
        item.quit()
def add():
    hw.setting(ui_main.ed_url.text(), ui_main.ed_css.text())
    name, okPressed =QInputDialog.getText(window_main,"请输入字符或者数字", "账号备注名:", QLineEdit.Normal, "")
    if okPressed and name != '':
        hw.addLogin(name,window_main,ms)

def openWeb():
    hw.setting(ui_main.ed_url.text(), ui_main.ed_css.text())
    ui_main.ed_log.append('现在请自己选择好产品的尺寸,规格,型号等参数,然后点全部开始,别关闭浏览器!')
    for item in os.listdir(path='cookies'):
        # 创建浏览器
        driver.append(webdriver.Chrome())
        # 创建线程
        t.append(threading.Thread(target=hw.start,args=(item.split('.')[0], driver[-1],ms)))
        # 设置主线程关闭时,它也跟着关闭
        t[-1].setDaemon(True)
        # 开始运行
        t[-1].start()
def true_or_Flase():

    if len(driver)==0:
        log_add('请先点击启动浏览器!')

        return
    global start
    if start==True:
        ui_main.bt_start.setText('3.全部开始')
        log_add('已经全部暂停!')
        start = False
    else:
        ui_main.bt_start.setText('3.全部暂停')

        log_add('已经全部开始!')


        start =True
    hw.start_kg =start
def log_add(text):
    print(text)
    ui_main.ed_log.append(text)
if __name__ == '__main__':

    # 自定义一个信号
    ms = log_sg = Myignals()
    # 绑定日志更新的信号
    ms.log_add.connect(log_add)

    #实例化华为对象
    hw = HaiWei()

    t = []#线程容器
    driver = []#浏览器容器
    start=False#全局暂停和开始的开关
    app=QApplication(sys.argv)
    window_main = QMainWindow()  # 主界面
    ui_main = Ui_MainWindow()  # 实例化
    ui_main.setupUi(window_main)  # 运行里面的代码
    init_window_main()  # 初始化和对接代码功能
    window_main.show()
    sys.exit(app.exec_())
    #'抱歉，没有抢到'
    #'#boxText > p'

