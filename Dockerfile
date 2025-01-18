# Dockerfile

# Use a lightweight Python base image
FROM python:3.9-slim-buster

# Set the working directory inside the container
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose Flask's port
EXPOSE 5000

# By default, we'll run the Flask app in development mode.
# In a production setting, you may want to use gunicorn or uwsgi.
CMD [ "python", "app.py" ]
