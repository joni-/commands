#!/usr/bin/python

import argparse
import json
import os
import sys

FILE = 'entries.json';

def read_data_json():
  if not os.path.isfile(FILE):
    return []

  with open(FILE, 'r') as f:
    contents = f.read()
    if not contents.strip():
      return []
    return json.loads(contents);

def add_entry(command, tags, comment):
  data = read_data_json()
  entry = {'command': command, 'tags': tags, 'comment': comment}
  data.append(entry)
  with open(FILE, 'w') as f:
    f.write(json.dumps(data, indent=2))

def find(tags):
  tags = set(tags)
  data = read_data_json()
  for entry in data:
    entry_tags = set(entry['tags'])
    if len(tags.intersection(entry_tags)) == len(tags):
      print json.dumps(entry, indent=2)

def main(args):
  parser = argparse.ArgumentParser()
  parser.add_argument("--add", help="add a new command")
  parser.add_argument("--tags", help="tags for the command")
  parser.add_argument("--comment", help="what the command does")
  parser.add_argument("--find", help="find commands by tag names")
  args = parser.parse_args()

  command = args.add if args.add else ''
  tags = args.tags.split() if args.tags else []
  comment = args.comment if args.comment else ''
  find_tags = args.find.split() if args.find else []

  if command:
    add_entry(command, tags, comment)
  elif find_tags:
    find(find_tags)

if __name__ == '__main__':
  main(sys.argv)
