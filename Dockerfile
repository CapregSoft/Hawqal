# Python version
FROM python:3 

# Copy the code from current folder to Docker Container
COPY . .

# Running the main CMD Command
CMD ["python","main.py"]
