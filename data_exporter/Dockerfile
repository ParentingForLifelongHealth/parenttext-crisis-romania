# Inherit from your central pipeline image
FROM docker.io/idems/parenttext-pipeline-ckan-export:latest

RUN pip install pandas

COPY scripts/ /app/scripts/
COPY entrypoint.sh /app/entrypoint.sh

RUN chmod +x /app/entrypoint.sh

ENTRYPOINT ["/app/entrypoint.sh"]