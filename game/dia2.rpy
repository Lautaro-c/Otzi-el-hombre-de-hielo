label dia2_inicio:
    $ dia = 2
    $ energia = ENERGIA_DIA_2
    scene bg sala_comun with fade

    if investigacion_otzi >= 3:
        narrador "El día anterior con la Dra. Calisto fue muy productivo deciden continuar trabajando juntos para descubrir la verdad tras el misterio de Ötzi"
    elif investigacion_otzi > 0:
        narrador "El día anterior con la Dra. Calisto fue productivo deciden continuar trabajando juntos para descubrir la verdad tras el misterio de Ötzi"
    else:
        narrador "Aunque el día anterior no fuiste de mucha ayuda, después de una larga, y un poco humillante, disculpa deciden trabajar juntos para descubrirla verdad tras el misterio de Ötzi"

    if investigacion_otzi >= 1:
        show calisto sonriente
        calisto "Okey sospechamos que Ötzi sufre de algún tipo de enfermedad, pero todavía no tenemos certeza de cual. Para encontrar la cura voy a necesitar equipamiento, deberíamos encontrarlo en el almacén. Vamos a buscarlo."
        jump almacen
    else:
        show calisto decepsionada
        calisto "No tenemos ni idea de que pasa con Ötzi, deberíamos ir e inspeccionarlo nuevamente ¿O preferís primero ir a buscar los suministros?"
        menu:
            "Ir al almacén de suministros":
                jump almacen
            "Volver a revisar a Ötzi":
                jump sala_otzi


label me_mentiste:
    $ relacion_calisto -= 10
    show calisto enojada
    calisto "Me mentiste, no puedo creer que lo hayas vuelto a hacer, no se porque sigo escuchándote."
    prota "Perdón tenes que entenderlo, el frio es insoportable y con estas linternas no se ve nada. No es mi culpa que estemos en esta situación."
    calisto "¿Entonces es mía?"
    prota "No para nada lo qu-"
    calisto "¡Córtala! Ninguno eligió esta situación, se nos dio una oportunidad unica y la tomamos."
    calisto "Que las cosas salgan tan mal no estaba en ninguno de nuestros planes pero aca estamos y tenemos que resolverlo."
    show calisto canchera
    calisto "Entonces que vas a decidir ¿Ser el que se rindió ante las circunstancias o el que ayudo a una genia a lograr la mayor hazaña medica de la historia?"
    prota "Perdón, tenes razon, no voy a dejarme superar por las circunstancias, juro que voy a ayudarte."
    show calisto decepsionada
    calisto "Ya no quiero promesas vacías, no falta nada para que Ötzi se descongele y no puedo sola, mañana quiero ver otra versión tuya, sin excusas."
    prota "Si Dra."

    narrador "Por mas de que estaban en el mismo edificio el viaje silencioso devuelta a donde estaban los demás se hizo eterno. Aunque se hayan hecho promesas la relación con la Dra. Calisto nunca va a ser igual"
    narrador "Todos estaban frustrados por no haber llegado a ningún lado con sus planes, agotados y abatidos se van a dormir"
    jump dia3_inicio


label reagruparse_dia2:
    scene bg sala_comun

    if investigacion_otzi >= PISTAS_PARA_CURA:
        show calisto emocionada
        calisto "Creo que lo logramos Dr. ya tengo toda la información y herramientas necesarias para encontrar la cura. Mañana con las energías renovadas voy a dedicarme completamente a eso."
        show calisto sonriente
        calisto "Le agradezco mucho todo su apoyo y espero que podamos salir de esto siendo amigos."
        prota "Dra. TODO es gracias a usted, yo solo hago mi mayor esfuerzo por ayudarla."
        hide calisto
        narrador "Ambos vuelven contentos a donde se encuentran los demás"
        show timor asustada at right
        timor "¡ALTO! ¿Como puedo saber que no están poseídos por la maldición?"
        show calisto decepsionada
        calisto "No moleste Timor, no hay maldición, solo virus y bacterias, y trajimos lo necesario para probarlo."
        show nostrov enojado at left
        nostrov "Bravo camaradas, consiguieron lo que buscaban. Pero ¿Y ahora que? Descubren que efectivamente hay un virus ¿y lo resuelven en un solo día?"
        nostrov "Que inmaduros. Yo ya podría haber arreglado ese generador y no pasaríamos otra noche de frio, pero ustedes se niegan a cooperar y esta miedosa solo busca escapar."
        prota "Mañana se va a decidir todo, y van a ver que nuestros esfuerzos no fueron en vano."

        narrador "Por mas de que el ansia por lo que pasara mañana es mucha, el cansancio los supera y deciden dormir. Mañana es el día decisivo."
        $ relacion_calisto += 2

    elif investigacion_otzi >= 3:
        show calisto sonriente
        calisto "Hoy no se logro, pero estamos muy cerca, puedo sentirlo."
        prota "Pienso lo mismo Dra. mañana lo lograremos."
        hide calisto
        narrador "Ambos vuelven pensando que podría ser lo que les falta"
        show timor asustada at right
        timor "¡ALTO! ¿Como puedo saber que no están poseídos por la maldición?"
        show calisto decepsionada
        calisto "No moleste Timor, no hay maldición, solo virus y bacterias, y mañana vamos a probarlo."
        show nostrov enojado at left
        nostrov "Bravo camaradas, ¿consiguieron lo que buscaban?. Yo ya podría haber arreglado ese generador y no pasaríamos otra noche de frio, pero ustedes se niegan a cooperar y esta miedosa solo busca escapar."
        prota "Mañana se va a decidir todo, y van a ver que nuestros esfuerzos no fueron en vano."

        narrador "Por mas de que el ansia por lo que pasara mañana es mucha, el cansancio los supera y deciden dormir. Mañana es el día decisivo."
        $ relacion_calisto += 1

    elif investigacion_otzi > 0:
        show calisto preocupada
        calisto "Estamos mucho mas lejos del objetivo de lo que pensaba. Pero no podemos bajar los brazos, tenemos que seguir adelante, es nuestra unica opción."
        prota "Tambien me preocupa Dra. pero tenemos que mantenernos unidos."
        hide calisto
        narrador "Ambos vuelven pensando que podría ser lo que les falta"
        show timor asustada at right
        timor "¡ALTO! ¿Como puedo saber que no están poseídos por la maldición?"
        show calisto decepsionada
        calisto "No moleste Timor, no hay maldición, solo virus y bacterias, o eso creemos."
        show nostrov enojado at left
        nostrov "Bravo camaradas, ¿consiguieron lo que buscaban?. Yo ya podría haber arreglado ese generador y no pasaríamos otra noche de frio."
        nostrov "Pero ustedes se niegan a cooperar y esta miedosa solo busca escapar."
        prota "Mañana se va a decidir todo, tengas razon o no ya no importa."

        narrador "Por mas de que el ansia por lo que pasara mañana es mucha, el cansancio los supera y deciden dormir. Mañana es el día decisivo."

    else:
        narrador "Nadie dijo ni una palabra esa noche, solo cayeron dormidos, victimas del cansancio."

    jump dia3_inicio