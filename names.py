# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'},
#      {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#      {'first_name' : 'KB', 'last_name' : 'Tonel'}
# ]

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

def names(a):
    for category in a:
        print category
        for i in range(len(a[category])):
            user_first = a[category][i]['first_name'].upper()
            user_last  = a[category][i]['last_name'].upper()
            user_length = len(user_first+user_last)
            person = ""
            person += str(i+1) + " - "
            print person + user_first + ' ' + user_last + ' - ' + str(user_length)


names(users)