import os
import time
import sys
class Terminal:
    def __get_centered_text(self, text, width):
        return text.center(width)
    
    def choose_promo(self, promos: list):
        print("\u001b[37m", "To start, choose a promo from the list below:")
        x =[i["name"] for i in promos][:5]
        for i, j in enumerate(x):
            print(f"\u001b[32m{i+1}  -", "\u001b[37m",j)
        return promos[int(input("Choose a promo: ")) - 1]
    
    def greet(self):
        # get the width of the terminal
        
        width = os.get_terminal_size().columns
        
        message = self.__get_centered_text("Welcome to the VTEX Promo Poster Generator", width)
        
        print("\u001b[32m", "-" * (width - 1))
        print()
        print("\u001b[32m", message, "\u001b[37m")
        print("\u001b[32m", "-" * (width - 1))
        
        
    def info(self, message):
        print("\u001b[34m", "[INFO]", "\u001b[0m", message)
        
    def fake_loading(self, message="Loading...", bar_length=20, sleep=2):
        
        for i in range(bar_length):
            bar = "\u001b[34m"+ " [INFO]"+ "\u001b[0m" + "  " + message + "[" + "=" * i + " " * (bar_length - i - 1) + "]"
            time.sleep(sleep / bar_length)
            sys.stdout.write(bar)
            # sys.stdout.flush()
            print ("\033[A")
        sys.stdout.write("\n")
        