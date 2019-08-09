#!/usr/bin/env python3

from nornir import InitNornir

def my_task(task):
    print("Hello ")
    host = task.host
    print(host.hostname)
    #printing vaue from data of the host. Nornir select host -> group1 -> group2 -> defaults
    print(host["dns1"])
    print(host["dns2"])


if __name__ == "__main__":
    nr = InitNornir()

    print(nr.inventory)
    print(nr.inventory.hosts)

    print(nr.inventory.hosts["localhost"])
    print(nr.inventory.hosts["localhost"].hostname)


    for host_name, host_obj in nr.inventory.hosts.items():
        print(host_name)
        print(f"Host: {host_name}")
        print(f"Groups: {host_obj.groups}")
        print(f"Groups: {host_obj.platform}")
        print(f"Groups: {host_obj.username}")
        print(f"Groups: {host_obj.password}")

nr.run(task=my_task)

