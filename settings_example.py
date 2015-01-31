"""
Example settings module.

This should be copied as `settings.py` and the values modified there.

That file is ignored by the repo, since it will contain environment
specific and sensitive information (like passwords).
"""

import logging
import os
import re

import yaml

from imap import EmailCheckError, EmailServer
from postgresql import DatabaseServer


# If this is set to a valid path, all CSV files extracted from emails will be
# stored in sub-folders within it.
CSV_FOLDER = os.getcwd()

SETTINGS_YAML_PATH = os.path.join(os.getcwd(), 'settings.yaml')


#- file: %(pathname)s
#  function: %(funcName)s
LOGGING_FORMAT = '''
- level: %(levelname)s
  line: %(lineno)s
  logger: %(name)s
  message: |
    %(message)s
  time: %(asctime)s
'''.strip()

LOGGING_KWARGS = dict(
	fromat=LOGGING_FORMAT,
	level=logging.DEBUG
)


def get_csv_file_types():
	csv_file_types = None

	with open(SETTINGS_YAML_PATH) as r:
		csv_file_types = yaml.load(r)

	return csv_file_types


def get_database_client():
	con = 'my_username/my_password@database.example.com:5432/my_database'
	return DatabaseServer(con)


def get_email_client():
	return EmailServer('mail.example.com', 'my_username', 'my_password')
