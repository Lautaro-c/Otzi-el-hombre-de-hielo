# ──────────────────────────────────────────
#  LÓGICA DE COMBINACIÓN — objeto seleccionado + hotspot
# ──────────────────────────────────────────
init python:
    def auto_toggle_item(item):
        if store.item_seleccionado == item:
            store.item_seleccionado = None
        else:
            store.item_seleccionado = item

    def auto_evaluar(target):
        """Decide qué pasó al usar item_seleccionado sobre 'target'.
        Devuelve una clave de resultado y deja el objeto sin seleccionar."""
        item = store.item_seleccionado
        store.item_seleccionado = None

        if target == "rueda":
            if item == "gato" and store.auto_paso_rueda == 0:
                return "rueda_gato"
            elif item == "llave_cruz" and store.auto_paso_rueda == 1:
                return "rueda_cruz"
            elif item == "rueda" and store.auto_paso_rueda == 2:
                return "rueda_colocar"
            else:
                return "fail"

        elif target == "motor":
            if item == "llave_cruz" and store.auto_paso_motor == 0:
                return "motor_cruz"
            elif item == "cables" and store.auto_paso_motor == 1:
                return "motor_cables"
            elif item == "pieza" and store.auto_paso_motor == 2:
                return "motor_colocar"
            else:
                return "fail"

        else:  # arranque, ventanas: siempre señuelo
            return "fail"


label escape_en_auto:
    scene bg sala_comun

    narrador "Después de pensarlo bien llegas a la conclusion de que el auto es la mejor opción"
    narrador "Dejar a los demás esperando por si podes volver o no sería justo"

    $ tiene_gato = False
    $ tiene_cables = False
    $ tiene_pieza = False
    $ tiene_llave_cruz = False
    $ tiene_rueda = False
    $ energia_auto = ENERGIA_AUTO_DIA_1
    $ dia_auto = 1
    $ rueda_colocada = False
    $ motor_colocado = False
    $ auto_paso_rueda = 0
    $ auto_paso_motor = 0
    $ item_seleccionado = None

    jump auto_seguir


label auto_seguir:
    prota "Lo estuve pensando bien y tenemos que escapar usando el auto."
    show nostrov orgullo_ruso
    nostrov "La madre Rusia no cría a hombres débiles, ayúdenme con el generador y dormiremos calientes esta noche."
    prota "Nostrov ya viste el generador, es tan viejo que ni vos debes saber con certeza como arreglarlo."
    show nostrov serio
    nostrov "Camarada odio admitirlo pero tiene un punto."
    show calisto sonriente at left
    calisto "Pero podríamos investigar que le paso a Ötzi, lo tenemos ahí mismo, no podemos perder esta oportunidad."
    prota "Mire Dra. no quiero subestimarla pero debe reconocer que desarrollar una vacuna en 3 días para una enfermedad que no sabe si existe o como esta compuesta no es realista."
    show calisto canchera at left
    calisto "¿Y fingiendo ser mecánicos nos va a ir mejor?"
    prota "Si colaboramos todos sí. Nostrov ya tiene grandes conocimientos en mecánica y nosotros somos personas inteligentes vamos a poder ayudarlo."
    show timor neutral at right
    timor "El Dr. tiene razón, es nuestra mejor opción por favor ayúdenos Calisto."
    show calisto decepcionada at left
    calisto "Perdón pero no puede dejar pasar una oportunidad así, ustedes hagan lo que quieran."

    narrador "Después de esto vos, Timor y Nostrov se dirigen al taller"

    jump ir_al_taller_auto


# ══════════════════════════════════════════
#  BÚSQUEDA DE PIEZAS (sin cambios)
# ══════════════════════════════════════════
label ir_al_taller_auto:
    scene bg taller

    if dia_auto == 2:
        prota "Este es nuestro segundo día acá. No debe faltarnos mucho."

    jump taller_auto_hub


