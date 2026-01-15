
document.addEventListener('DOMContentLoaded', function() {
    console.log('Página de Productos cargada.');

    // Ejemplo: Animación o filtro futuro
    const buttons = document.querySelectorAll('.product-btn');
    buttons.forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.preventDefault();
            alert('Producto seleccionado. Pronto disponible.');
        });
    });
});
