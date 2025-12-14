
serbian_dict = {
    'hello' : 'Здраво',
    'good morning' : 'Добро јутро',
    'how are you?' : 'Како си?',
    'yes' : 'да',
    'no' : 'не',
    'goodbye' : 'Збогом',
    'good day' : 'Добар дан',
    'food' : 'Храна',
    'water' : 'вода',
    'thank you' : 'Хвала',
    'house' : 'Хвала',
    'book' : 'Књига',
    'friend' : 'Пријатељ',
    'tomorrow' : 'Сутра',
    'today' : 'Данас',
    'money' : 'Новац',
    'cat' : 'Мачка',
    'cold' : 'Хладно',
    'beautiful' : 'Лепо',
    'dog' : 'Пас'
}

language = input('What language do you want? ')
language = language.lower()
if language == 'serbian':
    word = input('Enter a word to translate: ')
    word = word.lower()
    if word in serbian_dict:
        translation = serbian_dict.get(word)
        print(word,' is ',translation, ' in ', language)
    else:
        print('Sorry, that word does not exist in this dictionary')