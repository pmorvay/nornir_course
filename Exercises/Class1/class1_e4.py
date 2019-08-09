#!/usr/bin/env python3

from nornir import InitNornir

def my_task(task):
    print("Hello ")
    print(task.host.hostname)

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

