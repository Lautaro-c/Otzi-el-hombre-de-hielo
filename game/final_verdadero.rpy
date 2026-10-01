label final_bueno_hub:
    scene bg sala_comun

    prota "Lo peor que podemos hacer ahora es separarnos y remar en direcciones opuestas, tenemos que estar unidos y pensar una solucion."
    prota "Oye Calisto, te puedo pedir un favor?"
    calisto "Ah, si. Que necesitas?"
    prota "Creo que en este momento lo que mas necesitamos es estar unidos."
    calisto "Estoy de acuerdo, pero esos dos nunca se pondran de acuerdo."
    prota "Lo se, pero hay que intentarlo, puedes ir a buscar a uno mientras busco al otro?"
    calisto "Claro, a quien quieres buscar tu?"

    menu:
        "Buscar a Timor":
            jump buscar_a_timor
        "Buscar a Nostrov":
            jump buscar_a_nostrov


label buscar_a_timor:
    $ busco_a = "timor"

    prota "Ire a buscar a Timor, quiero ver si puedo calmarla un poco. Confio en ti para que convenzas a Nostrov."
    calisto "Entiendo."
    narrador "Te sonrie gentilmente."
    prota "Pasa algo?"
    calisto "No es nada."

    narrador "La doctora Calisto va a buscar a Nostrov"

    jump cuarto_de_timor


label buscar_a_nostrov:
    $ busco_a = "nostrov"

    prota "Ire a buscar a Nostrov intentare convencerlo de venir, creo que es mas facil que tu calmes a Timor,"
    calisto "Entiendo."
    narrador "Te sonrie gentilmente."
    prota "Pasa algo?"
    calisto "No es nada."

    narrador "La doctora Calisto va a buscar a Timor"

    jump sala_del_motor


label cuarto_de_timor:
    scene bg cuarto_timor with fade

    prota "Timor... Queria, llamarte a la sala principal... Esta todo bien?"
    narrador "Dice al verla cubierta entre sus sabanas"

    narrador "Timor no responde"

    prota "Te molesta si me siento a tu lado un momento?"
    narrador "Timor niega con la cabeza, aun cubierta por las sabanas"

    prota "*Se sienta a su lado* Tienes miedo de la maldicion no?"
    timor "Si..."
    narrador "Dice con una voz debil desde debajo de las sabanas"

    prota "Es normal sentir eso... No voy a mentir que tambien me asuste bastante cuando se fueron las luces."
    timor "..."
    prota "Pero aun asi no es momento de quedarse escondida... Si quieres que todo salga bien y que la maldicion no se cumpla, lo mas importante es relajarse y pensar con la cabeza fria."
    timor "Pero... Y si me pasa algo?"
    narrador "Dice sacando la cabeza de las sabanas con una expresion asustada"

    prota "Entonces yo te protegere."
    narrador "Dice sonriendo"

    narrador "Timor se sonroja mucho"
    timor "Tonto..."

    prota "Oh vamos!"
    narrador "Digo riendo"

    timor "Querias que vaya a la sala principal no?"
    prota "Si."
    timor "Dame un momento a solas... Esperame ahi..."
    prota "Perfecto."

    narrador "Mientras me retiro, puedo ver por el rabillo del ojo como se tapa la cara sonrojada con las sabanas"

    jump volver_a_la_sala


label sala_del_motor:
    scene bg sala_generador with fade

    prota "Nostrov, como va todo en el motor?"
    nostrov "Estoy investigando la causa de la aberia. Me puedes ayudar con esto?"
    prota "Me encantaria, pero necesito hablar contigo en la sala general."
    nostrov "Como podras notar, estoy un poquito ocupado. No podemos hablarlo en otro momento?"
    prota "Prometo que no durara mucho, es importante que sea ahora."
    nostrov "Mas te vale que no sea una estupidez."

    jump volver_a_la_sala


label volver_a_la_sala:
    scene bg sala_comun

    if busco_a == "nostrov":
        narrador "Vuelvo a la sala con Nostrov detras mio"
        narrador "Poco despues veo llegar a Calisto con Timor un poco irritada a su espalda"
    else:
        narrador "Vuelvo a la sala y veo a Nostrov con Calisto jugando a las cartas"

        nostrov "Adivino, esa gallina sigue encerrada en su cuarto asustada."
        timor "A quien le dices gallina?!"
        narrador "Dice entrando detras mio justo despues"
        nostrov "A quien mas?"
        calisto "Vamos, no se peleen."

    jump empezar_la_reunion


label empezar_la_reunion:
    calisto "Okay ahora que estamos todos. Que querias hablar doctor?"
    prota "Okay, tenemos que decidir que hacer ahora."
    nostrov "Lo mas optimo es arreglar la electricidad."
    timor "Lo mas seguro es encontrar una forma de irnos de aquí y volver cuando la tormenta pare."
    nostrov "Irnos para que? Morir en el hielo"
    timor "Y que haras si no logras reparar el generador? Morirte de hambre"

    narrador "Los 2 se lanzan una mirada de muerte, suspirando les digo"

    prota "No se peleen, ustedes 2 tienen esas ideas. Calisto, que piensas?"
    calisto "Personalmente queria analizar un poco mas a Otzi."
    prota "Entiendo. Los 3 tienen ideas muy distintas de que hacer, asi que es imposible que lleguemos a un mismo lugar."
    nostrov "Y entonces que sugieres."
    prota "Revivamos a Otzi."

    jump revelacion_clon


