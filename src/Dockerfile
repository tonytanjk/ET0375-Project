# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3-slim

EXPOSE 5000

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Set the PYTHONPATH to include the src directory
ENV PYTHONPATH=/src

# Install pip requirements
COPY requirements.txt /src/
RUN apt-get update -y && apt-get install -y gcc python3-dev python3-rpi.gpio make
RUN pip install RPi.GPIO smbus
RUN python -m pip install -r /src/requirements.txt

# Set the working directory
WORKDIR /src

# Copy the application files
COPY . /src

# Creates a non-root user with an explicit UID and adds permission to access the /src folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /src
USER appuser

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "Server:app"]
