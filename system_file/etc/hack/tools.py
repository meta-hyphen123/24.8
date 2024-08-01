class AnonymouslySurf():
    TITLE = "Anonymously Surf"
    DESCRIPTION = "It automatically overwrites the RAM when\n" \
                  "the system is shutting down and also change Ip."
    INSTALL_COMMANDS = [
        "sudo git clone https://gitclone.com/github.com/Und3rf10w/kali-anonsurf.git",
        "cd kali-anonsurf && sudo ./installer.sh && cd .. && sudo rm -r kali-anonsurf"
    ]
    RUN_COMMANDS = ["sudo anonsurf start"]
    PROJECT_URL = "https://gitclone.com/github.com/Und3rf10w/kali-anonsurf"

    def __init__(self):
        super(AnonymouslySurf, self).__init__([('Stop', self.stop)])

    def stop(self):
        os.system("sudo anonsurf stop")


class Multitor():
    TITLE = "Multitor"
    DESCRIPTION = "How to stay in multi places at the same time"
    INSTALL_COMMANDS = [
        "sudo git clone https://gitclone.com/github.com/trimstray/multitor.git",
        "cd multitor;sudo bash setup.sh install"
    ]
    RUN_COMMANDS = ["multitor --init 2 --user debian-tor --socks-port 9000 --control-port 9900 --proxy privoxy --haproxy"]
    PROJECT_URL = "https://gitclone.com/github.com/trimstray/multitor"

    def __init__(self):
        super(Multitor, self).__init__(runnable = False)
class ddos():
    TITLE = "ddos"
    DESCRIPTION = (
        "Best DDoS Attack Script With 36 Plus Methods."
        "DDoS attacks\n\b "
        "for SECURITY TESTING PURPOSES ONLY! "
    )

    INSTALL_COMMANDS = [
        "git clone https://gitclone.com/github.com/the-deepnet/ddos.git",
        "cd ddos;sudo pip3 install -r requirements.txt",
    ]
    PROJECT_URL = "https://gitclone.com/github.com/the-deepnet/ddos.git"

    def run(self):
        method = input("Enter Method >> ")
        url = input("Enter URL >> ")
        threads = input("Enter Threads >> ")
        proxylist = input(" Enter ProxyList >> ")
        multiple = input(" Enter Multiple >> ")
        timer = input(" Enter Timer >> ")
        os.system("cd ddos;")
        subprocess.run(
            [
                "sudo",
                "python3 ddos",
                method,
                url,
                "socks_type5.4.1",
                threads,
                proxylist,
                multiple,
                timer,
            ]
        )


class SlowLoris():
    TITLE = "SlowLoris"
    DESCRIPTION = (
        "Slowloris is basically an HTTP Denial of Service attack."
        "It send lots of HTTP Request"
    )
    INSTALL_COMMANDS = ["sudo pip3 install slowloris"]

    def run(self):
        target_site = input("Enter Target Site:- ")
        subprocess.run(["slowloris", target_site])


class Asyncrone():
    TITLE = "Asyncrone"
    DESCRIPTION = (
        "aSYNcrone is a C language based, mulltifunction SYN Flood "
        "DDoS Weapon.\nDisable the destination system by sending a "
        "SYN packet intensively to the destination."
    )
    INSTALL_COMMANDS = [
        "git clone https://gitclone.com/github.com/fatih4842/aSYNcrone.git",
        "cd aSYNcrone;sudo gcc aSYNcrone.c -o aSYNcrone -lpthread",
    ]
    PROJECT_URL = "https://gitclone.com/github.com/fatihsnsy/aSYNcrone"

    def run(self):
        source_port = input("Enter Source Port >> ")
        target_ip = input("Enter Target IP >> ")
        target_port = input("Enter Target port >> ")
        os.system("cd aSYNcrone;")
        subprocess.run(
            ["sudo", "./aSYNcrone", source_port, target_ip, target_port, 1000]
        )


class UFONet():
    TITLE = "UFOnet"
    DESCRIPTION = (
        "UFONet - is a free software, P2P and cryptographic "
        "-disruptive \n toolkit- that allows to perform DoS and "
        "DDoS attacks\n\b "
        "More Usage Visit"
    )
    INSTALL_COMMANDS = [
        "sudo git clone https://gitclone.com/github.com/epsylon/ufonet.git",
        "cd ufonet;sudo python3 setup.py install;sudo pip3 install GeoIP;sudo pip3 install python-geoip;sudo pip3 install pygeoip;sudo pip3 install requests;sudo pip3 install pycrypto;sudo pip3 install pycurl;sudo pip3 install whois;sudo pip3 install scapy-python3",
    ]
    RUN_COMMANDS = ["sudo python3 ufonet --gui"]
    PROJECT_URL = "https://gitclone.com/github.com/epsylon/ufonet"


class GoldenEye():
    TITLE = "GoldenEye"
    DESCRIPTION = (
        "GoldenEye is a python3 app for SECURITY TESTING PURPOSES ONLY!\n"
        "GoldenEye is a HTTP DoS Test Tool."
    )
    INSTALL_COMMANDS = [
        "sudo git clone https://gitclone.com/github.com/jseidl/GoldenEye.git;"
        "chmod -R 755 GoldenEye"
    ]
    PROJECT_URL = "https://gitclone.com/github.com/jseidl/GoldenEye"

    def run(self):
        os.system("cd GoldenEye ;sudo ./goldeneye.py")
        print("\033[96m Go to Directory \n [*] USAGE: ./goldeneye.py <url> [OPTIONS]")


class Saphyra():
    TITLE = "SaphyraDDoS"
    DESCRIPTION = "A complex python code to DDoS any website with a very easy usage.!\n"
    INSTALL_COMMANDS = [
        "sudo su",
        "git clone https://gitclone.com/github.com/anonymous24x7/Saphyra-DDoS.git",
        "cd Saphyra-DDoS",
        "chmod +x saphyra.py",
        "python saphyra.py",
    ]
    PROJECT_URL = "https://gitclone.com/github.com/anonymous24x7/Saphyra-DDoS"

    def run(self):
        url = input("Enter url>>> ")
        try:
            os.system("python saphyra.py " + url)
        except Exception:
            print("Enter a valid url.")
class RouterSploit():
    TITLE = "RouterSploit"
    DESCRIPTION = "The RouterSploit Framework is an open-source exploitation " \
                  "framework dedicated to embedded devices"
    INSTALL_COMMANDS = [
        "sudo git clone https://gitclone.com/github.com/threat9/routersploit.git",
        "cd routersploit && sudo python3 -m pip install -r requirements.txt"
    ]
    RUN_COMMANDS = ["cd routersploit && sudo python3 rsf.py"]
    PROJECT_URL = "https://gitclone.com/github.com/threat9/routersploit"


class WebSploit():
    TITLE = "WebSploit"
    DESCRIPTION = "Websploit is an advanced MITM framework."
    INSTALL_COMMANDS = [
        "sudo git clone https://gitclone.com/github.com/The404Hacking/websploit.git;cd websploit/Setup;sudo chmod +x install.sh && sudo bash install.sh"
    ]
    RUN_COMMANDS = ["sudo websploit"]
    PROJECT_URL = "https://gitclone.com/github.com/The404Hacking/websploit "


