/*
 * The event listeners in this file are solely for the 'search' DIV in index.html
 */

$('#find-path').on('click', function() {
    city = $('#city').val();
    state = $('#state').val();
    $.post('/get_trails', {
        city: city,
        state: state
    })   /* Parse JSON and run element assembly functions to prepare left-box. */
        .then(res => {
            trails = JSON.parse(res);
            assembleLeftBox(trails);
            renderMap(trails);
        }
    )
});

/* When "saved trails" button is clicked, run assembleBucketList on the response. */
$('#saved-trails').on('click', function() {
    $.get('/get_trails')
        .then(res => {
            assembleBucketList(res);
        });
});
