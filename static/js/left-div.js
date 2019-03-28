/*
 * Functions used to build HTML elements from JSON in left-box DIV
 */

function assembleTrailDIV(trail) {
    // For attribute in trail object, create a <p> and append it to trail DIV.
    let trailEl = document.createElement('div');
    trailEl.className = 'trail';
    for (attr in trail) {
        let trailAttr = document.createElement('p');
        trailAttr.className = 'trail-attr';
        trailAttr.innerHTML = `<b>${attr}:</b> ${trail[attr]}`;
        //trailAttr.style.display = "none";    Uncomment this to hide trails
        trailEl.append(trailAttr);
    }
    $('#left-box').append(trailEl);
    console.log('Trail appended!');
}

function assembleLeftBox(trails) {
    // TODO: 
    for (trail in trails) {
        assembleTrailDIV(trails[trail]);
    }

}
