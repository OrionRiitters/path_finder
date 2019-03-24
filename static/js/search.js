$('#find-path').on('click', function() {
    city = $('#city').val();
    state = $('#state').val();
    $.post('/get_trails', {
        city: city,
        state: state
    })
        .then(res => {
            // Call functions to render leaflet map with JSON
        }
    );
});

$('#saved-trails').on('click', function() {
    $.get('/get_trails')
        .then(res => {
            // It seems that rendering a template might be easiest here.
        });
});
