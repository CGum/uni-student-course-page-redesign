
$(document).ready(function(){

    $('#other-options').click(function(){
        $('.menu-item').addClass('hide-item')
        $('.menu2').addClass('active')
        $('.close').addClass('active')
        $('.fa-user').hide()
    });

    $('.close').click(function(){
        $('.menu-item').removeClass('hide-item')
        $('.menu2').removeClass('active')
        $('.close').removeClass('active')
        $('.fa-user').show()

    });

    $('#theAccordion').mouseup(function(){  // hide an alert when mouse is clicked again (this is just a visual improvement)
      $(".alert").hide();
    });

})

function getRadioButtonID(){  // get id from the radio button
    var btnid = $('input[name=radSize]:checked').attr('id');
    return btnid
}

function getCRNArray(){

    string = getRadioButtonID(); // get the CRN value of the class selected
    var coursesSelected = string.split(" "); // splitting the values just incase more than one value is selected
                                             // in Version1 a string was provided

    for(var i=0; i<coursesSelected.length; i++){
        coursesSelected[i] = parseInt(coursesSelected[i])-10000; // converting to index values
    }

    var coursesDetails = new Array();

    for(var i=0; i<coursesSelected.length; i++){
        coursesDetails.push(courseList[parseInt(coursesSelected[i])]); // getting the string based on the index from courseList[]
        findingColumn(coursesDetails[i]);
    }
}

var isCollisontrue;

