# La región donde desplegar los recursos
variable "aws_region" {
  description = "La región donde se desplegarán los recursos de AWS"
  default     = "us-east-1"
}

# El ID de la AMI (Amazon Machine Image) que usaremos para la instancia EC2
variable "ami_id" {
  description = "ID de la AMI para lanzar la instancia EC2"
  default     = "ami-0c55b159cbfafe1f0"  # Ejemplo de una AMI de Ubuntu en us-east-1
}

# Tipo de instancia
variable "instance_type" {
  description = "Tipo de instancia de EC2"
  default     = "t2.micro"
}

# Clave SSH para acceder a la instancia
variable "key_name" {
  description = "Nombre del par de claves SSH"
  default     = "my-key"  # Esto puede cambiar según tus claves SSH
}
