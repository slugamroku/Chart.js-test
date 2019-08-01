var time = []
var temperature = [];
	
var xmlhttp = new XMLHttpRequest();
xmlhttp.onreadystatechange = function() {
  if (this.readyState == 4 && this.status == 200) {
    var myObj = JSON.parse(this.responseText);
    //document.getElementById("demo").innerHTML = myObj[0];
	
	var len = myObj.length;

	for (i = 0; i < len; i++){
		time[i] = myObj[i][0];
		temperature[i] = myObj[i][1];
	}
//	document.getElementById("demo").innerHTML = temperature[0];

  }
};
xmlhttp.open("GET", "data.json", true);
xmlhttp.send(); 

let data = {
        labels: time,
        datasets: [
            {
                label: "Temperature",
                data: temperature
            }
        ]
    };

    let options = {};
    let ctx = document.getElementById("myChart").getContext("2d");
    let myLineChart = new Chart(ctx, {
        type: 'line',
        data: data,
        options: options
    });