label taller_auto_hub:
    call screen pantalla_taller_auto
    $ resultado = _return

    if resultado == "listo":
        jump auto_dia2_completo
    else:
        jump expression "auto_encontrar_" + resultado


label auto_encontrar_pieza:
    prota "Acá hay algo muy pesado, voy a necesitar su ayuda."
    prota "Empujemos juntos, 3, 2, 1, YA."

    narrador "Con mucho esfuerzo sacan el motor."

    if dia_auto == 1:
        show nostrov serio
        nostrov "Todo parece estar en buen estado excepto los cables."
        if tiene_cables:
            show nostrov feliz
            nostrov "Por suerte ya tenemos un par."
        else:
            nostrov "No debería ser muy difícil encontrar un par."
        show timor feliz at right
        timor "Que suerte la maldición no parece haber afectado mucho esta parte del edificio."
        prota "Si claro como vos digas."
        $ costo = 2
    else:
        show timor feliz
        timor "Que suerte la maldición no parece haber afectado mucho esta parte del edificio."
        prota "Si claro como vos digas."
        $ costo = 2
    hide timor 
    hide nostrov
    $ tiene_pieza = True
    $ energia_auto -= costo
    jump auto_tras_encontrar_item


label auto_encontrar_gato:
    if dia_auto == 1:
        show nostrov feliz
        nostrov "¡Camaradas miren esto!"
        prota "¿Que encontraste Nostrov?"
        show nostrov serio
        nostrov "Es un... ¿Como se llama esto en español? La herramienta para levantar autos."
        prota "¿Un gato?"
        show nostrov confundido
        nostrov "¿Que? NO ¿que haría un pequeño e indefenso michi aquí? ¿Y como nos ayudaría con el auto?"
        prota "No ese tipo de gato, un gato hidráulico."
        show nostrov feliz
        nostrov "Ahh, si encontré eso."
        $ costo = 2
    else:
        show timor feliz
        timor "¡Encontré un gato!"
        prota "¿Un gato?"
        show timor neutral
        timor "La herramienta, no el animal."
        prota "Ahh, claro."
        $ costo = 1

    hide timor
    hide nostrov
    $ tiene_gato = True
    $ energia_auto -= costo
    jump auto_tras_encontrar_item


label auto_encontrar_rueda:
    narrador "Después de revolver en una pila de piezas rotas, sucias y viejas encuentras una rueda"
    narrador "La revisas bien para asegurarte de que no este pinchada y la inflan"

    $ tiene_rueda = True
    $ energia_auto -= 1
    jump auto_tras_encontrar_item


label auto_encontrar_llave_cruz:
    show timor feliz
    timor "¡Una cruz, estamos a salvo!"
    narrador "Remueve la pieza de la pila"
    show timor confundida
    timor "Esperen, esto no es una cruz ¿Les sirve?"
    prota "SI, va a ser ideal para cambiar las ruedas."
    show timor feliz
    timor "Perfecto entonces la llevamos."
    hide timor
    $ tiene_llave_cruz = True
    $ energia_auto -= 1
    jump auto_tras_encontrar_item


label auto_encontrar_cables:
    show timor neutral
    timor "Eu chicos encontré algo."
    prota "¿Que es?"
    timor "Son un par de cables, parecen estar en muy buen estado."

    if dia_auto == 1:
        show nostrov feliz at right
        nostrov "Buen descubrimiento camarada. Van a sernos útiles."
    else:
        prota "Buen descubrimiento, probablemente sean útiles."
    hide timor
    hide nostrov
    $ tiene_cables = True
    $ energia_auto -= 1
    jump auto_tras_encontrar_item


label auto_tras_encontrar_item:
    if energia_auto > 0:
        jump taller_auto_hub
    elif dia_auto == 1:
        jump descanso_dia1_auto
    else:
        jump descanso_dia2_auto


