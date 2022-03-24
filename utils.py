def mount_filename(class_index, file_index):
    folder_path = 'assets/'
    return folder_path + str(class_index) + str(file_index) + '.txt'


def open_file(_filename):
    array = list()
    file = open(_filename, 'r')
    text = file.readlines()
    for line in text:
        array.append(int(line))
    file.close()
    return array


def write_file(_filename, _results):
    formatted_array = list()
    file = open(_filename, 'a')

    formatted_array.append(str(_results.get("comparisons")) + " ")
    formatted_array.append(str(_results.get("swap")) + " ")
    formatted_array.append(str(_results.get("time")) + " ")
    formatted_array.append(_filename)
    formatted_array.append('\n')

    file.writelines(formatted_array)
    print(_filename + "executed", end="")
