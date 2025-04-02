#!/bin/bash

echo "🔍 Starting secret scan..."
echo "=========================================="

# Run TruffleHog and capture its output
output=$(trufflehog .)
result=$?

# Show the output
echo "$output"

# Exit with code 1 if secrets were found
if [ $result -eq 0 ]; then
    echo "✅ No secrets found"
else
    echo "❌ Secrets found!"
    exit 1
fi

echo "==========================================" 