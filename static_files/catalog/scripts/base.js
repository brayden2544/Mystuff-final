// this is just an example of placing Javascript in the app
// $('#site_header').text("Hello from base.js (this is JS example)!");

$(document).ready(function() {
	$('#search_button').off('click.search').on('click.search', function() {
		$('#search_button').loadmodal({
			id: 'search_modal',
			title: 'Search For A Product',
			url: '/catalog/search/',
		}); //load modal
	});//click	
}); //ready