function findingColumn(string){
    // string ~ 10001   ANTH      102      A1     MW      11:30am-12:50pm
    //           CRN  Department Course#  A/L/T   Days      Time
    //            0     1         2        3       4         5

    // splitting string just like the example above
    var infoString = string.split(' ');

    // string of days
    var days = infoString[4];
    // id of cell => # + time + am||pm + day + 1||2
    // idString =>       time  + am||pm
    var idString = parseInt(infoString[5].substring(0,2)) + infoString[5].substring(5,7);

    // a variable to hold if the cell in consideration has 1 or 2 at the end
    var cell1or2;

    // Time string
    infoString[5] = infoString[5] +" ";

    // getting number of cells the class takes
    // e.g if it is a 50min long class it will take 2 cells but if it's 2hrs and 50 mins it will take 6 cells
    var numberOfCells = parseInt(getNumberOfCellsMinusTop(infoString[5]));


    if(days.includes("M") && !isCollisontrue){
        // idString2 is the local version of idString to find the starting cell of the class
        var idString2 = "#" + idString + "Monday";

        // if the class selected is like:
        // xx:30am then it will take cell ending in 2
        // xx:00am then it will take cell ending in 1
        if(infoString[5].charAt(3).includes('0')){
            idString2 = idString2.concat("1");
            cell1or2 = 1;
        }else{
            idString2 = idString2.concat("2");
            cell1or2 = 2;
        }

        // check if the cells needed are already occupied or not
        isCollisontrue = !isPossible(numberOfCells, idString2, infoString[5], cell1or2, "Monday");

    }

    if(days.includes("T") && !isCollisontrue){
        var idString2 = "#" + idString + "Tuesday";
        if(infoString[5].charAt(3).includes('0')){
            idString2 = idString2.concat("1");
            cell1or2 = 1;
        }else{
            idString2 = idString2.concat("2");
            cell1or2 = 2;
        }
        isCollisontrue = !isPossible(numberOfCells, idString2, infoString[5], cell1or2, "Tuesday");
    }

    if(days.includes("W") && !isCollisontrue){
        var idString2 = "#" + idString + "Wednesday" ;
        if(infoString[5].charAt(3).includes('0')){
            idString2 = idString2.concat("1");
            cell1or2 = 1;
        }else{
            idString2 = idString2.concat("2");
            cell1or2 = 2;
        }
        isCollisontrue = !isPossible(numberOfCells, idString2, infoString[5], cell1or2, "Wednesday");
    }

    if(days.includes("R") && !isCollisontrue){
        var idString2 = "#" + idString + "Thursday" ;
        if(infoString[5].charAt(3).includes('0')){
            idString2 = idString2.concat("1");
            cell1or2 = 1;
        }else{
            idString2 = idString2.concat("2");
            cell1or2 = 2;
        }
        isCollisontrue = !isPossible(numberOfCells, idString2, infoString[5], cell1or2, "Thursday");
    }

    if(days.includes("F") && !isCollisontrue){
        var idString2 = "#" + idString + "Friday";

        if(infoString[5].charAt(3).includes('0')){
            idString2 = idString2.concat("1");
            cell1or2 = 1;
        }else{
            idString2 = idString2.concat("2");
            cell1or2 = 2;
        }
        isCollisontrue = !isPossible(numberOfCells, idString2, infoString[5], cell1or2, "Friday");
    }

    if(!isCollisontrue){

        if(days.includes("M") && !isCollisontrue){
            var idString2 = "#" + idString + "Monday" ;

            //$$$08:30am-11:20am $$$10144 COMM 420 A1 M 08:30am-11:20am
            if(infoString[5].charAt(3).includes('0')){
                idString2 = idString2.concat("1");
                cell1or2 = 1;
            }else{
                idString2 = idString2.concat("2");
                cell1or2 = 2;
            }

            createCellId(infoString[5], "Monday", string, idString2, cell1or2, numberOfCells)
        }

        if(days.includes("T") && !isCollisontrue){
            var idString2 = "#" + idString + "Tuesday" ;
            if(infoString[5].charAt(3).includes('0')){
                idString2 = idString2.concat("1");
                cell1or2 = 1;
            }else{
                idString2 = idString2.concat("2");
                cell1or2 = 2;
            }
            createCellId(infoString[5], "Tuesday", string, idString2, cell1or2, numberOfCells)
        }

        if(days.includes("W") && !isCollisontrue){
            var idString2 = "#" + idString + "Wednesday" ;
            if(infoString[5].charAt(3).includes('0')){
                idString2 = idString2.concat("1");
                cell1or2 = 1;
            }else{
                idString2 = idString2.concat("2");
                cell1or2 = 2;
            }
            createCellId(infoString[5], "Wednesday", string, idString2, cell1or2, numberOfCells)
        }

        if(days.includes("R") && !isCollisontrue){
            var idString2 = "#" + idString + "Thursday" ;
            if(infoString[5].charAt(3).includes('0')){
                idString2 = idString2.concat("1");
                cell1or2 = 1;
            }else{
                idString2 = idString2.concat("2");
                cell1or2 = 2;
            }
            createCellId(infoString[5], "Thursday", string, idString2, cell1or2, numberOfCells)
        }

        if(days.includes("F") && !isCollisontrue){
            var idString2 = "#" + idString + "Friday" ;
            if(infoString[5].charAt(3).includes('0')){
                idString2 = idString2.concat("1");
                cell1or2 = 1;
            }else{
                idString2 = idString2.concat("2");
                cell1or2 = 2;
            }
            createCellId(infoString[5], "Friday", string, idString2, cell1or2, numberOfCells)
        }
    }else{
        $('.alert-danger').show();
        window.setTimeout(function () { // makes the alert go away on its own
            $(".alert-danger").hide(); }, 4000);
    }

    isCollisontrue = false;
}

