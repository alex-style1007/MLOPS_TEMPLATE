# IP pública de la instancia EC2 creada
output "instance_public_ip" {
  description = "La dirección IP pública de la instancia EC2"
  value       = aws_instance.web.public_ip
}

# ID del grupo de seguridad creado
output "security_group_id" {
  description = "ID del grupo de seguridad de la instancia web"
  value       = aws_security_group.web_sg.id
}
