resource "aws_ecs_service" "my_service" {
  name            = "my-ecs-service"
  cluster         = aws_ecs_cluster.my_cluster.id
  task_definition = aws_ecs_task_definition.my_task.family
  desired_count   = 1
  launch_type     = "FARGATE"
  
  network_configuration {
    subnets          = ["subnet-12345678", "subnet-87654321"]
    assign_public_ip = true
  }
  
  load_balancer {
    target_group_arn = aws_lb_target_group.my_target_group.arn
    container_name   = "my-container"
    container_port   = 80
  }

  deployment_minimum_healthy_percent = 50
  deployment_maximum_percent         = 200
  force_new_deployment               = true  # This ensures the service uses the latest task definition
}
