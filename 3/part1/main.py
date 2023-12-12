def get_data():
    data = """467..114..
...*......
..35..633."""
    return data

current_tal = ""
ok_numbers = []
index = -1
def get_current_tal(index):
    global current_tal
    num = ""
    for i in range(0,10):
        if data[index].isdigit():
            num += data[index]
            index += 1
        else:
            break
    
    current_tal = num
    num = ""

data = get_data()
def check_nine(index, char):
    return "hi"
#print(data)
for i in range(len(data)):
    get_current_tal(index)
    if current_tal:
        print(current_tal)
    index += len(current_tal)
    if index != len(data) - 1:
        index += 1
