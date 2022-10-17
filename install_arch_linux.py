from os import system as run


run("pacman -Syu")
run(f"pacman xorg")
run(f"pacman gdm")
run(f"pacman cutefish")
run("systemctl enable gdm.service")
run("systemctl start gdm.service")
