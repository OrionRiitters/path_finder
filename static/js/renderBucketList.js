/* Call functions from below to append proper DIVs to right-box */
function assembleBucketList(res) {

    assembleLeftBox(res);

    bucketList = document.createElement('div');
    bucketList.setAttribute('id', 'bucket-list');
    table = assembleTable(res);
    bucketList.appendChild(table);
    $('#right-box').empty();
    $('#right-box').append(bucketList);
}

/* Assemble table "frame" onto which rows will be appended. */
function assembleTable(res) {
    let table = document.createElement('table');
    let tableBody = document.createElement('tbody');
    table.appendChild(tableBody);

    let nameHeader = document.createElement('th');
    nameHeader.innerHTML = 'Trail Name';
    tableBody.appendChild(nameHeader);

    let hasHikedHeader = document.createElement('th');
    hasHikedHeader.innerHTML = 'Hiked?';
    tableBody.appendChild(hasHikedHeader);

    let showDetailsHeader = document.createElement('th');
    showDetailsHeader.innerHTML = 'Details';
    tableBody.appendChild(showDetailsHeader);

    for (trail in res) {
        assembleRow(res[trail], tableBody);
    }

    return table;
}

/* Create a td element for every column. */
function assembleRow(trail, tableBody) {
    let row = document.createElement('tr');

    let name = document.createElement('td');
    let nameText = document.createTextNode(`${trail['name']}`);
    name.append(nameText);
    row.append(name);

    let hasHiked = document.createElement('td');
    let hasHikedText = trail['hasHiked'] == 1 ? 'Yes' : 'No';
    hasHiked.append(hasHikedText);
    row.append(hasHiked);

    let detailsEl = document.createElement('td');
    let btnDetails = document.createElement('button');
    btnDetails.setAttribute('id', `b${trail['id']}`);
    btnDetails.setAttribute('class', 'btn btn-secondary btn-right');
    btnDetails.innerHTML = 'View Details';
    detailsEl.append(btnDetails);
    row.append(detailsEl);
    /* Event listener for details button */
    btnDetails.addEventListener('click', function(e) {
        key = 'k' + `${e['target']['id']}`.slice(1);
        trailEl = $(`#${key}`);
        hideMostTrails(trailEl[0]);
    });

    let hikedEl = document.createElement('td');
    let btnHiked = document.createElement('button');
    btnHiked.setAttribute('class', 'btn btn-secondary btn-right');
    btnHiked.setAttribute('id', `h${trail['id']}`);
    hikedEl.append(btnHiked);
    row.append(hikedEl);
    tableBody.append(row);

    btnHiked.innerHTML = 'Change "hiked" status';
    /* Event listener for hiked status button */
    btnHiked.addEventListener('click', function (e) {
        jsonDIV = $(`#k${e['target']['id'].slice(1)}`)[0];
        jsonOBJ = JSON.parse(jsonDIV.getAttribute('json'));
        jsonOBJ['hasHiked'] = !jsonOBJ['hasHiked'];
        $.post('/update_hiked', JSON.stringify(jsonOBJ))
            .then(res => {
                assembleBucketList(res);
                key = 'k' + `${e['target']['id']}.slice(1)`;
                trailEl = $(`#${key}`);
                hideMostTrails(trailEl[0]);
            });
    });

}
