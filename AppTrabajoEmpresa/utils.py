from datetime import date, timedelta

def calcular_viernes_santo(year):
    """
    Calcula la fecha de Viernes Santo usando el algoritmo de Butcher's (computus).
    """
    a = year % 19
    b = year // 100
    c = year % 100
    d = b // 4
    e = b % 4
    f = (b + 8) // 25
    g = (b - f + 1) // 3
    h = (19 * a + b - d - g + 15) % 30
    i = c // 4
    k = c % 4
    l = (32 + 2 * e + 2 * i - h - k) % 7
    m = (a + 11 * h + 22 * l) // 451
    
    # Marzo es 3, Abril es 4
    month = (h + l - 7 * m + 114) // 31
    day = ((h + l - 7 * m + 114) % 31) + 1
    
    domingo_resurreccion = date(year, month, day)
    viernes_santo = domingo_resurreccion - timedelta(days=2)
    
    return viernes_santo

def obtener_feriados(year):
    """
    Devuelve una lista de fechas (strings YYYY-MM-DD) con los feriados de Chile.
    Incluye feriados fijos, Viernes Santo y Sábado Santo.
    """
    feriados = [
        date(year, 1, 1),    # Año Nuevo
        date(year, 5, 1),    # Día del Trabajo
        date(year, 5, 21),   # Día de las Glorias Navales
        date(year, 6, 20),   # Día Nacional de los Pueblos Indígenas (Aprox, suele ser fijo o movible)
        date(year, 6, 29),   # San Pedro y San Pablo
        date(year, 7, 16),   # Día de la Virgen del Carmen
        date(year, 8, 15),   # Asunción de la Virgen
        date(year, 9, 18),   # Independencia Nacional
        date(year, 9, 19),   # Día de las Glorias del Ejército
        date(year, 10, 12),  # Encuentro de Dos Mundos
        date(year, 10, 31),  # Día de las Iglesias Evangélicas
        date(year, 11, 1),   # Día de Todos los Santos
        date(year, 12, 8),   # Inmaculada Concepción
        date(year, 12, 25),  # Navidad
    ]

    # Calcular Viernes Santo y Sábado Santo
    viernes_santo = calcular_viernes_santo(year)
    sabado_santo = viernes_santo + timedelta(days=1)
    
    feriados.append(viernes_santo)
    feriados.append(sabado_santo)

    # Ordenar y formatear a string
    feriados.sort()
    return [d.strftime("%Y-%m-%d") for d in feriados]
