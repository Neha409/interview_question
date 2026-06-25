terraform {
  required_version = ">= 1.5.0"

  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 4.0"
    }
  }
}

provider "azurerm" {
  features {}
}


module "resource_group_name" {
  source = "./terraform_module/resource_creation"
  location = "East US"
}

module "network" {
  source = "./terraform_module/network"
  location = module.resource_group_name.location
  resource_group_name = module.resource_group_name.resource_group_name
}

module "aks_cluster" {
  source = "./terraform_module/terraform_aks_cluster"
  location = module.resource_group_name.location
  resource_group_name = module.resource_group_name.resource_group_name
  subnet_id = module.network.subnet_id
}

