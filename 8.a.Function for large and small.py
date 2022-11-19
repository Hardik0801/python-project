#Largest n Smallest number
def r_list(user):
    store_largest = 0
    store_smallest = user[0]
    for ele in user:
        if ele > store_largest:
            store_largest = ele
        elif ele < store_smallest:
            store_smallest = ele
    return f'The laregst number from the list is "{store_largest}" and the smallest is "{store_smallest}".'

