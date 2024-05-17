![project_logo](/docs/assets/pydeserialize.png)

<p align="center">
	<a href="https://www.python.org/"><img src="https://img.shields.io/badge/made%20with-python-red"></a>
	<a href="#"><img src="https://img.shields.io/badge/platform-osx%2Flinux%2Fwindows-blueviolet"></a>
	<a href="https://github.com/joaoviictorti/pydeserialize/releases"><img src="https://img.shields.io/github/release/joaoviictorti/pydeserialize?color=blue"></a>
</p>

<h4 align="center">pydeserialize test for insecure python deserialization vulnerabilities</h4>


<p align="center">
  <a href="#features">Features</a> •
  <a href="#installation">Installation</a> •
  <a href="#how-to-use"> How to use</a> •
  <a href="#details">Details</a> •
  <a href="#running-pydeserialize">Running pydeserialize</a>  
</p>

---


pydeserialize is a tool that generates insecure deserialization payloads in Python. It has a feature that encodes the desired payloads, making it simple and optimized for speed.

I designed `pydeserialize` to fulfill all the responsibilities for generating payloads and encodes, keeping a consistently passive model to make it useful for penetration testers.

# Features

 - Generates payloads to exploit insecure deserialization vulnerabilities in python  

# How to use

```sh
pydeserialize -ip 192.168.4.113 -p 80 -e shell -o Windows
pydeserialize -ip 192.168.4.113 -e b64 -p 80 -o Linux
```

# Details

![project_logo](/docs/assets/help.png)

# Installation

pydeserialize requires **python3** and to download it just use:

```sh
pip3 install pydeserialize
```

# Running pydeserialize

![project_logo](/docs/assets/exec.png)

<img width=100% src="https://capsule-render.vercel.app/api?type=waving&color=0000FF&height=120&section=footer"/>
