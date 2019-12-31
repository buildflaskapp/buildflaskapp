## Create Flask App

Create flask apps simply by running one command.

### Get started
You can start by cloning this repository to your local machine and you should be good to go
```
$ git clone https://github.com/kouul/create-flask-app
$ cd create-flask-app
```

### Usage
Ensure that you have flask installed on your environment. You can install flask using _pip3 install flask_.
```
$ python3 create-flask-app.py app_name
$ cd app_name
$ python3 app.py
```
Open up http://localhost:5000/ to see your Hello World app.

#### Set to path variable(Optional)
```
$ cp create-flask-app.py /usr/local/bin/
$ chmod +x /usr/local/bin/create-flask-app.py
```
After setting environment variable, you should be able to run _create-flask-app.py_ from anywhere on you pc

#### Arguments
- ##### Enable Debug Mode
    You can enable debug mode on while creating your flask app by using the option **-dB**
    - *python3 create-flask-app.py {app_name} **-dB***


- ##### Import style.css and app.js
    You can import stylesheet and javascript file automatically while creating the app using **-sS** option
    - *python3 create-flask-app.py {app_name} **-sS***


- ##### Create Dockerfile and docker-compose script
    You can push the app to a docker container instead of running it locally. Simply use **-dC** option
    - *python3 create-flask-app.py {app_name} **-dC***

    Please note that the image generated in Dockerfile is *python:3.7-alpine*. You might want to change this to the non-alpine version for big projects

### Coming features
- [ ] Manual(man create-flask-app)
- [x] Debug option on (-dB)
- [x] Include Stylesheet and Script (-Ss)
- [x] Push app to docker container (-dC)

Feel free to create issue in case something is not working :)