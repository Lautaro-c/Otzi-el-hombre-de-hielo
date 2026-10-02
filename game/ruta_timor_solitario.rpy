label doctora_timor:
    scene bg sala_comun

    $ busco_a = "timor"

    show timor asustada
    timor "Tenemos que escapar."
    prota "¿Por que?"
    timor "Esa momia, tiene una maldición, ya se llevo a los científicos anteriores, ahora vendrá por nosotros."
    prota "¿Y como escaparías con este clima?"

    jump como_piensas_escapar


label como_piensas_escapar:
    timor "Como yo lo veo tenemos 2 opciones escapar con el auto o con el traje."
    prota "Pero el auto no funciona, ¿Cómo lo usaríamos?"
    timor "Hay una habitación llena de partes viejas de autos y mecánica, ahí debe haber algo que nos sirva."
    prota "Podría ser cierto, antes mencionaste el traje pero solo tenemos uno ¿Pretendes escapar sola?"
    timor "No, no, lo que yo digo es que uno debería llevar el traje pedir refuerzos y volver por los demás. Iría yo, pero no podría con este clima. Vos sos la mejor opción, sos fuerte y no confió en Nostrov para que vaya el."
    timor "¿Entonces que vas a hacer?"

    menu:
        "Escape solitario":
            jump escape_solitario
        "Escape en auto":
            jump escape_en_auto


label escape_solitario:
    scene bg sala_comun

    show timor neutral at left
    show calisto preocupada at right
    show nostrov serio

    prota "Con la Dra. Timor decidimos que sería una buena idea si voy en busca de ayuda, nada esta funcionando dentro de este lugar. Esperar encerrados solo seria esperar a la muerte."
    
    show nostrov enojado
    nostrov "Muerte sería salir ahi afuera en estas condiciones, no te detendre si eso es lo que preguntas. Me servirá el silencio para intentar reparar la electricidad."
    
    show timor asustada at left
    timor "E-Ey nno va a morir, solo nececitamos que encuentre ayuda. Y resistir hasta entonces, solo asi nos salvaremos."
    nostrov "Eres una idiota si planeas esperar ayuda que no va a venir, nuestra mejor opcion es reparar el generador y esperar la tormenta."
    
    show calisto decepcionada at right
    calisto "Pelearnos no llevara a ningun lado."
    calisto "Estas seguro de esto?"
    prota "Si, volvere con ayuda pronto, lo prometo."

    narrador "Deberias preparar unas cosas, no es buena idea salir con las manos vacias."

    $ objetos_faltantes = 3
    $ linterna = False
    $ abrigo = False
    $ comida = False

    jump prepararse

label prepararse:
    scene bg sala_comun

    call screen pnc_ts

    jump expression _return

label linterna:
    $ objetos_faltantes -= 1
    $ linterna = True

    narrador "Agarraste una linterna."

    if (objetos_faltantes == 0):
        jump salir_refugio_solitario
    else:
        jump prepararse

label abrigo:
    $ objetos_faltantes -= 1
    $ abrigo = True

    narrador "Agarraste una mochila."

    if (objetos_faltantes == 0):
        jump salir_refugio_solitario
    else:
        jump prepararse

label comida:
    $ objetos_faltantes -= 1
    $ comida = True

    narrador "Agarraste comida para tu viaje."

    if (objetos_faltantes == 0):
        jump salir_refugio_solitario
    else:
        jump prepararse


label salir_refugio_solitario:

    narrador "Supongo que con eso sera suficiente."    

    scene bg exterior_nieve with fade

    narrador "Apenas das un paso fuera, sientes instantaneamente el frio de la nevada en el exterior."
    narrador "Pese a esto, decides caminar en busqueda de cualquiera capaz de ayudar. Teniendo como unico punto de referencia el refugio distante y apenas visible."
    narrador "Decides continuar caminando..."

    jump continuar_divagando


label continuar_divagando:
    narrador "Ya perdiendo la noción del tiempo, te das cuenta que se vuelve cada vez mas oscuro. Sacas tu linterna de la mochila para intentar ver mejor..."
    narrador "Blanco... Kilometros y kilometros, perdiste tu unico punto de referencia hace tanto tiempo. Guiandote unicamente por tu sentido de gravedad. Sabiendo que el mejor camino es hacia abajo... Empiezas a dudar si verdaderamente existe una posibilidad en la cual salgas con vida"

    menu:
        "Girar a la izquierda":
            jump circulos
        "Seguir al frente":
            jump avanzar_oscuridad_nieve
        "Girar a la derecha":
            jump muerte_asolada
        "Sentarse en el suelo y descansar un poco":
            jump sentarse_descansar


label circulos:
    narrador "Caminar... Caminar... Caminar..."
    narrador "Es en lo unico que puedes pensar, es lo unico que te distrae del frio. Aunque... A la distancia puede verse una luz ¿Acaso son personas? ¿Sera que al fin estan todos salvados?"
    narrador "Empiezas a correr, logras usar fuerzas que creias no tenias. Empiezas a gritar"

    prota "¿Hola? ¿Alguien me escucha? ¿Hay alguien ahi?"

    narrador "Es entonces que tu sonrisa desaparece, con el solo escuchar una palabra"

    timor "Doctor?"

    scene black with fade
    centered "Fin."

    $ registrar_final("timor_solitario")
    return


