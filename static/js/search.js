/*
 * The event listeners in this file are solely for the 'search' DIV in index.html
 */

$('#find-path').on('click', function() {
    city = $('#city').val();
    state = $('#state').val();
    $.post('/get_trails', {
        city: city,
        state: state
    })   /* Parse JSON and run element assembly functions to prepare left-box.
          * TODO: Create functions to render leaflet map with JSON
          */
        .then(res => {
            trails = JSON.parse(res);
            assembleLeftBox(trails);
            renderMap(trails);
        }
    );
});

$('#saved-trails').on('click', function() {
    $.get('/get_trails')
        .then(res => {
            assembleBucketList(res);
        });
});
