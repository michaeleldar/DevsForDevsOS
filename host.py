from os import system as run  # To make it quicker to type.


def error(step, reason, fatal):
    print()
    print("------------------------------------------")
    print(f"Error during {step}!")
    print(reason)

    if fatal:
        print("Fatal, now quiting.")
    print("------------------------------------------")
    print()


easy_install_answered_correctly = False
while easy_install_answered_correctly == False:
    easy_install = input("Do you want advanced configuration or not (y/n)? ")
    if easy_install == "y":
        easy_install = True
        easy_install_answered_correctly = True
    elif easy_install == "n":
        easy_install = True
        easy_install_answered_correctly = True
    else:
        print("Sorry, we couldn't understand that, please enter y or n.")

boot_partition = input("Please enter your root partition path, e.g /dev/sdb1. ")
root_partition = input("Please enter your root partition path, e.g /dev/sdb2. ")


def install_depends():
    run("apt install binutils")  # To install "ar"


def format():
    run(f"mke2fs -j {root_partition}")
    run("mkdir /mnt/debinst")
    run(f"mount {root_partition} /mnt/debinst")
    run("mkdir work")
    run(
        "cd $HOME/work && wget ftp.debian.org/debian/pool/main/d/debootstrap/debootstrap_1.0.128_all.deb"
    )
    run("cd $HOME/work && ar -x debootstrap_1.0.128_all.deb")
    run("cd /")
    run("zcat $HOME/work/data.tar.gz | tar xv")
    run(
        "/usr/sbin/debootstrap --arch amd64 bullseye /mnt/debinst http://ftp.us.debian.org/debian"
    )
