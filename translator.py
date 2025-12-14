
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

twi_dict = {
        'please':'Mepa wo kyƐw',
        'yes':'Aane',
        'no':'Daabi',
        'home':'Fie',
        'thank you':'Meda wo ase',
        'bird':'Nnomma',
        'tree':'Dua',
        'child': 'Abofra',
        'water':'Nsuo',
        'hunger': 'kƆm',
        'good morning': 'Meda wo akye',
        'chicken': 'Akoko',
        'food': 'Aduane',
        'welcome': 'Akwaaba',
        'love': 'ƆDƆ',
        'sleep': 'Da',
        'matter' :'asƐm',
        'come': 'Bra',
        'go': 'KƆ',
        'friend': 'adamfo',
}

gbagyi_dictionary = {
    'good morning' : 'ha gyi fe',
    'good evening': 'hazeeye',
    'what is your name':'ayihogona',
    'sit down': 'saseye',
    'stand up': 'lakala',
    'have u heard': 'hokuwoe',
    'go':'lo',
    'come':'ba',
    'water':'nuwa',
    'give me':'gami',
    'baby':'bibi',
    'head':'tukwo',
    'thank you':'magode',
    'drink':'si',
    'hair':'tinyi',
    'peace':'shimi',
    'welcome':'mambaah',
    'mouth':'alu',
    'nose':'ohva',
    'stomach': 'nubobiya',
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
elif language == 'twi':
    word = input('Enter a word to translate: ')
    word = word.lower()
    if word in twi_dict:
        translation = twi_dict.get(word)
        print(word, ' is ', translation, ' in ', language)
    else:
        print('Sorry, that word does not exist in this dictionary')
elif language == 'gbagyi':
    word = input('Enter a word to translate: ')
    word = word.lower()
    if word in gbagyi_dictionary:
        translation = gbagyi_dictionary.get(word)
        print(word, ' is ', translation, ' in ', language)
    else:
        print('Sorry, that word does not exist in this dictionary')
