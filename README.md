# RailwayStation

This application reads in the operating directory of Deutsche Bahn AG as a .csv file and provides a REST endpoint that uses the RL-100 code to locate the operating location and provides more detailed information.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the requirements [Flask](https://github.com/pallets/flask/) and [FlaskRESTful](https://flask-restful.readthedocs.io/en/latest/).

```bash
pip3 install -r requirements.txt
```

## Usage

To run the flask application, go to the main directory `RailwaySystem` and use

```bash
python3 scripts/restAPI.py
```

By default, this application will run at `127.0.0.1:8080` and by entering the RL-100-code in the absulut path, it provides more detailed information on the railway station. For example:

```
127.0.0.1:8080/betriebsstelle/aamp
```
