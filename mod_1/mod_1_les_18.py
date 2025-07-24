account1 = {'login': 'ivan', 'password': 'q1'}
account2 = {'login': 'petr', 'password': 'q2'}
account3 = {'login': 'olga', 'password': 'q3'}
account4 = {'login': 'anna', 'password': 'q4'}

user1 = {'name': 'Иван', 'age': 20, 'account': account1}
user2 = {'name': 'Петр', 'age': 25, 'account': account2}
user3 = {'name': 'Ольга', 'age': 18, 'account': account3}
user4 = {'name': 'Анна', 'age': 27, 'account': account4}

user_list = [user1, user2, user3, user4]

# 1
request1 = input('Enter the key (name or account): ').lower()
if request1 == 'name':
    print(f'the key value {request1} for user1 is', user1['name'])
    print(f'the key value {request1} for user1 is', user2['name'])
    print(f'the key value {request1} for user1 is', user3['name'])
    print(f'the key value {request1} for user1 is', user4['name'])
elif request1 == 'account':
    print(f'the key value {request1} for user1 is', user1['account'])
    print(f'the key value {request1} for user1 is', user2['account'])
    print(f'the key value {request1} for user1 is', user3['account'])
    print(f'the key value {request1} for user1 is', user4['account'])

# 2
request2 = int(input('Enter the index number: '))
user = user_list[request2-1]
print(f'User{request2} data:')
print('Name:', user['name'])
print('Age:', user['age'])
print('Login:', user['account']['login'])
print('Password:', user['account']['password'])

# 3
request3 = int(input('Which user should I move to the end:'))
print(f'User {request3} has been moved to the end')
print('The list before change')
print(user_list)
del_user = user_list.pop(request3-1)
user_list.append(del_user) 
print('The list after change')
print(user_list)

# 4
print('Average age of users')
print((user1['age'] + user2['age'] + user3['age'] + user4['age'])/4)