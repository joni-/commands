# Commands
Tool for storing commands (or whatever) from command line and querying them by tags.

# Usage

- Install requirements `pip install -r requirements.txt`
- Rename config.json.sample to config.json
- Fill your GitHub email and password in config.json

```
Add entry:
python commands.py --add "command" --comment "what the command does" --tags "tag1 tag2 tag3"

Find entries:
python commands.py --find "tag1 tag2"
````

# Todo
- Ability to remove entries
- List all entries
- Format results