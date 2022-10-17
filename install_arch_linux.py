from os import system as run


def install(package):
    run(f"pacman -s {package}")


run("pacman -Syu")
run("pacman -S xorg")
install("xorg")
install("gdm")
install("cutefish")
run("systemctl enable gdm.service")