class Commix():
    TITLE = "Commix"
    DESCRIPTION = "Automated All-in-One OS command injection and exploitation " \
                  "tool.\nCommix can be used from web developers, penetration " \
                  "testers or even security researchers\n in order to test " \
                  "web-based applications with the view to find bugs,\n " \
                  "errors or vulnerabilities related to command injection " \
                  "attacks.\n Usage: python commix.py [option(s)]"
    INSTALL_COMMANDS = [
        "git clone https://gitclone.com/github.com/commixproject/commix.git commix",
        "cd commix;sudo python setup.py install"
    ]
    RUN_COMMANDS = ["sudo python commix.py --wizard"]
    PROJECT_URL = "https://gitclone.com/github.com/commixproject/commix"

    def __init__(self):
        super(Commix, self).__init__(runnable = False)
class Autopsy():
    TITLE = "Autopsy"
    DESCRIPTION = "Autopsy is a platform that is used by Cyber Investigators.\n" \
                  "[!] Works in any OS\n" \
                  "[!] Recover Deleted Files from any OS & Media \n" \
                  "[!] Extract Image Metadata"
    RUN_COMMANDS = ["sudo autopsy"]

    def __init__(self):
        super(Autopsy, self).__init__(installable = False)


class Wireshark():
    TITLE = "Wireshark"
    DESCRIPTION = "Wireshark is a network capture and analyzer \n" \
                  "tool to see what’s happening in your network.\n " \
                  "And also investigate Network related incident"
    RUN_COMMANDS = ["sudo wireshark"]

    def __init__(self):
        super(Wireshark, self).__init__(installable = False)


class BulkExtractor():
    TITLE = "Bulk extractor"
    DESCRIPTION = "Extract useful information without parsing the file system"
    PROJECT_URL = "https://gitclone.com/github.com/simsong/bulk_extractor"

    def __init__(self):
        super(BulkExtractor, self).__init__([
            ('GUI Mode (Download required)', self.gui_mode),
            ('CLI Mode', self.cli_mode)
        ], installable = False, runnable = False)

    def gui_mode(self):
        os.system(
            "sudo git clone https://gitclone.com/github.com/simsong/bulk_extractor.git")
        os.system("ls src/ && cd .. && cd java_gui && ./BEViewer")
        print(
            "If you getting error after clone go to /java_gui/src/ And Compile .Jar file && run ./BEViewer")
        print(
            "Please Visit For More Details About Installation >> https://gitclone.com/github.com/simsong/bulk_extractor")

    def cli_mode(self):
        os.system("sudo apt install bulk-extractor")
        print("bulk_extractor and options")
        os.system("bulk_extractor -h")
        os.system(
            'echo "bulk_extractor [options] imagefile" | boxes -d headline | lolcat')


class Guymager():
    TITLE = "Disk Clone and ISO Image Acquire"
    DESCRIPTION = "Guymager is a free forensic imager for media acquisition."
    INSTALL_COMMANDS = ["sudo apt install guymager"]
    RUN_COMMANDS = ["sudo guymager"]
    PROJECT_URL = "https://guymager.sourceforge.io/"


class Toolsley():
    TITLE = "Toolsley"
    DESCRIPTION = "Toolsley got more than ten useful tools for investigation.\n" \
                  "[+]File signature verifier\n" \
                  "[+]File identifier \n" \
                  "[+]Hash & Validate \n" \
                  "[+]Binary inspector \n " \
                  "[+]Encode text \n" \
                  "[+]Data URI generator \n" \
                  "[+]Password generator"
    PROJECT_URL = "https://www.toolsley.com/"

    def __init__(self):
        super(Toolsley, self).__init__(installable = False, runnable = False)

class NMAP():
    TITLE = "nmap"
    DESCRIPTION = "Free and open source utility for network discovery and security auditing"
    INSTALL_COMMANDS = [
        "sudo git clone https://gitclone.com/github.com/nmap/nmap.git",
        "sudo chmod -R 755 nmap && cd nmap && sudo ./configure && make && sudo make install"
    ]
    PROJECT_URL = "https://gitclone.com/github.com/nmap/nmap"

    def __init__(self):
        super(NMAP, self).__init__(runnable = False)


class Dracnmap():
    TITLE = "Dracnmap"
    DESCRIPTION = "Dracnmap is an open source program which is using to \n" \
                  "exploit the network and gathering information with nmap help."
    INSTALL_COMMANDS = [
        "sudo git clone https://gitclone.com/github.com/Screetsec/Dracnmap.git",
        "cd Dracnmap && chmod +x dracnmap-v2.2-dracOs.sh  dracnmap-v2.2.sh"
    ]
    RUN_COMMANDS = ["cd Dracnmap;sudo ./dracnmap-v2.2.sh"]
    PROJECT_URL = "https://gitclone.com/github.com/Screetsec/Dracnmap"

#    def __init__(self):
#        super(Dracnmap, self).__init__(runnable = False)


class PortScan():
    TITLE = "Port scanning"

    def __init__(self):
        super(PortScan, self).__init__(installable = False)

    def run(self):
        clear_screen()
        target = input('Select a Target IP: ')
        subprocess.run(["sudo", "nmap", "-O", "-Pn", target])


class Host2IP():
    TITLE = "Host to IP "

    def __init__(self):
        super(Host2IP, self).__init__(installable = False)

    def run(self):
        clear_screen()
        host = input("Enter host name (e.g. www.google.com):-  ")
        ips = socket.gethostbyname(host)
        print(ips)


class XeroSploit():
    TITLE = "Xerosploit"
    DESCRIPTION = "Xerosploit is a penetration testing toolkit whose goal is to perform\n" \
                  "man-in-the-middle attacks for testing purposes"
    INSTALL_COMMANDS = [
        "git clone https://gitclone.com/github.com/LionSec/xerosploit.git",
        "cd xerosploit && sudo python install.py"
    ]
    RUN_COMMANDS = ["sudo xerosploit"]
    PROJECT_URL = "https://gitclone.com/github.com/LionSec/xerosploit"


class RedHawk():
    TITLE = "RED HAWK"
    DESCRIPTION = "All in one tool for Information Gathering and Vulnerability Scanning."
    INSTALL_COMMANDS = [
        "git clone https://gitclone.com/github.com/Tuhinshubhra/RED_HAWK.git"]
    RUN_COMMANDS = ["cd RED_HAWK;php rhawk.php"]
    PROJECT_URL = "https://gitclone.com/github.com/Tuhinshubhra/RED_HAWK"


class ReconSpider():
    TITLE = "ReconSpider"
    DESCRIPTION = "ReconSpider is most Advanced Open Source Intelligence (OSINT)" \
                  " Framework for scanning IP Address, Emails, \n" \
                  "Websites, Organizations and find out information from" \
                  " different sources.\n"
    INSTALL_COMMANDS = [
        "sudo git clone https://gitclone.com/github.com/bhavsec/reconspider.git",
        "sudo apt install python3 python3-pip && cd reconspider && sudo python3 setup.py install"
    ]
    RUN_COMMANDS = ["cd reconspider;python3 reconspider.py"]
    PROJECT_URL = "https://gitclone.com/github.com/bhavsec/reconspider"

#    def __init__(self):
#        super(ReconSpider, self).__init__(runnable = False)


class IsItDown():
    TITLE = "IsItDown"
    DESCRIPTION = "Check Website Is Online or Not"

    def __init__(self):
        super(IsItDown, self).__init__(
            [('Open', self.open)], installable = False, runnable = False)

    def open(self):
        webbrowser.open_new_tab("https://www.isitdownrightnow.com/")


