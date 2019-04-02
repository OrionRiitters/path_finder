function assembleBucketList(res) {

    assembleLeftBox(res);

    bucketList = document.createElement('div');
    bucketList.setAttribute('id', 'bucket-list');
    table = assembleTable(res);
    bucketList.appendChild(table);
    $('#right-box').empty();
    $('#right-box').append(bucketList);
}

function assembleTable(res) {
    let table = document.createElement('table');
    let tableBody = document.createElement('tbody');
    table.appendChild(tableBody);

    let nameHeader = document.createElement('th');
    nameHeader.innerHTML = 'Trail Name';

    let hasHikedHeader = document.createElement('th');
    hasHikedHeader.innerHTML = 'Hiked?';

    let showDetailsHeader = document.createElement('th');
    tableBody.appendChild(nameHeader);
    tableBody.appendChild(hasHikedHeader);
    tableBody.appendChild(showDetailsHeader);

    for (trail in res) {
        assembleRow(res[trail], tableBody);
    }

    return table;
}

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

    let btn = document.createElement('button');
    btn.setAttribute('id', `b${trail['id']}`);
    row.append(btn);
    tableBody.append(row);
    btn.addEventListener('click', function(e) {
        key = 'k' + `${e['target']['id']}`.slice(1);
        trailEl = $(`#${key}`);
        hideMostTrails(trailEl[0]);
    });
}



  /*  for (i = 0 ; i < 2; i++) {
        let td = document.createElement('td');
        let tn = document.createTextNode(`${trail[attributes[i]]}`);
        td.append(tn);
        tr.append(td);
    } 



    rowString = 
        `
        <tr>
        <td>${trail['name']}</td>
        <td>${trail['hasHiked'] == 1 ? 'Yes' : 'No'}
        <button id='${buttonID}'>Details</button>
        </tr>
        `;
    return rowString;    */

