document.addEventListener('DOMContentLoaded', function () {
    // --- 1. LÓGICA DE FILTRADO ---
    const filterBtns = document.querySelectorAll('.portfolio-filter-btn');
    const items = document.querySelectorAll('.portfolio-item');

    filterBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            // Remover clase active de todos los botones
            filterBtns.forEach(b => b.classList.remove('active'));
            // Agregar clase active al botón clickeado
            btn.classList.add('active');

            const filterValue = btn.getAttribute('data-filter');

            items.forEach(item => {
                if (filterValue === 'all' || item.getAttribute('data-category') === filterValue) {
                    item.style.display = 'block';
                    // Pequeña animación de entrada
                    item.style.opacity = '0';
                    setTimeout(() => {
                        item.style.opacity = '1';
                    }, 50);
                } else {
                    item.style.display = 'none';
                }
            });
        });
    });

    // --- 2. LÓGICA DE LIGHTBOX (Visor de Fotos) ---
    const lightbox = document.getElementById('lightbox');
    const lightboxImg = document.getElementById('img-lightbox');
    const lightboxCaption = document.getElementById('caption');
    const closeBtn = document.querySelector('.close-lightbox');

    // El botón de zoom es el link con el icono bi-zoom-in (primer .project-overlay-btn)
    // O podemos seleccionar cualquier .project-overlay-btn que no sea el de "link" si quisieras
    // Por ahora, asumimos que todos los botones de zoom en overlay abren el lightbox.
    // Pero tu HTML tiene dos botones. Identifiquemos el de zoom.

    // Opción A: Agregar clase específica al botón de zoom en el HTML.
    // Opción B: Delegación de eventos o selector específico.

    // Vamos a buscar todos los botones que tengan el icono de zoom-in dentro
    const zoomButtons = document.querySelectorAll('.project-overlay-btn i.bi-zoom-in');

    zoomButtons.forEach(icon => {
        // El listener va al padre <a>, no al icono <i>
        const btn = icon.parentElement;

        btn.addEventListener('click', (e) => {
            e.preventDefault();

            // Buscar la carta (card) padre
            const card = btn.closest('.project-card');

            // Buscar la imagen dentro de la carta
            const img = card.querySelector('.project-img-wrapper img');
            const title = card.querySelector('.project-title').textContent;

            // Setear valores en el Lightbox
            lightboxImg.src = img.src;
            lightboxImg.alt = img.alt;
            lightboxCaption.textContent = title;

            // Mostrar Lightbox
            lightbox.style.display = "block";
            // Prevenir scroll del body
            document.body.style.overflow = 'hidden';
        });
    });

    // Función para cerrar
    const closeLightbox = () => {
        lightbox.style.display = "none";
        document.body.style.overflow = 'auto';
    };

    // Cerrar con la X
    closeBtn.addEventListener('click', closeLightbox);

    // Cerrar si haces clic fuera de la imagen (en el fondo oscuro)
    lightbox.addEventListener('click', (e) => {
        if (e.target === lightbox || e.target.classList.contains('lightbox-content-wrapper')) {
            closeLightbox();
        }
    });

    // Cerrar con tecla Escape
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && lightbox.style.display === 'block') {
            closeLightbox();
        }
    });
});
