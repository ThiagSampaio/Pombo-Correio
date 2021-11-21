

$('#data1').on('submit', async (e) => {

    e.preventDefault()
    data = new FormData();
    data.append('file', $('#database')[0].files[0]);
    const coluna = $("#coluna").val();
    const coluna_email = $("#coluna_email").val();
    const params = new URLSearchParams({ coluna, data, coluna_email });

    const resp = await fetch(`/data?${params}`).then(r => r.json());


});

/*
$('#data1').submit(function (e) {

    var data, xhr;

    data = new FormData();
    data.append('database', $('#database')[0].files[0]);

    xhr = new XMLHttpRequest();

    xhr.open('POST', '/data', true);
    xhr.onreadystatechange = function (response) { };
    xhr.send(data);

    e.preventDefault();
});
*/