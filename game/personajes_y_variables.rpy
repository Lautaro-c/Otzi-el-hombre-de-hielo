# ──────────────────────────────────────────
#  PERSONAJES
# ──────────────────────────────────────────
define narrador    = Character(None, what_italic=True)
define prota       = Character("Protagonista",       color="#00ffff")
define calisto     = Character("Dra. Calisto",       color="#b366ff")
define timor       = Character("Dra. Timor",         color="#00ff00")
define nostrov     = Character("Ingeniero Nostrov",  color="#ffa500")
define desconocido = Character("???",                color="#aaaaaa")
define rescatista  = Character("Equipo de Rescate",  color="#aaaaaa")

# ──────────────────────────────────────────
#  CONSTANTES
# ──────────────────────────────────────────
define ENERGIA_DIA_1 = 3
define ENERGIA_DIA_2 = 6
define ENERGIA_DIA_3 = 6
define PISTAS_PARA_CURA = 6

define ENERGIA_AUTO_DIA_1 = 3
define ENERGIA_AUTO_DIA_2 = 4
define ENERGIA_AUTO_DIA_3 = 14

# ──────────────────────────────────────────
#  VARIABLES — ruta Dra. Calisto (investigación de Ötzi)
# ──────────────────────────────────────────
default dia = 1
default energia = ENERGIA_DIA_1
default investigacion_otzi = 0
default relacion_calisto = 0

default pulmon = False
default sangre_rara = False
default caries_encontradas = False

default microscopio = False
default bisturi = False
default pinza = False

default dia2_perdido = False

# ──────────────────────────────────────────
#  VARIABLES — ruta Ingeniero Nostrov (generador)
# ──────────────────────────────────────────
default tiene_llave_inglesa = False

# ──────────────────────────────────────────
#  VARIABLES — ruta escape en auto
# ──────────────────────────────────────────
default tiene_gato = False
default tiene_cables = False
default tiene_pieza = False
default tiene_llave_cruz = False
default tiene_rueda = False
default rueda_colocada = False
default motor_colocado = False
default energia_auto = ENERGIA_AUTO_DIA_1
default dia_auto = 1
default auto_paso_rueda = 0   # 0=nada, 1=auto levantado con el gato, 2=rueda vieja sacada con la cruz, 3=rueda nueva colocada
default auto_paso_motor = 0   # auto_paso_motor: 0=nada, 1=motor viejo sacado, 2=motor nuevo abierto con la cruz, 3=cables puestos, 4=motor colocado
default item_seleccionado = None   # objeto del inventario actualmente seleccionado (o None)

# quién fue a buscar a quién en la previa del final verdadero
default busco_a = None   # "timor" o "nostrov"

# ──────────────────────────────────────────
#  SEGUIMIENTO DE FINALES
#  (habilita "Llamarlos a todos" en el hub "Con quien vas")
# ──────────────────────────────────────────
define FINALES_REQUERIDOS = {
    "calisto_bueno", "calisto_malo_cura", "calisto_malo_ira",
    "nostrov_bueno",
    "auto_bueno", "auto_malo",
    "timor_solitario",
    "energia_agotada",
}

init python:
    if persistent.finales_vistos is None:
        persistent.finales_vistos = set()

    def registrar_final(nombre):
        persistent.finales_vistos.add(nombre)

    def todos_los_finales_vistos():
        return FINALES_REQUERIDOS.issubset(persistent.finales_vistos)

    def auto_gastar_energia(costo=1):
        """Resta energía en el minijuego del auto y decide a qué label saltar."""
        store.energia_auto -= costo
        if store.energia_auto <= 0:
            if store.dia_auto == 2:
                return "descanso_dia2_auto"
            else:
                return "ver_final_auto"
        return None