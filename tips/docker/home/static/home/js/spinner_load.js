
const spinnerBox = document.getElementById('spinner-box')
const dataBox = document.getElementById('data-box')





$.ajax({
	type : 'GET',
	url : '/home/init_model_obj/',
	success : function(response){
    	
    	spinnerBox.classList.add('not-visible')
    	
		
	},
	error: function(error){
		console.log(error)
	}

})




$('#id_btn').click(function () {

        // On click, execute the ajax call.
        $.ajax({
            type: "POST",
            url : '/home/init_model_obj/',
            dataType: 'json',
            beforeSend: function () { // Before we send the request, remove the .hidden class from the spinner and default to inline-block.
               
                $('#data-box').removeClass('not-visible')
                $('#spinner-box').addClass('not-visible')
            },
            success: function (data) {
                // On Success, build our rich list up and append it to the #richList div.
                console.log(data)
            },
            complete: function () { // Set our complete callback, adding the .hidden class and hiding the spinner.
                $('#data-box').addClass('not-visible')
                $('#spinner-box').removeClass('not-visible')
                
            },
        });
    });
    



    