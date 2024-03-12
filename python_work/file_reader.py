from pathlib import Path

path = Path('pi_digits.txt')
#Method chain
contents = path.read_text().rstrip()
print(contents)

#Relative file path
path = Path('text_files/pi_digits.txt')
contents = path.read_text().rstrip()
print(contents)

#Absolute file path
path = Path('C:/Users/rxw14/OneDrive/桌面/python_work/text_files/pi_digits.txt')
contents = path.read_text().rstrip()
print(contents)

#list of all items in file
lines = contents.splitlines()
for line in lines:
    print(line)