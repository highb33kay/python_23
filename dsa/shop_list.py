# collect lists from user
list_1 = input("Enter Items separated by a comma: ")
list_2 = input("Enter Items separated by a comma: ")

set_1 = set(list_1.split(","))
set_2 = set(list_2.split(","))

combined_set = set_1.union(set_2)

sorted_tuple = tuple(combined_set)

print(f"Dad, these are the items we want to buy:\n {sorted_tuple}")
