# Trier des étudiants

def sort_by_mark(my_class):
    a_list = sorted(my_class, key=lambda my_class: my_class[0], reverse=True)
    return a_list

def sort_by_name(my_class):
    a_list = sorted(my_class, key=lambda my_class: my_class[1])
    return a_list

# Uncomment the following lines as needed
# if you want to test your implementation a bit:

# my_class = [(25, "Shannon"), (50, "Alan"), (75, "Ada")]

# print(sort_by_mark(my_class))
# print(sort_by_name(my_class))