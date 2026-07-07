FROM python:3.12-slim

WORKDIR /app

# Install dependencies
RUN pip install --no-cache-dir "fastmcp>=2.0"

COPY server.py .

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
  CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/health')" || exit 1

CMD ["python", "server.py", "streamable-http"]
