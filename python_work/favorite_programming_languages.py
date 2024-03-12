favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}")

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

friends = ['phil', 'sarah']

#using method key()
for name in sorted(favorite_languages.keys()):
    print(f"Hi {name.title()}")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

#using method values()
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

#This is repetitive, use set
print("\nThe following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())


#Set defination looks like dictionary but different
languages = {'python', 'rust', 'python', 'c'}
print(languages)