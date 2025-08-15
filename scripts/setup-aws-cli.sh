#!/usr/bin/env bash
set -e
aws --version || { echo "Install AWS CLI first"; exit 1; }
echo "Run: aws configure"
