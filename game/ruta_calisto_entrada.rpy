label doctora_calisto:
    scene bg sala_comun
    show calisto sonriente
    calisto "Hola, ¿no fue la mejor primer impresión no? Jaja"
    prota "Es normal que en estas situaciones cunda el pánico... Pero, ¿Cómo estas?"
    show calisto preocupada
    calisto "Preocupada... Vine aquí a comprobar mi teoría."
    prota "¿Tu teoría?"
    show calisto sonriente
    calisto "La maldición de Otzi nace a partir de un virus del pasado del cual no somos inmunes hoy en día."
    prota "Entiendo... ¿Entonces viniste a comprobar eso?"
    show calisto canchera
    calisto "No solo me llamaron para comprobarlo, me dijeron que si lo probaba cierto, tenia que desarrollar una cura. Pero si alguien puede, soy yo."
    prota "Entiendo... Parece una misión difícil."
    calisto "Lo es, no me vendrían mal un par de manos extra."

    $ investigacion_otzi = 0
    $ energia = ENERGIA_DIA_1
    $ relacion_calisto = 0
    $ dia = 1
    $ pulmon = False
    $ sangre_rara = False
    $ caries_encontradas = False

    menu:
        "Aceptar ayudarla a curar a Otzi.":
            jump aceptar_ayudar_otzi
        "Negarte.":
            jump negarte_calisto_final_malo


# TODO: el texto de este final todavía no fue enviado.
label negarte_calisto_final_malo:
    narrador "Rechazas el plan de tu compañero. Puedes seguir recorriendo el lugar mientras te quede energía."
    menu:
        "Ir a ver si la doctora Timor esta bien.":
            jump doctora_timor
        "Ir a ayudar a Nostrov con el generador.":
            jump ruso
        "Llamarlos a todos." if todos_los_finales_vistos():
            jump final_bueno_hub