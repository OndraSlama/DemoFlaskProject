FROM python:3.8-slim-buster

EXPOSE 5000

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Credentials: for this demo saved to env variables from here for convenience
# Correct endpoint credentials
ENV USER_NAME=myUser123
ENV USER_PASS=secretSecret

# Rossum credentials
ENV ROSSUM_USER=civek71553@697av.com
ENV ROSSUM_PASS=rossum123456

# Install pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /app
COPY . /app

# During debugging, this entry point will be overridden.
CMD ["python", "main.py"]
