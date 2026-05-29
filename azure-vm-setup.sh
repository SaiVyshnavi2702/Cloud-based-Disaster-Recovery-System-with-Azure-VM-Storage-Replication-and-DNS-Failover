# Create Production VM
az vm create \
--resource-group DNS-project-rg \
--name DNSProd-vm \
--location eastus \
--public-ip-sku Standard \
--image UbuntuLTS \
--admin-username azureuser \
--generate-ssh-keys \
--custom-data cloud-init-github.txt

# Create Backup VM
az vm create \
--resource-group DNS-project-rg \
--name DNSCnr-vm \
--location eastus \
--public-ip-sku Standard \
--image UbuntuLTS \
--admin-username azureuser \
--generate-ssh-keys \
--custom-data cloud-init-github.txt

# Open port 80
az vm open-port \
--port 80 \
--resource-group DNS-project-rg \
--name DNSProd-vm