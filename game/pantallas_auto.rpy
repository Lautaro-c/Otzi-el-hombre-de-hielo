# ──────────────────────────────────────────
#  INVENTARIO EN PANTALLA — ruta escape en auto
# ──────────────────────────────────────────
screen inventario_auto():
    frame:
        align (0.02, 0.02)
        vbox:
            spacing 4
            text "Inventario" size 24

            if not (tiene_pieza or tiene_gato or tiene_llave_cruz or tiene_cables or tiene_rueda):
                text "(vacío)" color "#888888"
            if tiene_pieza:
                text "🔧 Motor nuevo"
            if tiene_gato:
                text "🚗 Gato hidráulico"
            if tiene_llave_cruz:
                text "✚ Llave de cruz"
            if tiene_cables:
                text "🔌 Cables nuevos"
            if tiene_rueda:
                text "🛞 Rueda nueva"

screen hud_auto():
    use inventario_auto
    frame:
        align (0.98, 0.02)
        text "Energía: [energia_auto]"


# ──────────────────────────────────────────
#  PANTALLA 1: buscar piezas en el taller
# ──────────────────────────────────────────
screen pantalla_taller_auto():
    modal True
    use hud_auto

    if not tiene_pieza:
        use zona((150, 680, 320, 220), "Algo pesado bajo unos escombros", "pieza")
    if not tiene_gato:
        use zona((550, 760, 220, 160), "Una herramienta metálica en el piso", "gato")
    if not tiene_rueda:
        use zona((850, 650, 240, 240), "Una pila de neumáticos viejos", "rueda")
    if not tiene_llave_cruz:
        use zona((1150, 710, 180, 160), "Un objeto con forma de cruz", "llave_cruz")
    if not tiene_cables:
        use zona((1400, 620, 220, 160), "Cables enrollados en un rincón", "cables")

    if tiene_pieza and tiene_gato and tiene_rueda and tiene_llave_cruz and tiene_cables:
        vbox:
            align (0.5, 0.96)
            textbutton "Ya revisamos todo, volver con los demás" action Return("listo")


# ──────────────────────────────────────────
#  PANTALLA 2: reparar el auto (la "parte final")
#  Dos secuencias en paralelo: rueda y motor,
#  más 2 hotspots señuelo que siempre están mal.
# ──────────────────────────────────────────
screen pantalla_reparar_auto():
    modal True
    use hud_auto

    # secuencia de la rueda
    if auto_paso_rueda == 0:
        use zona((250, 750, 260, 180), "Usar el gato debajo del auto", "gato_auto")
    elif auto_paso_rueda == 1:
        use zona((250, 750, 260, 180), "Usar la cruz en la rueda", "cruz_rueda")
    elif auto_paso_rueda == 2:
        use zona((250, 750, 260, 180), "Colocar la rueda nueva", "colocar_rueda")

    # secuencia del motor
    if auto_paso_motor == 0:
        use zona((900, 500, 320, 220), "Abrir el capó", "capo")
    elif auto_paso_motor == 1:
        use zona((900, 500, 320, 220), "Sacar el motor viejo", "sacar_motor")
    elif auto_paso_motor == 2:
        use zona((900, 500, 320, 220), "Abrir el motor nuevo con la cruz", "abrir_motor")
    elif auto_paso_motor == 3:
        use zona((900, 500, 320, 220), "Ponerle los cables nuevos", "poner_cables")
    elif auto_paso_motor == 4:
        use zona((900, 500, 320, 220), "Dejar el motor en su lugar", "colocar_motor")

    # señuelos: siempre disponibles, siempre gastan energía sin avanzar
    use zona((1500, 850, 220, 130), "Intentar prender el motor", "decoy_prender")
    use zona((1500, 640, 220, 130), "Bajar las ventanas", "decoy_ventanas")

    if rueda_colocada and motor_colocado:
        vbox:
            align (0.5, 0.96)
            textbutton "Girar la llave" action Return("arrancar")