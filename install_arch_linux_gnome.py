from os import system as run


run("pacman -Syu --noconfirm")
run(f"pacman -S xorg --noconfirm")
run(f"pacman -S gdm --noconfirm")
run(f"pacman -S gnome --noconfirm")
run("systemctl enable gdm.service")

run("pacman -Rs epiphany --noconfirm")
run("pacman -S firefox --noconfirm")

"""
easy_install_answered_correctly = False
while easy_install_answered_correctly == False:
    easy_install = input(
        "Do you want to use the stable (recommended), beta or commitly update channel? "
    )
    if easy_install == "stable" or easy_install == "beta" or easy_install == "commitly":
        easy_install_answered_correctly = True
    else:
        print("Please enter stable, nightly or commitly.")

install_config = open("/etc/devsfordevsupdates.config")
install_config.write()
"""

run("systemctl start gdm.service")
