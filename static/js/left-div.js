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
        attrValue = attrSwitch(attr, trailObj[attr]);
        if (attrValue) {
            let trailAttr = document.createElement('p');
            trailAttr.className = 'trail-attr';
            trailAttr.innerHTML = `${capitalize(attr)}: ${attrValue}`;
            trailEl.append(trailAttr);
        }
    }
    // This line stores json so trail attributes can be accessed easily.
    trailEl.setAttribute('json', trailStr);
    trailEl.setAttribute('latitude', `lat${trailObj['latitude']}`);
    trailEl.setAttribute('id', 'k' + trailObj['id']);
    saveTrailBtn(trailEl);
    trailEl.style.display = 'none';
    $('#left-box').append(trailEl);
}

function assembleLeftBox(trails) {

    // Delete child of left-box and populate with (hidden) trail DIVs
    $('#left-box').empty();
    for (trail in trails) {
        assembleTrailDIV(trails[trail]);
    }
}

// This code gets a 400 error for some reason. The console.log shows the correct json is
// being send in the reques t though.
function saveTrailBtn(trailEl) {
    btn = document.createElement('button');
    btn.setAttribute('class', 'save-trail btn btn-secondary btn-left');
    btn.innerHTML = 'Save Trail';
    trailEl.append(btn);
    btn.addEventListener('click', function() {
        let json_data = trailEl.getAttribute('json');
        $.ajax({
            url:'/save_trail',
            type:"POST",
            data: json_data,
            contentType:"application/JSON",
            success: function(){
                alert("Trailed was added to your bucket list");
            },
            error: function () {
                alert("Trail could not be added");
            }
        });
        console.dir(trailEl);
    });
}

function createChildren(attr) {
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
}

function attrSwitch(key, value) {
    returnable = null;

    switch(key) {
    case 'difficulty':
        returnable = capitalize(value);
        break;
    case 'length':
        returnable = value + ' miles';
        break;
    case 'latitude':
        returnable = value;
        break;
    case 'longitude':
        returnable = value;
        break;
    case 'location':
        if (value[0] == ',') {
            returnable = capitalize(value.slice(2));
        } else {
            returnable = capitalize(value);
        }
        break;
    case 'name':
        returnable = value;
        break;
    case 'stars':
        returnable = value;
        break;
    case 'summary':
        returnable = value;
        break;
    default:
        returnable = null;
    }
    return returnable;
}

function placeHolderText(){
    document.getElementById('left-box').innerHTML = 'Find a path to view the details here!';
}