class Infoga():
    TITLE = "Infoga"
    DESCRIPTION = "Infoga is a tool gathering email accounts information\n" \
                  "(ip, hostname, country,...) from different public source"
    INSTALL_COMMANDS = [
        "git clone https://gitclone.com/github.com/m4ll0k/Infoga.git",
        "cd Infoga;sudo python3 setup.py install"
    ]
    RUN_COMMANDS = ["cd Infoga;python3 infoga.py"]
    PROJECT_URL = "https://gitclone.com/github.com/m4ll0k/Infoga"


class ReconDog():
    TITLE = "ReconDog"
    DESCRIPTION = "ReconDog Information Gathering Suite"
    INSTALL_COMMANDS = ["git clone https://gitclone.com/github.com/s0md3v/ReconDog.git"]
    RUN_COMMANDS = ["cd ReconDog;sudo python dog"]
    PROJECT_URL = "https://gitclone.com/github.com/s0md3v/ReconDog"


class Striker():
    TITLE = "Striker"
    DESCRIPTION = "Recon & Vulnerability Scanning Suite"
    INSTALL_COMMANDS = [
        "git clone https://gitclone.com/github.com/s0md3v/Striker.git",
        "cd Striker && pip3 install -r requirements.txt"
    ]
    PROJECT_URL = "https://gitclone.com/github.com/s0md3v/Striker"

    def run(self):
        site = input("Enter Site Name (example.com) >> ")
        os.chdir("Striker")
        subprocess.run(["sudo", "python3", "striker.py", site])


class SecretFinder():
    TITLE = "SecretFinder"
    DESCRIPTION = "SecretFinder - A python script for find sensitive data \n" \
                  "like apikeys, accesstoken, authorizations, jwt,..etc \n " \
                  "and search anything on javascript files.\n\n " \
                  "Usage: python SecretFinder.py -h"
    INSTALL_COMMANDS = [
        "git clone https://gitclone.com/github.com/m4ll0k/SecretFinder.git secretfinder",
        "cd secretfinder; sudo pip3 install -r requirements.txt"
    ]
    PROJECT_URL = "https://gitclone.com/github.com/m4ll0k/SecretFinder"

    def __init__(self):
        super(SecretFinder, self).__init__(runnable = False)


class Shodan():
    TITLE = "Find Info Using Shodan"
    DESCRIPTION = "Get ports, vulnerabilities, information, banners,..etc \n " \
                  "for any IP with Shodan (no apikey! no rate limit!)\n" \
                  "[X] Don't use this tool because your ip will be blocked by Shodan!"
    INSTALL_COMMANDS = ["git clone https://gitclone.com/github.com/m4ll0k/Shodanfy.py.git"]
    PROJECT_URL = "https://gitclone.com/github.com/m4ll0k/Shodanfy.py"

    def __init__(self):
        super(Shodan, self).__init__(runnable = False)


class PortScannerRanger():
    TITLE = "Port Scanner rang3r"
    DESCRIPTION = "rang3r is a python script which scans in multi thread\n " \
                  "all alive hosts within your range that you specify."
    INSTALL_COMMANDS = [
        "git clone https://gitclone.com/github.com/floriankunushevci/rang3r.git;"
        "sudo pip install termcolor"]
    PROJECT_URL = "https://gitclone.com/github.com/floriankunushevci/rang3r"

    def run(self):
        ip = input("Enter Ip >> ")
        os.chdir("rang3r")
        subprocess.run(["sudo", "python", "rang3r.py", "--ip", ip])


class Breacher():
    TITLE = "Breacher"
    DESCRIPTION = "An advanced multithreaded admin panel finder written in python."
    INSTALL_COMMANDS = ["git clone https://gitclone.com/github.com/s0md3v/Breacher.git"]
    PROJECT_URL = "https://gitclone.com/github.com/s0md3v/Breacher"
    
    def run(self):
        domain = input("Enter domain (example.com) >> ")
        os.chdir("Breacher")
        subprocess.run(["python3", "breacher.py", "-u", domain])
class HatCloud():
    TITLE = "HatCloud"
    DESCRIPTION = "HatCloud build in Ruby. It makes bypass in CloudFlare for " \
                  "discover real IP."
    INSTALL_COMMANDS = ["git clone https://gitclone.com/github.com/HatBashBR/HatCloud.git"]
    PROJECT_URL = "https://gitclone.com/github.com/HatBashBR/HatCloud"

    def run(self):
        site = input("Enter Site >> ")
        os.chdir("HatCloud")
        subprocess.run(["sudo", "ruby", "hatcloud.rb", "-b", site])
class TheFatRat():
    TITLE = "The FatRat"
    DESCRIPTION = "TheFatRat Provides An Easy way to create Backdoors and \n" \
                  "Payload which can bypass most anti-virus"
    INSTALL_COMMANDS = [
        "sudo git clone https://gitclone.com/github.com/Screetsec/TheFatRat.git",
        "cd TheFatRat && sudo chmod +x setup.sh"
    ]
    RUN_COMMANDS = ["cd TheFatRat && sudo bash setup.sh"]
    PROJECT_URL = "https://gitclone.com/github.com/Screetsec/TheFatRat"

    def __init__(self):
        super(TheFatRat, self).__init__([
            ('Update', self.update),
            ('Troubleshoot', self.troubleshoot)
        ])

    def update(self):
        os.system(
            "cd TheFatRat && bash update && chmod +x setup.sh && bash setup.sh")

    def troubleshoot(self):
        os.system("cd TheFatRat && sudo chmod +x chk_tools && ./chk_tools")


class Brutal():
    TITLE = "Brutal"
    DESCRIPTION = "Brutal is a toolkit to quickly create various payload," \
                  "powershell attack,\nvirus attack and launch listener for " \
                  "a Human Interface Device"
    INSTALL_COMMANDS = [
        "sudo git clone https://gitclone.com/github.com/Screetsec/Brutal.git",
        "cd Brutal && sudo chmod +x Brutal.sh"
    ]
    RUN_COMMANDS = ["cd Brutal && sudo bash Brutal.sh"]
    PROJECT_URL = "https://gitclone.com/github.com/Screetsec/Brutal"

    def show_info(self):
        super(Brutal, self).show_info()
        print("""
        [!] Requirement
            >> Arduino Software (I used v1.6.7)
            >> TeensyDuino
            >> Linux udev rules
            >> Copy and paste the PaensyLib folder inside your Arduino libraries
    
        [!] Kindly Visit below link for Installation for Arduino 
            >> https://gitclone.com/github.com/Screetsec/Brutal/wiki/Install-Requirements 
        """)


class Stitch():
    TITLE = "Stitch"
    DESCRIPTION = "Stitch is Cross Platform Python Remote Administrator Tool\n\t" \
                  "[!] Refer Below Link For Wins & MAc Os"
    INSTALL_COMMANDS = [
        "sudo git clone https://gitclone.com/github.com/nathanlopez/Stitch.git",
        "cd Stitch && sudo pip install -r lnx_requirements.txt"
    ]
    RUN_COMMANDS = ["cd Stitch && sudo python main.py"]
    PROJECT_URL = "https://nathanlopez.gitclone.com/github.io/Stitch"


