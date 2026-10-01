label start:
    jump introduccion

label introduccion:
    scene bg exterior_nieve with fade

    centered "Ubicación: Siberia, Rusia.\nFecha: Septiembre de 2006"

    narrador "Hace ya 15 años encontraron el cuerpo de Ötzi en la nieve, con la innovación de los tratamientos químicos, se decidió llevar el cuerpo a un laboratorio en Rusia para su reconstrucción."
    narrador "Eres un doctor que fue mandado a ese laboratorio a analizar el cuerpo."

    jump afuera_del_laboratorio


label afuera_del_laboratorio:
    scene bg exterior_nieve

    narrador "El frio es brutal, el ambiente totalmente congelado, mientras el viento es tan fuerte que parece que saldrás volando y te impide ver absolutamente nada."
    narrador "Afortunadamente, tus superiores te dieron un traje térmico que te permite mantenerte firme y no morir de hipotermia, aunque el frio sigue siendo muy fuerte."

    prota "¡Maldita sea! ¡Agh! Debería estar por aquí."

    menu:
        "Seguir recto.":
            jump seguir_recto
        "Buscar en tu GPS.":
            jump buscar_en_tu_gps


label seguir_recto:
    narrador "Avanzas, tus pasos son fuertes y tu determinación lo es mas. Cada paso te acerca mas, repites en tu cabeza una y otra vez, hasta que finalmente."

    prota "¿Eso es?"

    narrador "Logras ver una luz a la distancia y corres a la misma."

    jump introduccion_al_conflicto


label buscar_en_tu_gps:
    narrador "Intentas mirar tu GPS, pero no hay ningún tipo de señal, parece que esto no es una tormenta normal."

    prota "¡Dios, casi no puedo ni verme a mi mismo con tanta nieve!"

    narrador "Cuando estabas por darte la vuelta y volver a intentarlo con un mejor clima, logras ver una luz a la distancia y corres a la misma por calor."

    jump introduccion_al_conflicto


label introduccion_al_conflicto:
    scene bg laboratorio_entrada with fade

    narrador "Llegas al laboratorio desde la enorme tormenta de nieve, pasas unos minutos quitándote el traje, respirando y entrando en calor, hasta que decides ir a la sala principal donde ves."
    show nostrov enojado
    narrador "Un ruso con cara de pocos amigos."
    hide nostrov
    show timor neutral
    narrador "Una chica de aspecto sombrío."
    hide timor neutral
    show calisto canchera
    narrador "Una mujer de apariencia madura y una bata de laboratorio."
    hide calisto

    jump primer_conflicto


label primer_conflicto:
    scene bg sala_comun with fade
    show timor asustada
    timor "No lo entienden, ¡esta momia tiene una maldición! ¡Tenemos que terminar esto e irnos lo antes posible!"
    show nostrov enojado at right
    nostrov "¡¿Maldición?! Esto no es una película de terror señorita, ¡es la vida real!"
    show calisto decepsionada at left
    calisto "..."
    show calisto sonriente at left
    calisto "Tu debes ser el nuevo. ¿Como fue el viaje?"
    hide calisto
    hide timor 
    hide nostrov

    menu:
        "Mal":
            jump viaje_mal
        "Bien":
            jump viaje_bien


label viaje_mal:
    prota "Horrible, la nieve no me dejo ver nada, estuve perdido un buen rato."
    show calisto sonriente
    calisto "Que bueno que llegaste bien entonces, según parece pronto va a haber una tormenta, espero que no pase nada malo."
    show timor asustada at left
    timor "¡No digas eso! ¡Da mala suerte!"
    show calisto canchera
    nostrov "¿Mala suerte? Tonterías, eso no existe, este lugar esta sellado, ¡No va a pasar nada!"

    hide nostrov
    hide calisto
    hide timor
    narrador "Justo al momento que dice eso, las luces del lugar se cortan."

    prota "Eso fue un muy mal tiempo..."

    jump charla_tormenta


label viaje_bien:
    prota "Dentro de todo me fue bien, con la nieve que hay afuera, era posible que nunca llegara aquí, jaja."
    show calisto sonriente
    calisto "¡Genial! Segun parece pronto va a haber una tormenta, así que tuviste mucha suerte de que no te paso nada."
    show nostrov serio at right
    nostrov "Parece que por la tormenta tendremos que sellar todas las puertas."
    show timor asustada at left
    timor "¿¡Sellar las puertas!? ¿¡Nos vamos a quedar atrapados con esa momia?!"
    show nostrov enojado at right
    nostrov "¡Te preocupas demasiado, no va a pasar nada malo!"

    hide nostrov
    hide calisto
    hide timor
    narrador "Justo al momento que dice eso, las luces del lugar se cortan."
    

    prota "Eso fue un muy mal tiempo..."

    jump charla_tormenta


label charla_tormenta:
    narrador "Rápidamente Nostrov enciende su linterna de emergencia y nos pasa unas a nosotros también."
    show timor asustada
    timor "¿¡Qué paso?!"
    show nostrov serio at right
    nostrov "La tormenta debe haber dañado al generador..."
    show calisto preocupada at left
    calisto "Esto es peligroso... Si no lo solucionamos pronto se descongelara Otzi."
    timor "¡Lo dije! ¡La maldición ya nos esta afectando! ¡Tenemos que salir de aquí rápido!"
    hide timor
    narrador "Timor se acerca a la puerta por la que vine, pero cuando la abre una ola enorme de viento la empuja hacia atrás."
    prota "¡Maldición! ¡Cierra eso!"
    hide nostrov
    narrador "Nostrov cierra la puerta."
    show nostrov enojado at right
    nostrov "¡¿Eres tonta?! ¡¿Quieres irte a morir en el hielo?!"
    show timor asustada
    timor "Ya empezó... No hay salida... Todos vamos a morir..."
    show calisto sonriente
    narrador "Calisto se acerca a confortarla pero antes de poder hacer nada Timor se aleja corriendo."
    hide timor
    nostrov "Agh, que mujer irracional, ire a revisar el generador."
    hide nostrov
    narrador "Dice retirándose también."
    show calisto preocupada
    narrador "Calisto se pone una mano en la cabeza, sentándose en la silla."
    hide calisto

    menu:
        "Ir a ver si la doctora Timor esta bien.":
            jump doctora_timor
        "Ir a ayudar a Nostrov con el generador.":
            jump ruso
        "Quedarse a hablar con Calisto.":
            jump doctora_calisto
        "Llamarlos a todos." if todos_los_finales_vistos():
            jump final_bueno_hub