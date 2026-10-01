label reagruparse_dia3:
    scene bg sala_comun
    narrador "Los resultados estaban listos, llego el momento decisivo"

    if investigacion_otzi >= PISTAS_PARA_CURA:
        show calisto emocionada
        calisto "¡LO LOGRAMOS! ¡TENEMOS LA CURA PARA EL VIRUS! ¡EN SUS CARAS!"
        prota "¡VAMOOOOOOOOOS!"
        show nostrov feliz at right
        nostrov "Están locos camaradas, no puedo creer que lo hayan logrado."
        show timor triste at left
        timor "No puedo creer haber estado paralizada por el miedo todo este tiempo. Por favor discúlpenme, mi actitud fue horrible."
        prota "Eso ya quedo en el pasado lo que importa es que ahora todo va a estar bien. Por favor agradezcamos todos el increíble trabajo de la Dra. Calisto."
        show timor feliz at left
        narrador "Todos dieron una gran ronda de aplausos por la Dra. Calisto y su increíble capacidad para la medicina"
        show calisto sonrojada
        calisto "Gracias, gracias, pero no podría haberlo hecho sin la ayuda del Dr."
        narrador "Sin el riesgo de muerte cerca los 4 pudieron continuar en paz, arreglaron el generador y pudieron sacar mucha información de Ötzi, con lo que aprendieron se desarrollaron multiples medicinas."

        if relacion_calisto >= 6:
            hide nostrov
            hide timor
            narrador "El protagonista y la Dra. Calisto se volvieron pareja y ahora están casados con 3 hijos, viven a 10 kilómetros de donde hallaron a Ötzi."

        scene black with fade
        centered "Final bueno ruta Dra. Calisto Escrito por Lautaro Puig Da Silva."
        return

    else:
        show calisto decepcionada 
        calisto "No... no pude lograrlo. Ya es demasiado tarde."
        narrador "Se escucha como se rompe el hielo, un silencio se hace en la sala."
        narrador "Después un sinfín de gritos todos culpándose mutuamente, pero vos no lo haces, solo te culpas a vos mismo."
        narrador "Mientras tus pulmones se llenan de ese letal virus y empiezas a sentir como tu cuerpo arde desde adentro, te preguntas que es lo que podrías haber hecho distinto."

        if investigacion_otzi <= 0:
            narrador "En sus últimos momentos la Dra. Calisto solo quiere que sepas una cosa."
            show calisto enojada
            calisto "Te odio."
        elif(relacion_calisto <= 0):
            narrador "En sus últimos momentos la Dra. Calisto solo quiere que sepas una cosa."
            show calisto decepcionada 
            calisto "Tu victimismo y falta de valentía nos trajo hasta acá. Sos un cobarde."
        scene black with fade
        centered "Final malo ruta Dra. Calisto Escrito por Lautaro Puig Da Silva."
        return


label ira_total:
    scene bg sala_comun
    $ relacion_calisto -= 10
    if investigacion_otzi <= 0:
        show calisto enojada
        calisto "¿Que te pasa a vos? Me tuviste 3 días perdiendo el tiempo, No puedo creer haberte escuchado, vos y tu pateti-"
    else:
        show calisto decepcionada 
        calisto "¿Por que no hiciste nada estos últimos 2 días? Estábamos trabajando bien al principio pero fue como si de golpe te rindieras."
        prota "Es que esta situación era demasiado, no había nada que podíamos hacer. Entre el frio y la falta de luz, simplemente era imposible."
        show calisto enojada
        calisto "¡¿QUE NO HABIA NADA QUE PODÍAMOS HACER?! ¡Ni te esforzaste estos últimos días! ¿y venís a hablarme de lo que puedo o no puedo hacer? Al principio decidí negarlo pero ahora veo como sos solo un pedazo de basura insigni-"

    narrador "Antes de que ella pueda seguir con su desenfreno escuchan como el hielo se quiebra, saben que lo que sea que Ötzi traía ahora esta en el aire y pronto en sus pulmones."
    narrador "Empiezan a sentir un terrible ardor desde el interior, pronto empiezan a temer que el aspecto tan demacrado de Ötzi no solo se deba al tiempo y las peleas. En sus últimos momentos la Dra. Calisto solo quiere que sepas una cosa."

    if investigacion_otzi <= 0:
        show calisto enojada
        calisto "Te odio."
    elif(relacion_calisto <= 0):
        show calisto decepcionada 
        calisto "Tu victimismo y falta de valentía nos trajo hasta acá. Sos un cobarde."

    scene black with fade
    centered "Final Malo de la Ruta de la Dra. Calisto por Lautaro Puig Da Silva"
    return