label descanso_dia1_auto:
    show timor cansada
    timor "Ya fue mucho por hoy, si seguimos trabajando no vamos a poder escapar hoy ni nunca."
    show nostrov serio at right
    nostrov "La Dra. tiene razón, descansemos por hoy."

    narrador "Todos vuelven a reunirse"
    scene bg sala_comun

    prota "¿Como le fue Calisto?"
    show calisto decepcionada at left
    calisto "Eso... no importa"
    show nostrov serio at right
    nostrov "Camaradas tengo algo que decirles."
    prota "¿Que pasa Nostrov?"
    show nostrov orgullo_ruso at right
    nostrov "No puedo seguir intentando arreglar el auto. Mi orgullo me pide a gritos que arregle ese generador. Les deseo lo mejor."
    show timor asustada
    timor "¡¿QUE?! Pero si vos mismo dijiste que la opción lógica es arreglar el auto, ¿De que te sirve arreglar la electricidad si seguimos acá encerrados con esa momia?"
    prota "Déjalo Timor, es el camino que eligió y debemos respetarlo."
    show nostrov feliz at right
    narrador "Nostrov te agradece el gesto con la mirada, muertos de sueño todos van a dormir"

    jump dia_2_auto


label dia_2_auto:
    scene bg sala_comun
    narrador "Es difícil descansar bien con tanto frío. Igualmente Timor y tu se levantan listos para terminar lo que empezaron"

    prota "No creo que hayamos encontrado todo lo que necesitamos del taller, deberíamos volver a ir."
    show timor neutral
    timor "Estoy de acuerdo, vamos."

    $ energia_auto = ENERGIA_AUTO_DIA_2
    $ dia_auto = 2

    jump ir_al_taller_auto


label auto_dia2_completo:
    prota "No creo que podamos sacar mas cosas de acá."
    show timor neutral
    timor "Si, eso parece ser todo lo valioso que hay. ¿Ahora que hacemos?"

    menu:
        "Descansar":
            jump descanso_dia2_auto
        "Intentar reparar el auto":
            jump intentar_reparar_auto


label descanso_dia2_auto:
    show timor cansada
    timor "Odio tener que admitirlo, con tan poco tiempo hasta que se descongele esa cosa, pero ya no doy más."
    prota "Esta bien, no te preocupes, mañana seguro terminamos."

    narrador "Todos vuelven a reunirse"
    scene bg sala_comun
    prota "¿Como le fue Calisto?"
    show calisto enojada
    calisto "¿Como se ve que me fue?"
    show timor triste at right
    timor "No muy bien diría, debe ser la maldición, ayúdanos y escapemos antes."
    calisto "Escapar, escapar, escapar ¿Por que estas tan obsesionada con escapar?"
    show timor asustada at right
    timor "¡La maldición! Cuantas veces tengo que repetirlo."
    calisto "¡No hay maldición! Sos la mejor química y cirujana de tu generación ¿Y en que gastas tu talento? un auto que lleva años acá."

    narrador "Por un momento que parece una eternidad se hace un silencio"

    prota "Y... ¿Como te fue Nostrov?"
    show nostrov orgullo_ruso at left
    nostrov "Ese generador me esta dando pelea camarada. Pero yo nunca escapo de una buena pelea."
    prota "Si, eso imagine."

    narrador "Muertos de sueño todos van a dormir"

    jump dia_3_auto


label dia_3_auto:
    narrador "Ya tienen todo lo necesario y el tiempo no esta de su lado, van directo a intentar reparar el auto."

    $ energia_auto = ENERGIA_AUTO_DIA_3
    $ dia_auto = 3

    jump intentar_reparar_auto


# ══════════════════════════════════════════
#  REPARAR EL AUTO — point & click clásico
#  (seleccionar objeto del inventario → click en la escena)
# ══════════════════════════════════════════
label intentar_reparar_auto:
    scene bg taller

    narrador "El auto tiene una rueda pinchada y el motor no parece funcionar"
    narrador "Intentar cosas sin sentido solo les va a gastar energía, ¿Que van a hacer?"

    $ item_seleccionado = None
    jump reparar_auto_hub


