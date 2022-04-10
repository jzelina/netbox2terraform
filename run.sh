#!/bin/bash
python3 netbox-import.py
terraform init
terraform apply
