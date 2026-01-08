document.addEventListener('DOMContentLoaded', function () {

    var feriados = [
        "2026-01-01", "2026-05-01", "2026-05-21", "2026-06-20",
        "2026-07-16", "2026-08-15", "2026-09-18", "2026-09-19",
        "2026-10-31", "2026-11-01", "2026-12-08", "2026-12-25"
    ];

    flatpickr("#id_fecha", {
        locale: "es",
        dateFormat: "Y-m-d",
        minDate: "today",

        // --- AGREGA ESTAS LÍNEAS DE DISEÑO ---
        theme: "airbnb",              // Fuerza el tema visual
        monthSelectorType: 'static',  // Hace que el mes sea un texto simple, no un dropdown bugueado
        animate: true,                // Animación suave
        // -------------------------------------

        disable: [
            function (date) {
                return (date.getDay() === 0 || date.getDay() === 6);
            },
            ...feriados
        ],
    });
});