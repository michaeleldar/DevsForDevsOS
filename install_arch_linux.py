from os import system as run


run("pacman -Syu")
run(f"pacman -s xorg")
run(f"pacman -s gdm")
run(f"pacman -s cutefish")
run("systemctl enable gdm.service")
run("systemctl start gdm.service")
