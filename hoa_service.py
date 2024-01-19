from colorado.colo_downloader import *
from colorado.colo_cleaner import *
from colorado.colo_validator import *
from colorado.colo_upload_csv_to_gsheets import *

def download_hoa_data():
    print('\ndownload_hoa_data begins....')
    
    # colo_downloader()
    
    print('\n.... download_hoa_data completed.')

    
def validate_hoa_data():

    print('\nvalidate_hoa_data begins....')
    
    # colo_validate()
    
    print('\n.... validate_hoa_data completed.')


def clean_hoa_data():
    print('\nclean_hoa_data begins....')
    
    # colo_clean()
    
    print('\n.... clean_hoa_data completed.')


def import_hoa_data_to_gsheets():
    print('\nsimport_hoa_data_to_gsheets begins....')
    
    upload_hoa_data()

    print('\n.... import_hoa_data_to_gsheets completed.')


def main():
    #begin service
    download_hoa_data()
    
    # validate_hoa_data()
    
    clean_hoa_data()
    
    import_hoa_data_to_gsheets()

main()