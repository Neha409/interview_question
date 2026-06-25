resource "azurerm_kubernetes_cluster" "aks" {
  name                = "demo-aks"
  location            = var.location
  resource_group_name = var.resource_group_name
  dns_prefix          = "demoaks"

  kubernetes_version = "1.33"

  default_node_pool {
    name           = "system"
    node_count     = 2
    vm_size        = "Standard_DS2_v2"
    vnet_subnet_id = var.subnet_id
  }

  identity {
    type = "SystemAssigned"
  }

  network_profile {
    network_plugin = "azure"
    network_policy = "azure"
  }

  tags = {
    Environment = "Dev"
    ManagedBy   = "Terraform"
  }
}