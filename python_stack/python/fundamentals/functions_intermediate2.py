# x = [ [5,2,3], [10,8,9] ] 
# students = [
#     {'first_name':  'Michael', 'last_name' : 'Jordan'},
#     {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
# sports_directory = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }
# z = [ {'x': 10, 'y': 20} ]
# print(x)
# print(students)
# print(sports_directory)
# print(z)
# x[1][0]=15
# students[0]['last_name']='Bryant'
# sports_directory['soccer'][0]='Andres'
# z[0]['y']=30
# print(x)
# print(students)
# print(sports_directory)
# print(z)

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
# def xyz(n):
#     for row in n:
#         print(row)
# print(xyz(students))

# def xyz1(n):
#     for row in n:
#         for key in row:
#             print(key)
# print(xyz1(students))

# def xyz2(n):
#     for row in n:
#         for key in row:
#             print(key, row[key])
# print(xyz2(students))

def iterateDictionary(n): 
    # # # for x in range (len(n)):
    # # #     for y in range(len(n[x])):
    # # #         print(n[x].keys(y)+' - '+n[x][n[x].keys(y)]+', '+n[x].keys(y+1)+' - '+n[x][n[x].keys(y+1)])
    # # #     print (n[x].keys()[x],n[x].values()[x])
    # # # for key,val in n.items():
    # # #     print key, ' - ', val
    for x in n:
        print(f"first_name - {x['first_name']} last_name -  {x['last_name']} ")   
print(iterateDictionary(students))

#     for row in n:
#         for key in row:
#             print(key, row[key])
# print(iterateDictionary(students))
# def iterateDictionary2(key,n):
# # # #     for x in range (len(n)):
# # # #         for y in range(len(n[x])):
# # # #             print(n[x][y])
# # # # iterateDictionary2(students)
#     for row in n:
#         print(f"{row[key]}")
# print(iterateDictionary2('first_name', students))


dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
# def printInfo(n):
#     for key in n:
#         print(len(n[key]),key)
#         for value in n[key]:
#             print(value)
# printInfo(dojo)
    # for row in n:
    #     for x in range(len(row)):   
    #         print(len(n[x]),' ',n[x].keys())
            # print(f"{row[x]}")
    # # for key in n:
    # #     print(key)
    # #     print(dojo[key])
    # #     for val in dojo[key]:
    # #         print(val)

        # # for key in row:
        # #     print(len(row[key]), key,row[key])

        # #     for val in key:
        # #         print()