class MSFVenom():
    TITLE = "MSFvenom Payload Creator"
    DESCRIPTION = "MSFvenom Payload Creator (MSFPC) is a wrapper to generate \n" \
                  "multiple types of payloads, based on users choice.\n" \
                  "The idea is to be as simple as possible (only requiring " \
                  "one input) \nto produce their payload."
    INSTALL_COMMANDS = [
        "sudo git clone https://gitclone.com/github.com/g0tmi1k/msfpc.git",
        "cd msfpc;sudo chmod +x msfpc.sh"
    ]
    RUN_COMMANDS = ["cd msfpc;sudo bash msfpc.sh -h -v"]
    PROJECT_URL = "https://gitclone.com/github.com/g0tmi1k/msfpc"


class Venom():
    TITLE = "Venom Shellcode Generator"
    DESCRIPTION = "venom 1.0.11 (malicious_server) was build to take " \
                  "advantage of \n apache2 webserver to deliver payloads " \
                  "(LAN) using a fake webpage written in html"
    INSTALL_COMMANDS = [
        "sudo git clone https://gitclone.com/github.com/r00t-3xp10it/venom.git",
        "sudo chmod -R 775 venom*/ && cd venom*/ && cd aux && sudo bash setup.sh",
        "sudo ./venom.sh -u"
    ]
    RUN_COMMANDS = ["cd venom && sudo ./venom.sh"]
    PROJECT_URL = "https://gitclone.com/github.com/r00t-3xp10it/venom"


class Spycam():
    TITLE = "Spycam"
    DESCRIPTION = "Script to generate a Win32 payload that takes the webcam " \
                  "image every 1 minute and send it to the attacker"
    INSTALL_COMMANDS = [
        "sudo git clone https://gitclone.com/github.com/indexnotfound404/spycam.git",
        "cd spycam && bash install.sh && chmod +x spycam"
    ]
    RUN_COMMANDS = ["cd spycam && ./spycam"]
    PROJECT_URL = "https://gitclone.com/github.com/indexnotfound404/spycam"


class MobDroid():
    TITLE = "Mob-Droid"
    DESCRIPTION = "Mob-Droid helps you to generate metasploit payloads in " \
                  "easy way\n without typing long commands and save your time"
    INSTALL_COMMANDS = [
        "git clone https://gitclone.com/github.com/kinghacker0/mob-droid.git"]
    RUN_COMMANDS = ["cd mob-droid;sudo python mob-droid.py"]
    PROJECT_URL = "https://gitclone.com/github.com/kinghacker0/Mob-Droid"


class Enigma():
    TITLE = "Enigma"
    DESCRIPTION = "Enigma is a Multiplatform payload dropper"
    INSTALL_COMMANDS = [
        "sudo git clone https://gitclone.com/github.com/UndeadSec/Enigma.git"]
    RUN_COMMANDS = ["cd Enigma;sudo python enigma.py"]
    PROJECT_URL = "https://gitclone.com/github.com/UndeadSec/Enigma"
class autophisher():
    TITLE = "Autophisher RK"
    DESCRIPTION = "Automated Phishing Toolkit"
    INSTALL_COMMANDS = [
        "sudo git clone https://gitclone.com/github.com/CodingRanjith/autophisher.git",
        "cd autophisher"
    ]
    RUN_COMMANDS = ["cd autophisher;sudo bash autophisher.sh"]
    PROJECT_URL = "https://gitclone.com/github.com/CodingRanjith/autophisher"
    
class Pyphisher():
    TITLE = "Pyphisher"
    DESCRIPTION = "Easy to use phishing tool with 77 website templates"
    INSTALL_COMMANDS = [
        "sudo git clone https://gitclone.com/github.com/KasRoudra/PyPhisher",
        "cd PyPhisher/files",
        "pip3 install -r requirements.txt"
    ]
    RUN_COMMANDS = ["cd PyPhisher;sudo python3 pyphisher.py"]
    PROJECT_URL = "git clone https://gitclone.com/github.com/KasRoudra/PyPhisher"    
    
class AdvPhishing():
    TITLE = "AdvPhishing"
    DESCRIPTION = "This is Advance Phishing Tool ! OTP PHISHING"
    INSTALL_COMMANDS = [
        "sudo git clone https://gitclone.com/github.com/Ignitetch/AdvPhishing.git",
        "cd AdvPhishing;chmod 777 *;bash Linux-Setup.sh"]
    RUN_COMMANDS = ["cd AdvPhishing && sudo bash AdvPhishing.sh"]
    PROJECT_URL = "https://gitclone.com/github.com/Ignitetch/AdvPhishing"      

class Setoolkit():
    TITLE = "Setoolkit"
    DESCRIPTION = "The Social-Engineer Toolkit is an open-source penetration\n" \
                  "testing framework designed for social engine"
    INSTALL_COMMANDS = [
        "git clone https://gitclone.com/github.com/trustedsec/social-engineer-toolkit/",
        "cd social-engineer-toolkit && sudo python3 setup.py"
    ]
    RUN_COMMANDS = ["sudo setoolkit"]
    PROJECT_URL = "https://gitclone.com/github.com/trustedsec/social-engineer-toolkit"


class SocialFish():
    TITLE = "SocialFish"
    DESCRIPTION = "Automated Phishing Tool & Information Collector NOTE: username is 'root' and password is 'pass'"
    INSTALL_COMMANDS = [
        "sudo git clone https://gitclone.com/github.com/UndeadSec/SocialFish.git && sudo apt-get install python3 python3-pip python3-dev -y",
        "cd SocialFish && sudo python3 -m pip install -r requirements.txt"
    ]
    RUN_COMMANDS = ["cd SocialFish && sudo python3 SocialFish.py root pass"]
    PROJECT_URL = "https://gitclone.com/github.com/UndeadSec/SocialFish"


class HiddenEye():
    TITLE = "HiddenEye"
    DESCRIPTION = "Modern Phishing Tool With Advanced Functionality And " \
                  "Multiple Tunnelling Services \n" \
                  "\t [!]https://gitclone.com/github.com/DarkSecDevelopers/HiddenEye"
    INSTALL_COMMANDS = [
        "sudo git clone https://gitclone.com/github.com/Morsmalleo/HiddenEye.git ;sudo chmod 777 HiddenEye",
        "cd HiddenEye;sudo pip3 install -r requirements.txt;sudo pip3 install requests;pip3 install pyngrok"
    ]
    RUN_COMMANDS = ["cd HiddenEye;sudo python3 HiddenEye.py"]
    PROJECT_URL = "https://gitclone.com/github.com/Morsmalleo/HiddenEye.git"


class Evilginx2():
    TITLE = "Evilginx2"
    DESCRIPTION = "evilginx2 is a man-in-the-middle attack framework used " \
                  "for phishing login credentials along with session cookies,\n" \
                  "which in turn allows to bypass 2-factor authentication protection.\n\n\t " \
                  "[+]Make sure you have installed GO of version at least 1.14.0 \n" \
                  "[+]After installation, add this to your ~/.profile, assuming that you installed GO in /usr/local/go\n\t " \
                  "[+]export GOPATH=$HOME/go \n " \
                  "[+]export PATH=$PATH:/usr/local/go/bin:$GOPATH/bin \n" \
                  "[+]Then load it with source ~/.profiles."
    INSTALL_COMMANDS = [
        "sudo apt-get install git make;go get -u gitclone.com/github.com/kgretzky/evilginx2",
        "cd $GOPATH/src/gitclone.com/github.com/kgretzky/evilginx2;make",
        "sudo make install;sudo evilginx"
    ]
    RUN_COMMANDS = ["sudo evilginx"]
    PROJECT_URL = "https://gitclone.com/github.com/kgretzky/evilginx2"


