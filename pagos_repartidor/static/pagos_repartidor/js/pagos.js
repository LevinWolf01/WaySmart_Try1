document.querySelectorAll('.tarjeta').forEach((tarjeta) => {
    tarjeta.addEventListener('click', () => {
        tarjeta.classList.toggle('seleccionada');
    });
});