//  Set Firebase configuration and connection
var config = {
  //apiKey: "AIzaSyDW_zxokh1ym0nt_tecML6UitIFX-XYfzI",
  //authDomain: "iot-rpi-312d3.firebaseapp.com",
  databaseURL: //"https://iot-rpi-312d3-default-rtdb.firebaseio.com",
  "https://appdata-b53a0-default-rtdb.firebaseio.com",
  //storageBucket: "iot-rpi-312d3.appspot.com"
};
my_node = "shunt"

//  Initialize and Connect to Database
firebase.initializeApp(config);

//  Create new entry point into DB
const dbRef1 = firebase.database().ref(my_node + "/");

// Add "listener" to DB, updates id in the HTML (index.html)
// file when DB value is changed
//  Listen for any change in the entry point and update 
dbRef1.on('value', function(snapshot){
    if(snapshot.exists()){
        var content = '';
        $('#table').html(content); 
        snapshot.forEach(function(data){
            var val = data.val();
            var childKey = data.key;
            content +='<tr>';
            content += "<td class='tbl'>" + childKey + '</td>';
            content += '<td>' + "<input type='text' class='ipt' id= '" + childKey + "' value=" + val + " >" + '</td>';
            content += '<td>' + "<input type='button'  class='btn' value='Delete' class='delete' onclick=\"delete_row('" + childKey + "')\">" + '</td>';
            content += '<td>' + "<input type='button'  class='btn' value='Update' class='update' onclick=\"update_row('"+childKey+"')\">" + '</td>';
            content += '</tr>';
        });
        //$('#main').append(content);
        $('#table').html(content); 
        //humidityType.innerHTML= content;
    }
});

// Replaces entire child node with specified tags/data
function setDB() {
  dbRef1.set({
    temp: document.getElementById("temp").value,
    pressure: document.getElementById("pressure").value
  });
  document.getElementById("temp").value = "";
  document.getElementById("pressure").value = "";
  document.getElementById("temp").focus();
}

// Creates new key (scavenger hunt item) with value "no"
function new_item_db() {
  new_item = document.getElementById("New Item").value;
  //$('#new_item').html(new_item); 
  if (new_item != "") {
    dbRef1.child(new_item).set("no");
  }
}

// Updates specified tags in node with specified data
function update_row(key) {
  new_value = document.getElementById(key).value;
  updates = {[key]: new_value};
  dbRef1.update(updates);

}

// Updates specified tags in node with specified data
function delete_row(key) {
      console.log(key);
      dbRef1.child(key).remove();
}

// Deletes data at key
function delete_row_key(key) {
      database.child(key).remove();
}
