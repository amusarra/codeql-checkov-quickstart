FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

# Create a non-root group
RUN groupadd -r appuser

# Create a non-root user and add it to the 'appuser' group
RUN useradd -r -g appuser appuser

# Change ownership of /app to the non-root user
RUN chown -R appuser:appuser /app

# Switch to the non-root user to run the application
USER appuser

CMD ["python", "app.py"]