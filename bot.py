
import os
import schedule
import time
import pyautogui
from datetime import datetime
import time
import sys
#HORA DAS AULAS#
meeting_time = "07:00:00"  
meeting_time2 = "07:45:00"  
meeting_time3 = "08:30:00"
meeting_time4 = "9:15:00"
meeting_time5 = "10:30:00"
meeting_time6 = "11:15:00"
meeting_time7 = "12:00:00"

#CODIGO DAS SALAS#
codigo1 = input('Digite o codigo da 1 aula: ')
time.sleep(3)
senha1 = input('Digite a 1 senha: ')
time.sleep(3)

codigo2 = input('Digite o codigo da 2 aula: ')
time.sleep(3)
senha2 = input('Digite a 2 senha: ')
time.sleep(3)

codigo3 = input('Digite o codigo da 3 aula: ')
time.sleep(3)
senha3 = input('Digite a 3 senha: ')
time.sleep(3)

codigo4 = input('Digite o codigo da 4 aula: ')
time.sleep(3)
senha4 = input('Digite a 4 senha: ')
time.sleep(3)

codigo5 = input('Digite o codigo da 5 aula: ')
time.sleep(3)
senha5 = input('Digite a 5 senha: ')
time.sleep(3)

codigo6 = input('Digite o codigo da 6 aula: ')
time.sleep(3)
senha1 = input('Digite a 6 senha: ')
time.sleep(3)

codigo1 = input('Digite o codigo da 7 aula: ')
time.sleep(3)
senha1 = input('Digite a 7 senha: ')

# DIVIDINDO EM PARTES A HORA
meeting_hour = int(meeting_time2[0:2])
meeting_minute = int(meeting_time2[3:5])
meeting_second = int(meeting_time2[6:8])

meeting_hour2 = int(meeting_time[0:2])
meeting_minute2 = int(meeting_time[3:5])
meeting_second2 = int(meeting_time[6:8])

meeting_hour3 = int(meeting_time[0:2])
meeting_minute3 = int(meeting_time[3:5])
meeting_second3 = int(meeting_time[6:8])

meeting_hour4 = int(meeting_time[0:2])
meeting_minute4 = int(meeting_time[3:5])
meeting_second4 = int(meeting_time[6:8])

meeting_hour5 = int(meeting_time[0:2])
meeting_minute5 = int(meeting_time[3:5])
meeting_second5 = int(meeting_time[6:8])

meeting_hour6 = int(meeting_time[0:2])
meeting_minute6 = int(meeting_time[3:5])
meeting_second6 = int(meeting_time[6:8])

meeting_hour7 = int(meeting_time[0:2])
meeting_minute7 = int(meeting_time[3:5])
meeting_second7 = int(meeting_time[6:8])


#MOSTRANDO AS HORAS

print("meeting 1 time: " + str(meeting_hour) + " " + str(meeting_minute) + " " + str(meeting_second))
print("meeting 2 time: " + str(meeting_hour2) + " " + str(meeting_minute2) + " " + str(meeting_second2))
print("meeting 3 time: " + str(meeting_hour3) + " " + str(meeting_minute3) + " " + str(meeting_second3))
print("meeting 4 time: " + str(meeting_hour4) + " " + str(meeting_minute4) + " " + str(meeting_second4))
print("meeting 5 time: " + str(meeting_hour5) + " " + str(meeting_minute5) + " " + str(meeting_second5))
print("meeting 6 time: " + str(meeting_hour6) + " " + str(meeting_minute6) + " " + str(meeting_second6))
print("meeting 7 time: " + str(meeting_hour7) + " " + str(meeting_minute7) + " " + str(meeting_second7))


#CONFIGURACAO DE SLEEP#
sleep_time = 0.05
reiniciar = 42

#DEF`S#
def openZoom():
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


