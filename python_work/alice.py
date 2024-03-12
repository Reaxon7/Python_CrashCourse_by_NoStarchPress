from pathlib import Path

path = Path('text_files/alice.txt')
#use encoding when the the system's default doesn't match with file
try:
    contents = path.read_text(encoding = 'utf-8')
except FileNotFoundError:
    #fail silently
    pass
else:
    #Count the approximate number of words in the file:
    words = contents.split()
    num_words = len(words)
    print(f"The file {path} has about {num_words} words.")