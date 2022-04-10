# netbox2terraform

This script will allow to manage VMs using Netbox as UI.

Workflow:
1. Manage VMs in Netbox
2. This script will import active VMs from Netbox and create a terraform file.
3. Terraform will ensure the the state enforced on the hypervisor.

This is just a demo, this script must be adapted before using.

The output of this script must be adapted using the template to your Terraform
provider or module format.

## usage

```
python3 netbox-import.py
terraform init
terraform apply
```

sample output:
```
Generate VM List from Netbox.
add name: dts-lb, ID: 4, State: Active, Cluster: PRX, CPUs: 2.0
add name: dts-vm-01, ID: 1, State: Active, Cluster: PRX, CPUs: 2.0
add name: dts-vm-02, ID: 2, State: Active, Cluster: PRX, CPUs: None
skip name: dts-vm-03, ID: 3, State: Planned, Cluster: PRX, CPUs: None
Update complete, run Terraform
Initializing modules...

Initializing the backend...

Initializing provider plugins...
...
```

## requirements

- Netbox
- Terraform
- Python (incl. pynetbox, jinja2)
