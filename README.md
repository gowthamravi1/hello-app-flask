# Flask Example 

This is a simple [flask](http://flask.pocoo.org/) example application Built using [pybuilder](http://pybuilder.github.com).

Templates use [twitter bootstrap](http://twitter.github.com/bootstrap/) via [bootstrap CDN](http://bootstrapcdn.com).

# How to build

## Create a virtual environment

Python allows to develop in [virtual environments](http://pypi.python.org/pypi/virtualenv).

```bash
virtualen deveve
```

Activate the virtual environment

```bash
source deveve/bin/activate
```

## Install pybuilder

```bash
pip install pybuilder
```

 Install dependencies using pybuilder
```bash
pyb install_dependencies
```

Run pybuilder `pyb` to build run the unit and integration tests and build the project.
```bash
pyb
```

# How to run

After installation you can run the application in debug mode using
```bash
python src/main/python/com/jeavio/start_system_analyzer.py
```

# How to run in production
Working on it...

# How to run in docker
Working on it...

# CICD Setup (Jenkins)
1) Download the Jenkins data file (https://drive.google.com/a/jeavio.com/file/d/1YYrHg0pdAly0t66p5UP-ZP3qOnRmBBl_/view?usp=sharing)
2) Install Docker
3) docker run -d -p 8080:8080 -p 50000:50000 -v your_jenkins_data_location:/var/jenkins_home gowthamravi/jenkins-python-2.7.13:1 (If container is not started run the following command sudo chown -R 1000:1000 your_jenkins_data_location )
4) Jenkins login details (gowtham/gowtham)
5) Start the Build, if the build is failure due to depenedencies do the following

After Docker container is started, Insrtall the following depenedencies

1) apt-get install patch
2) apt-get install gcc
3) apt-get install make
4) apt-get install libmysqlclient-dev
5) apt-get install libssl-dev

# License

Licensed under [Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0.html)
