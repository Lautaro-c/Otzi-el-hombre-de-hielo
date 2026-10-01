label dia3_inicio:
    $ dia = 3
    $ energia = ENERGIA_DIA_3
    scene bg sala_comun with fade

    if relacion_calisto <= -10:
        narrador "El animo estaba tan por los suelos que ni se dirigieron la palabra al comenzar el día, ya conocías tus opciones"
    else:
        narrador "Finalmente llego el día decisivo, hoy todo se define."

    menu:
        "Acompañarla mientras trabaja." if investigacion_otzi >= PISTAS_PARA_CURA:
            jump acompanarla
        "Esperar a que de los resultados":
            jump reagruparse_dia3
        "Ir al almacén de suministros" if investigacion_otzi < PISTAS_PARA_CURA:
            jump almacen
        "Volver a revisar a Ötzi" if (not pulmon or not sangre_rara or not caries_encontradas):
            jump sala_otzi


label acompanarla:
    scene bg cuarto_timor with fade
    show calisto sonriente
    calisto "Buenos días Dr. ¿Que hace aquí?"
    prota "Solo quería hacerte compañía, debes estar muy tensa de que toda la responsabilidad caiga en tus hombros."
    show calisto canchera
    calisto "Ahora que lo decís es un poco cierto, pero no te preocupes, estas en las mejores manos de la medicina."
    prota "Después de todo lo vivido, no lo dudo. Me voy para no molestarla."

    if relacion_calisto >= 4:
        show calisto sonrojada
        calisto "Por favor no... prefiero que te quedes."
        narrador "Ambos se sonríen y el protagonista le hace compañía sin molestarla, después de un tiempo los resultados están listo."
        $ relacion_calisto += 4
    else:
        show calisto sonriente
        calisto "Esta bien, le avisare cuando este todo listo."

    jump reagruparse_dia3