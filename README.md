# NTUEE Webpage API Server

The purpose of this api sever is to response to frontend AJAX request and send back EE courses API in various form.
Current avaliable API are at:
- All `/api/course`: Give you all the courses.

# For Maintainers

In order to modify course content for future use, you can go into `/data/` and directly modify the csv file you want.
After modification, you should use the provided python script to tranfer the csv file into json format.
```bash
$ python csv_to_json.py
```
This will do all for you, and you don't need to restart the server.

# For Developers

## Getting Started 

### Installation

Develop on your own environment 

First, clone the project 

```bash
$ git clone https://github.com/dodo0822/ntueesa-backend.git
```

Then, install all the prerequisites listed in `requirements.txt` by:


```bash
$ pip install -r requirements.txt
```

Also, for reference, the project is developed with python 2.7.8. We recommend to use pyenv-virtualenv to create a clean python environment before installing all the packages. See [here](https://github.com/yyuu/pyenv) and  [here](https://github.com/yyuu/pyenv-virtualenv)

### Start The Service

We use python [Flask](http://flask.pocoo.org) framework to setup the webservice. To start the service, type:

```bash
$ python main.py
```
And the service is placed on port `7122`.

## Project Structure

```python
├── README.md        # This File
├── main.py          # Main Program
└── data             # Where CSV data is stored
    ├── 必修_系訂選修.csv
├── api              # API JSON File
    ├── course.json  # JSON for frontpage
├── csv_to_json.py   # Tool to transfer csv to json in required format
├── requirements.txt # Python Dependences                                
```                                                   