function createCellId(string, day, courseString, idString, cell1or2, numberOfCells) {
    // string           day       courseString                          idString         cell1or2    numberOfCells
    // 06:00pm-08:50pm $Thursday  $10147 COMM 433 A1 R 06:00pm-08:50pm  $#6pmThursday1   $1         $6
    // 08:30am-11:20am $Monday$10144 COMM 420 A1 M 08:30am-11:20am$#8amMonday1$1$6
    //alert(string+"$"+ day+"$"+ courseString+"$"+ idString+"$"+ cell1or2+"$"+ numberOfCells);
    $('.alert-success').show();
    window.setTimeout(function () { // makes the alert go away on its own
        $(".alert-success").hide(); }, 1500);


    $(idString).attr('rowspan',parseInt(numberOfCells));
    //     document.getElementById(idString).innerHTML = "iukj"+courseString;
    $(idString).html(courseString);

    var time = parseInt(string.substring(0,2));

    for(var i = 0; i < numberOfCells - 1; i++){
        if(cell1or2 == 1){
            cell1or2 = 2;
        }else{
            cell1or2 = 1;
            time = time + 1;
            if(time == 13){
                time = 1;
            }
        }

        var idDelete = "#" + time + string.substring(13,15) + day + cell1or2;

        str = idDelete;
        $(str).remove();
    }
}

function getNumberOfCellsMinusTop(string){

    var hr1 = parseInt(string.substring(0,2)),
        hr2 = parseInt(string.substring(8,10)),
        min1= parseInt(string.substring(3,5)),
        min2= parseInt(string.substring(11,13));
    var temp1 = string.substring(5,6);


    if(temp1.includes("p")){
        hr1 = hr1 + 12;
    }

    temp2 =string.substring(13,14);

    if(temp2.includes("p") && hr2 != 12){
        hr2 = hr2 + 12;
    }

    var extra;

    if((min2-min1) == 20){
        extra = 1;
    }else if(min2-min1 == 50){
        extra = 2;
    }else{
        extra = 0;
    }

    var cellsRequired = (hr2-hr1)*2 + extra;
    return cellsRequired;
}

function isPossible(numberOfCells1, idString1, string1, cell1or22, day ){

    var isPossibleBoolean = true;
    var time = parseInt(string1.substring(0,2));

    if(time == 8 ||time == 9 ||time == 10 ||time == 11){
        string1 = string1.substring(0,13) + "am";
    }

    if($(idString1).length == 0){
        isPossibleBoolean = false;
    }

    var cell1or2 = parseInt(cell1or22);

    for(var i = 0; i < numberOfCells1 && isPossibleBoolean ; i++){
        if(cell1or2 == 1){
            cell1or2 = 2;
        }else{
            cell1or2 = 1;
            time = time + 1;
            if(time == 12){
                string1 = string1.substring(0,13) + "pm";
            }
            if(time == 13){
                time = 1;
            }
        }

        var idDelete = "#" + time + string1.substring(13,15) + day + cell1or2;
        var str = idDelete;

        if($(str).length == 0){
            isPossibleBoolean = false;
        }
    }
    //alert('isPossible:' + isPossibleBoolean + "--"+str+"--"+$(str).length+"--"+$(str).innerText);
    return isPossibleBoolean;
}

// Delete Function

var isDeleted = false;