label reparar_auto_hub:
    call screen pantalla_reparar_auto
    $ target = _return

    if target == "arrancar":
        jump ver_final_auto

    $ resultado = auto_evaluar(target)
    jump expression "auto_resultado_" + resultado


label auto_resultado_rueda_gato:
    prota "El gato es la herramienta perfecta para esto, que bueno que la encontramos."
    prota "Ahora deberíamos sacar esa rueda vieja."
    $ auto_paso_rueda = 1
    jump auto_post_intento

label auto_resultado_rueda_cruz:
    show timor feliz
    timor "La cruz que encontré es perfecta para sacar la rueda."
    prota "Si, ahora solo queda poner la nueva."
    hide timor
    $ auto_paso_rueda = 2
    jump auto_post_intento

label auto_resultado_rueda_colocar:
    prota "Esta vieja rueda va a terminar siendo nuestra salvación."
    prota "La rueda nueva ya esta arreglada, ahora debería enfocarme en arreglar el motor."
    $ auto_paso_rueda = 3
    $ rueda_colocada = True
    jump auto_post_intento


label auto_resultado_motor_cruz:
    prota "Que bueno que lo abrimos, todos estos cables están destrozados."
    $ auto_paso_motor = 1
    jump auto_post_intento

label auto_resultado_motor_cables:
    show timor neutral
    timor "Déjame esto a mí, soy extremadamente precisa."
    prota "Ok, confió en vos. Ya estamos cerca."
    narrador "La Dra. Timor cambia los cables con una precision y velocidad increíble."
    show timor feliz
    prota "Wow, que velocidad."
    prota "Ahora deberíamos reorganizarlo en su lugar."
    hide timor
    $ auto_paso_motor = 2
    jump auto_post_intento

label auto_resultado_motor_colocar:
    prota "Un ultimo esfuerzo y ya estamos. Hagámoslo juntos. 3, 2, 1, YA."
    narrador "Uniendo sus fuerzas ponen el nuevo motor en su lugar y parece funcionar"
    $ auto_paso_motor = 3
    $ motor_colocado = True
    jump auto_post_intento

label auto_resultado_fail:
    prota "Me parece que esto no funciono."
    jump auto_post_intento


label auto_post_intento:
    $ destino = auto_gastar_energia(1)
    if destino:
        jump expression destino
    else:
        jump reparar_auto_hub


label ver_final_auto:
    prota "Solo queda ver si funciona..."
    narrador "Mientras giras la llave Timor empieza a rezar"
    show timor asustada
    timor "Padre nuestro que estas en el cielo..."
    narrador "Se hace un momento de silencio y..."

    if rueda_colocada and motor_colocado:
        prota "¡FUNCIONO!"
        show timor feliz
        timor "¡LO LOGRAMOS!"
        timor "Hay que ir a avisarle a los demás."
        hide timor
        narrador "Emocionados Timor y el protagonista van a buscar a los demás, Nostrov accede alegremente a subir al auto y escapar. Calisto al principio le cuesta dejar a Ötzi ahí y la oportunidad que ve en el pero entra en razón y termina aceptando."
        narrador "Después de informarle a las autoridades del país el lugar donde se encuentra Ötzi es sellado permanentemente y eso hace muy feliz a Timor."
        narrador "Al día de hoy nadie se atrevió a entrar."

        scene black with fade
        centered "Final bueno ruta escape en auto escrito por Juan Cruz Izurieta."

        $ registrar_final("auto_bueno")
    else:
        prota "No... no prende."

        narrador "En ese momento escuchan el hielo quebrarse y a la Dra. Calisto gritar"

        calisto "Noooooooooooooooo."

        narrador "En sus últimos momentos antes de partir, se lanzan una mirada reconociendo el esfuerzo del otro y se abrazan antes de morir."

        scene black with fade
        centered "Final malo ruta escape en auto escrito por Juan Cruz Izurieta."

        $ registrar_final("auto_malo")

    return