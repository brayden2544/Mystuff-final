// this is just an example of placing Javascript in the app
// $('#site_header').text("Hello from base.js (this is JS example)!");

$(document).ready(function() {
	$('#login_button').off('click.login').on('click.login', function() {
		$('#login_button').loadmodal({
			id: 'login_modal',
			title: 'Login to MyStuff',
			url: '/account/login/',
		}); //load modal
	});//click	
}); //ready