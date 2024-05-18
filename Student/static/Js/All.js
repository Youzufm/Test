function calculate(){
	var hardware=parseInt(document.getElementById('hardware').value);
	var multimedia=parseInt(document.getElementById('multimedia').value);
	var web=parseInt(document.getElementById('web').value);
	var network=parseInt(document.getElementById('network').value);
	var database=parseInt(document.getElementById('database').value);
  var programming=parseInt(document.getElementById('programming').value);
  var book=parseInt(document.getElementById('book').value);
	if (hardware>100 || multimedia>100 || web>100 || network>100 || database>100||programming>100||book>100) {
		alert("Please enter correct value");
	}
	else
	{
		var total=hardware+multimedia+web+network+database+programming+book;
   
		document.getElementById('tot').value=total;
    var avg=total/7;
		document.getElementById("average").value=avg;
	
		if (avg>=95) {
			document.getElementById('grade').value="A+";
		}
		else if (avg>=90) {
			document.getElementById('grade').value="A";
		}
		else if (avg>=85) {
      document.getElementById('grade').value="A-";
		}
		else if (avg>=80) {
      document.getElementById('grade').value="B+";
		}
		else if (avg>=75) {
			document.getElementById('grade').value="B";
		}
    else if (avg>=70) {
			document.getElementById('grade').value="B-";
		}
    else if (avg>=65) {
			document.getElementById('grade').value="C";
		}
    else if (avg>=60) {
			document.getElementById('grade').value="C+";
		}
    else if (avg>=55) {
			document.getElementById('grade').value="C-";
		}
    else if (avg>=50) {
			document.getElementById('grade').value="D";
		}
		else{
			document.getElementById('grade').textContent="F";
		}
	}
	return false;
}


