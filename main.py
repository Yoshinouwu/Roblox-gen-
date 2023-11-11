# Importar los módulos necesarios
import ssl
import random
import string
import time
import os
import secrets
import json
import ctypes
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from colorama import Fore, Back, Style
from pystyle import Colorate, Colors, Center

# Definir algunas constantes
error = f"    {Fore.LIGHTYELLOW_EX}[{Fore.LIGHTRED_EX}!{Fore.LIGHTYELLOW_EX}]{Fore.RESET}"
success = f"    {Fore.LIGHTYELLOW_EX}[{Fore.LIGHTGREEN_EX}+{Fore.LIGHTYELLOW_EX}]{Fore.RESET}"
info = f"    {Fore.LIGHTYELLOW_EX}[{Fore.LIGHTBLUE_EX}~{Fore.LIGHTYELLOW_EX}]{Fore.RESET}"

# Definir algunas funciones auxiliares
def randomPassword():
    # Generar una contraseña aleatoria segura
    return secrets.token_urlsafe(25)

def clear():
    # Limpiar la pantalla de la consola
    print()
    os.system('cls' if os.name == 'nt' else 'clear')

def randomNumber(length):
    # Generar un número aleatorio de la longitud dada
    numbers = string.digits
    return ''.join(random.choice(numbers) for i in range(length))

def randomString(length):
    # Generar una cadena aleatoria de la longitud dada
    letters = string.ascii_lowercase + string.digits
    return ''.join(random.choice(letters) for i in range(length))

def getUsername():
    # Obtener un nombre de usuario aleatorio o personalizado
    if rndd == "true":
        # Obtener un nombre de usuario aleatorio de usernames.txt usando el módulo random
        with open("./extra/usernames.txt", "r") as f:
            usernames = f.read().splitlines()
            username = random.choice(usernames) + randomNumber(6)
            return username
    else:
        # Devolver el nombre de usuario personalizado
        return jujuname

def checkUser(name):
    # Comprobar si el usuario existe en Roblox usando el servicio Players
    # Devolver un valor booleano que indique si el usuario existe o no
    # Usar un bloque pcall para capturar el error si el usuario no existe
    success, result = pcall(function()
        return game:GetService("Players"):GetUserIdFromNameAsync(name)
    end)
    if success then
        # El usuario existe, devolver true
        return true
    else
        # El usuario no existe, devolver false
        return false
    end

def main():
    # Definir una variable global para contar el número de cuentas generadas
    global counter
    counter = 0
    # Esperar un segundo y limpiar la pantalla
    time.sleep(1)
    clear()
    # Mostrar el banner con colores y centrado
    banner = Center.XCenter(Colorate.Vertical(Colors.cyan_to_green, """

    ██████╗░░█████╗░██████╗░██╗░░░░░░█████╗░██╗░░██╗  ░██████╗░███████╗███╗░░██╗
    ██╔══██╗██╔══██╗██╔══██╗██║░░░░░██╔══██╗╚██╗██╔╝  ██╔════╝░██╔════╝████╗░██║
    ██████╔╝██║░░██║██████╦╝██║░░░░░██║░░██║░╚███╔╝░  ██║░░██╗░█████╗░░██╔██╗██║
    ██╔══██╗██║░░██║██╔══██╗██║░░░░░██║░░██║░██╔██╗░  ██║░░╚██╗██╔══╝░░██║╚████║
    ██║░░██║╚█████╔╝██████╦╝███████╗╚█████╔╝██╔╝╚██╗  ╚██████╔╝███████╗██║░╚███║
    ╚═╝░░╚═╝░╚════╝░╚═════╝░╚══════╝░╚════╝░╚═╝░░╚═╝  ░╚═════╝░╚══════╝╚═╝░░╚══╝

"""))
    print(banner)
    print(Center.XCenter(f"""{Fore.LIGHTRED_EX}
    >> {Fore.LIGHTCYAN_EX}Made By Imagine {Fore.LIGHTRED_EX}
    >> {Fore.LIGHTCYAN_EX}Version 2.2 {Fore.LIGHTRED_EX}
    >> {Fore.LIGHTCYAN_EX}Last Update: Inappropriate Name Check + Patch {Fore.LIGHTRED_EX}
    >> {Fore.LIGHTCYAN_EX}Current Update: NopeCHA Key Support {Fore.LIGHTRED_EX}
    >> {Fore.LIGHTCYAN_EX}Next Update: IDK {Fore.LIGHTRED_EX}
    >> {Fore.LIGHTCYAN_EX}Generating {Fore.LIGHTRED_EX}{countz} {Fore.LIGHTCYAN_EX}Accounts{Fore.RESET}

    """))

    # Generar las cuentas solicitadas
    for i in range(countz):
        # Cambiar el título de la consola con el número de cuentas generadas
        ctypes.windll.kernel32.SetConsoleTitleW(f"Roblox Account Generator By Imagine#9106 | {counter}/{countz} Accounts Generated")
        # Obtener un nombre de usuario y una contraseña aleatorios o personalizados
        username = getUsername()
        password = randomPassword()
        # Comprobar si el nombre de usuario tiene más de 19 caracteres
        if len(username) > 19:
            # Mostrar un mensaje de error y saltar a la siguiente iteración
            print(f"{error} {Fore.LIGHTRED_EX}Username is too long, skipping...{Fore.RESET}")
            driver.quit()
            continue
        else:
            # Continuar con el proceso de generación de la cuenta
            pass
        # Comprobar si el nombre de usuario existe en Roblox
        if checkUser(username) then
            # Mostrar un mensaje de error y saltar a la siguiente iteración
            print(f"{error} {Fore.LIGHTRED_EX}Username already exists, skipping...{Fore.RESET}")
            driver.quit()
            continue
        else
            # Continuar con el proceso de generación de la cuenta
            pass