# Twine: "Peru" — asumo que es un typo de "Pero"; renombrado a algo descriptivo.
label revelacion_clon:
    narrador "Todos se quedan callados un segundo y de la nada Nostrov se empieza a reir"

    nostrov "¿Revivir a Otzi?! Estas bromeando no?"
    timor "Porque Querrias revivir a esa Momia maldita?!"
    calisto "... Espera. Tu eres..."
    narrador "Sonrie"

    prota "Me trajeron aquí desde el centro de tecnologias de clonacion, para probar si podia traer a Otzi a la vida Es la razon de la creacion de este centro."
    nostrov "Espera... Estas hablando en serio? Para eso eran esas maquinas tan extrañas."
    prota "En efecto, pero para poder hacerlo necesito su ayuda."
    timor "Espera Espera, porque quieres revivir a Otzi ahora?!"
    prota "Porque esa es la razon por la que estamos nosotros aquí, sabian que la tormenta vendria. Es necesario que el cuerpo este en una temperatura minima para poder clonarse sin que las maquinas se sobrecalienten."
    nostrov "Por eso vinieron a esta zona tan alejada dentro de mi pais..."
    prota "Exactamente. Si esperamos a que termine la tormenta, quizas no volvamos a tener otra oportunidad."
    timor "Ahhh pero y la maldicion?!"
    prota "La señorita Calisto puede encargarse de eso."

    jump hablar_todos


label hablar_todos:
    calisto "Asi que lo sabes todo... Si, hace mucho desarolle una teoria de que la maldicion de Otzi provenia de una enfermedad del pasado para la cual no tenemos anticuerpos."
    prota "Si queremos revivirlo, tendremos que reparar la electricidad para activar la maquina. Ahi es donde entras tu."
    narrador "Señalo a Nostrov y este sonrie confiado"

    prota "Y ademas tenemos que desarollar la cura para que todo salga bien."
    calisto "Puedes confiar en mi."
    timor "Y yo que tendria que hacer?"
    narrador "Pregunta timida"

    prota "Tu tienes la parte mas importante."
    narrador "Sonrie"
    prota "Seras la que reviva a Otzi."
    timor "QUE?!"

    jump minijuego_dias_final_bueno


label minijuego_dias_final_bueno:
    narrador "Los point and click de esta ruta son complicados porque en los 3 dias tienes que ayudar a Calisto y Nostrov a la vez, pero como para llegar aca ya hiciste sus rutas es facil saber que hacer sin perder mucho tiempo. Al final del tercer dia si hiciste todo bien se llega al climax."

    # TODO: minijuego combinado de 3 días (rutas de Calisto y Nostrov a la vez).
    # El material original no detalla la mecánica más allá de esta descripción;
    # de momento pasa directo al día 4.

    jump dia_4_final_bueno


label dia_4_final_bueno:
    scene bg laboratorio_entrada

    prota "Estas lista?"
    timor "Me repites porque tengo que ser yo la que haga esto?!"
    prota "Este proceso requiere precision milimetrica, cualquier minimo error puede causar una catastrofe, eres la mejor calificada del pais, no, posiblemente del mundo para este trabajo."
    timor "Ahhh... Esta bien esta bien!"
    narrador "Dice sonrojada acercandose a la maquina en la cual esta el cuerpo de otzi"

    prota "Nostrov, emcargate de la maquinaria, Calisto, Extrae el adn. Por mi parte, me encargare de la reconstruccion. Entendido?!"
    calisto "Si!"
    nostrov "Si señor."
    timor "S-Si!"

    narrador "Mientras digo eso me siento en la pc y activo la maquina de extraccion de adn"

    jump point_and_click_final


label point_and_click_final:
    narrador "La secuencia de point and click mas dificil, tenes que revisar que el adn se extraiga con exito, Timor lo repare e inserte cuidadosamente en la maquina de clonacion y generar el clon con exito."
    narrador "Si la logras completar sin fallar, obtienes la secuencia final. Si fallas, vas a un game over y lo puedes reintentar"

    # TODO: igual que el minijuego de 3 días, este tampoco tiene mecánica
    # detallada ni un passage de fallo real en el material original —
    # solo la descripción y el link directo al final bueno.

    jump final_bueno_verdadero


label final_bueno_verdadero:
    timor "Lo hicimos?"
    calisto "Esta... Esta hecho!"
    nostrov "Ja, sabia que funcionaria."
    prota "Solo nos queda abrirla..."

    narrador "La capsula con el clon de Otzi se abre y de dentro de ella..."

    scene black with fade
    centered "{b}FIN{/b}"

    $ registrar_final("final_verdadero")
    return