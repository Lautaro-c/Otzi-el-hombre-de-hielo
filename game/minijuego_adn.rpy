# Usa las imágenes registradas por Ren'Py: adn 1, adn 2 y adn 3.
# Cambia estas constantes si quieres ajustar la dificultad o el tamaño.
define ADN_SPRITES = ("adn 1", "adn 2", "adn 3")
define ADN_OBJETIVO = 30
define ADN_TIEMPO = 15.0
define ADN_CANTIDAD = 20
define ADN_TAMANO = 96

default adn_fragmentos = []
default adn_aciertos = 0
default adn_inicio = None
default adn_tiempo_restante = 15.0
default adn_proximo_id = 0

init python:
    import time as adn_reloj

    def adn_preparar():
        store.adn_fragmentos = []
        store.adn_aciertos = 0
        store.adn_inicio = None
        store.adn_tiempo_restante = ADN_TIEMPO
        store.adn_proximo_id = 0

    def adn_crear_fragmento():
        # Cada fragmento ocupa una casilla distinta; el desplazamiento dentro
        # de ella hace que las posiciones no formen una cuadrícula rígida.
        ancho = config.screen_width - 160
        alto = config.screen_height - 280
        columnas = max(1, ancho // (ADN_TAMANO + 24))
        filas = max(1, alto // (ADN_TAMANO + 24))
        ancho_casilla = ancho // columnas
        alto_casilla = alto // filas
        ocupadas = {fragmento["casilla"] for fragmento in store.adn_fragmentos}
        libres = [i for i in range(columnas * filas) if i not in ocupadas]

        if not libres:
            raise Exception("No hay espacio para los fragmentos de ADN. Reduce ADN_CANTIDAD o ADN_TAMANO.")

        casilla = renpy.random.choice(libres)
        x = 80 + (casilla % columnas) * ancho_casilla
        y = 190 + (casilla // columnas) * alto_casilla
        x += renpy.random.randint(0, max(0, ancho_casilla - ADN_TAMANO))
        y += renpy.random.randint(0, max(0, alto_casilla - ADN_TAMANO))
        store.adn_proximo_id += 1

        return {
            "id": store.adn_proximo_id,
            "casilla": casilla,
            "sprite": renpy.random.choice(ADN_SPRITES),
            "x": x,
            "y": y,
        }

    def adn_empezar():
        if store.adn_inicio is not None:
            return

        store.adn_fragmentos = []
        for _ in range(ADN_CANTIDAD):
            store.adn_fragmentos.append(adn_crear_fragmento())

        # El reloj empieza después de preparar las imágenes.
        store.adn_inicio = adn_reloj.monotonic()
        store.adn_tiempo_restante = ADN_TIEMPO

    def adn_actualizar():
        if store.adn_inicio is None:
            return

        transcurrido = adn_reloj.monotonic() - store.adn_inicio
        store.adn_tiempo_restante = max(0.0, ADN_TIEMPO - transcurrido)
        if transcurrido >= ADN_TIEMPO:
            return "agotado"

    def adn_pulsar(fragmento_id):
        if store.adn_inicio is None:
            return

        # Comprueba la hora también en el clic: no se aceptan aciertos
        # tardíos aunque todavía no se haya ejecutado el siguiente timer.
        resultado = adn_actualizar()
        if resultado is not None:
            return resultado

        for indice, fragmento in enumerate(store.adn_fragmentos):
            if fragmento["id"] == fragmento_id:
                nuevo = adn_crear_fragmento()
                store.adn_fragmentos[indice] = nuevo
                store.adn_aciertos += 1

                if store.adn_aciertos >= ADN_OBJETIVO:
                    return "exito"
                return
        # Un clic que todavía refiera al fragmento anterior no cuenta dos veces.


screen pantalla_adn_final():
    modal True
    zorder 100

    add Solid("#07141ce8")

    key "rollback" action NullAction()
    key "rollforward" action NullAction()

    if adn_inicio is None:
        frame:
            align (0.5, 0.5)
            padding (50, 40)
            background Solid("#102c36")

            vbox:
                spacing 24
                xalign 0.5

                text "RECONSTRUCCIÓN DEL ADN":
                    size 42
                    color "#86eef2"
                    xalign 0.5

                text "Seleccioná [ADN_OBJETIVO] fragmentos antes de que pasen [ADN_TIEMPO:.0f] segundos.":
                    size 28
                    color "#ffffff"
                    xalign 0.5

                text "Los tres tipos de ADN cuentan. Cada acierto hace aparecer otro fragmento.":
                    size 24
                    color "#c5dbe1"
                    xalign 0.5

                textbutton "Comenzar":
                    xalign 0.5
                    action Function(adn_empezar)

    else:
        # Durante estos 15 segundos, Esc no abre el menú de guardado.
        key "game_menu" action NullAction()

        frame:
            area (60, 160, config.screen_width - 120, config.screen_height - 220)
            background Solid("#102c36b0")

        hbox:
            xalign 0.5
            ypos 45
            spacing 100

            text "ADN: [adn_aciertos] / [ADN_OBJETIVO]":
                size 36
                color "#86eef2"

            text "Tiempo: [adn_tiempo_restante:.1f] s":
                size 36
                color ("#ff7272" if adn_tiempo_restante <= 5.0 else "#ffffff")

        for fragmento index fragmento["id"] in adn_fragmentos:
            imagebutton:
                xpos fragmento["x"]
                ypos fragmento["y"]
                idle Transform(fragmento["sprite"], xysize=(ADN_TAMANO, ADN_TAMANO), fit="contain")
                hover Transform(fragmento["sprite"], xysize=(ADN_TAMANO, ADN_TAMANO), fit="contain", alpha=0.75)
                action Function(adn_pulsar, fragmento["id"])

        text "Extraé y repará los fragmentos para completar la clonación.":
            xalign 0.5
            yalign 0.98
            size 24
            color "#c5dbe1"

        timer 0.05 repeat True action Function(adn_actualizar)
