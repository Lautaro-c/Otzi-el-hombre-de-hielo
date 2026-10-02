label dia2_sin_plan:
    scene bg sala_comun

    narrador "Es el comienzo de otro día. Recorre la base para ver qué hacen tus compañeros o busca cosas por hacer (tienes 5 de energía)."

    jump hub_dia2_sin_plan


label hub_dia2_sin_plan:
    menu:
        "Ver a Calisto":
            jump calisto_dia2_sin_plan
        "Ver al Ruso":
            jump ruso_dia2_sin_plan
        "Ver a Timor":
            jump timor_dia2_sin_plan


label calisto_dia2_sin_plan:
    show calisto preocupada
    narrador "Sigue intentando curar a Otzi por su cuenta. Se le nota estresada y frustrada, ya que no ha logrado ningún progreso por sí misma en todo el día."
    hide calisto preocupada

    menu:
        "Decirle que es inutil":
            jump decirle_inutil_calisto
        "Ofrecer ayuda a curarlo":
            jump ofrecer_ayuda_curarlo
        "no decir nada e irte":
            jump no_decir_nada_irte_calisto


label ruso_dia2_sin_plan:
    show Nostrov serio
    narrador "Se lo ve muy enojado mientras trabaja en el generador e insulta entre murmullos. Quizá molestarlo no sea una buena idea."
    hide Nostrov serio

    menu:
        "Decirle que es inutil":
            jump decirle_inutil_ruso
        "no decir nada e irte":
            jump no_decir_nada_irte_ruso
        "Ofrecer ayuda a arreglarlo":
            jump ofrecer_ayuda_arreglarlo


label timor_dia2_sin_plan:
    narrador "Vas a ver en qué anda Timor, pero no la encuentras por ninguna parte. Revisas su habitación y encuentras una nota que dejó atrás."

    menu:
        "no decir nada e irte":
            jump no_decir_nada_irte_timor
        "Leer la nota":
            jump leer_la_nota


label ofrecer_ayuda_curarlo:
    show calisto sonriente
    narrador "Trabajas junto a Calisto para hacer lo posible, pero no se logra mucho progreso y piensas que fue una pérdida de tiempo."
    hide calisto sonriente
    jump en_la_noche_sin_plan
    

label ofrecer_ayuda_arreglarlo:
    show Nostrov feliz
    narrador "Trabajas junto al Ruso para hacer lo posible, pero no se logra mucho progreso y piensas que fue una pérdida de tiempo."
    hide Nostrov feliz
    jump en_la_noche_sin_plan


label leer_la_nota:
    narrador "Agarras la nota que dice: «No se preocupen por mí. Fui a buscar ayuda y volveré en dos días con las autoridades.»"
    jump en_la_noche_sin_plan


label decirle_inutil_calisto:
    show calisto enojada
    narrador "Se enfada contigo, te insulta de muchas maneras mientras te grita que te vayas, que solo eres un estorbo e inútil, bueno para nada."
    hide calisto enojada
    jump en_la_noche_sin_plan

label decirle_inutil_ruso:
    show nostrov enojado
    narrador "Se enfada contigo, te insulta de muchas maneras mientras te grita que te vayas, que solo eres un estorbo e inútil, bueno para nada."
    hide nostrov enojado
    jump en_la_noche_sin_plan

label no_decir_nada_irte_calisto:
    narrador "Te retiras para seguir deambulando por la base y ver qué hacen los demás."

    menu:
        "Ver a Timor":
            jump timor_dia2_sin_plan
        "Ver al Ruso":
            jump ruso_dia2_sin_plan
        "Ir a dormir":
            jump en_la_noche_sin_plan

label no_decir_nada_irte_ruso:
    narrador "Te retiras para seguir deambulando por la base y ver qué hacen los demás."

    menu:
        "Ver a Timor":
            jump timor_dia2_sin_plan
        "Ver a Calisto":
            jump calisto_dia2_sin_plan
        "Ir a dormir":
            jump en_la_noche_sin_plan

