$('#email-form').on('submit', async (e) => {
    e.preventDefault();

    const email = $("#email").val();
    const senha = $("#senha").val();
    const params = new URLSearchParams({ email, senha });
    const resp = await fetch(`/login?${params}`).then(r => r.json());


    //document.getElementById("positiva_1").innerHTML = lista_positiva[0]

});