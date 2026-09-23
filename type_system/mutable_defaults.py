def add_item_buggy(item, target_list=[]):
    target_list.append(item)
    return target_list

print(add_item_buggy("A"))
print(add_item_buggy("B"))


def add_item(item, target_list=None):
    if target_list is None:
        target_list = []
    target_list.append(item)
    return target_list

print(add_item("A"))
print(add_item("B"))
