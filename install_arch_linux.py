from os import system as run


run("pacman -Syu --noconfirm")
run(f"pacman -S xorg --noconfirm")
run(f"pacman -S gdm --noconfirm")
run(f"pacman -S cutefish --noconfirm")
run("systemctl enable gdm.service")
run("systemctl start gdm.service")