class ISeeYou():
    TITLE = "I-See_You"
    DESCRIPTION = "[!] ISeeYou is a tool to find Exact Location of Victom By" \
                  " User SocialEngineering or Phishing Engagement..\n" \
                  "[!] Users can expose their local servers to the Internet " \
                  "and decode the location coordinates by looking at the log file"
    INSTALL_COMMANDS = [
        "sudo git clone https://gitclone.com/github.com/Viralmaniar/I-See-You.git",
        "cd I-See-You && sudo chmod u+x ISeeYou.sh"
    ]
    RUN_COMMANDS = ["cd I-See-You && sudo bash ISeeYou.sh"]
    PROJECT_URL = "https://gitclone.com/github.com/Viralmaniar/I-See-You"


class SayCheese():
    TITLE = "SayCheese"
    DESCRIPTION = "Take webcam shots from target just sending a malicious link"
    INSTALL_COMMANDS = ["sudo git clone https://gitclone.com/github.com/hangetzzu/saycheese"]
    RUN_COMMANDS = ["cd saycheese && sudo bash saycheese.sh"]
    PROJECT_URL = "https://gitclone.com/github.com/hangetzzu/saycheese"


class QRJacking():
    TITLE = "QR Code Jacking"
    DESCRIPTION = "QR Code Jacking (Any Website)"
    INSTALL_COMMANDS = [
        "sudo git clone https://gitclone.com/github.com/cryptedwolf/ohmyqr.git && sudo apt -y install scrot"]
    RUN_COMMANDS = ["cd ohmyqr && sudo bash ohmyqr.sh"]
    PROJECT_URL = "https://gitclone.com/github.com/cryptedwolf/ohmyqr"
    
class WifiPhisher():
    TITLE = "WifiPhisher"
    DESCRIPTION = "The Rogue Access Point Framework"
    INSTALL_COMMANDS = [
        "sudo git clone https://gitclone.com/github.com/wifiphisher/wifiphisher.git",
        "cd wifiphisher"]
    RUN_COMMANDS = ["cd wifiphisher && sudo python setup.py"]
    PROJECT_URL = "https://gitclone.com/github.com/wifiphisher/wifiphisher"   
    
class BlackEye():
    TITLE = "BlackEye"
    DESCRIPTION = "The ultimate phishing tool with 38 websites available!"
    INSTALL_COMMANDS = [
        "sudo git clone https://gitclone.com/github.com/thelinuxchoice/blackeye",
        "cd blackeye "]
    RUN_COMMANDS = ["cd blackeye && sudo bash blackeye.sh"]
    PROJECT_URL = "https://gitclone.com/github.com/An0nUD4Y/blackeye"      

class ShellPhish():
    TITLE = "ShellPhish"
    DESCRIPTION = "Phishing Tool for 18 social media"
    INSTALL_COMMANDS = ["git clone https://gitclone.com/github.com/An0nUD4Y/shellphish.git"]
    RUN_COMMANDS = ["cd shellphish;sudo bash shellphish.sh"]
    PROJECT_URL = "https://gitclone.com/github.com/An0nUD4Y/shellphish"
    
class Thanos():
    TITLE = "Thanos"
    DESCRIPTION = "Browser to Browser Phishingtoolkit"
    INSTALL_COMMANDS = [
        "sudo git clone https://gitclone.com/github.com/TridevReddy/Thanos.git",
        "cd Thanos && sudo chmod -R 777 Thanos.sh"
    ]
    RUN_COMMANDS = ["cd Thanos;sudo bash Thanos.sh"]
    PROJECT_URL = "https://gitclone.com/github.com/TridevReddy/Thanos"    
    
class QRLJacking():
    TITLE = "QRLJacking"
    DESCRIPTION = "QRLJacking"
    INSTALL_COMMANDS = [
        "git clone https://gitclone.com/github.com/OWASP/QRLJacking.git",
        "cd QRLJacking",
        "git clone https://gitclone.com/github.com/mozilla/geckodriver.git",
        "chmod +x geckodriver",
        "sudo mv -f geckodriver /usr/local/share/geckodriver",
        "sudo ln -s /usr/local/share/geckodriver /usr/local/bin/geckodriver",
        "sudo ln -s /usr/local/share/geckodriver /usr/bin/geckodriver",
        "cd QRLJacker;pip3 install -r requirements.txt"
    ]
    RUN_COMMANDS = ["cd QRLJacking/QRLJacker;python3 QrlJacker.py"]
    PROJECT_URL = "https://gitclone.com/github.com/OWASP/QRLJacking"
    
class Maskphish():
    TITLE = "Miskphish"
    DESCRIPTION = "Hide phishing URL under a normal looking URL (google.com or facebook.com)"
    INSTALL_COMMANDS = [
        "sudo git clone https://gitclone.com/github.com/jaykali/maskphish.git",
        "cd maskphish"]
    RUN_COMMANDS = ["cd maskphish;sudo bash maskphish.sh"]
    PROJECT_URL = "https://gitclone.com/github.com/jaykali/maskphish"            


class BlackPhish():
    TITLE = "BlackPhish"
    INSTALL_COMMANDS = [
        "sudo git clone https://gitclone.com/github.com/iinc0gnit0/BlackPhish.git",
        "cd BlackPhish;sudo bash install.sh"
    ]
    RUN_COMMANDS = ["cd BlackPhish;sudo python3 blackphish.py"]
    PROJECT_URL = "https://gitclone.com/github.com/iinc0gnit0/BlackPhish"

    def __init__(self):
        super(BlackPhish, self).__init__([('Update', self.update)])

    def update(self):
        os.system("cd BlackPhish;sudo bash update.sh")

class dnstwist():
    Title='dnstwist'
    Install_commands=['sudo git clone https://gitclone.com/github.com/elceef/dnstwist.git','cd dnstwist']
    Run_commands=['cd dnstwist;sudo python3 dnstwist.py']
    project_url='https://gitclone.com/github.com/elceef/dnstwist'

class Vegile():
    TITLE = "Vegile"
    DESCRIPTION = "This tool will set up your backdoor/rootkits when " \
                  "backdoor is already setup it will be \n" \
                  "hidden your specific process,unlimited your session in " \
                  "metasploit and transparent."
    INSTALL_COMMANDS = [
        "sudo git clone https://gitclone.com/github.com/Screetsec/Vegile.git",
        "cd Vegile && sudo chmod +x Vegile"
    ]
    RUN_COMMANDS = ["cd Vegile && sudo bash Vegile"]
    PROJECT_URL = "https://gitclone.com/github.com/Screetsec/Vegile"

    def before_run(self):
        os.system('echo "You can Use Command: \n'
                  '[!] Vegile -i / --inject [backdoor/rootkit] \n'
                  '[!] Vegile -u / --unlimited [backdoor/rootkit] \n'
                  '[!] Vegile -h / --help"|boxes -d parchment')


class ChromeKeyLogger():
    TITLE = "Chrome Keylogger"
    DESCRIPTION = "Hera Chrome Keylogger"
    INSTALL_COMMANDS = [
        "sudo git clone https://gitclone.com/github.com/UndeadSec/HeraKeylogger.git",
        "cd HeraKeylogger && sudo apt-get install python3-pip -y && sudo pip3 install -r requirements.txt"
    ]
    RUN_COMMANDS = ["cd HeraKeylogger && sudo python3 hera.py"]
    PROJECT_URL = "https://gitclone.com/github.com/UndeadSec/HeraKeylogger"
