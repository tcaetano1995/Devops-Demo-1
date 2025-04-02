#!/bin/bash

echo "🔍 Starting secret scan..."
echo "=========================================="

# Run detect-secrets and capture its output
output=$(detect-secrets scan)

# Check if results are empty using jq
if echo "$output" | jq -e '.results | length > 0' > /dev/null; then
    echo "❌ Secrets found in the following locations:"
    echo "-------------------------------------------"
    echo "$output" | jq -r '.results | to_entries[] | "📄 \(.key):\(.value[0].line_number)"'
    echo "-------------------------------------------"
    exit 1
else
    echo "✅ No secrets found"
fi

echo "==========================================" 