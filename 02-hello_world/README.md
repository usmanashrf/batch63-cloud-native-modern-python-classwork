# How to run this code
### Checking to see if Docker is running:
```bash
docker version
```
### Building the Image for Dev:
```bash
docker build -f Dockerfile -t my-dev-image .
```
### Check Images:
```bash
docker images
```
### Running the Container:
```bash
docker run -d --name dev-cont1 -p 8000:8000 my-dev-image
```
