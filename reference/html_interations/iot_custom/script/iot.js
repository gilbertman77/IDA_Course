//  Sets Firebase configuration and connection
var config = {
  //apiKey: "AIzaSyDW_zxokh1ym0nt_tecML6UitIFX-XYfzI",
  //authDomain: "iot-rpi-312d3.firebaseapp.com",
  databaseURL: //"https://iot-rpi-312d3-default-rtdb.firebaseio.com",
  "https://appdata-b53a0-default-rtdb.firebaseio.com",
  //storageBucket: "iot-rpi-312d3.appspot.com"
};
my_node = "iot"

//  Initialize and Connect to Database
firebase.initializeApp(config);

// Set entry point in database, this is the root
var database = firebase.database().ref();

var gauge1 = new JustGage({
    id:"gauge1",// required
});
var gauge2 = new JustGage({
    id:"gauge2",// required
});
var gauge3 = new JustGage({
    id:"gauge3",// required
});

// Creates variables for index.html id elements
const tempType = document.getElementById('tempType'); 
const pressureType = document.getElementById('pressureType');  
const humidityType = document.getElementById('humidityType'); 
const xType = document.getElementById('xType');
const yType = document.getElementById('yType'); 
const zType = document.getElementById('zType');
const message = document.getElementById('messageType');

const message_on = document.getElementById('messageOn');
const message_mode = document.getElementById('messageMode');
const message_units = document.getElementById('messageUnits');

//  Create new entry point into DB
const dbRef1 = firebase.database().ref(my_node + "/");
// Add "listener" to DB, updates id in the HTML (index.html)
// file when DB value is changed
//  Listen for any change in the entry point and update pressure/temp
dbRef1.on('value', snap => {

  //  Set web elements to new x, y, z, msg values
  xType.innerHTML = snap.val().x;
  yType.innerHTML = snap.val().y;
  zType.innerHTML = snap.val().z;
  messageType.innerHTML = snap.val().message;

  //  Put DB values in variables since we will modify/use
  this_temp = snap.val().temp;
  this_press = snap.val().pressure;
  this_hum = snap.val().humidity;

  //  Set checkbox depending on status
  messageOn.checked = snap.val().message_on;
  
  //  Set checkbox depending on mode
  if (snap.val().message_mode == "msg")
    messageMode.checked = true;
  else  
    messageMode.checked = false;
  
  // Conversion, set checkbox depending on units, update new data
  humidityType.innerHTML = this_hum + " %";
  if (snap.val().message_units == "metric") {
    messageUnits.checked = true;
    pressureType.innerHTML = (this_press * 0.000986923).toFixed(3)  + " ATM";
    tempType.innerHTML = ((this_temp * 9/5) + 32).toFixed(2) + " F";
  } else {
    pressureType.innerHTML = this_press  + " mbar";
    tempType.innerHTML = this_temp + " C";    
    messageUnits.checked = false;
  }

  //  Refresh gauge values
  gauge1.refresh(this_temp, 212, -50, "Temp");
  gauge2.refresh(this_press, 1200, 800, "Pressure");
  gauge3.refresh(this_hum, 100, 0, "Humidity");
});

// Replaces entire child node with specified tags/data
function setDB() {
  database.child(my_node).set({
    temp: document.getElementById("temp").value,
    pressure: document.getElementById("pressure").value
  });
  document.getElementById("temp").value = "";
  document.getElementById("pressure").value = "";
  document.getElementById("temp").focus();
}

// Updates specified tags in node with specified data
function updateMessage() {
  database.child(my_node).update({
    message: document.getElementById("message").value
  });
  document.getElementById("message").value = "",
  document.getElementById("message").focus();
}

// Updates specified tags in node with specified data
function updateMessageOn() {
  database.child(my_node).update({
    message_on: messageOn.checked
  });
}

// Updates specified tags in node with specified data
function updateMessageMode() {
  var my_mode = "env";
  if (messageMode.checked)
    my_mode = "msg";
  database.child(my_node).update({
    message_mode: my_mode
  });
}

// Updates specified tags in node with specified data
function updateMessageUnits() {
  var my_units = "standard";
  if (messageUnits.checked)
    my_units = "metric";
  database.child(my_node).update({
      message_units: my_units
  });
}

//  Print temp to console whenever script is first run
var myTemp = firebase.database().ref(my_node + '/temp');
myTemp.on('value', (snapshot) => {
  const data = snapshot.val();
  console.log(snapshot.val());
});

/*
//  Returns the data in the specifed node and prints to console
function showDB() {
  return firebase.database().ref('/appdata').once('value').then((snapshot) => {
    console.log(snapshot.val());
    console.log(snapshot.val().temp);
    console.log(snapshot.val().pressure);
    // ...
  });
}
showDB()
*/

/*
function readUserData( 
  dbRef.get().then((snapshot) => {
    if (snapshot.exists()) {
      console.log(snapshot.val());
    } else {
      console.log("No data available");
    }
  }).catch((error) => {
    console.error(error);
  });
)
*/


