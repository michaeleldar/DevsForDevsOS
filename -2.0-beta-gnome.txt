from os import system as run


run("pacman -Syu --noconfirm")
run(f"pacman -S xorg --noconfirm")
run(f"pacman -S gdm --noconfirm")
run(f"pacman -S gnome --noconfirm")
run("systemctl enable gdm.service")

run("pacman -Rs epiphany --noconfirm")
run("pacman -S firefox --noconfirm")

run("systemctl start gdm.service")
