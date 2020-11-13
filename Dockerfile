FROM python:3

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Install requirements
ADD requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN rm requirements.txt

COPY Dockerfile ./.env* ./


# copy application codebase
RUN mkdir /app
WORKDIR /app
COPY eHealth .

CMD tail -f /dev/null
