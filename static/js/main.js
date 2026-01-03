document.addEventListener('DOMContentLoaded', function () {

    // 1. LISTA DE FERIADOS (Irrenunciables y otros importantes en Chile 2026)
    // Puedes agregar más fechas a esta lista siguiendo el formato "AAAA-MM-DD"
    var feriados = [
        "2026-01-01", // Año Nuevo
        "2026-05-01", // Día del Trabajador (Irrenunciable)
        "2026-05-21", // Glorias Navales
        "2026-06-20", // Pueblos Indígenas
        "2026-07-16", // Virgen del Carmen
        "2026-08-15", // Asunción de la Virgen
        "2026-09-18", // Independencia (Irrenunciable)
        "2026-09-19", // Glorias del Ejército (Irrenunciable)
        "2026-10-31", // Iglesias Evangélicas
        "2026-11-01", // Todos los Santos
        "2026-12-08", // Inmaculada Concepción
        "2026-12-25", // Navidad (Irrenunciable)
        // Aquí en el futuro Django inyectará las fechas ocupadas por tu jefe:
        // "2026-02-15", 
    ];

    flatpickr("#inputFecha", {
        locale: "es",              // Idioma español
        dateFormat: "Y-m-d",       // Formato para la base de datos

        // 2. MARGEN DE 1 DÍA DE ANTICIPACIÓN
        // "new Date().fp_incr(1)" significa: Hoy + 1 día = Mañana
        minDate: new Date().fp_incr(1),

        // 3. BLOQUEO DE FINES DE SEMANA Y FERIADOS
        disable: [
            function (date) {
                // Devuelve 'true' si es Domingo (0) o Sábado (6)
                return (date.getDay() === 0 || date.getDay() === 6);
            },
            // Aquí sumamos la lista de feriados que definimos arriba
            ...feriados
        ],

        disableMobile: "true"
    });
});
