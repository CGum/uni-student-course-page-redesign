import sys
from database import check
from automated_database import courseDetailsLHS

# This script will generate an html file from scratch, based on user input of desired classes
# The input will be the 4 letter code names of the classes ex. CPSC COMM BIOL ANTH COMM etc.

f = open("index.html", "w+")  # make a file named index.html


def make_head():  # make the head part of the html
    f.write(  # basic stuff needed to get started with bootstrap
        '<!DOCTYPE html>\n'
        '<html lang="en">\n'
        '<head>\n'
        '\t<meta charset="utf-8">\n'
        '\t<meta name="viewport" content="width=device-width, initial-scale=1">\n'
        '\t<title>Look Up Classes</title>\n'
        '\t<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">\n'
        '\t<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>\n'
        '\t<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"></script>\n'
        '\t<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"></script>\n'
        '\t<script src="https://use.fontawesome.com/releases/v5.0.8/js/all.js"></script>\n'
        '\t<link href="style.css" rel="stylesheet">\n'
        '</head>'
    )


def make_body():
    f.write('\n<body>')
    put_images_at_top()
    make_navbar()
    make_container()
    f.write(    # end of the html
        '\n<script src="script.js"></script>'
        '\n</body>'
        '\n</html>'
    )

    end_msg()
    close_file()


def put_images_at_top():    # current design includes 6 pictures
    # modify this variable if more/less pictures are needed (keep in mind you need to modify the css file as well)
    pic_num = 6
    for i in range(pic_num):
        f.write(
            '\n\t<div class="bgimg-' + str(i) + '"></div>'
        )


def make_navbar():  # some good old html code for a navigation bar (it's animated with the use of CSS and JavaScript!)
    f.write(
        '\n\t<nav class="navbar navbar-expand-md">'
        '\n\t\t<div class="menu">'
        '\n\t\t\t<ul>'
        '\n\t\t\t\t<li><a href="#!"><img src="img/logo.png"></i></a></li>'
        '\n\t\t\t\t<li><a href="#!" class="menu-item">Student Online Services</a></li>'
        '\n\t\t\t\t<li><a href="#!" class="menu-item">Account & Personal Information</a></li>'
        '\n\t\t\t\t<li><a href="#!" class="menu-item">Awards & Financial Aid</a></li>'
        '\n\t\t\t\t<li><a class="menu-item" id="other-options" href="#!"><i class="fa fa-user"></i></a></li>'
        '\n\t\t\t</ul>'
        '\n\t\t\t<div class="menu2">'
        '\n\t\t\t\t<ul>'
        '\n\t\t\t\t\t<li><a href="#!" class="menu-item2">Return to Menu</a></li>'
        '\n\t\t\t\t\t<li><a href="https://ssb.unbc.ca/ssb/twbkfrmt.P_DispHelp?pagename_in=twbksite.P_DispSiteMap" target="_blank" class="menu-item2">Site Map</a></li>'
        '\n\t\t\t\t\t<li><a href="#!" class="menu-item2">Help</a></li>'
        '\n\t\t\t\t\t<li><a href="#!" class="menu-item2">Log Out</a></li>'
        '\n\t\t\t\t</ul>'
        '\n\t\t\t</div>'
        '\n\t\t\t<a class="close"><i class="fa fa-times"></i></a>'
        '\n\t\t</div>'
        '\n\t</nav>'
    )


def make_container():  # this will contain both lhs and rhs inside of it
    f.write('\n<div class="container-fluid">'
            '\n\t<div class="row padding">')

    make_lhs_beginning()
    make_lhs_accordion()
    make_rhs_beginning()
    make_schedule_cells()

    f.write('\n\t</div>'
            '\n</div>')  # close out the divs for the tags that contain both lhs and rhs


def make_lhs_beginning():
    f.write(
        '\n<!-- LHS -->'
        '\n\t\t<div class="col-sm-12 col-md-6 col-lg-6">'
        '\n\t\t\t<div class="card">'
        '\n\t\t\t\t<div class="card-body">'
        '\n\t\t\t\t\t<h4 class="card-title">Sections found</h4>'
    )


