from nornir import InitNornir
from nornir.plugins.tasks.networking import netmiko_file_transfer


def file_copy(task):
    # Obtain the group_name
    group_name = task.host.groups[0]

    # Set the filename based on the platform (ios, eos, et cetera)
    source_file = "test_file.txt"
    dest_file = f"{group_name}/test_new.txt"

    # Transfer the file
    results = task.run(
        netmiko_file_transfer,
        source_file=source_file,
        dest_file=dest_file,
        direction="get",
    )

    print()
    print("-" * 40)
    print(task.host)
    print(source_file)
    print()
    if results[0].changed is False:
        print("File not transferred: correct file is already on the device")
    else:
        print("File downloaded")

    if results[0].result is True:
        print("Retrieved file exists and is correct")
    print("-" * 40)
    print()


if __name__ == "__main__":

    nr = InitNornir(config_file="config.yaml")
    nr = nr.filter(name="arista1")
    results = nr.run(task=file_copy, num_workers=10)
