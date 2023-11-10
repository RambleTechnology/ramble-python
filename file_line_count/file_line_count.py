import os


class Line():

    _line = 0
    _java = ""
    _dict = {}


def traverse_directory(path):
    for filename in os.listdir(path):
        full_path = os.path.join(path, filename)
        if os.path.isdir(full_path):
            traverse_directory(os.path.join(path, filename))
        else:
            if filename.endswith(".java"):
                print(os.path.join(path, filename))
                with open(full_path, 'r', encoding='utf-8') as file:
                    l = file.readlines()
                    count = len(l)
                    # print(count)
                    if(count > Line._line):
                        Line._line = count
                        Line._java = full_path
                        statistics(count, full_path)


def statistics(line_count, java):
    Line._dict[line_count] = java
    # 对字典的键进行排序，倒序
    sorted_keys = sorted(Line._dict.keys(), reverse=True)
    # 创建一个新的字典，使用排序后的键和原始字典的值
    Line._dict = {key: Line._dict[key] for key in sorted_keys}
    # print(Line._dict)


if __name__ == "__main__":
    traverse_directory("D:\\Code\\ngh-smart-ar")
    print("最大行是：")
    print(Line._line)
    print("最大行对应的java文件是：")
    print(Line._java)
    print("前十的文件及其行数：")

    c = 1
    for k, v in (Line._dict).items():
        if(c > 11):
            break
        print(f" {k}: {v} ")
        c = c+1
