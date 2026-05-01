FROM python:3.11-alpine

RUN apk add --no-cache curl \
 && curl -L https://github.com/typst/typst/releases/latest/download/typst-x86_64-unknown-linux-musl.tar.xz \
 | tar -xJ \
 && mv typst*/typst /usr/local/bin/typst

WORKDIR /app

RUN pip install flask

COPY app.py .

CMD ["python", "app.py"]
