# Get basic dependency for Python app to work
FROM python:3.10-alpine

# Set working directory
WORKDIR /app

# Copy requirements.txt that contain necessary modules
COPY requirements.txt requirements.txt

# Install necessary modules
RUN pip3 --no-cache-dir install -r requirements.txt

# Get the rests of python app
COPY . .

# Run app on port 5000
EXPOSE 5000

# Run python app
CMD ["python3", "app.py"]