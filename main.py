from get_source_automatic import run_get_source
from extract_data import run_extract_data
from Create_Website import run_create_website

# Before running main.py go to secret.py and enter UNBC login and password so the bot can log in and scrape data automatically.
# Running main.py will first make the bot log in, select all the classes, scrape data and save to a text file
# Then the database will be updated based on that text file
# At last the user will enter input to tell the website which classes it will contain


def main():
    #run_get_source()
    #run_extract_data()
    run_create_website()


if __name__ == '__main__':
    main()