def end_lhs_beginning():  # end div tags for the 3 above
    f.write(
        '\n\t\t\t</div>'
        '\n\t\t</div>'
        '\n\t</div>'
    )


def make_accordion_table():
    global tn

    f.write('\n\t\t\t\t\t\t\t<table>')
    if tn == 0:
        initial_accordion_table_contents()
        tn += 1


def initial_accordion_table_contents():  # this is hard-coded since this part will never change
    f.write(
        '\n\t\t\t\t\t\t\t\t<tr>'
        '\n\t\t\t\t\t\t\t\t\t<th><abbr title="Course Reference Number">CRN</abbr></th>'
        '\n\t\t\t\t\t\t\t\t\t<th>Select</th>'
        '\n\t\t\t\t\t\t\t\t\t<th><abbr title="Section">Sec</abbr></th>'
        '\n\t\t\t\t\t\t\t\t\t<th><abbr title="Campus">Cmp</abbr></th>'
        '\n\t\t\t\t\t\t\t\t\t<th><abbr title="Credits">Cred</abbr></th>'
        '\n\t\t\t\t\t\t\t\t\t<th>Days</th>'
        '\n\t\t\t\t\t\t\t\t\t<th>Time</th>'
        '\n\t\t\t\t\t\t\t\t\t<th><abbr title="Capacity">Cap</abbr></th>'
        '\n\t\t\t\t\t\t\t\t\t<th><abbr title="Actual">Act</abbr></th>'
        '\n\t\t\t\t\t\t\t\t\t<th><abbr title="Remaining">Rem</abbr></th>'
        '\n\t\t\t\t\t\t\t\t</tr>'
    )


def make_accordion_table_content(name, num, crn, sec, cmp, cred, days, time, cap, act, rem):
    f.write('\n\t\t\t\t\t\t\t\t<tr>')
    link = make_link(name, num, crn)
    f.write('\n\t\t\t\t\t\t\t\t\t' + link)
    make_radio_button(crn)
    f.write(
        '\n\t\t\t\t\t\t\t\t\t<td>' + sec + '</td>'
        '\n\t\t\t\t\t\t\t\t\t<td>' + cmp + '</td>'
        '\n\t\t\t\t\t\t\t\t\t<td>' + cred + '</td>'
        '\n\t\t\t\t\t\t\t\t\t<td>' + days + '</td>'
        '\n\t\t\t\t\t\t\t\t\t<td>' + time + '</td>'
        '\n\t\t\t\t\t\t\t\t\t<td>' + cap + '</td>'
        '\n\t\t\t\t\t\t\t\t\t<td>' + act + '</td>'
        '\n\t\t\t\t\t\t\t\t\t<td>' + rem + '</td>'
        '\n\t\t\t\t\t\t\t\t</tr>'
    )


def end_section_part():
    global tn, n

    f.write(
        '\n\t\t\t\t\t\t\t</table>'
        '\n\t\t\t\t\t\t</div>'
    )  # end table/card-body div tags

    make_remove_button()
    make_submit_button()
    make_alert()

    f.write(
        '\n\t\t\t\t\t</div>'
        '\n\t\t\t\t</div>'
        '\n'
    )   # end card/collapse n div tags

    tn = 0
    n += 1


def make_submit_button():   # add class button
    f.write(
        '\n\t\t\t\t\t\t\t<button id="addBtn" type="button" class="btn btn-outline-secondary" onclick="getCRNArray()">Add</button>'
        '\n\t\t\t\t\t\t\t<br/><br/>'
    )


def make_remove_button():   # remove class button
    f.write(
        '\n\t\t\t\t\t\t\t<button id="removeBtn" type="button" class="btn btn-outline-secondary" onclick="getCRNDelete()">Remove</button>'
    )


