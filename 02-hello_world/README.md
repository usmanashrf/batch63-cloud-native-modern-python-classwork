# How to run this code
### Checking to see if Docker is running:
```bash
docker version
```
### Building the Image for Dev:
```bash
docker build -f Dockerfile -t my-first-image .
```
### Check Images:
```bash
docker images
```
### Running the Container:
first way
```bash
docker run --name first-cont1 my-first-image
```
second way
```bash
docker run -d --name first-cont1 my-first-image
```

---

# Dockerfile Explanation

### Base Image:
```bash
FROM python:3.12
```
This line tells Docker to use the Python 3.12 image as the base for your container. This image already includes a minimal operating system along with Python 3.12 installed. So, you don’t need to install an operating system separately.
### Set Up Working Directory:
```bash
WORKDIR /app
```
This sets the working directory inside the container to /app. It’s like saying, “Whenever I do something in this container, let’s do it inside this /app folder.”

### Copy Files:
```bash
COPY . /app/
```
•	This line copies all the files from your current directory on your computer (where the Dockerfile is) to the /app directory inside the container. It’s like packing all your project files and putting them in the /app folder inside the container.

### Command to Run:
```bash
CMD ["python", "main.py"]
```
This specifies the command to run when the container starts. In this case, it runs python main.py, which means it will execute the main.py script using Python. It’s like saying, “When you turn on this computer, automatically run this Python script.”

## Putting It All Together
1.	You start with a box that already has Python 3.12 installed (base image).
2.	You decide that all work inside this box will happen in a specific area called /app (working directory).
3.	You pack all your project files into this area (copy files).
4.	You set the box to automatically run your main Python script (main.py) whenever it’s opened (command to run).
