bags = {'trash': []}


def ostap_workflow(bags, *args):
    if len(args) > 6:
        return 'Слишком много данных, Остап сломается :('
    sorted_numbers = sorted(list(args))
    bag = []
    for num in sorted_numbers:
        if num + sum(bag) > 100 or len(bag) + 1 > 5:
            bags['trash'].append(num)
        else:
            bag.append(num)
    bags[f'{sum(bag)}_{len(bag)}'] = bag
    return bags


# {'trash': [55, 122], '62_3': [12, 20, 30]}
print(ostap_workflow(bags, 20, 30, 12, 55, 122))
print(ostap_workflow(bags, 1, 2, 3, 4, 5, 6, 7)
      )  # Слишком много данных, Остап сломается :(
# {'trash': [55, 122, 101], '62_3': [12, 20, 30], '99_1': [99]}
print(ostap_workflow(bags, 99, 101))
# {'trash': [55, 122, 101, 101], '62_3': [12, 20, 30], '99_1': [99], '0_0': []}
print(ostap_workflow(bags, 101))
