provider "aws" {
  region     = "us-west-2"

}

resource "aws_instance" "myec2" {
   ami = "ami-0518bb0e75d3619ca"
   instance_type = "t2.micro"
}