def make_alert():
    # alerts for adding a class successfully, removing a class successfully, error while removing a class (for trying to remove a class that wasn't added into the weekly schedule), error alert for clashing times
    f.write(
        '\n\t\t\t\t\t\t\t<div class="alert alert-danger">'
        '\n\t\t\t\t\t\t\t\t<strong>Error!</strong> The class you are trying to add has clashing times with another class that is already in the schedule!. Make sure your schedule is empty on the days and hours of this class.'
        '\n\t\t\t\t\t\t\t</div>'
        '\n\t\t\t\t\t\t\t<div class="alert alert-success">'
        '\n\t\t\t\t\t\t\t\t<strong>Success!</strong> You have successfully added a class to your weekly schedule.'
        '\n\t\t\t\t\t\t\t</div>'
        '\n\t\t\t\t\t\t\t<div class="alert alert-warning remove-success">'
        '\n\t\t\t\t\t\t\t\t<strong>Success!</strong> You have successfully removed a class from your weekly schedule.'
        '\n\t\t\t\t\t\t\t</div>'
        '\n\t\t\t\t\t\t\t<div class="alert alert-warning remove-error">'
        '\n\t\t\t\t\t\t\t\t<strong>Error!</strong> You have not added this class to your schedule so you can not remove it!'
        '\n\t\t\t\t\t\t\t</div>'
    )


def make_radio_button(crn):  # radio button that is located at the left of each section
    f.write(
        '\n\t\t\t\t\t\t\t\t\t<td><input type = "radio" name = "radSize" id = "' + crn + '"  value = "small" class="radio-button"/></td> ')


def make_card():    # this will make each accordion which is made up of a heading number and a collapse number
    f.write('\n\t\t\t\t<div class="card">')
    take_input()
    end_section_part()  # after the very last collapse number, close out all necessary tags
    f.write('\n\t\t\t\t</div>')


def make_lhs_accordion():
    f.write('\n\t\t\t<div class="accordion" id="theAccordion">')
    make_card()
    f.write('\n\t\t\t</div>')
    end_lhs_beginning()  # need to close out the 3 tags from the beginning


def take_input():   # take user input, some error handling is included
    inp = input("\nEnter the course names you want the website to contain (ANTH, CPSC, COMM, BIOL ... etc.) or E to exit : ").upper()

    if len(inp) == 0:
        print("Please enter at least 1 class so the left hand side of the screen can be made! (input should be something like CPSC BIOL COMM ANTH... etc.")
        take_input()
    elif inp == 'E':
        print('Exit successful. Since you chose to exit, the HTML was not made properly!')
        sys.exit(0)

    isCorrect = check_correctness(inp)

    if isCorrect:
        pass
    elif not isCorrect:
        print("\nError! Make sure you have typed the name of all the classes correctly!")
        print('\nThe list of correct input are the following \n'+', '.join(check))
        take_input()

    arr = inp.split(" ")  # allows for more than 1 input subject,  ex. cpsc math phys (if more than one input, must have spaces in between)
    for i in range(0, len(arr)):
        find_all(arr[i])


def check_correctness(user_input):  # look if user input is correct (contains classes in the database)

    ans = False
    split_input = user_input.split(" ")
    print('HTML will be created with the following classes :')

    for i in range(0, len(split_input)):
        print(split_input[i])
        if split_input[i] in check:
            ans = True
        else:
            return False  # if at any point the input is wrong, just return false and exit out

    return ans


def find_all(inp):  # find all the indexes of the array that has the given course name  ex. cpsc
    for i, j in enumerate(courseDetailsLHS):
        if inp in j:
            separate_everything(courseDetailsLHS[i])


string = ''  # 2 strings used in logic for making the HTML code correctly
string2 = ''
n = 1  # each heading and collapse needs a different number
n2 = 1  # part of the logic for making sure all the classes/tutorials/labs get written under the same collapse
tn = 0  # used to print the hard coded initial collapse information for each different class once

