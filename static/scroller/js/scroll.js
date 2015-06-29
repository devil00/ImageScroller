var image_view = {
	init: function() {
	    "use init";
		var images_data;
		var that = this;
		$.ajax({
			url: "/home/",
			contentType: "application/json",
			success: function(response) {
				that.render(response.items);
			},
			error: function(xhr, status, error) {
				console.log(error);
			}
		});
		this.register_events();
	},

	render: function(images) {
		var image_template = $("#images-list").html();
		//$("#container").html(_.template(image_template, {items: images}));
		$("#image-container").html(_.template(image_template)({items: images}));
		$('#vertical').scroller({direction: 'vertical', interval: 8});

		// Register event for delete button.
		$("li button").on('click', function(event) {
			event.preventDefault();
			$(event.target.parentNode.parentNode).remove();
		});

	},

	refresh: function() {
		this.init();
	},

	register_events: function() {
		// Register an event for refresh button.
		var that = this;
		$("#refresh").on('click', function(event){
			event.preventDefault();
			console.log("refresh");
			that.refresh();
		});
	}
}

$(function() {
    image_view.init();
});
