from os import system as run


def install(package):
    run(f"pacman {package}")


run("pacman -Syu")
install("-s xorg")
install("-s gdm")
install("-s cutefish")
run("systemctl enable gdm.service")
run("systemctl start gdm.service")
