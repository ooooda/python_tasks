def read_file():
    fields = []
    with open('info.txt', "r") as f:
        for cnt, lines in enumerate(f.read().splitlines()):
            info = {}
            line = lines.split(", ")
            if cnt == 0:
                fields = line
            else:
                for i, el in enumerate(line):
                    info[fields[i]] = el
                information.append(info)
    print(information)


# def sort_by_data():
#     ## to do сортировка не работает
#     information.sort(key=lambda x: x["date"])


# def filtrate():
#     field, obj = FILTER_PAR
#     information = filter(lambda x: x % 2 != 0, information)


if __name__ == "__main__":
    information = []
    FIELD = "staff_id"
    OBJ = "_Petrov_"
    FILTER_PAR = [FIELD, OBJ]
    read_file()
    # sort_by_data()
    # filtrate()
