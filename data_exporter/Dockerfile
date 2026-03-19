# Inherit from your central pipeline image
FROM ghcr.io/idemsinternational/parenttext-ckan-export:latest

RUN pip install pandas

COPY scripts/ /app/scripts/
COPY entrypoint.sh /app/entrypoint.sh

RUN chmod +x /app/entrypoint.sh

ENTRYPOINT ["/app/entrypoint.sh"]