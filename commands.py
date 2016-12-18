#!/usr/bin/python

import argparse
import json
import os
import sys

import api

def add_entry(command, tags, comment):
  data = api.get_commands()
  entry = {'command': command, 'tags': tags, 'comment': comment}
  data.append(entry)
  api.write_commands(data)

def find(tags):
  tags = set(tags)
  data = api.get_commands()
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
