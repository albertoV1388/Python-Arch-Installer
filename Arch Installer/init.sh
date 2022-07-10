#!/bin/bash
# Script para apredizaje e instalación de Arch Linux
echo Easy Python Arch Linux Installer
sleep 5
echo Instalando Python...
pacman -S python python-pip
echo Instalando Dependencias...
curl -O https://bootstrap.pypa.io/get-pip.py
python get-pip.py
pip install pyfiglet
pip install os
pip install requests
pip install time
