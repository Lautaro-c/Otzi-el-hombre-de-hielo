# Para probar, conectá esto con tu escena anterior:  jump aceptar_ayudar_otzi
# label start:
#     jump aceptar_ayudar_otzi

# Comienza la primer sección de Point and Click: la doctora te pide que
# analices el cuerpo para ver si hay algo que ella no haya visto.
    
label aceptar_ayudar_otzi:
    scene bg sala_otzi with fade
    show calisto sonriente
    calisto "Voy a necesitar tu ayuda para analizar a Ötzi, con tan poca luz otro par de ojos es de gran ayuda."
    calisto "Pero intentemos no pasar mucho tiempo acá, no queremos drenar todas nuestras energías el primer día."
    jump sala_otzi


label reagruparse_dia1:

    if investigacion_otzi >= 3:
        show calisto sonriente
        calisto "Me fuiste de mucha ayuda hoy Dr., sus observaciones me van a ser muy útiles."
        prota "Me alegra haber sido de ayuda."
        $ relacion_calisto += 2
    elif investigacion_otzi > 0:
        show calisto sonriente
        calisto "Siento que hay algo que nos falto por ver, pero estuvo bien por hoy."
        prota "Me alegra haber sido de ayuda."
        $ relacion_calisto += 1
    else:
        show calisto enojada
        calisto "Siendo sincera esperaba mas de vos. No me ayudaste en nada."
        prota "Lo siento."
        $ relacion_calisto -= 1

    hide calisto
    narrador "Después de esta interacción se reúnen con los demás."
    scene bg sala_comun with fade

    show timor asustada
    timor "No puedo creer que se hayan acercado a esa momia maldita, ¿Lograron ver algo útil?"

    if investigacion_otzi >= 3:
        show calisto sonriente at right
        calisto "Si, gracias a la ayuda del Dr. y mis conocimientos estamos mas cerca de descubrir que esa maldición probablemente no lo sea."
    elif investigacion_otzi > 0:
        show calisto sonriente at right
        calisto "No pudimos verlo todo con tan poca luz pero tenemos razones para creer que esa maldición probablemente no lo sea."
    else:
        show calisto enojada at right
        calisto "Por mas de que el Dr. y tan poca luz no hayan ayudado a encontrar nada, dudo que esa maldición exista."

    show nostrov enojado at left
    nostrov "Bueno en eso estamos de acuerdo Dra. pero de seguro mas luz les habría sido util por eso debimos haber arreglado los fusibles."
    timor "Ni fusibles ni vacunas desarrolladas en 3 días, lo que tenemos que hacer es SALIR DE ACÁ."
    prota "Lo mejor va a ser descansar, ya hicimos mucho por hoy, mañana podemos seguir discutiendo."
    narrador "Todos están de acuerdo y se van a dormir."
    jump dia2_inicio