class Stitch():
    TITLE = "Stitch"
    DESCRIPTION = "Stitch is a cross platform python framework.\n" \
                  "which allows you to build custom payloads\n" \
                  "For Windows, Mac and Linux."
    INSTALL_COMMANDS = [
        "sudo git clone https://gitclone.com/github.com/nathanlopez/Stitch.git",
        "cd Stitch;sudo pip install -r lnx_requirements.txt"
    ]
    RUN_COMMANDS = ["cd Stitch;python main.py"]
    PROJECT_URL = "https://gitclone.com/github.com/nathanlopez/Stitch"


class Pyshell():
    TITLE = "Pyshell"
    DESCRIPTION = "Pyshell is a Rat Tool that can be able to download & upload " \
                  "files,\n Execute OS Command and more.."
    INSTALL_COMMANDS = [
        "sudo git clone https://gitclone.com/github.com/knassar702/Pyshell.git;"
        "sudo pip install pyscreenshot python-nmap requests"
    ]
    RUN_COMMANDS = ["cd Pyshell;./Pyshell"]
    PROJECT_URL = "https://gitclone.com/github.com/knassar702/pyshell"
class SteganoHide():
    TITLE = "SteganoHide"
    INSTALL_COMMANDS = ["sudo apt-get install steghide -y"]

    def run(self):
        choice_run = input(
            "[1] Hide\n"
            "[2] Extract\n"
            "[99]Cancel\n"
            ">> ")
        choice_run = validate_input(choice_run, [1, 2, 99])
        if choice_run is None:
            print("Please choose a valid input")
            return self.run()

        if choice_run == 99:
            return

        if choice_run == 1:
            file_hide = input("Enter Filename you want to Embed (1.txt) >> ")
            file_to_be_hide = input("Enter Cover Filename(test.jpeg) >> ")
            subprocess.run(
                ["steghide", "embed", "-cf", file_to_be_hide, "-ef", file_hide])

        elif choice_run == "2":
            from_file = input("Enter Filename From Extract Data >> ")
            subprocess.run(["steghide", "extract", "-sf", from_file])


class StegnoCracker():
    TITLE = "StegnoCracker"
    DESCRIPTION = "SteganoCracker is a tool that uncover hidden data inside " \
                  "files\n using brute-force utility"
    INSTALL_COMMANDS = [
        "pip3 install stegcracker && pip3 install stegcracker -U --force-reinstall"]

    def run(self):
        filename = input("Enter Filename:- ")
        passfile = input("Enter Wordlist Filename:- ")
        subprocess.run(["stegcracker", filename, passfile])

        
class StegoCracker():
    TITLE = "StegoCracker"
    DESCRIPTION = "StegoCracker is a tool that let's you hide data into image or audio files and can retrieve from a file " 
                  
    INSTALL_COMMANDS = [
        "sudo git clone https://gitclone.com/github.com/W1LDN16H7/StegoCracker.git",
        "sudo chmod -R 755 StegoCracker"
    ]
    RUN_COMMANDS = ["cd StegoCracker && python3 -m pip install -r requirements.txt ",
                   "./install.sh"
    ]
    PROJECT_URL = "https://gitclone.com/github.com/W1LDN16H7/StegoCracker"
    

class Whitespace():
    TITLE = "Whitespace"
    DESCRIPTION = "Use whitespace and unicode chars for steganography"
    INSTALL_COMMANDS = [
        "sudo git clone https://gitclone.com/github.com/beardog108/snow10.git",
        "sudo chmod -R 755 snow10"
    ]
    RUN_COMMANDS = ["cd snow10 && ./install.sh"]
    PROJECT_URL = "https://gitclone.com/github.com/beardog108/snow10"
class Web2Attack():
    TITLE = "Web2Attack"
    DESCRIPTION = "Web hacking framework with tools, exploits by python"
    INSTALL_COMMANDS = [
        "sudo git clone https://gitclone.com/github.com/santatic/web2attack.git"]
    RUN_COMMANDS = ["cd web2attack && sudo python3 w2aconsole"]
    PROJECT_URL = "https://gitclone.com/github.com/santatic/web2attack"


class Skipfish():
    TITLE = "Skipfish"
    DESCRIPTION = "Skipfish – Fully automated, active web application " \
                  "security reconnaissance tool \n " \
                  "Usage: skipfish -o [FolderName] targetip/site"
    RUN_COMMANDS = [
        "sudo skipfish -h",
        'echo "skipfish -o [FolderName] targetip/site"|boxes -d headline | lolcat'
    ]

    def __init__(self):
        super(Skipfish, self).__init__(installable = False)


class SubDomainFinder():
    TITLE = "SubDomain Finder"
    DESCRIPTION = "Sublist3r is a python tool designed to enumerate " \
                  "subdomains of websites using OSINT \n " \
                  "Usage:\n\t" \
                  "[1] python3 sublist3r.py -d example.com \n" \
                  "[2] python3 sublist3r.py -d example.com -p 80,443"
    INSTALL_COMMANDS = [
        "sudo pip3 install requests argparse dnspython",
        "sudo git clone https://gitclone.com/github.com/aboul3la/Sublist3r.git",
        "cd Sublist3r && sudo pip3 install -r requirements.txt"
    ]
    RUN_COMMANDS = ["cd Sublist3r && python3 sublist3r.py -h"]
    PROJECT_URL = "https://gitclone.com/github.com/aboul3la/Sublist3r"


class CheckURL():
    TITLE = "CheckURL"
    DESCRIPTION = "Detect evil urls that uses IDN Homograph Attack.\n\t" \
                  "[!] python3 checkURL.py --url google.com"
    INSTALL_COMMANDS = [
        "sudo git clone https://gitclone.com/github.com/UndeadSec/checkURL.git"]
    RUN_COMMANDS = ["cd checkURL && python3 checkURL.py --help"]
    PROJECT_URL = "https://gitclone.com/github.com/UndeadSec/checkURL"


class Blazy():
    TITLE = "Blazy"
    DESCRIPTION = "Blazy is a modern login page bruteforcer"
    INSTALL_COMMANDS = [
        "sudo git clone https://gitclone.com/github.com/UltimateHackers/Blazy.git",
        "cd Blazy && sudo pip2.7 install -r requirements.txt"
    ]
    RUN_COMMANDS = ["cd Blazy && sudo python2.7 blazy.py"]
    PROJECT_URL = "https://gitclone.com/github.com/UltimateHackers/Blazy"


class SubDomainTakeOver():
    TITLE = "Sub-Domain TakeOver"
    DESCRIPTION = "Sub-domain takeover vulnerability occur when a sub-domain " \
                  "\n (subdomain.example.com) is pointing to a service " \
                  "(e.g: GitHub, AWS/S3,..)\n" \
                  "that has been removed or deleted.\n" \
                  "Usage:python3 takeover.py -d www.domain.com -v"
    INSTALL_COMMANDS = [
        "git clone https://gitclone.com/github.com/m4ll0k/takeover.git",
        "cd takeover;sudo python3 setup.py install"
    ]
    PROJECT_URL = "https://gitclone.com/github.com/m4ll0k/takeover"

    def __init__(self):
        super(SubDomainTakeOver, self).__init__(runnable = False)

