import re
def read_file(file):
    with open(file) as f:
        data = f.read().splitlines()
    return data

def get_instructions(data):
    directions = ""
    for line in data:
        for char in line:
            if char == "R":
                directions += "1"
            if char == "L":
                directions += "0"
        if line == "":
            break
    return directions # string of 1s (right) and 0s (left)

def get_name(data):
    dict_inst = {}
    for line in data:
        word = ""
        for char in line:
            if char.isalpha():
                word += (char)
        if len(word) != 9:
            word = ""
            continue
        # here i will create a dictonary
        # where key is the name and value is the directions
        #first 3 chars is key, next 3 chars is first element of a list and last 3 chars is the second element of a list
        dict_inst[word[:3]] = [word[3:6], word[6:9]]
        if line == "":
            continue
    return dict_inst

def direction_search(directions, dict_inst, instruction, counter):
    for direction in directions:
        instruction = dict_inst[instruction][int(direction)]
        counter += 1
        if instruction == "ZZZ":
            print(counter)
            return counter
    if instruction != "ZZZ":
        direction_search(directions, dict_inst, instruction, counter)




    # if len(directions) == 0:
    #     print("end")
    #     return counter
    # while len(directions) > 0:
    #     # print(len(directions))
    #     direction = int(directions[0])
    #     directions = directions[1:]
    #     new_inst = dict_inst[instruction][direction]
    #     print(new_inst)
    #     counter += 1
    #     direction_search(const_directions, directions, dict_inst, new_inst, counter)

def main():
    data = read_file("day8_data")
    directions = get_instructions(data)
    dict_inst = get_name(data)
    direction_search(directions, dict_inst, "AAA", 0)
main()