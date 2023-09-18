
def main():
    provinces_list = read_list("provinces.txt")
    print(provinces_list)
    times = provinces_list.count("Alberta")
    print()
    print(f"Alberta occurs {times} times in the modified list.")


def read_list(filename):
    list = []
    with open(filename,"rt") as text_file:
        for line in text_file:
            clean_line = line.strip()
            if "AB" in clean_line:
                clean_line = "Alberta"
            list.append(clean_line)
    list.pop(0)
    list.pop()
    return list

if __name__ == "__main__":
    main()