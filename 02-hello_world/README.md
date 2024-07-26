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
