from selenium import webdriver
from selenium.webdriver.common.by import By
import time
class kb():
    def __init__(self):
        self.driver=webdriver.Chrome()
        self.url='http://jwcas.cczu.edu.cn/login'
        self.username=input('请输入学号：')
        self.password=input('请输入密码：')
        self.cla=input('请输入你暗恋的人的班级：')
        self.driver.maximize_window()

    def login(self):
        self.driver.get(self.url)
        time.sleep(2)
        self.driver.find_element(By.ID,'username').send_keys(self.username)
        self.driver.find_element(By.ID,'password').send_keys(self.password)
        time.sleep(3)
        self.driver.find_element(By.XPATH,'//*[@id="fm1"]/div[3]/input[4]').click()
        time.sleep(9)
    
    def enter(self):
        self.driver.find_element(By.XPATH,'//*[@id="main"]/div[2]/ul[1]/li[1]/a').click()
        time.sleep(6)
        win=self.driver.window_handles
        self.driver.switch_to.window(win[1])
        time.sleep(10)
        self.driver.find_element(By.XPATH,'//*[@id="5201-0021"]/a').click()
        time.sleep(5)
        
    def search(self):
        # iframe
        iframe1=self.driver.find_element(By.XPATH,'//*[@id="frame5201-0021"]')
        self.driver.switch_to.frame(iframe1)
        self.driver.find_element(By.ID,'Cxbj_all1_Txtbj').send_keys(self.cla)
        time.sleep(2)
        self.driver.find_element(By.ID,'Cxbj_all1_btbjxz').click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,'//*[@id="Cxbj_all1_GVbj"]/tbody/tr[2]/td[1]/input').click()
        time.sleep(10)
        # 回退
        self.driver.switch_to.default_content()
        print("回退成功")
        time.sleep(5)
        # iframe
        
        iframe2=self.driver.find_element(By.XPATH,'//*[@id="layui-layer-iframe1"]')
        self.driver.switch_to.frame(iframe2)
        print("进入iframe2成功")
        time.sleep(10)
        self.driver.find_element(By.ID,"dataout").click()
        print("点击成功")
        print("记得关闭安全设置")
        time.sleep(10)




if __name__=='__main__':
    kb=kb()
    kb.login()
    kb.enter()
    kb.search()


        

