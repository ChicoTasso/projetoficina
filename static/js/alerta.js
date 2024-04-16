function alerta() {
    var r = confirm("Tem certeza que deseja excluir esta oficina?");
    if (r == true) {
        window.location.href = "{% url 'geral:deletarOficina' oficina.id %}";
    } else {
        window.location.href = "{% url 'geral:listaOficina' %}";
    }
}