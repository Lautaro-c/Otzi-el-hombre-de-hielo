label ruso:
    scene bg sala_generador with fade

    narrador "Te acercas al Ingeniero Nostrov, quien sostiene una linterna pesada entre los dientes mientras examina unos esquemas eléctricos desplegados sobre una mesa metálica. Al verte llegar, se endereza y suspira, liberando un humo blanco por la boca debido a la baja temperatura del lugar."

    $ busco_a = "nostrov"
    jump ruso_decisiones


label ruso_decisiones:
    show nostrov serio
    nostrov "Escúchame bien, colega. Olvídate de maldiciones o supersticiones. La realidad es simple, el corte acabó por cortar la refrigeración y los sistemas de Ötzi aguantarán 3 días antes del deshielo total. Si no recuperamos la energía para el Día 3, moriremos congelados o arruinaremos el hallazgo."
    prota "¿Tienes un plan para el generador?"
    nostrov "El panel principal sufrió un cortocircuito por la tormenta."
    narrador "Responde señalando el pasillo inferior."
    nostrov "Para repararlo necesito dos cosas, la llave inglesa pesada del taller y un fusible de repuesto de alta capacidad. ¿Me vas a ayudar a reparar esta chatarra o vas a quedarte a esperar un milagro?"

    menu:
        "Aceptar ayudarlo a reparar el generador":
            jump ruso_aceptar
        "Negarte":
            jump negarte_nostrov_final_malo


label ruso_aceptar:
    show nostrov feliz
    nostrov "Sabia decisión. Vamos al taller por la herramienta."
    jump pasillo


label pasillo:
    scene bg pasillo_oscuro

    narrador "Recorren el pasillo a oscuras con las linternas. El aire es cada vez más frío. Nostrov te explica que el plan tomará tiempo, despejar las tuberías congeladas llevará un día entero, por lo que deben reunir los materiales de inmediato."

    jump taller_generador


label taller_generador:
    scene bg taller

    narrador "Al llegar al taller, encuentran la puerta abierta y notas pisadas que se dirigen hacia la salida de emergencia."

    jump buscar_llave


label buscar_llave:
    narrador "Entran al taller. Encuentras la llave inglesa pesada sobre el banco de trabajo, pero notas que falta uno de los trajes térmicos livianos del estante."

    show nostrov confundido
    nostrov "La Dra. Timor estuvo aquí."
    narrador "Refunfuñando."
    nostrov "Estaba aterrorizada con lo de la maldición. Presiento que intentó hacer alguna estupidez."

    show nostrov preocupado at center
    narrador "Antes de ir al almacén a buscar el fusible, escuchan una alarma distante. La puerta exterior de la base ha sido forzada."

    menu:
        "Correr con Nostrov hacia la salida exterior":
            jump premisa_muerte_timor
        "Tomar la llave":
            jump tomar_la_llave


label tomar_la_llave:
    $ tiene_llave_inglesa = True
    narrador "Has adquirido la llave inglesa. Se añade en tu inventario."
    jump premisa_muerte_timor


label premisa_muerte_timor:
    hide nostrov confundido
    narrador "Se terminó por hacer tan tarde que ha oscurecido y no logran ver nada a la distancia. Toman la desición de descansar y buscarla al día siguiente."

    if not tiene_llave_inglesa:
        jump volver_tomar_llave
    else:
        jump muerte_timor


label volver_tomar_llave:
    $ tiene_llave_inglesa = True
    narrador "Has adquirido la llave inglesa. Se añade en tu inventario."
    jump muerte_timor


label muerte_timor:
    scene bg exterior_nieve

    narrador "Regresan a la esclusa para revisar que ocurrió y terminan por encontrar a unos metros afuera, sepultada por la ventisca de la noche, yace el cuerpo congelado de la Dra. Timor. Intentó escapar a pie para huir de la \"maldición\", pero el frío extremo de -35°C la mató en cuestión de minutos."
    show nostrov serio at center
    narrador "Nostrov observa el cadáver sin inmutarse."

    jump vamonos_nada_que_hacer


label vamonos_nada_que_hacer:
    show nostrov enojado
    nostrov "La paranoia te mata más rápido que el frío. No podemos hacer nada por ella. Solo nos quedan 48 horas antes de que el contenedor de Ötzi pierda el frío restante. Vamos por el fusible."
    hide nostrov enojado
    jump almacen_fusible


label almacen_fusible:
    scene bg laboratorio_entrada

    narrador "Al llegar a la puerta del almacen observas que esta completamente tapada de nieve."
    show nostrov enojado
    nostrov "CARAJO!!!. Nos llevará otro día entero quitar todo eso, será mejor que lo hagamos ahora y luego nos retiremos a descansar colega. Estoy seguro de que resolveremos todo a tiempo al siguiente día."
    hide nostrov enojado
    jump siguiente_dia_nostrov


