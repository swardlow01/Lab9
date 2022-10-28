def replace_substring(string, target_sub, replace):
    output = []
    index = 0
    while index < len(string):
        if string[index:index + len(target_sub)] == target_sub:
            index += len(target_sub)
            output.append(replace)
        else:
            output.append(string[index])
            index += 1
    print("".join(output))


replace_substring("christmas", "christ", "wife")
