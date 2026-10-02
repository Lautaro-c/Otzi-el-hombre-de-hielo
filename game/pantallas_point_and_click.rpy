# Zona clickeable invisible: se ilumina al pasar el mouse.
# rect = (x, y, ancho, alto)  ->  AJUSTAR según tu arte (base 1920x1080)

style boton_otzi is default:
    background Solid("#000000")

screen zona(rect, texto, destino):
    button:
        area rect
        background None
        hover_background Solid("#ffffff40")
        tooltip texto
        action Return(destino)

screen interactImage(hoveredText, destino, x, y, ruta):
    vbox xpos x ypos y:
        imagebutton auto ruta action Return(destino)
        tooltip hoveredText

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

screen hud_decision():
    frame:
        align (0.98, 0.02)
        text "Energía: [energia_decision]"

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
            textbutton "Ir al almacén" action Return("almacen")
        textbutton "Reagruparse con los demás" action Return("reagruparse")


# Almacén de suministros
screen pantalla_almacen():
    modal True
    use hud

    if energia > 0:
        if not microscopio:
            use interactImage("Microscopio", "click_microscopio", 250, 300, "Objetos/microscopio_%s.png")
        if not bisturi:
            use interactImage("Bisturí", "click_bisturi", 1350, 394, "Objetos/visturi_%s.png")
        if not pinza:
            use interactImage("Pinza", "click_pinza", 784, -50, "Objetos/pinsas_%s.png")

    vbox:
        align (0.5, 0.96)
        spacing 10
        if energia > 0 and (not pulmon or not sangre_rara or not caries_encontradas):
            textbutton "Ir a revisar a Ötzi" action Return("sala_otzi")
        textbutton "Reagruparse con los demás" action Return("reagruparse")

# P&C final timor solitario

screen hudTS():
    frame:
        align (0.98, 0.02)
        text "Por encontrar: [objetos_faltantes]"

screen pnc_ts():
    modal True
    use hudTS

    if objetos_faltantes > 0:
        if not linterna:
            use interactImage("Linterna", "linterna", 220, 780, "Objetos/Linterna_%s.png")
        if not abrigo:
            use interactImage("Mochila", "abrigo", 650, 120, "Objetos/Mochila_%s.png")
        if not comida:
            use interactImage("Comida", "comida", 1000, 75, "Objetos/Comida_%s.png")
        