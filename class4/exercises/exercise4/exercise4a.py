from nornir import InitNornir
from nornir.core.filter import F
from nornir.plugins.functions.text import print_result
from nornir.plugins.tasks import networking


def configure_vlan(task, vlan_id, vlan_name):
    config_string = f"""vlan {vlan_id}
  name {vlan_name}"""
    task.run(task=networking.napalm_configure, configuration=config_string)


def main():
    nr = InitNornir(config_file="config.yaml")
    nr = nr.filter(F(groups__contains="eos") | F(groups__contains="nxos"))
    result = nr.run(task=configure_vlan, vlan_id="123", vlan_name="ntp_vlan")
    print_result(result)


if __name__ == "__main__":
    main()
