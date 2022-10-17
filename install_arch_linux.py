from os import system as run


run("pacman -Syu")
run(f"pacman -S xorg")
run(f"pacman -S gdm")
run(f"pacman -S cutefish")
run("systemctl enable gdm.service")
run("systemctl start gdm.service")
