/**
 * Sets Firebase configuration and connection
 * Note:  Since our database is "public" we only 
 * need the "databaseURL".  Other parameters would be
 * required if authenication was active
 */
var config = {
  apiKey: "",
  authDomain: "",
  databaseURL: "https://appdata-b53a0-default-rtdb.firebaseio.com",
  storageBucket: ""
};

// Get node for entry point to the database
my_node = "iot"

//  Initialize and Connect to Database
firebase.initializeApp(config);

//  Create entry point into DB at specified node
const dbRef1 = firebase.database().ref(my_node + "/");

//  Create gauge
var humidity_gauge = new JustGage({
  id: "humidity_gauge",// required
  value: 0,
  min: 0,
  max: 100,
  label: "Humidity"
});



/**
 * Adds "listener" to DB at dbRef1 node, 
 * updates "id" elements in the HTML (index.html)
 * file when DB value is changed
 */
dbRef1.on('value', function(snapshot) {
  if (snapshot.exists()) {
    //  Set web elements to new x, y, z, msg, humidity values
    document.getElementById('x').innerHTML = snapshot.val().x;
    document.getElementById('y').innerHTML = snapshot.val().y;
    document.getElementById('z').innerHTML = snapshot.val().z;
    document.getElementById('message').innerHTML = snapshot.val().message;
    document.getElementById('humidity').innerHTML = snapshot.val().humidity + "%";

    //  Get temp/pressure data since we might need to change it.
    my_temp = snapshot.val().temp;
    my_pressure = snapshot.val().pressure;

    // Set check boxes
    messageOn.checked = snapshot.val().message_on;

    // If message mode is "msg", set checked to true, else false
    if (snapshot.val().message_mode == "msg")
      messageMode.checked = true;
    else
      messageMode.checked = false;

    //  If units is metric do conversion, add units, set checkbox if metric
    if (snapshot.val().message_units == "metric") {
      messageUnits.checked = true;
      my_pressure = (my_pressure * 0.000986923).toFixed(3) + " ATM";
      my_temp = ((my_temp * 9 / 5) + 32).toFixed(1) + "&degF";
    } else {
      messageUnits.checked = false;
      my_pressure = my_pressure + " mbar";
      my_temp = my_temp.toFixed(1) + "&degC";
    }

    //  Update "temp" and "pressure"  HTML references with unit info
    document.getElementById('temp').innerHTML = my_temp;
    document.getElementById('pressure').innerHTML = my_pressure;
  }

  //  Refresh gauge values
  humidity_gauge.refresh(snapshot.val().humidity);
});

/**
 * Updates Firebase "message" to text in "textarea" element
 * when "Update Message to Firebase" button clicked
 */
function updateMessage() {
  dbRef1.update({
    message: document.getElementById("user_message").value
  });
  document.getElementById("user_message").value = "";
}


/**
 * Updates message_on to True/False in coordination "Display On" checkbox
 */
function updateMessageOn() {
  dbRef1.update({
    message_on: messageOn.checked
  });
}

/**
 * Updates Firebase "message_mode" key to "env" or "msg"
 * in coordination "Display Message" checkbox
 */
function updateMessageMode() {
  var my_mode = "env";
  if (messageMode.checked)
    my_mode = "msg";
  dbRef1.update({
    message_mode: my_mode
  });
}

/**
 * Updates Firebase "message_units" key to "standard" or "metric"
 * in coordination "Display Metric" checkbox
 */
function updateMessageUnits() {
  var my_units = "standard";
  if (messageUnits.checked)
    my_units = "metric";
  dbRef1.update({
    message_units: my_units
  });
}
