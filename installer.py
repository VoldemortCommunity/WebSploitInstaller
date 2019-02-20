#SELF DESTRUCTIVE WEBSPLOIT Installer for Termux v0.1
#Created by @voldemort1912 (GitHub)
#@hewhomustn0tbenamed (Telegram)
#Created on 20/02/2019 10:52 IST

#imports
import os 
import sys 
import subprocess
from time import sleep
from queue import Queue 
from os.path import exists
from subprocess import Popen
from threading import Thread, RLock

#body

#install requirements
os.system("pkg update -y")
os.system("pkg upgrade -y")

class Install:

    def __init__(self, path_to_req): 
        self.lock = RLock()
        self.is_alive = True
        self.is_reading = True 
        self.is_installing = False 
        self.requirements = Queue()
        self.path_to_req = path_to_req
    
    @property 
    def path_exists(self):
        return exists(self.path_to_req)
    
    def read_file(self):
        with open('requirements.txt', mode='rt') as file: 
            for line in file:
                if line:
                    with self.lock:
                        self.requirements.put(line.replace('\n', ''))

        self.is_reading = False 

    def install(self, name):
        print('[+] Installing {} ...'.format(name))
        cmd = 'pkg install -y {}'.format(name)
        cmd = cmd.split()

        try:
            self.is_installing = True 
            Popen(cmd).wait()
        except:
            print('[!] Failed to install {}'.format(name))
        finally:
            print('\n')
            self.is_installing = False 
    
    def install_all(self):
        while self.is_alive:

            while self.requirements.qsize():
                with self.lock:
                    name = self.requirements.get()
                self.install(name)

    def start_primary_threads(self):
        read_thread = Thread(target=self.read_file)
        install_all_thread = Thread(target=self.install_all)

        read_thread.daemon = True 
        install_all_thread.daemon = True 

        read_thread.start()
        install_all_thread.start()

    def start(self):
        if self.path_exists:
            self.start_primary_threads()

            while self.is_alive:

                try:
                    if not self.is_reading and not self.requirements.qsize() and not self.is_installing:
                        self.stop() 
                    sleep(0.5)
                except KeyboardInterrupt:
                    self.stop()             

        else:
            print('[*] Unable to locate the file requirements.txt') 
    
    def stop(self):
        self.is_alive = False 
    

if __name__ == '__main__':
    path_to_req = 'requirements.txt'

    install = Install(path_to_req)
    install.start()
	
os.system("pip install --upgrade pip")
os.system("pip2 install requests")
os.system("pip2 install scapy")
    
os.system("git clone https://github.com/websploit/websploit $HOME/WebSploit")
os.system("chmod +x $HOME/WebSploit/*")
os.system("echo '\033[01;32;1mWebSploit has Been Installed Successfully.\n\n'")
os.system("echo '\033[01;31mTHE PROGRAM WILL NOW SELF DESTRUCT...\n'")
os.system("echo '\033[01;32;1m \n'")
try:
	input("Press Enter to Continue...")
except SyntaxError:
	pass
	
	os.system("echo '\nDeleting!!!\033[0m\n'")
	# end of file 
dir = os.getcwd()
nam = sys.argv[0]
#print(dir)
#print(nam)
os.remove(dir+'/requirements.txt')
os.remove(dir+'/'+nam)
os.system("rm -rf "+dir)