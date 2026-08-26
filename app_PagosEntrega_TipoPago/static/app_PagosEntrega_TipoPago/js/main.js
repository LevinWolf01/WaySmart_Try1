document.addEventListener('DOMContentLoaded', () => {
    // Autocompletar la fecha actual en el selector de fecha/hora
    const fechaInput = document.getElementById('fecha_de_pago');
    if (fechaInput && !fechaInput.value) {
        const now = new Date();
        now.setMinutes(now.getMinutes() - now.getTimezoneOffset());
        fechaInput.value = now.toISOString().slice(0, 16);
    }
});