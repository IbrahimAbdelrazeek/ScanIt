#!/usr/bin/python
import socket , threading , sys 
from datetime import datetime 
from colorama import Fore ,Style , init ;

## Built a Function : 
def Scanport(target, port) : 
    try : 
        # Built a Socket TCP Object .
        ClientSocObject = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
        ClientSocObject.settimeout(1)
        ConnectionOutput = ClientSocObject.connect_ex((target,port))
        if ConnectionOutput == 0 : 
            print(f"Port {port} Is opened ")
        ClientSocObject.close()  ## For Closing the connection because the port is closed !

    
    except socket.error as er : 
        print(f"Socket error on port {port}:{er}")
    except Exception as ex : 
        print(f"Unexpected Error on port {port} , {ex}")

## Related to Command Structure .
def main() : 
    #python3 scanner.py hostname 
    if len(sys.argv) == 2 : 
        target = sys.argv[1]
        # port   = sys.argv[2]   
    else : 
        print(f"Invalid number of arguments \r\npythonx scanner.py Target ") ; sys.exit(1)
    
    try : 
        target_ip = socket.gethostbyname(target) 
    except socket.gaierror:
        print(f"Unable to resolve hostname{target}")
    ## Colorify the Output 
    init(autoreset=True)
    def display_intro(target=target):
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(Fore.BLUE + Style.BRIGHT + "=" * 30)
        print(Fore.BLUE + Style.BRIGHT + f"{'=' * 10}  ScanIt  {'=' * 10}")
        print(Fore.BLUE + Style.BRIGHT + "=" * 30)
        
        print(Fore.CYAN + "=" * 30)
        print(Fore.CYAN + f"Scanning Host :{target} {(target_ip)}") ; print(Fore.CYAN +f"Time {current_time}")
        print(Fore.CYAN + "=" * 30)
    display_intro()
    try : 
        # uyse multithreading to scan ports concurently : 
        threads = [] 
        
        for PortNum in range(1,65535) : ## For the range of 65536 PORT .
            thread = threading.Thread(target=Scanport , args=(target_ip , PortNum))
            threads.append(thread)
            thread.start()
        # Wait for all thread to complete .
        for thread in threads : 
            thread.join()
    except KeyboardInterrupt : 
        print("\nExisting program.")
    except socket.error as er : 
        print(f"Socket error {er}")
        sys.exit(1)
    print("Scann completed")

if __name__ == "__main__":
    main() 