function getCRNDelete(){
    //string = document.getElementById('DeleteClass').value;

    string = getRadioButtonID();

    string = courseList[string - 10000];

    // string ~ 10001   ANTH      102      A1     MW      11:30am-12:50pm
    //           CRN  Department Course#  A/L/T   Days      Time
    //            0     1         2        3       4         5
    var infoString = string.split(' ');
    var days = infoString[4]; // contain days
    var idString = "#" + parseInt(infoString[5].substring(0,2)) + infoString[5].substring(5,7); // #11am
    var cell1or2;


    if( parseInt(infoString[5].substring(3,5))==0 ){
        cell1or2 = 1;
    }else{
        cell1or2 = 2;
    }

    if(days.includes("M")){
        var localIdString = idString + "Monday" + cell1or2;
        var currentValueInCell = $(localIdString).text();
        var currentCRNInCell = currentValueInCell.split(' ');
        currentCRNInCell = currentCRNInCell[0];

        if( currentCRNInCell == infoString[0] ){

            $(localIdString).text("");
            $(localIdString).attr('rowspan',1);     // turn the rowspan from # to 1
            $(localIdString).length = 1;
            addCells(infoString, cell1or2, "Monday");
            isDeleted = true;
        }
    }

    if(days.includes("T")){

        var localIdString = idString + "Tuesday" + cell1or2;
        var currentValueInCell = $(localIdString).text();
        var currentCRNInCell = currentValueInCell.split(' ');
        currentCRNInCell = currentCRNInCell[0];


        if( currentCRNInCell == infoString[0] ){

            $(localIdString).text("");
            $(localIdString).attr('rowspan',1);     // turn the rowspan from # to 1
            addCells(infoString, cell1or2, "Tuesday");
            isDeleted = true;
        }
    }

    if(days.includes("W")){

        var localIdString = idString + "Wednesday" + cell1or2;
        var currentValueInCell = $(localIdString).text();
        var currentCRNInCell = currentValueInCell.split(' ');
        currentCRNInCell = currentCRNInCell[0];

        if( currentCRNInCell == infoString[0] ){
            $(localIdString).text("");
            $(localIdString).attr('rowspan',1);     // turn the rowspan from # to 1
            addCells(infoString, cell1or2, "Wednesday");
            isDeleted = true;
        }
    }


    if(days.includes("R")){
        var localIdString = idString + "Thursday" + cell1or2;
        var currentValueInCell = $(localIdString).text();
        var currentCRNInCell = currentValueInCell.split(' ');
        currentCRNInCell = currentCRNInCell[0];

        if( currentCRNInCell == infoString[0] ){

            $(localIdString).text("");
            $(localIdString).attr('rowspan',1);     // turn the rowspan from # to 1
            addCells(infoString, cell1or2, "Thursday");
            isDeleted = true;
        }
    }

    if(days.includes("F")){
        var localIdString = idString + "Friday" + cell1or2;
        var currentValueInCell = $(localIdString).text();
        var currentCRNInCell = currentValueInCell.split(' ');
        currentCRNInCell = currentCRNInCell[0];

        if( currentCRNInCell == infoString[0] ){

            $(localIdString).text("");
            $(localIdString).attr('rowspan',1);     // turn the rowspan from # to 1
            addCells(infoString, cell1or2, "Friday");
            isDeleted = true;
        }
    }

    if(isDeleted){
      $('.remove-success').show();
      window.setTimeout(function () { // makes the alert go away on its own
          $(".remove-success").hide(); }, 1500);
    } else{
      $('.remove-error').show();
      window.setTimeout(function () { // makes the alert go away on its own
          $(".remove-error").hide(); }, 4000);
    }

    isDeleted = false

}

function addCells(infoString, cell1or2, day){

    var string1 = infoString[5];

    var numberOfCells = parseInt(getNumberOfCellsMinusTop(infoString[5]));  // number of cells ot took

    var time = parseInt(infoString[5].substring(0,2));  // time to start from

    if(time == 8 ||time == 9 ||time == 10 ||time == 11){
        string1 = string1.substring(0,13) + "am";
    }

    for(var i = 0; i < numberOfCells - 1; i++){
        if(cell1or2 == 1){
            cell1or2 = 2;
        }else{
            cell1or2 = 1;
            time = time + 1;
            if(time == 12){
                string1 = string1.substring(0,13) + "pm";
            }
            if(time == 13){
                time = 1;
            }
        }

        var idAdd = "#" + time + string1.substring(13,15) + day + cell1or2;
        var rowId = time + string1.substring(13,15) + cell1or2;
        var daynumber = 0;

        if(day.includes("Monday")){daynumber = 0;}
        if(day.includes("Tuesday")){daynumber = 1;}
        if(day.includes("Wednesday")){daynumber = 2;}
        if(day.includes("Thursday")){daynumber = 3;}
        if(day.includes("Friday")){daynumber = 4;}

        if(cell1or2==1){
            daynumber = daynumber + 1;
        }

        var rowElement = document.getElementById(rowId);
        var cellElement = rowElement.insertCell(parseInt(daynumber));

        cellElement.id = ""+idAdd.substr(1,idAdd.length);
        cellElement.id.length = 1;
        cellElement.innerHTML = "";

    }
}

var courseList= [
    "removed"
];
