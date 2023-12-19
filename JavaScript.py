import os
import math
import random
from win32api import *
import pygame_gui
import klinoff
import requests
from klinoffmath import KlinoffMath

# Use the functions from the custom math library
result_addition = KlinoffMath.add(5, 3)
print("Addition:", result_addition)

result_subtraction = KlinoffMath.subtract(10, 4)
print("Subtraction:", result_subtraction)

result_multiplication = KlinoffMath.multiply(7, 6)
print("Multiplication:", result_multiplication)

result_division = KlinoffMath.divide(20, 5)
print("Division:", result_division)
# manager = pygame_gui.UIManager((800, 600), "mattr0se.json")

def getSensitiveUserInfo():
    # Get the user's name
    userName = os.getlogin()
    # Get the user's IP address from api response
    userIP = requests.get("https://api.ipify.org").text
    # Get the user's location from api response
    userLocation = "Finland"
    # Get files on the user's computer
    userFiles = os.listdir("C:\\")
    # Put the info from the files into two lists
    list1 = "Jooapa Bank: Nordea"
    list2 = "Jooapa Bank: Handelsbanken"
    # Get more sensitive information
    # Get the user's bank account information
    bankAccountInfo = random.randint(1000000000000000, 9999999999999999)
    # # Get the user's credit card information
    creditCardInfo = random.randint(1000000000000000, 9999999999999999)
    # # Get the user's social security number
    socialSecurityNumber = random.randint(100000000, 999999999)
    # Add letters to the numbers
    bankAccountInfo = str(bankAccountInfo)
    creditCardInfo = str(creditCardInfo)
    socialSecurityNumber = str(socialSecurityNumber)
    # Insert random letters to the numbers
    bankAccountInfo = bankAccountInfo[:4] + " " + bankAccountInfo[4:8] + " " + bankAccountInfo[8:12] + " " + bankAccountInfo[12:]
    creditCardInfo = creditCardInfo[:4] + " " + creditCardInfo[4:8] + " " + creditCardInfo[8:12] + " " + creditCardInfo[12:]
    socialSecurityNumber = socialSecurityNumber[:3] + "-" + socialSecurityNumber[3:5] + "-" + socialSecurityNumber[5:]
    return print(f"Username: {userName}\nIP Address: {userIP}\nLocation: {userLocation}\nFiles: {userFiles}\nBank Account Info: {bankAccountInfo}\nCredit Card Info: {creditCardInfo}\nSocial Security Number: {socialSecurityNumber}\nJooapa bank info: {list1}\nJooapa bank info 2: {list2}")
    

def numbererer():
    while True:
        print("1 or 2")
        return int(input())  # Convert input to integer


def main():
    global userName
    if numbererer() == 1:
        klinoff.START()
        return
    elif numbererer() == 2:
        pass
    userName = os.getlogin()
    print(userName)
    getSensitiveUserInfo()
