import os, pyautogui, time, random
from progress.bar import Bar

class color : 
   GREEN = '\033[92m'
   RED = '\033[91m'
   WHITE = '\033[0m'
   Blue    = "\033[94m"
   Yellow = '\033[33m'

# Set Title
os.system("title "+"ChatSpammer by SirArash")

# Clean the console or terminal
os.system('cls' if os.name == 'nt' else 'clear')


print(color.Yellow)
print("  [-] Welcome to ChatSpammer")
print("  [-] Programmer : Arash Azizi (-SirArash)")
print("  [-] Website : ArashAzizi.ir & SirArash.ir")
print("  [-] Github : github.com/MrArashAzizi")
print("  [-] Version : 1.0")
print(color.WHITE)
print()

# Get text from user
MessageText = input("  [?] What text should I send her/him? ")

# Number of messages sent
Repeats = int(input("  [?] How many times should I send the message? "))

# Send messages interval
MessageInterval = int(input("  [?] How many milliseconds(No seconds! -> 1000ms = 1s | Use 0 for Random) should I put between each message?  "))
print()

# Asking from user to open the app
isLoaded = input("  [!] OK, Please open the app and then Press [Enter] when your messaging app is loaded up.")
print()

# 5-second period for user to focus on the messenger text box
print("  [!] You have 5 Seconds to refocus the text input area of your messaging app")
# 5 second pause
time.sleep(5)

# Progressbar
bar = Bar('  [!] Processing' , max = Repeats)
for i in range(0,Repeats):
	# Message sending loop
	if MessageText != "":
		pyautogui.typewrite(MessageText)     
		pyautogui.press("enter")
	else:
		pyautogui.typewrite("Love U")     
		pyautogui.press("enter")

	bar.next()
	if MessageInterval == 0:
		time.sleep(random.randint(500, 3500)/1000)
	else:
		time.sleep(MessageInterval/1000)

print()
print()

bar.finish()
print(color.GREEN + "  [~] Done... :)")

print()
print()
print()

# Exit
input(color.WHITE + "  [*] Press ENTER for exit: ")