class Dirb():
    TITLE = "Dirb"
    DESCRIPTION = "DIRB is a Web Content Scanner. It looks for existing " \
                  "(and/or hidden) Web Objects.\n" \
                  "It basically works by launching a dictionary based " \
                  "attack against \n a web server and analyzing the response."
    INSTALL_COMMANDS = [
        "sudo git clone https://gitlab.com/kalilinux/packages/dirb.git",
        "cd dirb;sudo bash configure;make"
    ]
    PROJECT_URL = "https://gitlab.com/kalilinux/packages/dirb"

    def run(self):
        uinput = input("Enter Url >> ")
        subprocess.run(["sudo", "dirb", uinput])

class WIFIPumpkin():
    TITLE = "WiFi-Pumpkin"
    DESCRIPTION = "The WiFi-Pumpkin is a rogue AP framework to easily create " \
                  "these fake networks\n" \
                  "all while forwarding legitimate traffic to and from the " \
                  "unsuspecting target."
    INSTALL_COMMANDS = [
        "sudo apt install libssl-dev libffi-dev build-essential",
        "sudo git clone https://gitclone.com/github.com/P0cL4bs/wifipumpkin3.git",
        "chmod -R 755 wifipumpkin3",
        "sudo apt install python3-pyqt5",
        "cd wifipumpkin3;sudo python3 setup.py install"
    ]
    RUN_COMMANDS = ["sudo wifipumpkin3"]
    PROJECT_URL = "https://gitclone.com/github.com/P0cL4bs/wifipumpkin3"


class pixiewps():
    TITLE = "pixiewps"
    DESCRIPTION = "Pixiewps is a tool written in C used to bruteforce offline " \
                  "the WPS pin\n " \
                  "exploiting the low or non-existing entropy of some Access " \
                  "Points, the so-called pixie dust attack"
    INSTALL_COMMANDS = [
        "sudo git clone https://gitclone.com/github.com/wiire/pixiewps.git && apt-get -y install build-essential",
        "cd pixiewps*/ && make",
        "cd pixiewps*/ && sudo make install && wget https://pastebin.com/y9Dk1Wjh"
    ]
    PROJECT_URL = "https://gitclone.com/github.com/wiire/pixiewps"

    def run(self):
        os.system(
            'echo "'
            '1.> Put your interface into monitor mode using '
            '\'airmon-ng start {wireless interface}\n'
            '2.> wash -i {monitor-interface like mon0}\'\n'
            '3.> reaver -i {monitor interface} -b {BSSID of router} -c {router channel} -vvv -K 1 -f"'
            '| boxes -d boy')
        print("You Have To Run Manually By USing >>pixiewps -h ")


class BluePot():
    TITLE = "Bluetooth Honeypot GUI Framework"
    DESCRIPTION = "You need to have at least 1 bluetooth receiver " \
                  "(if you have many it will work with those, too).\n" \
                  "You must install/libbluetooth-dev on " \
                  "Ubuntu/bluez-libs-devel on Fedora/bluez-devel on openSUSE"
    INSTALL_COMMANDS = [
        "sudo wget https://raw.gitclone.com/githubusercontent.com/andrewmichaelsmith/bluepot/master/bin/bluepot-0.2.tar.gz"
        "sudo tar xfz bluepot-0.2.tar.gz;sudo rm bluepot-0.2.tar.gz"
    ]
    RUN_COMMANDS = ["cd bluepot && sudo java -jar bluepot.jar"]
    PROJECT_URL = "https://gitclone.com/github.com/andrewmichaelsmith/bluepot"


class Fluxion():
    TITLE = "Fluxion"
    DESCRIPTION = "Fluxion is a remake of linset by vk496 with enhanced functionality."
    INSTALL_COMMANDS = [
        "git clone https://gitclone.com/github.com/FluxionNetwork/fluxion.git",
        "cd fluxion && sudo chmod +x fluxion.sh",
    ]
    RUN_COMMANDS = ["cd fluxion;sudo bash fluxion.sh -i"]
    PROJECT_URL = "https://gitclone.com/github.com/FluxionNetwork/fluxion"


class Wifiphisher():
    TITLE = "Wifiphisher"
    DESCRIPTION = """
        Wifiphisher is a rogue Access Point framework for conducting red team engagements or Wi-Fi security testing. 
        Using Wifiphisher, penetration testers can easily achieve a man-in-the-middle position against wireless clients by performing 
        targeted Wi-Fi association attacks. Wifiphisher can be further used to mount victim-customized web phishing attacks against the
        connected clients in order to capture credentials (e.g. from third party login pages or WPA/WPA2 Pre-Shared Keys) or infect the 
        victim stations with malware..\n
        For More Details Visit >> https://gitclone.com/github.com/wifiphisher/wifiphisher
    """
    INSTALL_COMMANDS = [
        "git clone https://gitclone.com/github.com/wifiphisher/wifiphisher.git",
        "cd wifiphisher;sudo python3 setup.py install"
    ]
    RUN_COMMANDS = ["cd wifiphisher;sudo wifiphisher"]
    PROJECT_URL = "https://gitclone.com/github.com/wifiphisher/wifiphisher"


class Wifite():
    TITLE = "Wifite"
    DESCRIPTION = "Wifite is an automated wireless attack tool"
    INSTALL_COMMANDS = [
        "sudo git clone https://gitclone.com/github.com/derv82/wifite2.git",
        "cd wifite2 && sudo python3 setup.py install"
    ]
    RUN_COMMANDS = ["cd wifite2; sudo wifite"]
    PROJECT_URL = "https://gitclone.com/github.com/derv82/wifite2"


class EvilTwin():
    TITLE = "EvilTwin"
    DESCRIPTION = "Fakeap is a script to perform Evil Twin Attack, by getting" \
                  " credentials using a Fake page and Fake Access Point"
    INSTALL_COMMANDS = ["sudo git clone https://gitclone.com/github.com/Z4nzu/fakeap.git"]
    RUN_COMMANDS = ["cd fakeap && sudo bash fakeap.sh"]
    PROJECT_URL = "https://gitclone.com/github.com/Z4nzu/fakeap"


class Fastssh():
    TITLE = "Fastssh"
    DESCRIPTION = "Fastssh is an Shell Script to perform multi-threaded scan" \
                  " \n and brute force attack against SSH protocol using the " \
                  "most commonly credentials."
    INSTALL_COMMANDS = [
        "sudo git clone https://gitclone.com/github.com/Z4nzu/fastssh.git && cd fastssh && sudo chmod +x fastssh.sh",
        "sudo apt-get install -y sshpass netcat"
    ]
    RUN_COMMANDS = ["cd fastssh && sudo bash fastssh.sh --scan"]
    PROJECT_URL = "https://gitclone.com/github.com/Z4nzu/fastssh"


class Howmanypeople():
    TITLE = "Howmanypeople"
    DESCRIPTION = "Count the number of people around you by monitoring wifi " \
                  "signals.\n" \
                  "[@] WIFI ADAPTER REQUIRED* \n[*]" \
                  "It may be illegal to monitor networks for MAC addresses, \n" \
                  "especially on networks that you do not own. " \
                  "Please check your country's laws"
    INSTALL_COMMANDS = [
        "sudo apt-get install tshark"
        ";sudo python3 -m pip install howmanypeoplearearound"
    ]
    RUN_COMMANDS = ["howmanypeoplearearound"]



class Cupp():
    TITLE = "Cupp"
    DESCRIPTION = "WlCreator is a C program that can create all possibilities of passwords,\n " \
                  "and you can choose Length, Lowercase, Capital, Numbers and Special Chars"
    INSTALL_COMMANDS = ["git clone https://gitclone.com/github.com/Mebus/cupp.git"]
    RUN_COMMANDS = ["cd cupp && python3 cupp.py -i"]
    PROJECT_URL = "https://gitclone.com/github.com/Mebus/cupp"


