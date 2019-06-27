from nornir import InitNornir
from nornir.core.filter import F
from nornir.plugins.tasks.networking import napalm_get


def main():
    nr = InitNornir(config_file="config.yaml")
    ios_filt = F(groups__contains="ios")
    eos_filt = F(groups__contains="eos")
    nr = nr.filter(ios_filt | eos_filt)

    my_results = nr.run(task=napalm_get, getters=["arp_table"])
    parsed_results = []
    for host, multiresult in my_results.items():
        output = multiresult[0].result["arp_table"]
        desired_data = ""
        for entry in output:
            if entry["ip"] == "10.220.88.1":
                desired_data = entry
                break
        parsed_results.append((host, desired_data))

    print()
    for host, gw_data in parsed_results:
        print(f"Host: {host}, Gateway: {gw_data}")
    print()


if __name__ == "__main__":
    main()