# the function below will get called if the list of classes contains what the user is looking for.
# The idea here is to start with 2 empty strings, make the first string = name + ' ' + num ex. CPSC 101 and
# the 2nd string the same as the first string for the very first iteration because there's at least 1 thing to be
# displayed on the website if this function is called. Keep updating string and checking to see if it's still the
# same as string2, depending on this either make headings if different ex. CPSC 101, CPSC 110 (2 different classes,
# 2 different headings) or if they are the same then write the information under a collapse
# ex. CPSC 101 A1, CPSC 101 L1, CPSC 101 L2, CPSC 101 T1 ...


def separate_everything(line_in_array):  # logic for making n headings and n collapses
    global string, string2, n, n2

    crn, name, num, sec, cmp, cred, full_name, day, time, cap, act, rem, empty = line_in_array.split("$")    # split the string on the delimiter

    string = name + ' ' + num

    if string2 == '':   # make both strings same for first iteration
        string2 = string

    if n == 1 and n2 == 1:  # this makes sure the very first heading doesn't get skipped
        make_heading(name, num, full_name, crn)

    if string == string2:

        if n2 == 0:
            make_accordion_table_content(name, num, crn, sec, cmp, cred, day, time, cap, act, rem)
            return  # return is crucial here

        make_collapse()
        make_accordion_table_content(name, num, crn, sec, cmp, cred, day, time, cap, act, rem)
        n2 = 0

    elif string != string2:
        end_section_part()
        string2 = string
        make_heading(name, num, full_name, crn)
        make_collapse()
        make_accordion_table_content(name, num, crn, sec, cmp, cred, day, time, cap, act, rem)


def make_link(name, num, crn):  # make individual links for each course, lab or tutorial
    link = 'https://ssb.unbc.ca/ssb/bwckschd.p_disp_listcrse?term_in=202001&subj_in=' + name + '&crse_in=' + num + \
           '&crn_in=' + crn + ''
    final_link = '<td><a href="' + link + '" target="_blank">' + crn + '</a></td>'
    return final_link


def make_collapse():
    global n

    f.write(
        '\n\t\t\t\t<div id="collapse' + str(n) + '" class="collapse" aria-labelledby="heading' + str(n) +
        '" data-parent="#theAccordion">'
        '\n\t\t\t\t\t<div class="card-body">'
    )

    make_accordion_table()


def make_heading(name, num, full_name, crn):  # make the heading part of the HTML which is inside of the accordion
    global n
    f.write(
        '\n\t\t\t\t<div class="card">'
        '\n\t\t\t\t\t<div class="card-header" id="heading' + str(n) + '">'
        '\n\t\t\t\t\t\t<h2 class="mb-0">'
        '\n\t\t\t\t\t\t\t<button class="btn btn-text" type="button" data-toggle="collapse" data-target="#collapse' +
        str(n) + '" aria-expanded="true" aria-controls="collapse' + str(n) + '">'
    )

    link = make_link(name, num, crn)

    f.write(
        '\n\t\t\t\t\t\t\t\t' + link +
        '\n\t\t\t\t\t\t\t\t<td>' + name + '</td>'
        '\n\t\t\t\t\t\t\t\t<td>' + num + '</td>'
        '\n\t\t\t\t\t\t\t\t<td>' + full_name + '</td>'
        '\n\t\t\t\t\t\t\t</button>'
        '\n\t\t\t\t\t\t</h2>'
        '\n\t\t\t\t\t</div>'
    )


def make_rhs_beginning():  # start off the rhs schedule
    f.write(
        '\n<!-- RHS -->'
        '\n<div class="col-md-6 ">'
        '\n\t<div class="sticky-top">'
        '\n\t\t<div style="width:auto;height:720px;overflow:auto;">'
        '\n\t\t\t<div class="card">'
        '\n\t\t\t\t<div class="card-body">'
        '\n\t\t\t\t\t<h4 class="card-title">Weekly Schedule</h4>'
        '\n\t\t\t\t\t\t<div class="table-responsive">'
        '\n\t\t\t\t\t\t\t<table class="table table-light table-bordered " id="WeeklySchedule" SUMMARY="This layout table is used to present the weekly course schedule." WIDTH="150%">'
    )

    make_schedule_head()