label no_decir_nada_irte_timor:
    narrador "Te retiras para seguir deambulando por la base y ver qué hacen los demás."

    menu:
        "Ver al Ruso":
            jump ruso_dia2_sin_plan
        "Ver a Calisto":
            jump calisto_dia2_sin_plan
        "Ir a dormir":
            jump en_la_noche_sin_plan

label en_la_noche_sin_plan:
    narrador "Te despiertas por los gritos de tus compañeros que escuchas desde el pasillo. Parecen estar peleando por algo, pero no llegas a distinguir sobre qué discuten."

    menu:
        "ir a ver que sucede":
            jump ir_a_ver_que_sucede
        "ignorarlos y vuelves a dormir":
            jump ignorarlos_dormir


label ir_a_ver_que_sucede:
    show calisto enojada left 
    show nostrov enojado rigth 
    narrador "Los ves gritándose insultos y amenazas, diciendo que lo que hace el otro es inútil y que tendría que concentrarse en su tarea porque es más importante."
    hide calisto enojada left 
    hide nostrov enojado rigth 
    menu:
        "intervenir en la pelea":
            jump intervenir_en_la_pelea
        "ignorarlos y vuelves a dormir":
            jump ignorarlos_dormir


label ignorarlos_dormir:
    narrador "Te pones tapones en los oídos y vuelves a dormir, indiferente a lo que suceda afuera."

    jump en_la_manana_siguiente


label intervenir_en_la_pelea:
    show calisto enojada left 
    show nostrov enojado rigth 
    narrador "Te interpones entre ellos intentando frenar la pelea, pero no hay manera de hacer que se calmen. En el calor de la discusión, Nostrov saca un arma y le dispara a Calisto, matándola. El Ruso, horrorizado por sus acciones, se pone el revólver en la cabeza y se mata."
    hide calisto enojada left 
    hide nostrov enojado rigth 
    menu:
        "intentar dormir para esperar la ayuda de Timor por la mañana":
            jump intentar_dormir_esperar_timor
        "Agarra el arma":
            jump agarrar_el_arma


label en_la_manana_siguiente:
    scene bg pasillo_oscuro

    narrador "Sales de tu habitación y te encuentras un charco de sangre. Avanzas por el pasillo y te encuentras los cadáveres de tus compañeros. Tal parece que el Nostrov mató a Calisto y luego se suicidó. Horrorizado por la escena, sales a ver si Timor llegó con ayuda."

    jump sales_ver_timor_ayuda


label intentar_dormir_esperar_timor:
    narrador "Duermes ignorando lo sucedido, sabiendo que Timor llegará mañana con ayuda."

    jump sales_ver_timor_ayuda


label agarrar_el_arma:
    narrador "Teniendo el arma en las manos y luego de lo sucedido, dejas que tu mente se descontrole con tus sentimientos de miedo y horror, cuando un pensamiento se fija en tu cabeza: rendirse, poner el arma en tu cabeza y dejarte ir, tener un final rápido."

    menu:
        "dispararte en la cabeza":
            jump dispararte_en_la_cabeza
        "Sales a ver si llego Timor con la ayuda":
            jump sales_ver_timor_ayuda


label sales_ver_timor_ayuda:
    scene bg exterior_nieve

    narrador "Despiertas y sales de la base para ver si llega Timor con la ayuda. Al abrir la puerta, ves el cuerpo de Timor tumbado en la nieve, inmóvil. Tal parece que murió congelada afuera, no muy lejos de la base. En ese momento, en medio de la desesperanza, decides rendirte: tomas el revólver de la base, te lo pones en la frente y aprietas el gatillo."

    jump dispararte_en_la_cabeza


label dispararte_en_la_cabeza:
    scene black with fade
    centered "Conseguiste el Final Malo. ¿Quieres jugar de nuevo?"

    $ registrar_final("energia_agotada")

    jump introduccion