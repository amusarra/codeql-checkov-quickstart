resource "aws_s3_bucket" "vulnerable_bucket" {
  bucket = "vulnerable-bucket-example-name" # Sostituisci con un nome bucket univoco
  acl    = "public-read" # ACL pubblico RIMOSSO, bucket privato di default (corretto)
  versioning { # Versioning non abilitato (vulnerabilità potenziale, a seconda dei requisiti)
     enabled = false
  }
}
