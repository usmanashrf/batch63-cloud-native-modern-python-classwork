# Environment Setup
We'll start with downloading and setting up the necessary software and tools.

## 1. Visual Studio Code
Visual Studio Code (VSCode) is a free, open-source, cross-platform text editor that allows you to write code, edit code, and debug code. It is used for development, debugging, and version control.

It is language agnostic and can be used for many different programming languages. It is free to download and install.

[Download VSCode](https://code.visualstudio.com/download)

## 2. Docker Desktop
Docker Desktop is a software application that allows to build, share, and run containerized applications and microservices on local machine. It provides a user-friendly interface for managing containers, images, and Docker Compose files. Essentially, it's a tool that makes working with Docker easier and more accessible for developers.

Docker Desktop is free for education and learning purpose. However, commercial use of Docker Desktop at a company of more than 250 employees OR more than $10 million in annual revenue requires a paid subscription (Pro, Team, or Business).

[Download Docker Desktop](https://www.docker.com/products/docker-desktop) and install. 

### 2.1 Docker Desktop for Windows

**Pre-requisites:**
- Windows 10 or later (64-bit)
- Enable Hardware Virtualization from BIOS Settings
- Windows Subsystem for Linux (WSL) - *required to run linux containers*

    **Enable WSL:**
    1. Open Start menu and search for "Turn Windows Features on or off". A new window will open.
    2. Enable "Windows Subsystem for Linux (WSL)" and "Virtual Machine Platform".
    3. Save it and restart the system. 
    4. To check the installed version of WSL, run `wsl -l -v` in the command prompt.
    5. If you see version '1', we've to update to version '2'. In command prompt, run `wsl --update`. After update, run this command `wsl --set-default-version 2`.

    Read more about [How to install WSL.](https://learn.microsoft.com/en-us/windows/wsl/install)

### 2.2 Docker Desktop for Mac
 Check out [Docker Desktop for Mac](https://docs.docker.com/desktop/install/mac-install)

### 2.3 Docker Desktop for Linux
 Check out [Docker Desktop for Linux](https://docs.docker.com/desktop/install/linux-install/)

### 2.4 Run your first container
After successful installation, run docker desktop.
Open CLI tool and run this command `docker --version`. this will show the version of docker installed.

In CLI, run `docker run hello-world` command. Read the output.