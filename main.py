from colorama import Fore, init
import difflib
import sqlite3
import os.path
import os
import time
i = 0
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "formul.db")
init(autoreset=True)

def connect_db():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    return conn, cursor
def similarity(s1, s2):
    normalized1 = s1.lower()
    normalized2 = s2.lower()
    matcher = difflib.SequenceMatcher(None, normalized1, normalized2)
    return matcher.ratio()
print("""█▀ ▄▀▄ █▀▀▄ █▄░▄█ █░█ █░░     █▀▄ █░░ ▀▄░▄▀ ▄▀▀ ▀ ▄▀ ▄▀▀ 
█▀ █░█ █▐█▀ █░█░█ █░█ █░▄     █░█ █▀▄ ░░█░░ ░▀▄ █ █░ ░▀▄ 
▀░ ░▀░ ▀░▀▀ ▀░░░▀ ░▀░ ▀▀▀     █▀░ ▀░▀ ░░▀░░ ▀▀░ ▀ ░▀ ▀▀░ 

Создатель: © Игнат Филиппов Юрьевич. 

""")
update = input("Хотите ли вы обновить базу данных с формулами?(у/n)\n")
if (update == "y"):
    os.popen("git pull https://github.com/IgFil/Physics")
    os.system('cls' if os.name == 'nt' else 'clear')
    time.sleep(2)
while True:
    data = input(Fore.YELLOW + "Введите данные задачи через пробел.[Первым то что вы хотите найти] \n").replace(' ','')
    print(data)
    conn , cursor = connect_db()
    cursor.execute("SELECT * FROM formuls;")
    formuls = cursor.fetchall()
    chances = []
    for formula in formuls:
        
        chances.append(similarity(data, formula[3]))
        
    for chance in chances: 
        if chance >= 0.50 :
                chance_percent = chance * 100
                chance_percent = int(chance_percent)
                print (Fore.GREEN + formuls[i][1] + "  " + str(chance_percent) +"% \n" + (Fore.BLUE + formuls[i][2]))
        i = i + 1   
    i = 0
    