def make_schedule_head():   # the headings will never change, so it's hard-coded
    f.write(
        '\n\t\t\t\t\t\t\t\t<thead class="thead-light">'
        '\n\t\t\t\t\t\t\t\t\t<tr>'
        '\n\t\t\t\t\t\t\t\t\t\t<th class="ddheader" scope="col">Time</th>'
        '\n\t\t\t\t\t\t\t\t\t\t<th class="ddheader" scope="col">Monday</th>'
        '\n\t\t\t\t\t\t\t\t\t\t<th class="ddheader" scope="col">Tuesday</th>'
        '\n\t\t\t\t\t\t\t\t\t\t<th class="ddheader" scope="col">Wednesday</th>'
        '\n\t\t\t\t\t\t\t\t\t\t<th class="ddheader" scope="col">Thursday</th>'
        '\n\t\t\t\t\t\t\t\t\t\t<th class="ddheader" scope="col">Friday</th>'
        '\n\t\t\t\t\t\t\t\t\t</tr>'
        '\n\t\t\t\t\t\t\t\t</thead>'
    )


day = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
hours = ['8', '9', '10', '11', '12', '1', '2', '3', '4', '5', '6', '7', '8', '9']
am_pm = ['am', 'pm']
one_two = ['1', '2']    # in the weekly schedule, an hour is currently divided into 2 cells (30 min blocks)

day_index = 0
hours_index = 0
am_pm_index = 0
one_two_index = 0


def make_schedule_cells():
    global hours_index, am_pm_index, one_two_index

    for i in range(14):  # starting from 8 am, there will be 14 loops to get to 9 pm

        if i >= 4:  # starting at 12, time goes from am to pm
            am_pm_index = 1

        one_two_index = 0   # need to reset the index since tr id each loop has to start with 1 (index 0)
        f.write(
            '\n\t\t\t\t\t\t\t\t<tr id="' + hours[hours_index] + am_pm[am_pm_index] + one_two[one_two_index] + '">'
            '\n\t\t\t\t\t\t\t\t\t<td rowspan="2" id="' + hours[hours_index] + am_pm[am_pm_index] + '"scope="row">' + hours[hours_index] + am_pm[am_pm_index] + '</td>'
        )
        make_cells_part1()
        f.write('\n\t\t\t\t\t\t\t\t</tr>')

        f.write('\n\t\t\t\t\t\t\t\t<tr id="' + hours[hours_index] + am_pm[am_pm_index] + one_two[one_two_index] + '">')
        make_cells_part2()
        f.write('\n\t\t\t\t\t\t\t\t</tr>')

        hours_index += 1

    f.write('\n\t\t\t\t\t\t</table>')
    end_schedule_rhs()


def make_cells_part1():
    global day_index, hours_index, am_pm_index, one_two_index

    day_index = 0

    for i in range(5):
        f.write('\n\t\t\t\t\t\t\t\t\t<td id="' + hours[hours_index] + am_pm[am_pm_index] + day[day_index] + one_two[one_two_index] + '" class="align-middle"></td>')
        day_index += 1

    one_two_index += 1


def make_cells_part2():
    global day_index, hours_index, am_pm_index, one_two_index

    day_index = 0

    for i in range(5):
        f.write('\n\t\t\t\t\t\t\t\t\t<td id="' + hours[hours_index] + am_pm[am_pm_index] + day[day_index] + one_two[one_two_index] + '" class="align-middle"></td>')
        day_index += 1


def end_schedule_rhs():  # need div tags to end rhs

    f.write(
        '\n\t\t\t\t\t\t\t</div>'
        '\n\t\t\t\t\t\t</div>'
        '\n\t\t\t\t\t</div>'
        '\n\t\t\t\t</div>'
        '\n\t\t\t</div>'
        '\n\t\t</div>'
    )


def end_msg():
    print("\nHTML has been created successfully!")


def close_file():
    f.close()


def run_create_website():
    make_head()
    make_body()
