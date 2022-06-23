// Set Firebase configuration and connection
var config = {
  apiKey: "",
  authDomain: "",
  databaseURL: "https://appdata-b53a0-default-rtdb.firebaseio.com/",
  storageBucket: ""
};
my_node = "shunt"

//  Initialize and Connect to Database
firebase.initializeApp(config);

//  Create new entry point into DB
const dbRef1 = firebase.database().ref(my_node + "/");

// Creates new key (scavenger hunt item) with value "no"
function new_item_db() {
  new_item = document.getElementById("New Item").value;
  if (new_item != "") {
    dbRef1.child(new_item).set("no");
  }
  document.getElementById("New Item").value = "";
}

// Add "listener" to DB, updates id in the HTML (index.html)
// file when DB value is changed
// Listen for any change in the entry point and update 
dbRef1.on('value', function(snapshot){
    if(snapshot.exists()){
        var content = "<table>";
        //content += "<tr><th>Item</th> <th>Status</th> <th>Delete</th> <th>Update</th></tr>";
        $('#js-table').html(content); 
        snapshot.forEach(function(data){
            var val = data.val(); // Status
            var item = data.key;  // Item
            content +='<tr>';    // Start row
            content += "<td>" + item + '</td>';   // Col1
            //content += "<td>" + val + '</td>';    // Col2
            content += '<td>' + "<input type='text' id= '" + item + "' value=" + val + " >" + '</td>';
            content += '<td>' + "<input type='button'  class='button' value='Delete' class='delete' onclick=\"delete_row('" + item + "')\">" + '</td>';
            content += '<td>' + "<input type='button'  class='button' value='Update' class='update' onclick=\"update_row('" + item + "')\">" + '</td>';
            content += '</tr>';  // End row
        });
        content += '</table>';
        $('#js-table').html(content);
    }
});

// Updates specified tags in node with specified data
function update_row(key) {
  new_value = document.getElementById(key).value;
  updates = {[key]: new_value};
  dbRef1.update(updates);
}

// Updates specified tags in node with specified data
function delete_row(key) {
      dbRef1.child(key).remove();
}