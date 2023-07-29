<img width=100% src="https://capsule-render.vercel.app/api?type=waving&color=0000FF&height=120&section=header"/>

![logo_do_projeto](/docs/assets/pydeserialize.png)

<p align="center">
	<a href="https://www.python.org/"><img src="https://img.shields.io/badge/made%20with-python-red"></a>
	<a href="#"><img src="https://img.shields.io/badge/platform-osx%2Flinux%2Fwindows-blueviolet"></a>
	<a href="https://github.com/joaoviictorti/pydeserialize/releases"><img src="https://img.shields.io/github/release/joaoviictorti/pydeserialize?color=blue"></a>
</p>

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

![logo_do_projeto](/docs/assets/help.png)

# Instalação

pydeserialize requer **python3** e para baixá-lo só usar:

```sh
pip3 install pydeserialize
```

# Executando pydeserialize

![logo_do_projeto](/docs/assets/exec.png)

<img width=100% src="https://capsule-render.vercel.app/api?type=waving&color=0000FF&height=120&section=footer"/>