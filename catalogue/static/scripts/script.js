var devices;

var request = new XMLHttpRequest();
request.open('GET', 'devices.json');
request.responseType = 'json';
request.onload = function() {
  if(request.status === 200) {
	devices = request.response;
	initialise();
  } else {
	console.log('Network request for devices.json failed with response ' + request.status + ': ' + request.statusText);
  }
}

request.send();

function initialise() {
  var searchTerm = document.querySelector('#searchTerm');
  var searchBtn = document.querySelector('button');
  var main = document.querySelector('main');

  var lastSearch = searchTerm.value;

  var searchResults;

  searchResults = devices;
  updateDisplay();

  searchResults = [];

  searchBtn.onclick = selectDevices;

  function selectDevices() {
	searchResults = [];

	if(searchTerm.value === lastSearch) {
	  return;
	} else {
	  lastSearch = searchTerm.value;
	  if(searchTerm.value === '') {
		searchResults = devices;
		updateDisplay();
	  } else {
	  var lowerCaseSearchTerm = searchTerm.value.toLowerCase();
	  for(var i = 0; i < devices.length; i++) {
		var equipment = devices[i].equipment.toLowerCase();
		var description = devices[i].description.toLowerCase();
		var location = devices[i].location.toLowerCase();
		var email = devices[i].email.toLowerCase();
		if(equipment.indexOf(lowerCaseSearchTerm) !== -1 ||
		   description.indexOf(lowerCaseSearchTerm) !== -1 ||
		   location.indexOf(lowerCaseSearchTerm) !== -1 ||
		   email.indexOf(lowerCaseSearchTerm) !== -1) {
		  searchResults.push(devices[i]);
		}
	  }
	  updateDisplay();
	  }
	}
  }

  function updateDisplay() {
	while (main.firstChild) {
	  main.removeChild(main.firstChild);
	}

	if(searchResults.length === 0) {
	  var para = document.createElement('p');
	  para.setAttribute('id', 'para');
	  para.textContent = 'No results to display!';
	  main.appendChild(para);
	} else {
	  for(var i = 0; i < searchResults.length; i++) {
		fetchJson(searchResults[i]);
	  }
	}
  }

  function fetchJson(device) {
	var request = new XMLHttpRequest();
	request.open('GET', 'devices.json');
	request.responseType = 'json';
	request.onload = function() {
	  if(request.status === 200) {
		var json = request.response;
		showDevice(json, device);
	  } else {
		console.log('Network request for devices.json failed with response ' + request.status + ': ' + request.statusText);
	  }
	}
	request.send();
  }

  function showDevice(json, device) {
	var table = document.createElement('table');
	var row1 = document.createElement('tr');
	var row2 = document.createElement('tr');
	var row3 = document.createElement('tr');
	var row4 = document.createElement('tr');
	var data11 = document.createElement('td');
	var data21 = document.createElement('td');
	var data31 = document.createElement('td');
	var data41 = document.createElement('td');
	var data12 = document.createElement('td');
	var data22 = document.createElement('td');
	var data32 = document.createElement('td');
	var data42 = document.createElement('td');

	data11.setAttribute('class', 'column1');
	data21.setAttribute('class', 'column1');
	data31.setAttribute('class', 'column1');
	data41.setAttribute('class', 'column1');
	data12.setAttribute('class', 'column2');
	data22.setAttribute('class', 'column2');
	data32.setAttribute('class', 'column2');
	data42.setAttribute('class', 'column2');

	data11.setAttribute('id', 'equipment');
	data11.textContent = 'Equipment';
	data21.textContent = 'Description';
	data31.textContent = 'Location';
	data41.textContent = 'Email';
	data12.textContent = device.equipment;
	data22.textContent = device.description;
	data32.textContent = device.location;
	data42.textContent = device.email;

	main.appendChild(table);
	table.appendChild(row1);
	table.appendChild(row2);
	table.appendChild(row3);
	table.appendChild(row4);
	row1.appendChild(data11);
	row1.appendChild(data12);
	row2.appendChild(data21);
	row2.appendChild(data22);
	row3.appendChild(data31);
	row3.appendChild(data32);
	row4.appendChild(data41);
	row4.appendChild(data42);
  }
}