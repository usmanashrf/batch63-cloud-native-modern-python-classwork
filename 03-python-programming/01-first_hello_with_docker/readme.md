# CLASS-03 PART-01

## Steps for developing an application to containerizing it.

**We will create a simple python application which will print "hello world". Then will dockerize/containerize it.**

**Step-01:** Create a directory(folder) in your local system for creating a new application.

**Step-02:** Open directory in VSCode. You can open the directly in terminal and then write `code .`. This will open your VSCode in that directory.

**Step-03:** Create a new python file `main.py` in that directory (within VSCode).

**Step-04:** Write `print("hello world")` in the file.

**Great! our python application is developed. Now we will dockerize it.**

### What is Dockerizing/Containerizing an Application?

Dockerizing/Containerizing is the process of running a software application in a container. A container is an isolated, lightweight package of software/applicaton that includes everything needed to run an application.

So to run a **container**, first we have to bundle our application in a single package. This package is called `image`.

An **image** is essentially a snapshot of a container at a specific point in time. It includes your application, its dependencies, libraries, and configuration files. Once you have this image, you can create multiple instances of it, which are called **containers**.

But wait here. **How do we create an image?** Docker asks the developers, hey developers! i will create an image of the application for you but first i need instructions from your side what this image will contain.

_Here we have to provide the instructions to docker to create and image. We provide the instructions in a special file called `Dockerfile`_

_Let's start new steps for dockerizing our application._

**Step-01:** Create a new file `Dockerfile` in that directory (within VSCode).

**Step-02:** Copy below code and paste in `Dockerfile`. We'll learn about this code in upcoming classes.

```dockerfile
# base image
FROM python:3.12

# setup working directory in container
WORKDIR /app

# copy all files to app directory
COPY . /app/

# command to run on container start
CMD ["python", "main.py"]
```

**Step-03:** Now will write a command in CLI to create our image.

```bash
docker build -t my_first_image .
```

- _`docker` this intialize the docker's command line tool_.

- _`build` tells docker to build our image_.

- _`-t` this is option/switch which is used to tell the docker that whatever comes after it is the name/tag of our image_.

- _`my_first_image` the name/tag of our image_.

- _`.` used to identify the location of our application files. Here it means the current directory_.

Our image with name/tage `my_first_image` has been created. We can share it with anyone or deploy it anywhere.

**Step-03:** Now we will run application in container using the image `my_first_image` we created.
Here is the command to run the containter from the image.

```bash
docker run my_first_image
```

- _`docker` this intialize the docker's command line tool_.

- _`run` tells docker to run a container_.

- _`my_first_image` the name of our image whose container we want to run._

**Great! our application is dockerized.** You will see the output in "hello world" in terminal.

_See! how easy it is to dockerize an application._
