#! /usr/bin/python3
# run.py

import os

from app import create_app

config_name = os.environ.get('APP_SETTINGS') # config_name = "development"
appli = create_app(config_name)

if __name__ == '__main__':
    appli.run()