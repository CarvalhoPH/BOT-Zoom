import os
import schedule
import time
import pyautogui
from datetime import datetime
import time
import sys

#PASTA DO ZOOM
print('Normalmente fica em C:/Users/<nome do seu usuario>/AppData/Roaming/Zoom/bin')
pasta = str(input('Digite a diretorio para a pasta do zoom.exe: '))
time.sleep(4)
print('BOT FUNCIONANDO')

#CODIGO DAS SALAS#
codigo1 = input('Digite o codigo da 1 aula: ')
time.sleep(1)
senha1 = input('Digite a 1 senha: ')
time.sleep(1)
hora1 = int(input('Horario da 1 aula em 00:00 '))
time.sleep(1)

codigo2 = input('Digite o codigo da 2 aula: ')
time.sleep(1)
senha2 = input('Digite a 2 senha: ')
time.sleep(1)
hora2 = int(input('Horario da 2 aula em 00:00 '))
time.sleep(1)

codigo3 = input('Digite o codigo da 3 aula: ')
time.sleep(1)
senha3 = input('Digite a 3 senha: ')
time.sleep(1)
hora3 = int(input('Horario da 3 aula em 00:00 '))
time.sleep(1)

codigo4 = input('Digite o codigo da 4 aula: ')
time.sleep(1)
senha4 = input('Digite a 4 senha: ')
time.sleep(1)
hora4 = int(input('Horario da 4 aula em 00:00 '))
time.sleep(1)

codigo5 = input('Digite o codigo da 5 aula: ')
time.sleep(1)
senha5 = input('Digite a 5 senha: ')
time.sleep(1)
hora5 = int(input('Horario da 5 aula em 00:00 '))
time.sleep(1)

codigo6 = input('Digite o codigo da 6 aula: ')
time.sleep(1)
senha1 = input('Digite a 6 senha: ')
time.sleep(1)
hora6 = int(input('Horario da 6 aula em 00:00 '))
time.sleep(1)

codigo1 = input('Digite o codigo da 7 aula: ')
time.sleep(1)
senha1 = input('Digite a 7 senha: ')
hora7 = int(input('Horario da 7 aula em 00:00 '))
time.sleep(1)

#MOSTRANDO AS HORAS
print("Aula 1 : {}".format(hora1))
print("Aula 2 : {}".format(hora2))
print("Aula 3 : {}".format(hora3))
print("Aula 4 : {}".format(hora4))
print("Aula 5 : {}".format(hora5))
print("Aula 6 : {}".format(hora6))
print("Aula 7 : {}".format(hora7))

#DEF`S#
def abrirZoom():
    os.chdir(pasta)
    os.system("zoom.exe")
    pyautogui.moveTo(780, 780)
    pyautogui.click()
    pyautogui.moveTo(850, 503)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.typewrite(codigo1)
    time.sleep(0.5)
    pyautogui.moveTo(950, 650)
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(850, 500)
    pyautogui.typewrite(senha1)
    time.sleep(1)
    pyautogui.moveTo(950, 650)
    pyautogui.click()
    time.sleep(1)

def abrirZoom2():
    os.chdir(pasta)
    os.system("zoom.exe")
    pyautogui.moveTo(780, 780)
    pyautogui.click()
    pyautogui.moveTo(850, 503)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.typewrite(codigo2)  # enter the call "code"
    time.sleep(0.5)
    pyautogui.moveTo(950, 650)
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(850, 500)
    pyautogui.typewrite(senha2)  # enter the call "code"
    time.sleep(1)
    pyautogui.moveTo(950, 650)
    pyautogui.click()
    time.sleep(1)

def abrirZoom3():
    os.chdir(pasta)
    os.system("zoom.exe")
    pyautogui.moveTo(780, 780)
    pyautogui.click()
    pyautogui.moveTo(850, 503)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.typewrite(codigo3)  # enter the call "code"
    time.sleep(0.5)
    pyautogui.moveTo(950, 650)
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(850, 500)
    pyautogui.typewrite(senha3)  # enter the call "code"
    time.sleep(1)
    pyautogui.moveTo(950, 650)
    pyautogui.click()
    time.sleep(1)

def abrirZoom4():
    os.chdir(pasta)
    os.system("zoom.exe")
    pyautogui.moveTo(780, 780)
    pyautogui.click()
    pyautogui.moveTo(850, 503)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.typewrite(codigo4)  # enter the call "code"
    time.sleep(0.5)
    pyautogui.moveTo(950, 650)
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(850, 500)
    pyautogui.typewrite(senha4)  # enter the call "code"
    time.sleep(1)
    pyautogui.moveTo(950, 650)
    pyautogui.click()
    time.sleep(1)


def abrirZoom5():
    os.chdir(pasta)
    os.system("zoom.exe")
    pyautogui.moveTo(780, 780)
    pyautogui.click()
    pyautogui.moveTo(850, 503)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.typewrite(codigo5)  # enter the call "code"
    time.sleep(0.5)
    pyautogui.moveTo(950, 650)
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(850, 500)
    pyautogui.typewrite(senha5)  # enter the call "code"
    time.sleep(1)
    pyautogui.moveTo(950, 650)
    pyautogui.click()
    time.sleep(1)

def abrirZoom6():
    os.chdir(pasta)
    os.system("zoom.exe")
    pyautogui.moveTo(780, 780)
    pyautogui.click()
    pyautogui.moveTo(850, 503)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.typewrite(codigo6)  # enter the call "code"
    time.sleep(0.5)
    pyautogui.moveTo(950, 650)
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(850, 500)
    pyautogui.typewrite(senha6)  # enter the call "code"
    time.sleep(1)
    pyautogui.moveTo(950, 650)
    pyautogui.click()
    time.sleep(1)

def abrirZoom7():
    os.chdir(pasta)
    os.system("zoom.exe")
    pyautogui.moveTo(780, 780)
    pyautogui.click()
    pyautogui.moveTo(850, 503)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.typewrite(codigo7)  # enter the call "code"
    time.sleep(0.5)
    pyautogui.moveTo(950, 650)
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(850, 500)
    pyautogui.typewrite(senha7)  # enter the call "code"
    time.sleep(1)
    pyautogui.moveTo(950, 650)
    pyautogui.click()
    time.sleep(1)

#ENTRANDO NAS SALAS
schedule.every().day.at(hora1).do(abrirZoom)
schedule.every().day.at(hora2).do(abrirZoom2)
schedule.every().day.at(hora3).do(abrirZoom3)
schedule.every().day.at(hora4).do(abrirZoom4)
schedule.every().day.at(hora5).do(abrirZoom5)
schedule.every().day.at(hora6).do(abrirZoom6)
schedule.every().day.at(hora7).do(abrirZoom7)

while True:
    schedule.run_pending()
    time.sleep(1)

while True:
    print('BOT FUNCIONANDO')
    time.sleep(1*60)

