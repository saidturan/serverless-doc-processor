data "aws_caller_identity" "current" {}

resource "aws_s3_bucket" "input_bucket" {
  bucket = "${var.project_name}-input-${data.aws_caller_identity.current.account_id}"
}

resource "aws_s3_bucket" "output_bucket" {
  bucket = "${var.project_name}-output-${data.aws_caller_identity.current.account_id}"
}
