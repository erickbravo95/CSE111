from datetime import datetime
import csv

def main():
    try:
        products_dict = read_dictionary("products.csv")
        print("Inkom Emporium")
        print()
 
        with open("request.csv","rt") as request_file:
            reader = csv.reader(request_file)
            next(reader)
            quantity = 0  
            product_id = "" 
            number_items = 0
            multi = 0
            subtotal = 0
            for row in reader:
                quantity = row[1]
                product_id = row[0]
                product = products_dict[product_id]
                product_name = product[1]
                value = product[2] 
                number_items = number_items + int(quantity)
                multi = int(quantity) * float(value)
                subtotal = subtotal + multi
                print(f"{product_name}: {quantity} @ {value}")
        print()
        
        print(f"Number of Items: {number_items}")
        print(f"Subtotal: {subtotal:.2f}")
        sales_tax = subtotal*6/100
        print(f"Sales Tax: {sales_tax:.2f}")
        total=sales_tax+subtotal
        print(f"Total: {total:.2f}")
        today = datetime.now(tz=None)
        day_condition = today.strftime("%A")
        if day_condition == "Tuesday" or day_condition == "Wednesday":
            discount_total = total*10/100
            new_total = total-discount_total
            print(f"Today is {day_condition} so you get a 10% off!!")
            print(f"your new total is {new_total:.2f}")
        print()
        print("Thank you for shopping at the Inkom Emporium.")
        print(today.strftime("%c"))

    except KeyError as key_err:
        print(type(key_err).__name__, key_err)
    except FileNotFoundError as not_found_err:
        print(not_found_err)
    except PermissionError as perm_err:
        print(perm_err)
    





def read_dictionary(filename):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    dictionary = {}

    with open(filename,"rt") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row in reader:
            key = row[0]
            dictionary[key] = row
    return dictionary

if __name__ == "__main__":
    main()