count=0;
const count_list =[]
function my(){
    a=count++;
    count_list.push(a);
    DEBIT = document.createElement('input');
    DEBIT.setAttribute("type", 'text');
    DEBIT.setAttribute("class", 'text');
    DEBIT.setAttribute("id", +count+'debit');
    DEBIT.setAttribute("onkeypress", 'myFunction1(event)');
    CREDIT = document.createElement('input');
    CREDIT.setAttribute("type", 'text');
    CREDIT.setAttribute("id", +count+'credit');
    
    var slect = document.getElementById("add-row");
    option = slect.options[slect.selectedIndex].value;

    var tbodyRef = document.getElementById('mytable');

    // Insert a row at the end of table
    var newRow = tbodyRef.insertRow(1);

    // Insert a cell at the end of the row
    var newCell = newRow.insertCell(0);
    var newCell1 = newRow.insertCell(1).appendChild(DEBIT);
    var newCell2 = newRow.insertCell(2).appendChild(CREDIT);
    var newCell3 = newRow.insertCell(3);
    var newCell4 = newRow.insertCell(4);

    newCell.innerHTML = option;

}
function get_id() {
    document.getElementById
    
}

function myFunction1(event) {
    console.log(this)
    
    a=event.currentTarget.id
    const a=a.slice(0)
    for(i in count_list){
        if (a==i) {
            document.getElementById(+i+'credit').disabled=true;
        }
      
        
       
    }
}
function myFunction2() {
    document.getElementById("myBtn1").disabled = true;
}