label sentarse_descansar:
    narrador "Caminaste demasiado, decides descansar un poco. Te sientas en la fria nieve e intentas revisar si hay algo util que te sirva en tu mochila..."
    narrador "No se te ocurre nada mas que comer una barra energetica para intentar recuperar fuerzas."
    narrador "Empiezas a pensar, tal vez fue todo una horrible idea. Recuerdas a tu casa, todo lo que podrias estar haciendo ahora mismo, todo lo que viviste, todo... Completamente inutil ahora mismo. Ahora mismo... Solo existes tu, y la nieve..."
    narrador "Rendirse no es una opción."

    jump fin_caminando


label fin_caminando:
    narrador "Cada paso cuesta mas que el anterior. El frio te recuerda lo mucho que te duelen tus extremidades ahora mismo. sientes tu cabeza dandote vueltas, y sin sentido de orientación"

    jump fin_caminando_2


label fin_caminando_2:
    narrador "Sigues caminando, El tiempo sigue pasando. No sabes cuanto tiempo estuviste caminando, te sientes muy desorientado, jurarias ya viste la misma roca varias veces ya"

    jump fin_caminando


label avanzar_oscuridad_nieve:
    narrador "Decides dar al menos un ultimo empujón..."
    narrador "Sientes tus piernas frias y entumecidas. Tus manos congeladas, incluso a traves de los guantes. Aun asi, no queda de otra mas que seguir avanzando."

    jump grupo_de_personas


label grupo_de_personas:
    narrador "De repente, logras ver algo a la distancia. ¿Una luz? ¿Alguien quien pueda ayudarlos?"
    narrador "Empiezas a correr en su dirección, recuperando la poca esperanza que te faltaba, ignorando lo cansadas que estan tus piernas."
    narrador "Te encuentras con un grupo de personas..."

    prota "*Gritando a la distancia* ¿H-hola? ¿Hay alguien ahi?"
    desconocido "*Devolviendo el grito* ¿Quién anda ahi?"
    prota "¿Necesito ayuda? Mis compañeros estan aun mas arriba en la montaña, se nos fue la electricidad y temo que alguno muera por la intensa nieve. Necesitamos sacarlos de ahi lo mas rápido posible."
    desconocido "De acuerdo, Siguenos, te llevaremos a la ciudad mas cercana. Pediremos rescate desde ahi."

    jump volver_civilizacion


label volver_civilizacion:
    narrador "Por fin... Pensaste que nunca acabaria... Que moririas ahi fuera, congelado."
    narrador "Pero aún no acabó, lograste volver a salvo, ahora solo necesitas pedir ayuda."
    narrador "Junto con el grupo de personas, se dirigen a llamar a un equipo de rescate."

    prota "Necesitamos ayuda, hay unas personas aun en la montaña. No tienen electricidad y podrian morir en cualquier momento"
    rescatista "Lo siento, pero tendran que esperar. La tormenta no nos dejara buscar apropiadamente, solo estariamos arriesgandonos a perder a mas personas, habra que esperar a la mañana. Podremos enviar un helicoptero entonces."

    narrador "Temes no llegar a tiempo, pero no hay nada que puedas hacer por ahora. Tendras que aceptar la situación y esperar hasta mañana."

    jump salvar


label salvar:
    narrador "Ya es de mañana. No pudiste dormir en toda la noche, aun preocupado por tus camaradas."
    narrador "Te subes al helicoptero"

    prota "Puedo guiarlos, recuerdo el camino de memoria."

    narrador "Los guias hacia el resto de tu equipo. Se tardan un poco, pero por suerte, logran encontrarlo relativamente rápido."
    narrador "Aterriza el helicoptero y te preparas para entrar"

    jump ir_a_salvarlos


label ir_a_salvarlos:
    scene bg laboratorio_entrada

    narrador "Entran todos a investigar. Hace frio adentro, mas de lo usual. Escuchas a alguien llamando a la distancia, vas corriendo a la habitación de donde provino el ruido..."
    narrador "Era el equipo de rescate llamando porque habian visto algo, eran tus compañeros."
    narrador "Pero- Que fue lo que hiciste mal? No puedes contenerlo, vomitas en el suelo. Todo por lo que tuviste que pasar, se perdio tan rapidamente. Hace tan solo unos dias estaban todos investigando, trabajando juntos..."

    jump por_que_timor


label por_que_timor:
    narrador "El equipo de rescate decidio que no habia nada mas que pudieran hacer. Llevamos los cuerpos de vuelta a la ciudad asi podiamos contactar las familias y darles un descanso apropiado."
    narrador "Nunca supe lo mala que llego a ser esa decisión... Mis compañeros habian muerto siendo portadores de un virus que traía la momia, al final ese virus logro contagiando al equipo de rescate, las familias, y a mi." 
    narrador "Nunca supe que paso con el resto del mundo, pero si llegue a sobrevivir lo suficiente como para saber que los otros no tuvieron un destino distinto al mio."
    scene black with fade
    centered "Fin."

    $ registrar_final("timor_solitario")
    return


label muerte_asolada:
    narrador "Decides seguir caminando en linea recta..."
    narrador "El frio de la nieve alcanza a cada parte de tu cuerpo. no puedes sentir tus brazos, piernas, dedos. Hasta que eventualmente pierdes toda voluntad de continuar. Finalmente tus piernas ceden y escuchas a tu cuerpo golpear y enterrarse en la nieve."

    scene black with fade
    centered "Fin."

    $ registrar_final("timor_solitario")
    return