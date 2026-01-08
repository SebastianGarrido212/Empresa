
document.addEventListener('DOMContentLoaded', function () {

    // --- CONFIGURACIÓN CALENDARIO (Flatpickr) ---
    // --- CONFIGURACIÓN CALENDARIO (Flatpickr) ---
    // Los feriados ahora vienen integrados en 'fechasDesdeDjango' dinámicamente desde el backend.

    // Verificar si existe la variable global desde Django para evitar errores
    var fechasOcupadas = (typeof fechasDesdeDjango !== 'undefined') ? fechasDesdeDjango : [];

    var bloquearFinesDeSemana = function (date) {
        return (date.getDay() === 0 || date.getDay() === 6);
    };

    // Función para iniciar Flatpickr
    function iniciarCalendario() {
        flatpickr("#inputFecha", {
            locale: "es",
            dateFormat: "Y-m-d",
            minDate: new Date().fp_incr(1),
            disable: [bloquearFinesDeSemana].concat(fechasOcupadas),
            disableMobile: "true",
            static: true, // Importante para modales

            onDayCreate: function (dObj, dStr, fp, dayElem) {
                var fechaFormato = flatpickr.formatDate(dayElem.dateObj, "Y-m-d");

                if (fechasOcupadas.includes(fechaFormato)) {
                    dayElem.style.backgroundColor = "#e9ecef"; // Gris suave
                    dayElem.style.color = "#6c757d";           // Texto muted
                    dayElem.style.cursor = "not-allowed";
                    dayElem.title = "Fecha no disponible";
                    dayElem.classList.add("flatpickr-disabled");
                }
            }
        });
    }

    // Inicializar cuando el modal se abre (Bootstrap 5)
    var modalElement = document.getElementById('modalAgendar');
    if (modalElement) {
        modalElement.addEventListener('shown.bs.modal', function () {
            iniciarCalendario();
        });
    } else {
        // Fallback
        iniciarCalendario();
    }

    // --- MINI CALENDARIO (DISPONIBILIDAD) ---
    // --- MINI CALENDARIO (DISPONIBILIDAD) ---
    function renderizarMiniCalendario(anio, mes, contenedorId) {
        var contenedor = document.getElementById(contenedorId);
        if (!contenedor) return;

        // Nombres de meses y días
        var nombresMeses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"];
        var diasSemana = ["Lu", "Ma", "Mi", "Ju", "Vi", "Sa", "Do"];

        // Calcular datos del mes
        var primerDia = new Date(anio, mes, 1).getDay(); // 0 = Domingo, 1 = Lunes...
        // Ajustar para que Lunes sea 0 y Domingo 6 (formato ISO 8601 visual)
        var primerDiaAjustado = (primerDia === 0) ? 6 : primerDia - 1;

        var diasEnMes = new Date(anio, mes + 1, 0).getDate();

        // Construir HTML
        var html = `
            <div class="calendar-wrapper animate-enter">
                <div class="calendar-header">
                    ${nombresMeses[mes]} ${anio}
                </div>
                
                <div class="calendar-weekdays">
                    ${diasSemana.map(d => `<div>${d}</div>`).join('')}
                </div>

                <div class="calendar-grid">
        `;

        // Rellenar espacios vacíos antes del primer día
        for (let i = 0; i < primerDiaAjustado; i++) {
            html += `<div class="cal-day empty"></div>`;
        }

        // Generar días
        for (var dia = 1; dia <= diasEnMes; dia++) {
            var fechaObj = new Date(anio, mes, dia);

            // Formatear a YYYY-MM-DD
            var mesStr = (mes + 1).toString().padStart(2, '0');
            var diaStr = dia.toString().padStart(2, '0');
            var fechaStr = `${anio}-${mesStr}-${diaStr}`; // Año correcto viene por param

            var esFinDeSemana = (fechaObj.getDay() === 0 || fechaObj.getDay() === 6);
            var estaOcupado = fechasOcupadas.includes(fechaStr);
            var esPasado = fechaObj < new Date().setHours(0, 0, 0, 0);

            var claseEstado = "available"; // Por defecto disponible
            var tooltip = "Disponible";

            if (esFinDeSemana) {
                claseEstado = "weekend";
                tooltip = "Fin de Semana";
            } else if (estaOcupado || esPasado) {
                claseEstado = "busy";
                tooltip = "No Disponible";
            }

            html += `<div class="cal-day ${claseEstado}" title="${tooltip}">${dia}</div>`;
        }

        html += `
                </div>
            </div>
        `;

        contenedor.innerHTML = html;
    }

    // Renderizar Mes Actual y Mes Siguiente
    var fechaHoy = new Date();

    // Mes 1 (Actual)
    renderizarMiniCalendario(fechaHoy.getFullYear(), fechaHoy.getMonth(), 'cal-mes-1');

    // Mes 2 (Siguiente)
    // Manejo automático de cambio de año con setMonth
    var fechaSiguiente = new Date(fechaHoy.getFullYear(), fechaHoy.getMonth() + 1, 1);
    renderizarMiniCalendario(fechaSiguiente.getFullYear(), fechaSiguiente.getMonth(), 'cal-mes-2');
});
