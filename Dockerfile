# Step 1: Use an official Python runtime as a parent image
FROM python:3.12

# Step 2: Set the working directory inside the container
WORKDIR /bot

# Step 3: Copy the current directory contents into the container
COPY . /bot

# Step 4: Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Run the application
CMD ["python", "bot.py"]
