function showAlerts() {
    document.getElementById('bootstrap-alert').style.display = 'block';
    setTimeout(function () { document.getElementById('bootstrap-alert').style.display = 'none' }, 1700);
    alert('success! (JS alert)');
}