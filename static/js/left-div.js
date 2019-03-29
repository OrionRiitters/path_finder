/*
 * Functions used to build HTML elements from JSON in left-box DIV
 */

function capitalize(attr) {
    return attr[0].toUpperCase() + attr.slice(1);
}

function assembleTrailDIV(trailObj) {

    //Stringify JSON and create trail element to contain trail attributes
    trailStr = JSON.stringify(trailObj);
    let trailEl = document.createElement('div');
    trailEl.className = 'trail';

    // For attribute in trail object, create a <p> and append it to trail DIV.
    for (attr in trailObj) {
        // If attribute is 'id' or 'imgMedium', do not create <p>
        if (attr[0] != 'i') {
            let trailAttr = document.createElement('p');
            trailAttr.className = 'trail-attr';
            trailAttr.innerHTML = `<b>${capitalize(attr)}:</b> ${trailObj[attr]}`;
            trailEl.append(trailAttr);
        }
    }
    // This line stores json so trail attributes can be accessed easily.
    trailEl.setAttribute('json', trailStr);
    $('#left-box').append(trailEl);
}

function assembleLeftBox(trails) {

    // Delete child of left-box and populate with (hidden) trail DIVs
    $('#left-box').empty();
    for (trail in trails) {
        assembleTrailDIV(trails[trail]);
    }
}

