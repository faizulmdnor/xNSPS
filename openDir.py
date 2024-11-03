from pathlib import Path
entries = Path('c:/Exercises - Faizul/')

list = []
print("\n")
print(list)
print("\n")
for entry in entries.iterdir():
    print(entry.name)
    list = entry.name
