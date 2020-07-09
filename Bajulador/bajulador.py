import os, time, random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from senhas import LOGIN, PASSWORD
import re

class Bajulante:
    def __init__(self, username, password, bajular_pessoas, postagens):
        self.bajular_pessoas = bajular_pessoas
        self.username = username
        self.password = password
        self.postagens = postagens
        self.path = '/usr/bin/chromedriver'
        
        self.mensagens = [
            'Que maravilhosaaaa!!',
            'Você é demais! Te admiro muito!',
            'Ohhhh, você é incrível!!!!',
            'Não merece só palmas, merece Tocantins inteiro!!',
            'Você não devia estar entre nós meros mortais...',
            'UAUUUUUUU, essa foto merece virar um quadro!',
            '100& diva',
            'Alegrou meu dia.',
            'Apenas lindo!'            
        ]
        #os.chmod(self.path, 755) 
        mobile_emulation = {
        "deviceMetrics": {"width": 360, "height": 640, "pixelRatio": 3.0},
        "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19"}
        chrome_options = Options()
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        self.driver = webdriver.Chrome(self.path, chrome_options=chrome_options)

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(2)
        element = driver.find_element_by_name('username')
        element.send_keys(self.username)
        element = driver.find_element_by_name('password')
        element.send_keys(self.password)
        time.sleep(2)
        element.submit()
        time.sleep(5)

    def close_browser(self):
        self.driver.close()

    def comentar(self):
        for postagem in postagens:
            self.driver.get(postagem)
            print('\nAchei uma...\n')
            time.sleep(3)
            print('\nVou comentar algo...\n')
            self.driver.get(postagem+'comments/')
            time.sleep(3)
            element = self.driver.find_element_by_class_name('Ypffh')
            element.send_keys(random.choice(self.mensagens))
            time.sleep(2)
            element.submit()
            time.sleep(5)
            
    

if __name__ == '__main__':
    bajular_pessoas = ['@aclaracorrea', '@thaynasvnunes']
    
    postagens = ['https://www.instagram.com/p/B_nuUSCD9CP/',
                 'https://www.instagram.com/p/B9vECDllGDX/',
                 'https://www.instagram.com/p/B794KHvlLW-/',
                 'https://www.instagram.com/p/B7Z3gm3FU2H/'
                 ]
    
    ig = Bajulante(LOGIN, PASSWORD, bajular_pessoas, postagens)
    print("\nFiz o login...\n")
    ig.login()
    #exit()
    print('\nProcurando postagem para comentar idiotices...\n')
    ig.comentar()