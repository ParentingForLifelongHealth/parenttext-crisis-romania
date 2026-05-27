#!/bin/bash

# Exit immediately if any command fails (Crucial for pipelines!)
set -e

export OUTPUT_FILE=${OUTPUT_FILE:-contacts.csv}

echo "=== Step 1: RapidPro Export ==="
python -m parenttext.rapidpro_api_tools --steps export_contacts

echo "=== Step 2: Post-Processing ==="

echo "Running map_waves.py..."
python /app/scripts/map_waves.py -i "$OUTPUT_FILE" -o "$OUTPUT_FILE"

echo "=== Step 3: CKAN Upload ==="
python -m parenttext.ckan_tools \
  --file "$OUTPUT_FILE" \
  --dataset "$CKAN_DATASET" \
  --resource-name "$CKAN_RESOURCE_NAME" \
  --reconcile "uuid"

echo "Pipeline completed successfully!"