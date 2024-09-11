# Read the JSON file
locals {
  ssm_parameters = jsondecode(file("${path.module}/ssm_parameters.json"))
}

# Output the parameters
output "ssm_parameters" {
  value = local.ssm_parameters
}

# Create or update SSM parameters
resource "aws_ssm_parameter" "secure_parameters" {
  for_each = { for p in local.ssm_parameters : p.Name => p }

  name  = each.value.Name
  type  = "SecureString"
  value = each.value.Value
}
