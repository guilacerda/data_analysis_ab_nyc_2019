import pandas as pd

# Reads specific columns from a csv file
def read_column_csv(file, columns):
    columns_list = columns
    try:
        csv_file = pd.read_csv(file, usecols=columns_list)
    except:
        print("the file could not be read")

        return 0

    return csv_file


# Creates a csv file with specific columns 
def format_csv(name, csv_file, columns):
    csv_file_formated = read_column_csv(csv_file, columns)
    
    if not csv_file_formated.empty:
        try:
            csv_file_formated.to_csv(name, index=False)
            
            print("successfully created file")
        except:
            print("the file could not be created")


if __name__=='__main__':
    col_list = ["id", "host_id", "price", "number_of_reviews", "last_review"]
    format_csv("AB_NYC_2019_FORMATED.csv", "AB_NYC_2019.csv", col_list)

