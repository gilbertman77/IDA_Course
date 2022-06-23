$(document).ready(function() {
	var config = {
		//apiKey: 'AIzaSyDRrJC4cQsSynNZUgzNKIOrOdkrBbxJj9c',
    //apiKey: "AIzaSyDW_zxokh1ym0nt_tecML6UitIFX-XYfzI",
		
    //authDomain: 'idk-what-im-doing-here.firebaseapp.com',
		//authDomain: "iot-rpi-312d3.firebaseapp.com/AppData/",
    
    //databaseURL: 'https://idk-what-im-doing-here.firebaseio.com',
		databaseURL: "https://iot-rpi-312d3-default-rtdb.firebaseio.com",
    
    //projectId: 'idk-what-im-doing-here',
		//projectId: "iot-rpi-312d3",
    
    //storageBucket: 'idk-what-im-doing-here.appspot.com',
		//storageBucket: "iot-rpi-312d3.appspot.com",
    //storageBucket: "AppData",
    
    //messagingSenderId: '149620805248',
    //messagingSenderId: "391683313751",
    
    appId: "1:391683313751:web:d28f155770ac98fb78d312"

	};
	firebase.initializeApp(config);

	var guestBook = firebase.database().ref();
/*
	guestBook.on('child_added', function(guest) {
		if (
			guest.hasOwnProperty('node_') &&
			guest.node_.hasOwnProperty('children_') &&
			guest.node_.children_.hasOwnProperty('root_') &&
			guest.node_.children_.root_.hasOwnProperty('value') &&
			guest.node_.children_.root_.value.hasOwnProperty('value_') &&
			guest.hasOwnProperty('node_') &&
			guest.node_.hasOwnProperty('children_') &&
			guest.node_.children_.hasOwnProperty('root_') &&
			guest.node_.children_.root_.hasOwnProperty('left') &&
			guest.node_.children_.root_.left.value.hasOwnProperty('value_')
		) {
			signGuestbook(
				guest.node_.children_.root_.value.value_,
				guest.node_.children_.root_.left.value.value_
			);
		}
	});
*/
	$('#appData').submit(function(event) {
		event.preventDefault();
		// Add guest to guestbook
		guestBook.set({
			name: $('#temp').val(),
			comment: $('#pressure').val(),
		});
		$("#temp").val("");
		$("#pressure").val("");
		$("#temp").focus();
	});


/*
	function signGuestbook(name, comment) {
		//$('#comments').append('<p><b>' + XSSSanitize(name) + '</b><br/>' + XSSSanitize(comment) + '</p>');
		const e = document.createElement('p')
		e.textContent = comment

		const e2 = document.createElement('p')
		const e3 = document.createElement('b')
		e3.textContent = name
		e2.appendChild(e3)

		document.getElementById('comments').appendChild(e2);
		document.getElementById('comments').appendChild(e);
	}
*/


/*
	function XSSSanitize(str) {
        let output = '';
        const ruhroh = {
            '&': '&amp;',
            '<': '&lt;',
            '>': '&gt;',
            '"': '&quot;',
            "'": '&#x27;',
            '/': '&#x2F;',
        };
        for (var i = 0; i < str.length; i++) {
            if (ruhroh[str.charAt(i)]) {
                console.log(str.charAt(i))
                output += ruhroh[str.charAt(i)];
            } else {
                output += str.charAt(i);
            }
        }
        return output;
    }

*/
});


