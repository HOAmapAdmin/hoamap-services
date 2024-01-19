import csv

# input_file = F'colorado\HOA-Active.csv'
input_file = F'colorado\HOA-Active_pre_clean.csv'

def colo_validate():
    print('\ncolo_validate started....')

    if validate_csv_file(input_file):
        print("The CSV file is valid.")
    else:
        print("The CSV file is not valid.")
    
    print('\ncolo_validate done.')



def validate_csv_file(file_path):
  """Validates a CSV file.

  Args:
    file_path: The path to the CSV file.

  Returns:
    True if the CSV file is valid, False otherwise.
  """

  with open(file_path, "r") as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)

    for row in csv_reader:
      if len(row) != len(header):
        return False

      for column in row:
        if not column.strip():
        
          print('\nvalidate_csv_file done.')
          return False

  print('\nvalidate_csv_file done.')
  return True


# def validate_csv_file(file_path):
#   """Validates a CSV file.
  
#   Args:
#     file_path: The path to the CSV file.

#   Raises:
#     Exception: If the CSV file is not valid.
#   """
#   print('\nvalidate_csv_file started....')

#   with open(file_path, "r") as f:
#     reader = csv.reader(f)

#     # for i in range(len(reader)):
#     count = 0
#     for row in reader:
#       count = count + 1
#       # Check if the row has the correct number of columns.
#       if len(row) != 17:
#         raise Exception(F"Row {count} does not have the correct number of columns.")

#       # Check if the data in each column is valid.
#       for column in row:
#         if not column.isalnum():
#           raise Exception("Column does not contain a valid data.")

#   print('\nvalidate_csv_file done.')
