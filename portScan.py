from socket import *
from threading import *
import optparse
from colorama import Fore, Style

def portScan(targethost, targetport):
    try:
        sock = socket(AF_INET, SOCK_STREAM)
        sock.connect((targethost, targetport))
        print(f"{Fore.GREEN}[+] {targetport} => Port Open{Style.RESET_ALL}")
    except:
        print(f"{Fore.RED}[-] {targetport} => Port Close{Style.RESET_ALL}")
    finally:
        sock.close()

def hostScan(targethost, targetports):
    try:
        targetIp = gethostbyname(targethost)
        print("*" * 15, "*" * len(targetIp), sep="")
        print(f"{Fore.GREEN}[+] IP Address: {targetIp}{Style.RESET_ALL}")
        try:
            targetName = gethostbyaddr(targetIp)
            print(f"{Fore.GREEN}[+] IP Path: {targetName[0]}{Style.RESET_ALL}")
            print("*" * 13, "*" * len(targetName[0]), sep="")
        except:
            print(f"{Fore.RED}[-] Path Not Found{Style.RESET_ALL}")
            print("*" * 15, "*" * len(targetIp), sep="")
    except:
        print(f"{Fore.RED}[-] Host Not Found: {targethost}{Style.RESET_ALL}")

    setdefaulttimeout(1)
    for targetport in targetports:
        try:
            t = Thread(target=portScan, args=(targethost, int(targetport)))
            t.start()
        except ValueError:
            print("Invalid operation")

def main():
    parser = optparse.OptionParser("Program Usage: -H <Host Address> -p <Port Address>")
    parser.add_option("-H", dest="targetHost", type="string", help="Target Host")
    parser.add_option("-p", dest="targetPort", type="string", help="List of ports separated by (,) or without (,)")
    (options, args) = parser.parse_args()
    targetHost = options.targetHost
    targetPorts = str(options.targetPort).split(",")
    if (targetHost == None) or (targetPorts[0] == None):
        print(parser.usage)
        exit(0)
    hostScan(targetHost, targetPorts)

if __name__ == "__main__":
    main()
