student_dic={
    'sai':{'roll':10,'age':24,'course':'ml'},
    'ram':{'roll':11,'age':23,'course':'python'},
}

# print(student_dic['sai'])
# print(student_dic['sai']['roll'])
student_dic['sai']['phone']=79870
# print(student_dic['sai'])


# to delete the value
# del student_dic['sai']['phone']
# print(student_dic['sai'])

#to delete and return the value
# print(student_dic['sai'].pop('phone'))
# print(student_dic['sai'])

#nesting list within dictionary
# travel_data={
#     'Gujarat':['Dwaraka','Somnath','Statue of Unity'],
#     'Rajasthan':['Jaipur','Udaipur']
# }
# print(travel_data)
# print(travel_data['Gujarat'])

#nesting dictionary within list
student=[
    {'name':'sai','roll':10,'age':24,'course':'ml'},
    {'name':'ram','roll':11,'age':23,'course':'python'},
]
# print(student)
# print(student[0])
# print(student[0]['name'])
student[1]['phone']=[343412,24234]
print(student[1]['phone'])