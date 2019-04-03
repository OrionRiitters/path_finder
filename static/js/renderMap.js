
function getLat(trail) {
    return parseFloat(trail['latitude']);
}

function getLon(trail) {
    return parseFloat(trail['longitude']);
}

function findCenter(trails) {
    // Create placeholders for cardinal directions
    t = trails[0];

    n = getLat(t);
    e = getLon(t);
    s = getLat(t);
    w = getLon(t);

    // Find outtermost latitude and longitude in each direction, return midpoint
    for (trail in trails) {
        lat = getLat(trails[trail]);
        lon = getLon(trails[trail]);

        n = lat > n ? lat : n;
        e = lon > e ? lon : e;
        s = lat < s ? lat : s;
        w = lon < w ? lon : w;
    }

    midLat = (n + s) / 2;
    midLon = (e + w) / 2;

    return [midLat, midLon];
}

function addDIV() {
    // If a map aready exists, remove it. Add new map to right-box DIV.
    $('#right-box').empty();
    let mapDIV = document.createElement('div');
    mapDIV.setAttribute('id', 'map');
    $('#right-box').append(mapDIV);
}

function renderMap(trails) {
    addDIV();
    var mymap = L.map('map').setView(findCenter(trails), 9);
    L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox.streets',
    accessToken: 'pk.eyJ1Ijoibm9pcm9yaW9uIiwiYSI6ImNqczVhc3U0NzBkdGEzeXBicHlkZ24zNnEifQ.HvhsssPH_dHgAciNbU40tA'
    }).addTo(mymap);

    for (trail in trails) {
        lat = trails[trail]['latitude'];
        lon = trails[trail]['longitude'];

        // 
        let marker = L.marker([lat, lon]).addTo(mymap)
            .on('click', function(e) {
                // Find marker based on latitude
                trailEl = document.querySelector(`div[latitude='lat${e["target"]["_latlng"]["lat"]}']`);
                // Hide all trail elements, show only selected trail.
                hideMostTrails(trailEl);
        });
    }
}

/*
 * This function hides all of the trails in the left-box DIV. Then the function changes the "display"
 * value of the trailEl argument.
 */
function hideMostTrails(trailEl) {
    trails = document.getElementsByClassName('trail');
    for (i = 0; i < trails.length; i++) {
        trails[i].style.display = 'none';
    }
    trailEl.style.display = '';
}
