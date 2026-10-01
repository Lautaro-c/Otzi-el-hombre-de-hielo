# ══════════════════════════════════════════
#  SALA DE ÖTZI (hub)
# ══════════════════════════════════════════
label sala_otzi:
    scene bg sala_otzi
    call screen pantalla_sala_otzi
    jump expression _return

label click_pulmon:
    $ energia -= 1
    $ investigacion_otzi += 1
    $ pulmon = True

    prota "Ahí pareciera... pareciera que tiene algo.... UNA FLECHA."
    calisto "Gran observación Dr."
    prota "Probablemente haya muerto en combate, solo se encuentra la punta de la flecha así que su enemigo debe haber arrancado el resto antes de irse."
    calisto "En eso tiene razón Dr pero observe los alrededores de la herida, eso no lo provoca una flecha. Debe haber estado padeciendo una enfermedad, pero ¿Cuál será?"
    jump sala_otzi

label click_sangre:
    $ energia -= 1
    $ investigacion_otzi += 1
    $ sangre_rara = True

    prota "La sangre en su capa, ¿Es normal que tenga ese color?"
    calisto "Es normal que después de miles de años allá cambiado su tono pero no que tome ese en especifico, algo raro tenía Ötzi, pero voy a necesitar un microscopio para poder ver que es lo que le pasaba."
    jump sala_otzi

label click_boca:
    $ energia -= 1
    $ investigacion_otzi += 1
    $ caries_encontradas = True

    prota "Sabía que no había dentista en esa época pero dios mío, ¿Como uno puede tener los dientes así?"
    calisto "Tenes razón de que en esa época no existía salud bucal pero esas no son caries normales."
    calisto "Pocos doctores podrían decirte que bacterias llevan a esos dientes, por suerte estas con una de ellas."
    jump sala_otzi


# ══════════════════════════════════════════
#  ALMACÉN DE SUMINISTROS
# ══════════════════════════════════════════
label almacen:
    scene bg almacen
    narrador "Ambos llegan al almacén, es un lugar lleno de cosas tiradas por todos lados y aparte están viejas. No saben si van a encontrar algo aquí pero no pierden nada por buscar."
    jump almacen_hub

label almacen_hub:
    scene bg almacen
    call screen pantalla_almacen
    jump expression _return

label click_microscopio:
    $ energia -= 1
    $ investigacion_otzi += 1
    $ microscopio = True

    prota "Mire lo que encontré Dra., es un microscopio. ¿Esto podría servirle para algo?"
    if sangre_rara:
        calisto "¡Que gran descubrimiento Dr.! Eso nos va a ser de gran ayuda para analizar la sangre que tenía Ötzi"
    else:
        calisto "¡Que gran descubrimiento Dr.! Todavía no sabemos para que podría servirnos pero un microscopio nunca viene mal."
    prota "Me alegro de poder estar siendo de ayuda."
    calisto "No lo dude Dr."
    jump almacen_hub

label click_bisturi:
    $ energia -= 1
    $ investigacion_otzi += 1
    $ bisturi = True

    prota "Cajas, más cajas, aun más ca- AUCH"
    calisto "¿¡Que paso?!"
    prota "Nada, solo me pinche con algo, que sera... MIRE Dra. ES UN BISTURÍ."
    if pulmon:
        calisto "Buenísimo Dr., nos va a ser muy util. Sobre todo para extraer la punta de la flecha y ver si tiene algún tipo de veneno."
    else:
        calisto "Buenísimo Dr., nos va a ser muy util. Todavía no se para que pero lo averiguaremos."
    prota "Que bueno que fue un accidente fortuito."
    jump almacen_hub

label click_pinza:
    $ energia -= 1
    $ investigacion_otzi += 1
    $ pinza = True

    prota "Wow que pinza mas vieja, dudo que podamos usarlas."
    calisto "¡ESPERA!"
    prota "¿Que pasa?"
    calisto "Podrían sernos útiles."
    prota "¿Para que?"
    if caries_encontradas:
        calisto "Para sacarle los dientes a Ötzi"
        prota "Dios mío Dra. No esperaba esta actitud de usted."
        calisto "Créeme no lo hago por gusto, necesitamos analizar sus dientes, y una profesional como yo no retrocede por mas asqueroso que sea."
        prota "Sigue siendo un asco."
    else:
        calisto "Todavía no se para que pero lo averiguaremos."
        prota "Hagámoslo."
    jump almacen_hub


# ══════════════════════════════════════════
#  DESPACHADOR: "Reagruparse con los demás"
#  Decide a qué escena ir según el día y el estado
# ══════════════════════════════════════════
label reagruparse:
    if dia == 1:
        jump reagruparse_dia1

    elif dia == 2:
        if investigacion_otzi <= 0:
            jump me_mentiste
        elif energia == ENERGIA_DIA_2:      # no gastó nada de energía hoy
            jump que_paso
        else:
            jump reagruparse_dia2

    else:  # día 3
        if investigacion_otzi <= 0 or dia2_perdido:
            jump ira_total
        else:
            jump reagruparse_dia3

label que_paso:
    $ dia2_perdido = True

    if dia == 2 and investigacion_otzi >= 3 and relacion_calisto >= 2:
        calisto "Es una pena que hoy no hayamos podido avanzar tanto, pero seguro que mañana lo resolvemos."
        prota "Lamento no haber sido de mucha ayuda hoy, mañana lo haremos mejor."
        calisto "No lo dudo, somos un buen equipo."
    elif dia == 2 and investigacion_otzi > 0:
        calisto "El primer día no logramos avanzar mucho y hoy tampoco nos fue tan bien. Si no nos esforzamos el tiempo se va a acabar."
        prota "Lo se pero es muy difícil con estas circunstancias."
        calisto "Es cierto pero no podemos enfocarnos en las cosas que no controlamos, solo en hacer nuestro mejor esfuerzo y darlo todo hasta el final."
        prota "En eso tenes razon. No deja de sorprenderme su resiliencia Dra."
        calisto "Como están las cosas, es nuestra unica opción."

    if dia == 3 and investigacion_otzi >= 4 and relacion_calisto >= 2:
        calisto "No puedo creer que el ultimo día sea en el que menos avancemos. No se como vamos a decirles a nuestros compañeros que fallamos."
        prota "Yo tampoco, pero vamos a hacerlo juntos."
        calisto "No fue mucho tiempo pero fue un gusto conocerlo Dr."
        prota "Lo mismo digo Dra."
    elif dia == 3 and investigacion_otzi > 0:
        calisto "Estoy muy decepcionada de nuestro progreso, a veces siento como si no nos hubiésemos tomado el problema enserio, quien sabe que va a pasar cuando esa cosa se descongele. Estoy muy decepcionada de mi desempeño."
        narrador "Miraste a la Dra. buscando las palabras para consolarla, pero no había mucho que se pueda decir."

    narrador "Ambos vuelven con los demás"

    if dia == 2:
        jump reagruparse_dia2
    else:
        jump reagruparse_dia3