class WlCreator():
    TITLE = "WordlistCreator"
    DESCRIPTION = "WlCreator is a C program that can create all possibilities" \
                  " of passwords,\n and you can choose Length, Lowercase, " \
                  "Capital, Numbers and Special Chars"
    INSTALL_COMMANDS = ["sudo git clone https://gitclone.com/github.com/Z4nzu/wlcreator.git"]
    RUN_COMMANDS = [
        "cd wlcreator && sudo gcc -o wlcreator wlcreator.c && ./wlcreator 5"]
    PROJECT_URL = "https://gitclone.com/github.com/Z4nzu/wlcreator"


class GoblinWordGenerator():
    TITLE = "Goblin WordGenerator"
    DESCRIPTION = "Goblin WordGenerator"
    INSTALL_COMMANDS = [
        "sudo git clone https://gitclone.com/github.com/UndeadSec/GoblinWordGenerator.git"]
    RUN_COMMANDS = ["cd GoblinWordGenerator && python3 goblin.py"]
    PROJECT_URL = "https://gitclone.com/github.com/UndeadSec/GoblinWordGenerator.git"


class showme():
    TITLE = "showme"
    DESCRIPTION = "This tool allows you to perform OSINT and reconnaissance on " \
                  "an organisation or an individual. It allows one to search " \
                  "1.4 Billion clear text credentials which was dumped as " \
                  "part of BreachCompilation leak. This database makes " \
                  "finding passwords faster and easier than ever before."
    INSTALL_COMMANDS = [
        "sudo git clone https://gitclone.com/github.com/Viralmaniar/SMWYG-Show-Me-What-You-Got.git",
        "cd SMWYG-Show-Me-What-You-Got && pip3 install -r requirements.txt"
    ]
    RUN_COMMANDS = ["cd SMWYG-Show-Me-What-You-Got && python SMWYG.py"]
    PROJECT_URL = "https://gitclone.com/github.com/Viralmaniar/SMWYG-Show-Me-What-You-Got"


class Dalfox():
    TITLE = "DalFox"
    DESCRIPTION = "XSS Scanning and Parameter Analysis tool."
    INSTALL_COMMANDS = [
        "sudo apt-get install golang",
        "sudo git clone https://gitclone.com/github.com/hahwul/dalfox",
        "cd dalfox;go install"
    ]
    RUN_COMMANDS = [
        "~/go/bin/dalfox",
        'echo "You Need To Run manually by using [!]~/go/bin/dalfox [options]"'
    ]
    PROJECT_URL = "https://gitclone.com/github.com/hahwul/dalfox"


class XSSPayloadGenerator():
    TITLE = "XSS Payload Generator"
    DESCRIPTION = "XSS PAYLOAD GENERATOR -XSS SCANNER-XSS DORK FINDER"
    INSTALL_COMMANDS = [
        "git clone https://gitclone.com/github.com/capture0x/XSS-LOADER.git",
        "cd XSS-LOADER;sudo pip3 install -r requirements.txt"
    ]
    RUN_COMMANDS = ["cd XSS-LOADER;sudo python3 payloader.py"]
    PROJECT_URL = "https://gitclone.com/github.com/capture0x/XSS-LOADER.git"


class XSSFinder():
    TITLE = "Extended XSS Searcher and Finder"
    DESCRIPTION = "Extended XSS Searcher and Finder"
    INSTALL_COMMANDS = [
        "git clone https://gitclone.com/github.com/Damian89/extended-xss-search.git"]
    PROJECT_URL = "https://gitclone.com/github.com/Damian89/extended-xss-search"

    def after_install(self):
        print("""\033[96m 
        Follow This Steps After Installation:-
            \033[31m [*] Go To extended-xss-search directory,
                and Rename the example.app-settings.conf to app-settings.conf
        """)
        input("Press ENTER to continue")

    def run(self):
        print("""\033[96m 
        You have To Add Links to scan
        \033[31m[!] Go to extended-xss-search
            [*] config/urls-to-test.txt
            [!] python3 extended-xss-search.py
        """)


class XSSFreak():
    TITLE = "XSS-Freak"
    DESCRIPTION = "XSS-Freak is an XSS scanner fully written in python3 from scratch"
    INSTALL_COMMANDS = [
        "git clone https://gitclone.com/github.com/PR0PH3CY33/XSS-Freak.git",
        "cd XSS-Freak;sudo pip3 install -r requirements.txt"
    ]
    RUN_COMMANDS = ["cd XSS-Freak;sudo python3 XSS-Freak.py"]
    PROJECT_URL = "https://gitclone.com/github.com/PR0PH3CY33/XSS-Freak"


class XSpear():
    TITLE = "XSpear"
    DESCRIPTION = "XSpear is XSS Scanner on ruby gems"
    INSTALL_COMMANDS = ["gem install XSpear"]
    RUN_COMMANDS = ["XSpear -h"]
    PROJECT_URL = "https://gitclone.com/github.com/hahwul/XSpear"


class XSSCon():
    TITLE = "XSSCon"
    INSTALL_COMMANDS = [
        "git clone https://gitclone.com/github.com/menkrep1337/XSSCon.git",
        "sudo chmod 755 -R XSSCon"
    ]
    PROJECT_URL = "https://gitclone.com/github.com/menkrep1337/XSSCon"

    def run(self):
        website = input("Enter Website >> ")
        os.system("cd XSSCon;")
        subprocess.run(["python3", "xsscon.py", "-u", website])


class XanXSS():
    TITLE = "XanXSS"
    DESCRIPTION = "XanXSS is a reflected XSS searching tool\n " \
                  "that creates payloads based from templates"
    INSTALL_COMMANDS = ["git clone https://gitclone.com/github.com/Ekultek/XanXSS.git"]
    PROJECT_URL = "https://gitclone.com/github.com/Ekultek/XanXSS"

    def run(self):
        os.system("cd XanXSS ;python xanxss.py -h")
        print("\033[96m You Have to run it manually By Using\n"
              " [!]python xanxss.py [Options]")


class XSSStrike():
    TITLE = "Advanced XSS Detection Suite"
    DESCRIPTION = "XSStrike is a python script designed to detect and exploit XSS vulnerabilities."
    INSTALL_COMMANDS = [
        "sudo rm -rf XSStrike",
        "git clone https://gitclone.com/github.com/UltimateHackers/XSStrike.git "
        "&& cd XSStrike && pip install -r requirements.txt"
    ]
    PROJECT_URL = "https://gitclone.com/github.com/UltimateHackers/XSStrike"

    def __init__(self):
        super(XSSStrike, self).__init__(runnable = False)


class RVuln():
    TITLE = "RVuln"
    DESCRIPTION = "RVuln is multi-threaded and Automated Web Vulnerability " \
                  "Scanner written in Rust"
    INSTALL_COMMANDS = [
        "sudo git clone https://gitclone.com/github.com/iinc0gnit0/RVuln.git;"
        "curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh;"
        "source $HOME/.cargo/env;"
        "sudo apt install librust-openssl-dev;"
        "cd RVuln;sudo su;cargo build --release;mv target/release/RVuln"
    ]
    RUN_COMMANDS = ["RVuln"]
    PROJECT_URL = "https://gitclone.com/github.com/iinc0gnit0/RVuln"

