function checkEmpty() {
	if (document.getElementById('distance').value == "") {
		alert("Please Enter a Distance!");
	} else {
		document.getElementById('form').submit();
		alert("Calculating a Random Route!");
	}
}