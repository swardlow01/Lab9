#remove_substring

def remove_substring(string, target_sub):
    output = []
    index = 0
    while index < len(string):
        if string[index:index + len(target_sub)] == target_sub:
            index += len(target_sub)
        else:
            output.append(string[index])
            index += 1
    print("".join(output))


remove_substring("christmas", "christ")
