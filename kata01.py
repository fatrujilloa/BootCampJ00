import  sys

languages = {
'Python': 'Guido van Rossum',
'Ruby': 'Yukihiro Matsumoto',
'PHP': 'Rasmus Lerdorf',
}
def format():
    for key in languages.keys():
        print (key, "was created by", languages[key])

format()