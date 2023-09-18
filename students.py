import csv


def main():
    tuki = read_dictionary("students.csv")
    student_name = input("Please enter an I-Number (xxxxxxxxx): ")
    student_name = student_name.replace("-","")
    if student_name in tuki:
        print(tuki[student_name])
    else:
        print("No such student")
    
    


def read_dictionary(filename):
    """Read the contents of a CSV file into a
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
    Return: a dictionary that contains
        the contents of the CSV file.
    """
    dictionary = {}

    with open(filename,"rt") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row in reader:
            key = row[0]
            dictionary[key] = row[1]
    return dictionary



if __name__ == "__main__":
    main()