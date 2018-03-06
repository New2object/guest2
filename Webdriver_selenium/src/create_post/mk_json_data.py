import json

data = [
    {
        'title': "Don't cry because it's over, smile because it happened",
        'content': "Don't cry because it's over, smile because it happened. By Dr. Seuss"
    },

    {
        'title': "Be yourself; everyone else is already taken",
        'coontent': "Be yourself; everyone else is already taken. By Oscar Wilde"
    },

    {
        'title': 'So many books, so little time',
        'content': 'So many books, so little time. By  Frank Zappa'
    }

]

print(json.dumps(data))
