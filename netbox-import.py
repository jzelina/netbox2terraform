#!/usr/bin/python3

# Sample Implementation to import VMs from Netbox into Terraform
# v.02

import pynetbox
from jinja2 import Environment, FileSystemLoader

nb = pynetbox.api(
    'http://localhost:8000',
    token='xxx'
)

devices = nb.virtualization.virtual_machines.all()
out = ""

# load netbox template (for VMs)
file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)
env.trim_blocks = True
env.lstrip_blocks = True
template = env.get_template('netbox_vm.tpl')

def create_vm(device):
    out = template.render(device=device)
    return out

print('Generate VM List from Netbox.')
for device in devices:
    if device.status.label == 'Active':
        print("add name: {}, ID: {}, State: {}, Cluster: {}, CPUs: {}".
        format(device.name, device.id, device.status.label, device.cluster.name ,device.vcpus))
        out = out + create_vm(device)
    else:
        print("skip name: {}, ID: {}, State: {}, Cluster: {}, CPUs: {}".
        format(device.name, device.id, device.status.label, device.cluster.name ,device.vcpus))

# print(out)
outF = open("netbox.tf", "w")
outF.writelines(out)
outF.close()

print('Update complete, run Terraform')
