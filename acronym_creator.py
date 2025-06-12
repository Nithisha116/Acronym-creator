def create_acronym(phrase):
    return ''.join(word[0].upper() for word in phrase.split())
s = input("Enter a phrase: ")
acronym = create_acronym(s)
print(acronym)
