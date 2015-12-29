/* Product page: Quotation */
$.fn.rate_me = function() {

	// 1. User presses submit button
	$('#submit-rating').click(function(e){

		e.preventDefault();

		var dict = {};

		$('#rating-form :input[type=custom]').each(function(){

			console.log('jeej');

			if($(this).val() == 0) {
				console.log('tis nul!');
			}

			dict[$(this).attr('name')] = $(this).val();

			/*dict.push({
				key: $(this).attr('name'),
				value: $(this).val()
			});*/
		});	

		console.log(dict);

		
		console.log('submit button pressed!')

		// 2. Check values
		eerste = $('#input-1').val();
		tweede = $('#input-2').val();

		console.log(eerste + '--' + tweede)

	});
};