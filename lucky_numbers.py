original_sequence = list(range(1, int(input("type a number: "))+1))
length = len(original_sequence)
current_step = 1
print(original_sequence)

while length > current_step:
    removed_list = []
    count = 0
    for i in original_sequence:
        if count != current_step:
            removed_list.append(i)
            count += 1
        else:
            count = 0
    original_sequence = removed_list
    length = len(original_sequence)
    current_step += 1
    print(original_sequence)

print(original_sequence)