def openZoom2():
    pyautogui.moveTo(780, 780)
    pyautogui.click()
    pyautogui.moveTo(850, 503)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.typewrite('739 8326 6862')  # enter the call "code"
    time.sleep(0.5)
    pyautogui.moveTo(950, 650)
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(850, 500)
    pyautogui.typewrite('ursulamcz')  # enter the call "code"
    time.sleep(1)
    pyautogui.moveTo(950, 650)
    pyautogui.click()
    time.sleep(1)


def openZoom3():
    pyautogui.moveTo(780, 780)
    pyautogui.click()
    pyautogui.moveTo(850, 503)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.typewrite('739 8326 6862')  # enter the call "code"
    time.sleep(0.5)
    pyautogui.moveTo(950, 650)
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(850, 500)
    pyautogui.typewrite('ursulamcz')  # enter the call "code"
    time.sleep(1)
    pyautogui.moveTo(950, 650)
    pyautogui.click()
    time.sleep(1)


def openZoom4():
    pyautogui.moveTo(780, 780)
    pyautogui.click()
    pyautogui.moveTo(850, 503)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.typewrite('739 8326 6862')  # enter the call "code"
    time.sleep(0.5)
    pyautogui.moveTo(950, 650)
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(850, 500)
    pyautogui.typewrite('ursulamcz')  # enter the call "code"
    time.sleep(1)
    pyautogui.moveTo(950, 650)
    pyautogui.click()
    time.sleep(1)



def openZoom5():
    pyautogui.moveTo(780, 780)
    pyautogui.click()
    pyautogui.moveTo(850, 503)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.typewrite('739 8326 6862')  # enter the call "code"
    time.sleep(0.5)
    pyautogui.moveTo(950, 650)
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(850, 500)
    pyautogui.typewrite('ursulamcz')  # enter the call "code"
    time.sleep(1)
    pyautogui.moveTo(950, 650)
    pyautogui.click()
    time.sleep(1)


def openZoom6():
    pyautogui.moveTo(780, 780)
    pyautogui.click()
    pyautogui.moveTo(850, 503)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.typewrite('739 8326 6862')  # enter the call "code"
    time.sleep(0.5)
    pyautogui.moveTo(950, 650)
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(850, 500)
    pyautogui.typewrite('ursulamcz')  # enter the call "code"
    time.sleep(1)
    pyautogui.moveTo(950, 650)
    pyautogui.click()
    time.sleep(1)


def openZoom7():
    pyautogui.moveTo(780, 780)
    pyautogui.click()
    pyautogui.moveTo(850, 503)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.typewrite('739 8326 6862')  # enter the call "code"
    time.sleep(0.5)
    pyautogui.moveTo(950, 650)
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(850, 500)
    pyautogui.typewrite('ursulamcz')  # enter the call "code"
    time.sleep(1)
    pyautogui.moveTo(950, 650)
    pyautogui.click()
    time.sleep(1)

#ENTRANDO NAS SALAS

sim = True
while (sim):
    now = datetime.now()
    print("now time: " + str(now.hour) + " " + str(now.minute))
    if now.hour == meeting_hour and now.minute == meeting_minute:
        print("Entrando na sala 1")
        openZoom()
        break
    elif now.hour == meeting_hour2 and now.minute == meeting_minute2:
        print('Entrando na 2 sala')
        openZoom2()
        break
    elif now.hour == meeting_hour3 and now.minute == meeting_minute3:
        print('Entrando na 3 sala')
        openZoom3()
        break
    elif now.hour == meeting_hour4 and now.minute == meeting_minute4:
        print('Entrando na 4 sala')
        openZoom4()
        break
    elif now.hour == meeting_hour5 and now.minute == meeting_minute5:
        print('Entrando na 5 sala')
        openZoom5()
        break
    elif now.hour == meeting_hour6 and now.minute == meeting_minute6:
        print('Entrando na 6 sala')
        openZoom6()
        break
    elif now.hour == meeting_hour7 and now.minute == meeting_minute7:
        print('Entrando na 7 sala')
        openZoom7()
        break
    else:
        print("Ainda nao esta na hora. Tentando outra vez em %s minutos" % str(sleep_time))
        time.sleep(sleep_time * 60)

time.sleep(reiniciar * 60)



 