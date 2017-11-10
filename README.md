# Flask Example 

This is a simple [flask](http://flask.pocoo.org/) example application Built using [pybuilder](http://pybuilder.github.com).

Templates use [twitter bootstrap](http://twitter.github.com/bootstrap/) via [bootstrap CDN](http://bootstrapcdn.com).

# How to build

## Create a virtual environment

Python allows to develop in [virtual environments](http://pypi.python.org/pypi/virtualenv).

```bash
virtualen ve
```

Activate the virtual environment

```bash
source ve/bin/activate
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
python run.py
```

# How to run in production
Working on it...

# CICD Setup/ Jenkins
Working on it...


# License

Licensed under [Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0.html)
