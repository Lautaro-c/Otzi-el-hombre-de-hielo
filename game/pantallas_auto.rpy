# ──────────────────────────────────────────
#  INVENTARIO EN PANTALLA — ruta escape en auto
#  Click en un ítem: lo selecciona/deselecciona sin cerrar la pantalla.
# ──────────────────────────────────────────
screen inventario_auto():
    frame:
        align (0.02, 0.02)
        vbox:
            spacing 4
            text "Inventario" size 24

            if not (tiene_pieza or tiene_gato or tiene_llave_cruz or tiene_cables or tiene_rueda):
                text "(vacío)" color "#888888"

            if tiene_gato:
                textbutton "🚗 Gato hidráulico" selected (item_seleccionado == "gato") action Function(auto_toggle_item, "gato")
            if tiene_llave_cruz:
                textbutton "✚ Llave de cruz" selected (item_seleccionado == "llave_cruz") action Function(auto_toggle_item, "llave_cruz")
            if tiene_cables:
                textbutton "🔌 Cables nuevos" selected (item_seleccionado == "cables") action Function(auto_toggle_item, "cables")
            if tiene_rueda:
                textbutton "🛞 Rueda nueva" selected (item_seleccionado == "rueda") action Function(auto_toggle_item, "rueda")
            if tiene_pieza:
                textbutton "🔧 Motor nuevo" selected (item_seleccionado == "pieza") action Function(auto_toggle_item, "pieza")

            if item_seleccionado:
                text "Usando: [item_seleccionado]" size 18 color "#ffff66"
            else:
                text "(ningún objeto seleccionado)" size 18 color "#888888"

screen hud_auto():
    use inventario_auto
    frame:
        align (0.98, 0.02)
        text "Energía: [energia_auto]"


# ──────────────────────────────────────────
#  PANTALLA 1: buscar piezas en el taller
#  (sin cambios: acá solo se recolecta, no se combina nada)
# ──────────────────────────────────────────
screen pantalla_taller_auto():
    modal True
    use hud_auto

    if not tiene_pieza:
        use zona((510, 662, 227, 58), "Algo pesado bajo unos escombros", "pieza")
    if not tiene_gato:
        use zona((77, 757, 156, 295), "Una herramienta metálica en el piso", "gato")
    if not tiene_rueda:
        use zona((1101, 590, 59, 100), "Una pila de neumáticos viejos", "rueda")
    if not tiene_llave_cruz:
        use zona((1331, 869, 193, 204), "Un objeto con forma de cruz", "llave_cruz")
    if not tiene_cables:
        use zona((1445, 288, 81, 160), "Cables enrollados en un rincón", "cables")

    if tiene_pieza and tiene_gato and tiene_rueda and tiene_llave_cruz and tiene_cables:
        vbox:
            align (0.5, 0.96)
            textbutton "Ya revisamos todo, volver con los demás" action Return("listo")


# ──────────────────────────────────────────
#  PANTALLA 2: reparar el auto
#  Cada hotspot solo devuelve SU nombre al hacer click;
#  qué pasa con eso se resuelve en ruta_auto.rpy según
#  qué objeto esté seleccionado.
# ──────────────────────────────────────────
screen pantalla_reparar_auto():
    modal True
    use hud_auto

    use zona((250, 750, 260, 180), "Rueda pinchada", "rueda")
    use zona((900, 500, 320, 220), "Motor del auto", "motor")
    use zona((1500, 850, 220, 130), "Tablero de encendido", "arranque")
    use zona((1500, 640, 220, 130), "Ventanilla", "ventanas")

    if rueda_colocada and motor_colocado:
        vbox:
            align (0.5, 0.96)
            textbutton "Girar la llave" action Return("arrancar")