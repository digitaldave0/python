# Define a local variable to read the JSON file
locals {
  ssm_parameters = jsondecode(file("${path.module}/ssm_parameters.json"))
}

# Output the parameters to verify
output "ssm_parameters" {
  value = local.ssm_parameters
}