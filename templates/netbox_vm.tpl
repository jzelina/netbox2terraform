
module "instance_netbox_{{ device.name }}" {
 source = "../tf-module/lxc"
 hostname  = "{{ device.name }}"
 {% if device.memory %} memory  = "{{ device.memory }}" {% endif +%}
 {% if device.disk %} disksize  = "{{ device.disk }}G" {% endif +%}
 {% if 'ubuntu-linux-21-10' in device.platform.slug %} ostemplate  = "local:vztmpl/ubuntu-21.10-standard_21.10-1_amd64.tar.zst"{% endif %}
 {% if 'ubuntu-linux-20-04' in device.platform.slug %} ostemplate  = "local:vztmpl/ubuntu-20.04-standard_20.04-1_amd64.tar.gz"{% endif %}

}
