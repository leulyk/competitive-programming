# https://www.hackerrank.com/challenges/30-dictionaries-and-maps/problem

data_count = int(input())

phone_book = {}
for i in range(data_count):
    arguments = input().split()
    phone_book[arguments[0]] = arguments[1]

queries = []
while True:
    try:
        query = input()
        queries.append(query)
    except EOFError:
        break
    
for query in queries:
    if phone_book.get(query):
        print(f'{query}={phone_book[query]}')
    else:
        print('Not found')

