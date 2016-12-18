import json
import requests
from github import Github, GistFile, InputFileContent

from config import parse_config

COMMENT_IDENTIFIER = 'command store created by commands app'
FILENAME = 'commands'

def get_api():
  config = parse_config()
  email = config['user']['email']
  password = config['user']['password']
  return Github(email, password)

def get_gists():
  return get_api().get_user().get_gists()

def get_commands_gist():
  for gist in get_gists():
    if gist.description == COMMENT_IDENTIFIER:
      return gist
  return None

def get_commands_file():
  gist = get_commands_gist()
  return gist.files.get(FILENAME, None) if gist else None

# Returns JSON
def get_commands():
  # TODO: figure out why file.content is empty
  # ... https://github.com/PyGithub/PyGithub/issues/485
  file = get_commands_file()
  res = requests.get(file.raw_url)
  return json.loads(res.text if res.status_code == 200 else '[]')

# Takes dict as input
def write_commands(commands):
  file = get_commands_file()
  user = get_api().get_user()
  files = {
    FILENAME: InputFileContent(content=json.dumps(commands, indent=2))
  }
  if not file:
    user.create_gist(public=True, files=files, description=COMMENT_IDENTIFIER)
  else:
    gist = get_commands_gist()
    gist.edit(description=COMMENT_IDENTIFIER, files=files)
