from bs4 import BeautifulSoup  # pip install bs4

# This will be run after get_source_automatic.py is done saving all the page source into the automated_Scrape.txt file
# With the help of BeautifulSoup, data is extracted and made into a string array that can be used as the database to
# create the fully automated website

arr = []  # holds all the strings
s = ''  # each string will contain data that we choose
start = False  # variable that controls when to start and stop making the string
ctr = 0  # currently the strings are made of the first 12 sections of data


# there is a problem with FNST 311 where the word Nisga'a creates a problem. There seems to be a special character included
# in there so we either solve this problem by ignoring it and writing the word as Nisgaa or we don't ignore it but we force
# the coding to be UTF-8, this replaces the ' in the word with a  weird looking "?" unknown character


def open_txt():
    with open('automated_scrape.txt', 'r', encoding='utf8', errors='ignore') as file:  # this text file will already be filled with scraped data
        myData = file.read()

    soup = BeautifulSoup(myData, 'html.parser')
    make_db(soup)


def make_db(soup):
    global start, s, ctr

    for string in soup.stripped_strings:
        if start:
            if ctr == 8:
                if len(string) == 1 or len(string) == 2 or string == 'TBA':  # fixes the bug where UNBC leaves some days empty on the upper level classes so we have to write a TBA or the string will sometimes be 1 short
                    s += 'TBA$'
                    ctr += 1
            s += string + '$'
            ctr += 1
            if ctr == 12:  # number of data sections you want
                arr.append(s)  # add the string to array and reset everything for the next string
                s = ''
                ctr = 0
                start = False
        elif len(string) == 5 and '10' in string:  # this finds the CRN number and starts making the string including it
            start = True
            s += string + '$'
            ctr += 1


# example full string output below (I just extract the first 12 sections starting from the CRN number)
# Sections Found Anthropology Select CRN Subj Crse Sec Cmp Cred Title Days Time Cap Act Rem WL Cap WL Act WL Rem Instructor Date ( MM / DD ) Location Attribute


def update_database():  # update the database by writing the whole array that was generated

    f = open("automated_database.py", "w+")
    f.write('courseDetailsLHS = [\n')

    for i in range(len(arr)):
        f.write("    \"" + arr[i] + "\",\n")

    f.write(']\n')
    print('Database has been updated successfully!')


def run_extract_data():
    open_txt()
    update_database()
