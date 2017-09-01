$(document).ready(function(){
	var $form = $('#say-form');
	var $say_res = $('#say-res');

	$form.on('submit', function(event){
		event.preventDefault();
		var form = this;

		$.ajax({
			url: '/deaf/',
			method: 'POST',
			data: $(this).serialize(),
			success: function(data){
				console.log('server data:\n', data);
				form.reset();
				// $say_res.prepend('<br>'+data['said']+' | ' +data['say']);

				$say_res.html(data);
			}
		});
	});
});
