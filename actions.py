import os
import time
import pyautogui as pg

#atalhos

def b_tela() :
    pg.press('win')
    time.sleep(1)
    pg.click(40, 516)
    time.sleep(1)
    pg.doubleClick(65, 436)
    
def min() :
    pg.hotkey('win', 'm')

def close() :
    pg.hotkey('alt', 'f4')

def copiar() :
    pg.hotkey('ctrl', 'c')

def colar() :
    pg.hotkey('ctrl', 'v')

def desfaz() :
    pg.hotkey('ctrl', 'z')

def enter() :
    pg.press('enter')

def clean_all() :
    pg.hotkey('ctrl', 'a')
    pg.press('backspace')

def write(self):
    frase = self
    pg.write(frase)


# functions exe
def chrome() :
    os.system("start Chrome.exe")
    time.sleep(1)
    pg.hotkey('win', 'up')

def conda() :
    pg.press('win')
    time.sleep(1.5)
    pg.write('anaconda')
    time.sleep(1)
    pg.press('enter')

def house_code() :
    conda()
    time.sleep(0.5)
    pg.write('cd c:/house')

def thouse_code() :
    conda()
    time.sleep(0.5)
    pg.write('cd c:/thehouse')



# functions chrome
def opentwitter() :
    chrome()
    time.sleep(5)
    pg.write('twitter.com')
    time.sleep(0.5)
    pg.press('enter')

def openwpp() :
    chrome()
    time.sleep(5)
    pg.write('https://web.whatsapp.com/')
    time.sleep(0.5)
    pg.press('enter')

def writing() :
    pg.keyDown('ctrl')
    pg.keyDown('win')
    pg.keyDown('right')
    time.sleep(0.5)
    pg.keyUp('ctrl')
    pg.keyUp('win')
    pg.keyUp('right')
    os.system("start WINWORD.EXE")
    time.sleep(7)
    pg.press('enter')

def work() :
    pg.press('win')
    time.sleep(1.5)
    pg.write('anaconda')
    time.sleep(1)
    pg.press('enter')
    time.sleep(5)
    pg.write('cd c:/house')
    time.sleep(1)
    pg.press('enter')
    time.sleep(2)
    pg.write('code .')
    time.sleep(1)
    pg.press('enter')

def show() :
    chrome()
    time.sleep(7)
    pg.write('https://open.spotify.com/playlist/21HMLE2i89mEopw1re3shI')
    time.sleep(2)
    pg.press('enter')
    time.sleep(3)
    



