#task1
def favorit_muvie(muvie):
    print(f'Мой любимый фильм называется {muvie}')
favorit_muvie('Логан')

#task2
def make_country(name, capital):
    country={}
    country['name'] = name
    country['capital'] = capital
    return country
country = make_country('Ukraine', 'Kiyv')
print(country)
print(country['name'])
print(country['capital'])
