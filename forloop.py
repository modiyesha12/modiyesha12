"""
for i in range(1,6,4):
    print(i)
"""
subject_list =[]
for i in range(1,6,2):
    subject = input("wrute subject name :")
    subject_list.append(subject)
print(subject_list)

subject_n =input("write name which you want to remove:")
subject_list.remove(subject_n)
print(subject_list)