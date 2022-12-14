import pyautogui
import colorama
from colorama import Fore, Back, Style
from random import randint
from time import sleep
from timeit import default_timer as timer

colorama.init(autoreset=True)

def repeat_action(times, f, *args):
    for i in range(times): f(*args)

def type(string):
  pyautogui.write(string, interval = 0.5)
  sleep(randint(1, 2))
  pyautogui.hotkey('enter')
  sleep(randint(0, 3))

if __name__ == "__main__" : # make sure script is main and not imported before executing script
  print(Fore.YELLOW + "What do you want to type?")
  string = input(Fore.CYAN + "")
  print(Fore.YELLOW + "Well... weird thing to type but ok!")
  print(Fore.YELLOW + "How many times?")
  num = input(Fore.CYAN + "")
  input(Fore.YELLOW + "Press Enter key then put your cursor where you want to type, you will have a delay of 5 seconds ⏰")
  sleep(5)
  print(Fore.YELLOW + "Typing", Fore.CYAN + string, Fore.YELLOW + "a total of",Fore.CYAN + num, Fore.YELLOW + "times 🤓")

  start = int(timer())
  repeat_action(int(num), type, string)
  end = int(timer())

  timers_seconds = end - start
  timers_minutes = int(timers_seconds / 60)

  if timers_seconds <= 59:
    print(Fore.GREEN + "Done in", timers_seconds,Fore.GREEN + "seconds! 😎")
  else:
    print(Fore.GREEN + "Done in", str(timers_minutes) + (Fore.GREEN + " minutes! 😴" if timers_minutes > 1 else Fore.GREEN + " minute! 🤓"))
