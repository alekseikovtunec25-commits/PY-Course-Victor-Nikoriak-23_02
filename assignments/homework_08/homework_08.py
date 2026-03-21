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

#task3
def make_operation(operator , *args ):
    if operator =='+':
        result = 0
        for args in args:
            result += args
        return result
    elif operator =='-':
        resultt = 0
        for args in args:
            resultt -= args
        return resultt
    elif operator =='*':
        resulttt = 1
        for args in args:
            resulttt *= args
        return resulttt
result = make_operation('+',3,4,7,9)
resultt = make_operation('-',5,4,4,2)
resulttt = make_operation('*',5,4,8)
print(result,resultt,resulttt)