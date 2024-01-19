import gspread
import csv


gc = gspread.service_account(filename='cred\hoa-maps-site-52bb9d735d54.json')
# client = gspread.oauth("994671903258-27qs85gprshs4sf99glgugufa44ftd0t.apps.googleusercontent.com") # Please use your script for authorization.
spreadsheet_id = "1StrA2F0v3gU1IavTgYl14lFV6Uk_eRpCWlJRVg8-8_o"  # Please put your Spreadsheet ID.
sheet_name = "CSV-to-Google-Sheet"  # Please put the sheet ID of the sheet you want to use.
csv_file = "colorado\csv_test_file.csv"  # Please put the file path of the CSV file you want to use.

def upload_hoa_data():

    print(F'\nupload_hoa_data begins....')

    spreadsheet = gc.open_by_key(spreadsheet_id)
    worksheet = spreadsheet.worksheet(sheet_name)
    f = open(csv_file, "r")
    values = [r for r in csv.reader(f)]
    worksheet.update(values)

    print(F'\n.... upload_hoa_data is done.')
