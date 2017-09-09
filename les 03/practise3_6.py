klinker = ('a','e','i','o','u')
string = 'Guido van Rossum heeft programmeertaal Python bedacht.'

for char in string:
    for k in klinker:
        if(char == k):
            print(char)
