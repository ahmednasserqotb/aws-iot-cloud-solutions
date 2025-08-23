#!/usr/bin/env python3
import boto3

def main():
    s3 = boto3.client("s3")
    resp = s3.list_buckets()
    for b in resp.get("Buckets", []):
        print(b["Name"])

if __name__ == "__main__":
    main()
