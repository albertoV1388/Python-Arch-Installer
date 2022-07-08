from time import time
import pyfiglet #Framework para hacer artes ASCII
import os # Framework para ejecutar comandos en terminal
import requests # Framework para comprobar conexión a internet
import time
title = pyfiglet.figlet_format("Arch Linux Installer")
end = pyfiglet.figlet_format("Saliendo...")
conexion = pyfiglet.figlet_format("Conectando")
discos = pyfiglet.figlet_format("Particionado de discos")
part = pyfiglet.figlet_format("Particionando...")
mont = pyfiglet.figlet_format("Montaje de particiones")
instalacion = pyfiglet.figlet_format("Instalando")
fin = pyfiglet.figlet_format("Instalacion termiada")
print(title)
print("By Alberto Valenciano")
print("Esta usted de acuerdo con la licencia GPL(y/n)")
gpl = input("")
print(gpl)
if gpl == "y":
    print("Bienvenido a la instalación de Arch Linux")
else:{
    print(end)
}
print("Verificando integridad de tu medio de instalación")
os.system("gpg --keyserver-options auto-key-retrieve --verify archlinux-version-x86_64.iso.sig")
test = input("Hay errores de integridad?(y/n)")
print(test)
if test == "n":
    print("Es probable que tu medio de instalación este dañado o sea malicioso, vuelva a descargar la iso de nuevo desde la web del proyecto ArchLinux ")
    print(end)
else:
    if test == "y":{
        print("Continuando con la instalación")
    }
keydist = input("Introduzca su codigo de distribución de teclado ") # Introducción de distribución de teclado
os.system("loadkeys " + keydist)
print("Procedamos a comprobar su metodo de arranque")
os.system("ls /sys/firmware/efi/efivars") # Comprobación del directorio EFI
print("Se ha mostrado el directorio? (y/n)")
directorioefi = input("")
if directorioefi == "y":
    print("Su metodo de arranque es UEFI, deberá realizar posteriormente particiones GPT")
    uefi = 1
    time.sleep(5)
else:
    if directorioefi == "n":
        print("Su metodo de aranque es BIOS deberá usar el esquema de particionas MBR")
        uefi = 0
        time.sleep(5)
print("Realizando prueba de conexión a internet")
print(conexion)
os.system("ip link")
print("Realizando ping a archlinux.org")
try:
    request = requests.get("http://www.archlinux.org", timeout=5)
except (requests.ConnectionError, requests.Timeout):
    print("Sin conexión a internet.")
else:
    print("Con conexión a internet.")
print("Sincronizando Calendario")
os.system("timedatectl set-ntp true")
os.system("cal")
print("Calendario sincronizado")
print(discos)
os.system("sudo fdisk -l")
ruta = input("Introduzca la ruta de su disco, esta listada arriba")
print(part)
os.system("mkfs.ext4 " + ruta)
os.system("mkswap " + ruta)
os.system("mkfs.fat -F 32 " + ruta)
print(mont)
dpart = input("Introduzca la ruta de la partición root")
dpartb = input("Introduzca la ruta de la partición boot")
dparts = input("Introduzca la ruta de la partición swap")
print(dpart)
if uefi == 0:
    os.system("mount " + dpart + " /mnt")
else:
    if uefi == 1:
        os.system("mount --mkdir" + dpart + " /mnt/boot")
os.system("swapon " + dparts)
time.sleep(5)
print(instalacion)
time.sleep(5)
print("Instalando Kernel")
time.sleep(5)
os.system("pacstrap /mnt base linux linux-firmware")
print("Creando Fstab")
time.sleep(5)
os.system("genfstab -U /mnt >> /mnt/etc/fstab")
time.sleep(5)
os.system("arch-chroot /mnt")
time.sleep(5)
os.system("hwclock --systohc")
print("Descomenta en_US.UTF-8 UTF-8")
os.system("locale-gen")
time.sleep(5)
print("Configure la distribución de teclado")
time.sleep(5)
os.system("nano /etc/vconsole.conf")
os.system("touch /etc/hostname")
os.system("mkinitcpio -P")
os.system("passwd")
print(fin)
time.sleep(5)
print("Sal del chroot usando exit y reinicia con reboot")
print("Este script esta en fase experimental, es probable que tenga fallos")
time.sleep(10)