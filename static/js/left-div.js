/*
 * Functions used to build HTML elements from JSON in left-box DIV
 */

function assembleTrailDIV(trailObj) {

    // For attribute in trail object, create a <p> and append it to trail DIV.
    trail = JSON.stringify(trailObj);
    let trailEl = document.createElement('div');
    trailEl.className = 'trail';

    for (attr in trailObj) {
        // If attribute is 'id' or 'imgMedium', do not create <p>
        if (attr[0] != 'i') {
            let trailAttr = document.createElement('p');
            trailAttr.className = 'trail-attr';
            trailAttr.innerHTML = `<b>${attr}:</b> ${trailObj[attr]}`;
            trailEl.append(trailAttr);
        }
    }
    // This line stores json so trail attributes can be accessed easily.
    trailEl.setAttribute('json', trail);
    $('#left-box').append(trailEl);
}

function assembleLeftBox(trails) {
    /* TODO: Add formatTrails function, modify assembleTrailDIV to only show appropriate
     * attributes
     */
    for (trail in trails) {
        assembleTrailDIV(trails[trail]);
    }

}
