output "input_bucket_name" {
  value = aws_s3_bucket.input_bucket.id
}

output "lambda_function_name" {
  value = aws_lambda_function.processor.function_name
}
