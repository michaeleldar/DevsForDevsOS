from os import system as run


run("pacman -Syu --noconfirm")
run(f"pacman -S xorg --noconfirm")
run(f"pacman -S sddm --noconfirm")
run(f"pacman -S cutefish --noconfirm")
run("systemctl enable sddm")

run("pacman -S firefox --noconfirm")

run("systemctl start sddm")
