$(document).ready(function() {
	//Make the form submit via ajax
	$('form').ajaxForm({
		target: '.modal-body',
	});//load Modal
});//ready