label siguiente_dia_nostrov:
    scene bg sala_comun

    narrador "Pasas toda la noche casi congelado y consumido por el miedo, logras conciliar unas horas de sueño hasta que eres despertado por la Dra. Calisto."
    show calisto preocupada
    calisto "Muchacho levantate vamos, Nostrov dijo que te esperaria en la puerta del almacen para buscar el fusil."
    hide calisto preocupada

    jump buscar_fusible


label buscar_fusible:
    scene bg almacen

    narrador "Llegas al almacén y junto a Nostrov fuerzan la caja de repuestos helada y consigues el fusible de alta capacidad."
    show nostrov preocupado at center
    narrador "De repente desde los monitores portátiles salta la advertencia, el hielo de Ötzi se está derritiendo y las lecturas muestran la reactivación de un virus ancestral atrapado en sus tejidos."

    jump nostrov_hora_cero


label nostrov_hora_cero:
    show nostrov confundido
    nostrov "Llegó la hora cero. Con la llave y el fusible en mano, bajemos a la subestación."
    hide nostrov confundido

    jump sala_generador


label sala_generador:
    scene bg sala_generador with fade

    narrador "Descienden a la subestación. El gran motor diésel está inerte y cubierto de escarcha. Nostrov abre el panel principal."
    show nostrov serio at center
    nostrov "Sostén la luz. Voy a aflojar las tuercas congeladas con la llave inglesa, tú insertarás el fusible nuevo en cuanto abra la caja."
    show nostrov preocupado at center
    narrador "Una alarma roja retumba en la sala: El contenedor de Ötzi ha alcanzado temperatura crítica."

    menu:
        "Mantener la calma y ayudar a Nostrov a cambiar el fusible":
            jump reparar_panel
        "Paniquearte e intentar huir hacia el laboratorio":
            jump panico_generador


label reparar_panel:
    show nostrov serio at center
    narrador "Sostienes la linterna con firmeza. Nostrov usa la llave inglesa para retirar la pieza dañada y tú encajas el fusible de alta capacidad en su posición."
    narrador "Nostrov acciona la palanca. El motor diésel ruge y la energía regresa a la base. Sin embargo, el monitor central parpadea en rojo..."

    jump alerta_alerta


label panico_generador:
    show nostrov enojado
    narrador "El pánico te domina. Sueltas la linterna e intentas correr a las escaleras. Tropiezas en la oscuridad entre los cables y caes bruscamente."
    narrador "El fusible de repuesto se desliza de tus manos y cae por una rejilla de ventilación, perdiéndose en los niveles inferiores. Sin la pieza, la energía no regresa a tiempo y el virus se libera en la base."
    hide nostrov enojado
    narrador "La Dra. Calisto, Nostrov y tu caen muertos en cuestión de minutos..."

    jump sala_generador


label alerta_alerta:
    show text "{color=#FF0000}{b}ADVERTENCIA: PATÓGENO ANCESTRAL DETECTADO EN FASE DE PROPAGACIÓN AÉREA.{/b}" at top
    show nostrov serio
    nostrov "¡El descongelamiento de estos 3 días activo el virus!. Si no re-congelamos la sala ahora mismo, se extenderá por los conductos de aire."
    hide nostrov serio

    jump final_bueno_ruso


label final_bueno_ruso:
    scene bg sala_otzi
    narrador "Ejecutas la secuencia de súper-congelamiento desde la consola de comandos. Un torrente de fluido criogénico inunda el contenedor de Ötzi."
    narrador "En la pantalla ves cómo la temperatura del laboratorio cae drásticamente a -40°C, encapsulando a la momia y al virus en un bloque sólido de hielo. El peligro biológico ha sido neutralizado justo a tiempo."

    jump voltear_ver_nostrov


label voltear_ver_nostrov:
    show nostrov feliz at center
    narrador "Nostrov exhala una ultima vez y te da una fuerte palmada en la espalda."
    show nostrov orgullo_ruso
    nostrov "Ni maldiciones ni supersticiones, física y pragmatismo. El virus está atrapado en el hielo de nuevo. Gran trabajo, colega. Ahora esperemos al equipo de rescate."

    scene black with fade
    centered "FINAL BUENO: Contención Pragmática (Ruta de Nostrov)."

    $ registrar_final("nostrov_bueno")
    return


# TODO: el texto de este final todavía no fue enviado.
label negarte_nostrov_final_malo:
    show nostrov enojado
    nostrov "Como quieras, no esperaba mucho de un doctor de ciudad de todas formas."
    hide nostrov

    narrador "Rechazas la propuesta de Nostrov. Puedes seguir recorriendo el lugar mientras te quede energía."

    $ rechazo_nostrov = True
    $ energia_decision -= 1

    if energia_decision > 0:
        narrador "Te quedan [energia_decision] de energía."
        jump decision_hub
    else:
        jump dia2_sin_plan