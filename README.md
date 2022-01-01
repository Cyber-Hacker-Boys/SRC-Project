# IP Forger
## Forge your own packets

![IPForger](https://i.ibb.co/ZS3ZW7V/Captura-de-ecra-2022-01-01-a-s-10-04-31-removebg-preview.png)

[![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/Naereen/StrapDown.js/blob/master/LICENSE) [![GitHub version](https://d25lcipzij17d.cloudfront.net/badge.svg?id=gh&type=6&v=1.0&x2=0)](https://github.com/Naereen/StrapDown.js)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white) ![Python](https://img.shields.io/badge/scapy-green?style=for-the-badge&logo=python&logoColor=blue)

This the repository of our Network Security project for our Master Degree in Insecurity and Forensics.

###Goal
IP forger is an web app made in python with the Django Framework, the goal of the app is to send customized network packets and
scanning the network for active IP'S. The goal of the app is to be used on a local network and launched by the localhost.

### What we will offer

- Sending Packets in a GUI Like Form
- Realizing ICMP Scans
- Offering an educational form of learning how packets work

### Technology

The app is done using:

| Technology | Version      |
|------------|--------------|
| Python     | 3.9          |
| Django     | 3.2          |
|  Scapy     | 2.4          |

### Requirements

- [Python 3.9]
- [Pip]

### Installation

To download the project use the download on github or use the command line

```
$ git clone https://github.com/Cyber-Hacker-Boys/SRC-Project.git
$ cd SRC-Project
```

To install the dependencies do the following command inside the project foldeer

```
$ pip3 install -r requirements.txt
```

And to finally run the program do the following commands:

```
$ cd IPForger
$ python manage.py runserver  
```

The project should the open in your localhost.

### License

This code is open source and was based around documentation another references so the license is MIT.
See the license file for more information.

[Python 3.9]: <https://www.python.org/>
[Pip]: <https://pypi.org/project/pip/>
