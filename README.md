## Build Flask App

An easy to use flask app generator that allows users to create flask apps simply by running one command. You can check out the official website [here](https://build-flask-app.kouul.website). The project is published with MIT license and made open, so feel free to use and raise issue in case something not working properly on your end! :) | ![](./img/logo.png)
------------ | -------------

### Install using source code
To download the app generator, you can clone this repository to your local machine.
```
$ git clone https://github.com/kouul/build-flask-app
$ cd build-flask-app
```

### Install using pip3
```
$ pip3 install build-flask-app
```
Package @ PyPI repository: https://pypi.org/project/build-flask-app/

### Usage
Ensure that you have flask installed on your environment. You can install flask using _pip3 install flask_.
```
$ build-flask-app app_name
$ cd app_name
$ python3 app.py
```
![](./demo/build-flask-app.gif)

Open up http://localhost:5000/ to see your Hello World app.

### Arguments

Args | Usage | Definition
------------ | ------------- | -------------
-d | $ python3 build-flask-app.py app_name -d | debugger mode on
-cj | $ python3 build-flask-app.py app_name -cj | import style.css and app.js
-bs | $ python3 build-flask-app.py app_name -bs | import bootstrap cdn
-jq | $ python3 build-flask-app.py app_name -jq | import jQuery cdn
-gsap | $ python3 build-flask-app.py app_name -gsap | import GSAP cdn
-fa | $ python3 build-flask-app.py app_name -fa | import Font Awesome cdn
-dc | $ python3 build-flask-app.py app_name -dc | containerize app in docker

Below is a list of arguments you can pass when building your flask application.
##### Enable Debug Mode
You can enable debug mode on while creating your flask app by using the option **-d** or **--debugger**
```
$ python3 build-flask-app.py app_name -d
```

##### Import style.css and app.js
You can import stylesheet and javascript file automatically while creating the app using **-cj** or **--css-js** option
```
$ python3 build-flask-app.py app_name -cj
```

##### Import bootstrap CDN
You can import bootstrap automatically via the CDN using **-bs** or **--bootstrap** option
```
$ python3 build-flask-app.py app_name -bs
```

##### Import jQuery CDN
You can import jQuery automatically via the CDN using **-jq** or **--jquery** option
```
$ python3 build-flask-app.py app_name -jq
```

##### Import Gsap CDN
You can import Gsap automatically via the CDN using **-gsap** or **--gsap** option
```
$ python3 build-flask-app.py app_name -gsap
```

##### Import Font Awesome CDN
You can import Font Awesome automatically via the CDN using **-fa** or **--font-awesome** option
```
$ python3 build-flask-app.py app_name -fa
```

##### Create Dockerfile and docker-compose script
You can push the app to a docker container instead of running it locally. Simply use **-dc** or **--docker-container** option. Please note that the image generated in Dockerfile is *python:3.7-alpine*. You might want to change this to the non-alpine version for big projects
```
$ python3 build-flask-app.py app_name -dC
```


### Features
- [x] Manual(--help)
- [x] Debug option on (-d)
- [x] Include Stylesheet and Script (-cj)
- [x] Push app to docker container (-dc)
- [x] Import bootstrap css library (-bs)
- [x] Import jQuery library (-jq)
- [x] Import gsap js library (-gsap)
- [x] Import font awesome library (-fa)
- [ ] Import zurb foundations library (-zb)
- [ ] Import angular js library (-an)
- [ ] Deploy on heroku (-hK)

Feel free to create issue in case something is not working :)