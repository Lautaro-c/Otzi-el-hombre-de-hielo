# Zona clickeable invisible: se ilumina al pasar el mouse.
# rect = (x, y, ancho, alto)  ->  AJUSTAR según tu arte (base 1920x1080)
screen zona(rect, texto, destino):
    button:
        area rect
        background None
        hover_background Solid("#ffffff40")
        tooltip texto
        action Return(destino)

# Energía + texto de la zona que estás señalando
screen hud():
    frame:
        align (0.98, 0.02)
        text "Energía: [energia]"

    $ tt = GetTooltip()
    if tt:
        frame:
            align (0.5, 0.04)
            text "[tt]"

# Sala donde está Ötzi
screen pantalla_sala_otzi():
    modal True
    use hud

    if energia > 0:
        if not pulmon:
            use zona((810, 510, 33, 42), "Herida en el pulmón izquierdo", "click_pulmon")
        if not sangre_rara:
            use zona((910, 460, 93, 50), "Sangre en la capa", "click_sangre")
        if not caries_encontradas:
            use zona((715, 480, 22, 22), "Boca", "click_boca")

    vbox:
        align (0.5, 0.96)
        spacing 10
        if dia > 1 and energia > 0:
            textbutton "Ir al almacén de suministros" action Return("almacen")
        textbutton "Reagruparse con los demás" action Return("reagruparse")

# Almacén de suministros
screen pantalla_almacen():
    modal True
    use hud

    if energia > 0:
        if not microscopio:
            use zona((300, 600, 150, 120), "Microscopio", "click_microscopio")
        if not bisturi:
            use zona((900, 700, 100, 80), "Bisturí", "click_bisturi")
        if not pinza:
            use zona((1400, 650, 120, 100), "Pinza", "click_pinza")

    vbox:
        align (0.5, 0.96)
        spacing 10
        if energia > 0 and (not pulmon or not sangre_rara or not caries_encontradas):
            textbutton "Ir a revisar a Ötzi" action Return("sala_otzi")
        textbutton "Reagruparse con los demás" action Return("reagruparse")