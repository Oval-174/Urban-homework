my_list = ["apple", "pear", "peach", "apricot", "nectarine", "orange", "tangerine"]
print('List: ', my_list)
print('First element: ', my_list[0])
print('Last element: ', my_list[-1])
print('Sublist: ', my_list[2:5])
my_list[2] = 'rotten ' + my_list[2]
print('Modified list: ', my_list)
my_dict = {"apple":"яблоко", "pear":"груша", "peach":"персик"}
print('Dictionary: ', my_dict)
print('Translation', "apple :", my_dict['apple'])
my_dict["apple"] = "гнилое яблоко"
print('Modified dictionary: ', my_dict)
