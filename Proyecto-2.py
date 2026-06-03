import random

# ---------------------------------------------------------------------------
# CONFIGURACION GLOBAL
# ---------------------------------------------------------------------------

# Dificultad maxima de paginas por capitulo y de capitulos en la biblioteca.
# Se modifican desde dificultad() segun la eleccion del jugador.
dificultad_piso       = 10
dificultad_biblioteca = 10

# Estado actual de la partida (se inicializan en inicializar_partida)
largo_piso        = 0   # paginas por capitulo en esta partida
alto_biblioteca   = 0   # capitulos totales en esta partida
indice_piso       = 0   # pagina actual dentro del capitulo
indice_biblioteca = 0   # capitulo actual
resultado_dado    = 0   # ultimo resultado del dado

# ---------------------------------------------------------------------------
# CONTENIDO DEL LIBRO
# ---------------------------------------------------------------------------

# Titulos de los 15 capitulos (cubre el maximo posible de capitulos en el juego).
titulos_capitulos = [
    "Que es el solarpunk",
    "Economia y ciudad solarpunk",
    "Politica y educacion solarpunk",
    "Tecnologia y resistencia solarpunk",
    "Cultura y futuro solarpunk",
    "Origenes del movimiento solarpunk",
    "Arte y estetica solarpunk",
    "Comunidad y vida cotidiana solarpunk",
    "Energia y medio ambiente solarpunk",
    "Alimentacion y agricultura solarpunk",
    "Transporte y movilidad solarpunk",
    "Salud y bienestar solarpunk",
    "Infancia y educacion solarpunk",
    "Memoria y historia solarpunk",
    "El solarpunk como proyecto de vida",
]

# Pistas narrativas por capitulo y pagina (15 capitulos x 5 paginas).
pistas = [
    ["Pista cap1 pag1",  "Pista cap1 pag2",  "Pista cap1 pag3",  "Pista cap1 pag4",  "Pista cap1 pag5"],
    ["Pista cap2 pag1",  "Pista cap2 pag2",  "Pista cap2 pag3",  "Pista cap2 pag4",  "Pista cap2 pag5"],
    ["Pista cap3 pag1",  "Pista cap3 pag2",  "Pista cap3 pag3",  "Pista cap3 pag4",  "Pista cap3 pag5"],
    ["Pista cap4 pag1",  "Pista cap4 pag2",  "Pista cap4 pag3",  "Pista cap4 pag4",  "Pista cap4 pag5"],
    ["Pista cap5 pag1",  "Pista cap5 pag2",  "Pista cap5 pag3",  "Pista cap5 pag4",  "Pista cap5 pag5"],
    ["Pista cap6 pag1",  "Pista cap6 pag2",  "Pista cap6 pag3",  "Pista cap6 pag4",  "Pista cap6 pag5"],
    ["Pista cap7 pag1",  "Pista cap7 pag2",  "Pista cap7 pag3",  "Pista cap7 pag4",  "Pista cap7 pag5"],
    ["Pista cap8 pag1",  "Pista cap8 pag2",  "Pista cap8 pag3",  "Pista cap8 pag4",  "Pista cap8 pag5"],
    ["Pista cap9 pag1",  "Pista cap9 pag2",  "Pista cap9 pag3",  "Pista cap9 pag4",  "Pista cap9 pag5"],
    ["Pista cap10 pag1", "Pista cap10 pag2", "Pista cap10 pag3", "Pista cap10 pag4", "Pista cap10 pag5"],
    ["Pista cap11 pag1", "Pista cap11 pag2", "Pista cap11 pag3", "Pista cap11 pag4", "Pista cap11 pag5"],
    ["Pista cap12 pag1", "Pista cap12 pag2", "Pista cap12 pag3", "Pista cap12 pag4", "Pista cap12 pag5"],
    ["Pista cap13 pag1", "Pista cap13 pag2", "Pista cap13 pag3", "Pista cap13 pag4", "Pista cap13 pag5"],
    ["Pista cap14 pag1", "Pista cap14 pag2", "Pista cap14 pag3", "Pista cap14 pag4", "Pista cap14 pag5"],
    ["Pista cap15 pag1", "Pista cap15 pag2", "Pista cap15 pag3", "Pista cap15 pag4", "Pista cap15 pag5"],
]

# Cuestionario: lista de 15 capitulos.
# Cada capitulo tiene 7 preguntas.
# Cada pregunta es una lista de 3 elementos: [pregunta, pista, respuesta].
# Se accede como: cuestionarios[cap][pregunta][0] = texto pregunta
#                 cuestionarios[cap][pregunta][1] = pista
#                 cuestionarios[cap][pregunta][2] = respuesta
cuestionarios = [
    # Capitulo 1: Que es el solarpunk
    [
        ["Segun el solarpunk, la tecnologia debe trabajar _____ la naturaleza (con / contra):",
         "Piensa en la naturaleza como aliada, no como enemiga",
         "con"],
        ["El solarpunk es un movimiento que imagina futuros _____ (optimistas / distopicos):",
         "El solarpunk reacciona contra el pesimismo del cyberpunk",
         "optimistas"],
        ["El solarpunk combina ecologia con _____ (tecnologia / magia):",
         "Paneles solares, energia limpia, herramientas digitales",
         "tecnologia"],
        ["El solarpunk nacio como respuesta al genero literario _____ (cyberpunk / fantasy):",
         "El prefijo cyber viene de cibernetica y tecnologia oscura",
         "cyberpunk"],
        ["En el solarpunk las comunidades son _____ (autonomas / dependientes):",
         "Se gobiernan a si mismas sin depender de grandes corporaciones",
         "autonomas"],
        ["El color mas asociado al solarpunk es el _____ (verde / gris):",
         "Piensa en plantas, bosques y energia solar",
         "verde"],
        ["El solarpunk cree que el futuro debe ser _____ para todos (justo / competitivo):",
         "No hay ganadores ni perdedores, todos colaboran",
         "justo"],
    ],
    # Capitulo 2: Economia y ciudad solarpunk
    [
        ["La base economica del solarpunk son las _____ (cooperativas / empresas):",
         "Organizaciones donde todos son duenos y trabajadores a la vez",
         "cooperativas"],
        ["En una ciudad solarpunk los edificios suelen tener _____ en los techos (jardines / antenas):",
         "Piensa en producir alimentos y absorber lluvia",
         "jardines"],
        ["El solarpunk prefiere la economia _____ (local / global):",
         "Cerca de casa, sin grandes cadenas de distribucion",
         "local"],
        ["En el solarpunk los recursos son de la _____ (comunidad / empresa):",
         "Nadie los posee solo, todos los comparten",
         "comunidad"],
        ["Las ciudades solarpunk priorizan espacios _____ (publicos / privados):",
         "Plazas, parques y mercados abiertos a todos",
         "publicos"],
        ["El intercambio sin dinero se llama _____ (trueque / prestamo):",
         "Dar algo y recibir algo de igual valor sin billetes de por medio",
         "trueque"],
        ["El solarpunk apoya el comercio _____ (justo / libre):",
         "Que pague bien a quien produce y cuide el ambiente",
         "justo"],
    ],
    # Capitulo 3: Politica y educacion solarpunk
    [
        ["En el solarpunk la toma de decisiones se hace por _____ (asambleas / presidentes):",
         "Reunion donde todos pueden hablar y votar",
         "asambleas"],
        ["El modelo politico del solarpunk se llama _____ (anarquismo / monarquia):",
         "Sin jefes ni estados centralizados, gobierno entre iguales",
         "anarquismo"],
        ["La educacion solarpunk es _____ (libre / obligatoria):",
         "Sin presion ni castigos, cada quien aprende a su ritmo",
         "libre"],
        ["En el solarpunk el poder esta _____ (distribuido / concentrado):",
         "Muchos tienen un poco, nadie tiene todo",
         "distribuido"],
        ["El solarpunk rechaza la _____ (jerarquia / diversidad):",
         "Estructuras donde unos mandan y otros obedecen sin cuestionarlo",
         "jerarquia"],
        ["Las decisiones en el solarpunk buscan el _____ (consenso / voto mayoritario):",
         "Que todos esten de acuerdo, no solo la mitad mas uno",
         "consenso"],
        ["La participacion en la comunidad solarpunk es _____ (voluntaria / forzada):",
         "Nadie obliga, pero todos se benefician de colaborar",
         "voluntaria"],
    ],
    # Capitulo 4: Tecnologia y resistencia solarpunk
    [
        ["El solarpunk surgio como reaccion al genero literario _____ (cyberpunk / fantasy):",
         "El prefijo cyber viene de cibernetica y tecnologia oscura",
         "cyberpunk"],
        ["La tecnologia en el solarpunk debe ser _____ (abierta / patentada):",
         "Que cualquiera pueda usarla, modificarla y compartirla",
         "abierta"],
        ["El solarpunk prefiere herramientas _____ (reparables / desechables):",
         "Si se rompe, se arregla; no se tira y compra otra",
         "reparables"],
        ["El software solarpunk es de codigo _____ (abierto / cerrado):",
         "Cualquiera puede ver como funciona y mejorarlo",
         "abierto"],
        ["La resistencia solarpunk es _____ (no violenta / armada):",
         "Se lucha con ideas, arte y comunidad, no con armas",
         "no violenta"],
        ["El solarpunk promueve la tecnologia a escala _____ (humana / industrial):",
         "Que sirva a personas reales, no a megacorporaciones",
         "humana"],
        ["El solarpunk valora el conocimiento _____ (ancestral / corporativo):",
         "Sabiduria de pueblos y comunidades transmitida por generaciones",
         "ancestral"],
    ],
    # Capitulo 5: Cultura y futuro solarpunk
    [
        ["El solarpunk dice que la esperanza es un acto _____ (politico / religioso):",
         "Tiene que ver con cambiar el mundo, no con la fe",
         "politico"],
        ["El arte solarpunk suele mostrar ciudades llenas de _____ (plantas / maquinas):",
         "Verde, fotosintesis, naturaleza integrada en lo urbano",
         "plantas"],
        ["El solarpunk imagina el futuro con _____ (esperanza / miedo):",
         "Es la esencia del movimiento: creer que otro mundo es posible",
         "esperanza"],
        ["La estetica solarpunk mezcla lo natural con lo _____ (tecnologico / medieval):",
         "Paneles solares en jardines, drones entre arboles",
         "tecnologico"],
        ["El solarpunk celebra la _____ cultural (diversidad / uniformidad):",
         "Muchas lenguas, tradiciones y formas de vivir coexistiendo",
         "diversidad"],
        ["Las historias solarpunk suelen terminar con _____ (solucion colectiva / heroe individual):",
         "No hay un salvador, todos juntos resuelven el problema",
         "solucion colectiva"],
        ["El solarpunk cree que el cambio viene de la _____ (comunidad / tecnologia):",
         "Las herramientas ayudan pero las personas son el motor",
         "comunidad"],
    ],
    # Capitulo 6: Origenes del movimiento solarpunk
    [
        ["El movimiento solarpunk nacio alrededor del ano _____ (2012 / 2001):",
         "Justo despues de la expansion de las redes sociales",
         "2012"],
        ["El pais donde surgio el solarpunk fue _____ (brasil / japon):",
         "Pais de America del Sur famoso por su biodiversidad",
         "brasil"],
        ["El primer manifiesto solarpunk fue escrito en _____ (portugues / ingles):",
         "El idioma oficial de Brasil",
         "portugues"],
        ["El solarpunk nacio en _____ (internet / universidades):",
         "Blogs y foros donde la gente compartia ideas libremente",
         "internet"],
        ["El solarpunk se inspiro en el movimiento _____ (ecologista / feminista):",
         "Defensa del medio ambiente y critica al capitalismo industrial",
         "ecologista"],
        ["El nombre solarpunk une la palabra solar con _____ (punk / pop):",
         "Genero cultural de rebeldia y anticapitalismo",
         "punk"],
        ["El solarpunk llego a la literatura con antologias de cuentos _____ (colectivos / individuales):",
         "Varios autores distintos reunidos en un mismo libro",
         "colectivos"],
    ],
    # Capitulo 7: Arte y estetica solarpunk
    [
        ["En el solarpunk el arte busca ser _____ (accesible / exclusivo):",
         "El arte solarpunk quiere llegar a todos, no solo a museos",
         "accesible"],
        ["El arte solarpunk suele pintarse en _____ (murales / lienzos):",
         "Paredes de ciudades visibles para cualquier persona",
         "murales"],
        ["La arquitectura solarpunk integra _____ en los edificios (naturaleza / acero):",
         "Jardines verticales, techos vivos, agua de lluvia",
         "naturaleza"],
        ["El diseno solarpunk prefiere lo _____ a lo industrial (artesanal / masivo):",
         "Hecho a mano, con cuidado, por personas reales",
         "artesanal"],
        ["La moda solarpunk usa materiales _____ (sostenibles / sinteticos):",
         "Que no contaminan ni explotan recursos naturales",
         "sostenibles"],
        ["El solarpunk valora el arte como herramienta de _____ (cambio / entretenimiento):",
         "No es solo decoracion, sirve para transformar la sociedad",
         "cambio"],
        ["La musica solarpunk tiende a ser creada de forma _____ (colaborativa / individual):",
         "Grupos, colectivos y comunidades haciendo musica juntos",
         "colaborativa"],
    ],
    # Capitulo 8: Comunidad y vida cotidiana solarpunk
    [
        ["Las comunidades solarpunk prefieren vivir de forma _____ (cooperativa / individualista):",
         "Contrario a vivir solo y competir con otros",
         "cooperativa"],
        ["En el solarpunk los vecinos comparten _____ (herramientas / secretos):",
         "Una misma pala, un mismo taladro para toda la cuadra",
         "herramientas"],
        ["Las casas solarpunk suelen tener espacios _____ (comunes / privativos):",
         "Cocinas, jardines y talleres que todos usan",
         "comunes"],
        ["El cuidado de ninos y ancianos en el solarpunk es _____ (comunitario / individual):",
         "No solo la familia nuclear, toda la comunidad ayuda",
         "comunitario"],
        ["En el solarpunk se prioriza el tiempo _____ (libre / productivo):",
         "Vivir bien, descansar y disfrutar son tan importantes como trabajar",
         "libre"],
        ["El solarpunk elimina la distincion entre _____ y ocio (trabajo / estudio):",
         "Hacer algo util puede ser tambien placentero y viceversa",
         "trabajo"],
        ["Las fiestas en el solarpunk son _____ (comunitarias / privadas):",
         "Todos invitados, sin listas de acceso ni entradas de pago",
         "comunitarias"],
    ],
    # Capitulo 9: Energia y medio ambiente solarpunk
    [
        ["La principal fuente de energia en el solarpunk es _____ (solar / nuclear):",
         "La fuente mas abundante y limpia que existe",
         "solar"],
        ["El solarpunk tambien usa energia _____ ademas de solar (eolica / petroleo):",
         "La que viene del viento",
         "eolica"],
        ["El solarpunk busca una huella de carbono _____ (minima / maxima):",
         "Contaminar lo menos posible",
         "minima"],
        ["El agua en el solarpunk se gestiona de forma _____ (comunitaria / privada):",
         "Es un bien de todos, no una mercancia",
         "comunitaria"],
        ["El solarpunk promueve la _____ de residuos (reutilizacion / acumulacion):",
         "Darle una segunda vida a lo que ya existe",
         "reutilizacion"],
        ["Los ecosistemas en el solarpunk se _____ (restauran / explotan):",
         "Se reparan los danos causados por la industria",
         "restauran"],
        ["El solarpunk considera el cambio climatico como un problema _____ (politico / natural):",
         "Fue causado por decisiones humanas, no por la naturaleza sola",
         "politico"],
    ],
    # Capitulo 10: Alimentacion y agricultura solarpunk
    [
        ["El solarpunk promueve la agricultura _____ (local / industrial):",
         "Cerca de casa, sin grandes fabricas ni transporte largo",
         "local"],
        ["Las ciudades solarpunk tienen _____ urbanos para producir comida (huertos / supermercados):",
         "Espacios verdes donde la comunidad cultiva sus propios alimentos",
         "huertos"],
        ["El solarpunk prefiere la alimentacion de temporada porque es mas _____ (sostenible / barata):",
         "Lo que crece en su momento natural no necesita energia extra",
         "sostenible"],
        ["La semilla en el solarpunk debe ser _____ (libre / patentada):",
         "Que cualquiera pueda guardarla, intercambiarla y sembrarla",
         "libre"],
        ["El solarpunk rechaza los monocultivos porque destruyen la _____ (biodiversidad / economia):",
         "Sembrar solo una cosa empobrece el suelo y mata otras especies",
         "biodiversidad"],
        ["Compostar residuos organicos sirve para _____ el suelo (nutrir / limpiar):",
         "Devolver minerales y materia organica a la tierra",
         "nutrir"],
        ["El solarpunk valora el conocimiento _____ sobre plantas y cultivos (ancestral / cientifico):",
         "Sabiduria transmitida por generaciones en comunidades indigenas",
         "ancestral"],
    ],
    # Capitulo 11: Transporte y movilidad solarpunk
    [
        ["El transporte preferido en el solarpunk es _____ (bicicleta / avion):",
         "No contamina, no necesita combustible y es para todos",
         "bicicleta"],
        ["El solarpunk promueve el transporte _____ sobre el privado (publico / individual):",
         "Un autobus lleva a 50 personas; 50 autos contaminan mucho mas",
         "publico"],
        ["Las ciudades solarpunk disenan calles para _____ (peatones / autos):",
         "Prioridad a quien camina, no a quien conduce",
         "peatones"],
        ["El solarpunk apoya los vehiculos de propulsion _____ (electrica / a gasolina):",
         "Sin combustibles fosiles ni emisiones directas",
         "electrica"],
        ["Viajar menos lejos reduce la _____ de carbono (huella / velocidad):",
         "El impacto ambiental de cada desplazamiento",
         "huella"],
        ["El teletrabajo en el solarpunk reduce la necesidad de _____ (desplazarse / comunicarse):",
         "Si trabajas desde casa no tienes que moverte cada dia",
         "desplazarse"],
        ["Los puentes y caminos solarpunk priorizan la _____ (naturaleza / velocidad):",
         "Se construyen sin destruir ecosistemas ni rios",
         "naturaleza"],
    ],
    # Capitulo 12: Salud y bienestar solarpunk
    [
        ["En el solarpunk la salud se entiende como un bien _____ (comun / privado):",
         "Algo que pertenece a toda la sociedad, no a empresas",
         "comun"],
        ["El solarpunk promueve la medicina _____ junto a la convencional (tradicional / alternativa):",
         "Conocimientos de pueblos indigenas y comunidades sobre plantas y cuerpo",
         "tradicional"],
        ["El bienestar en el solarpunk incluye la salud _____ ademas de la fisica (mental / economica):",
         "La mente tambien necesita cuidado y descanso",
         "mental"],
        ["Los espacios verdes en las ciudades mejoran la salud _____ de las personas (mental / digestiva):",
         "Estar rodeado de naturaleza reduce el estres",
         "mental"],
        ["El solarpunk cree que el estres viene de un sistema _____ (injusto / natural):",
         "La ansiedad y el agotamiento son producto del capitalismo, no del ser humano",
         "injusto"],
        ["Cuidar a otros en el solarpunk es una responsabilidad _____ (comunitaria / individual):",
         "No solo el medico cuida: toda la comunidad se ocupa de sus miembros",
         "comunitaria"],
        ["El solarpunk ve el descanso como un _____ (derecho / lujo):",
         "No es un premio para los que trabajan mas, es algo basico",
         "derecho"],
    ],
    # Capitulo 13: Infancia y educacion solarpunk
    [
        ["La educacion solarpunk es _____ (libre / obligatoria):",
         "Sin presion ni castigos, cada quien aprende a su ritmo",
         "libre"],
        ["Los ninos en el solarpunk aprenden haciendo, es decir de forma _____ (practica / teorica):",
         "Con las manos, en el huerto, en el taller, no solo con libros",
         "practica"],
        ["El juego en el solarpunk es considerado una forma de _____ (aprendizaje / perder el tiempo):",
         "Jugar desarrolla creatividad, cooperacion y resolucion de problemas",
         "aprendizaje"],
        ["La infancia solarpunk crece en contacto con la _____ (naturaleza / tecnologia):",
         "Arboles, rios, animales y tierra antes que pantallas",
         "naturaleza"],
        ["En el solarpunk los adultos y ninos aprenden _____ (juntos / separados):",
         "Las generaciones se mezclan y cada una ensena algo a la otra",
         "juntos"],
        ["La curiosidad en el solarpunk es _____ (fomentada / controlada):",
         "Preguntar, explorar y dudar son virtudes, no problemas",
         "fomentada"],
        ["El error en el solarpunk es visto como parte del _____ (aprendizaje / fracaso):",
         "Equivocarse es normal y necesario para crecer",
         "aprendizaje"],
    ],
    # Capitulo 14: Memoria y historia solarpunk
    [
        ["El solarpunk valora la memoria de las comunidades _____ (originarias / coloniales):",
         "Pueblos que vivian aqui antes de la colonizacion",
         "originarias"],
        ["Recuperar lenguas indigenas es para el solarpunk un acto de _____ (resistencia / nostalgia):",
         "Preservar una lengua es preservar una forma de ver el mundo",
         "resistencia"],
        ["El solarpunk ve la historia oficial como una historia _____ (incompleta / verdadera):",
         "Siempre hay voces que no aparecen en los libros escolares",
         "incompleta"],
        ["La memoria colectiva en el solarpunk se transmite por _____ (oralidad / escritura):",
         "Cuentos, canciones y conversaciones entre generaciones",
         "oralidad"],
        ["El solarpunk rescata saberes de comunidades que fueron _____ (colonizadas / olvidadas):",
         "Pueblos cuyo conocimiento fue destruido o ignorado",
         "colonizadas"],
        ["Recordar el pasado en el solarpunk sirve para _____ el futuro (construir / repetir):",
         "Conocer lo que paso ayuda a no cometer los mismos errores",
         "construir"],
        ["El solarpunk incluye la historia de las mujeres como parte de la memoria _____ (colectiva / privada):",
         "Sus luchas y saberes pertenecen a toda la sociedad",
         "colectiva"],
    ],
    # Capitulo 15: El solarpunk como proyecto de vida
    [
        ["El solarpunk es mas un estilo de _____ que un genero literario (vida / moda):",
         "No es ropa ni decoracion, es como uno decide existir cada dia",
         "vida"],
        ["Vivir en solarpunk implica tomar decisiones _____ (conscientes / impulsivas):",
         "Pensar en el impacto de cada accion antes de actuar",
         "conscientes"],
        ["El solarpunk se puede practicar desde lo _____ (cotidiano / extraordinario):",
         "Compostar, reparar, compartir: cosas de todos los dias",
         "cotidiano"],
        ["Unirse a una comunidad es el primer paso _____ del solarpunk (practico / teorico):",
         "No se puede vivir en solarpunk completamente en solitario",
         "practico"],
        ["El solarpunk invita a imaginar futuros _____ (posibles / imposibles):",
         "Si no puedes imaginarlo, no puedes construirlo",
         "posibles"],
        ["La coherencia entre lo que se dice y se hace se llama _____ (congruencia / disciplina):",
         "Hacer lo que predicas, vivir como crees",
         "congruencia"],
        ["El solarpunk entiende la vida buena como algo _____ (colectivo / individual):",
         "No hay bienestar personal sin bienestar comunitario",
         "colectivo"],
    ],
]

# ---------------------------------------------------------------------------
# NARRATIVA
# ---------------------------------------------------------------------------

def introduccion():
    """Muestra el texto introductorio que contextualiza la historia del juego."""
    print("\n\nEres una nina en el ano 5284. Vas camino a tu casa y miras por la ventana mientras \n\n"
    "llevas una pregunta tan clara en tu cabeza que cualquiera podria verla al mirarte a los ojos: \n"
    "por que? \n\n"
    "Hace dos horas, en una clase de historia de tu escuela, hablaron sobre la guerra que comenzo \n"
    "en el ano 2027 con la invasion de China a Taiwan, durante el centenario del movimiento \n"
    "People's Liberation Army. Aquel acontecimiento impulso a China a tomar la isla por la fuerza. \n\n"
    "Estados Unidos, defendiendo a Taiwan, respondio lanzando dos misiles transcontinentales \n"
    "supersonicos contra dos de las ciudades mas importantes de China: Beijing y Shanghai. \n\n"
    "Rusia, aliado de China, ataco la capital de Estados Unidos y, apenas 23 segundos despues \n"
    "de que el misil fuera lanzado hacia Washington, Estados Unidos respondio por impulso y por \n"
    "sentirse contra las cuerdas. Lanzo armamento nuclear hacia Rusia, enviando cabezas nucleares \n"
    "a Moscu, San Petersburgo y Murmansk. \n\n"
    "Solo 41 segundos despues, China respondio con cuatro cabezas nucleares y Rusia con cinco \n"
    "mas dirigidas a Estados Unidos, sin un destino registrado. En ese momento, a las 2 y 34 de la manana de un \n"
    "sabado 16 de julio la sociedad tal y como era termino. Los pocos sobrevivientes, siglos tras la destruccion \n"
    "y el invierno nuclear, firmaron en nombre del miedo comun a otra autodestruccion masiva el llamado Pacto de la Segunda Sociedad. \n\n"
    "Absorta en este pensamiento ni siquiera piensas en cuanto falta para llegar a tu casa, pero al ver \n"
    "pasar la biblioteca al frente de tus ojos no puedes evitar pensar en si alli habran respuestas a tus preguntas: \n"
    "como naciones enteras fueron destruidas, por que lo hicieron y, mas importante, como una sociedad que suena tan autodestructiva, \n"
    "violenta y egoista pudo haberse convertido en esto que te rodea. Por lo que vas a la biblioteca y ves un libro que dice 'Post-society Punk'.\n\n")


def menu():
    """Pregunta al jugador si desea leer el libro y lo redirige segun su respuesta."""
    while True:
        accion = input("Lo lees? (y/n): ")

        if accion == "y":
            menu_principal()
            break
        elif accion == "n":
            print("Recuerda: todo pueblo que no conozca su historia esta condenado a repetirla.")
            break
        else:
            print("Entrada no valida. Por favor, ingresa 'y' para si o 'n' para no.")

# ---------------------------------------------------------------------------
# MENUS
# ---------------------------------------------------------------------------

def menu_principal():
    """Muestra el menu principal y despacha a Jugar, Dificultad o Creditos."""
    print("--- MENU PRINCIPAL ---")
    print("1. Jugar")
    print("2. Dificultad")
    print("3. Creditos")

    opcion = input("Selecciona una opcion del menu: ")

    if opcion == "1":
        inicializar_partida()
    elif opcion == "2":
        dificultad()
    elif opcion == "3":
        creditos()
    else:
        print("Opcion no valida, intenta de nuevo.")
        menu_principal()


def dificultad():
    """Permite al jugador elegir la cantidad de contenido que quiere leer."""
    global dificultad_piso, dificultad_biblioteca

    print("--- VAMOS A VER QUE TAN CURIOSO ERES ---\n")
    print("1. Mucho texto, dame algo corto\n")
    print("2. Me interesa pero quiero una experiencia casual\n")
    print("3. Tengo curiosidad y quiero aprender del tema\n")
    print("4. Quiero leer todo el libro y aprender del sistema de esta segunda sociedad\n")

    opcion = input("Selecciona que tanta curiosidad tienes para leer el libro:\n")

    if opcion == "1":
        dificultad_piso       = 5
        dificultad_biblioteca = 5
        menu_principal()
    elif opcion == "2":
        dificultad_piso       = 10
        dificultad_biblioteca = 10
        menu_principal()
    elif opcion == "3":
        dificultad_piso       = 13
        dificultad_biblioteca = 13
        menu_principal()
    elif opcion == "4":
        dificultad_piso       = 15
        dificultad_biblioteca = 15
        menu_principal()
    else:
        print("Demasiada curiosidad para un solo libro, por favor digita un numero mas tranquilo")
        dificultad()


def creditos():
    """Muestra los creditos del juego y regresa al menu principal."""
    print("Idea de Prof. Aurelio")
    print("Disenado por Tomas Andre Medina y Kaleb Coto")
    print("By CodeGaming")
    menu_principal()

# ---------------------------------------------------------------------------
# LOGICA DE LA PARTIDA
# ---------------------------------------------------------------------------

def inicializar_partida():
    """Genera el tamano aleatorio del libro y arranca el bucle de juego."""
    global dificultad_piso, dificultad_biblioteca
    global largo_piso, alto_biblioteca
    global indice_piso, indice_biblioteca, resultado_dado

    largo_piso        = random.randint(5, dificultad_piso)
    alto_biblioteca   = random.randint(5, dificultad_biblioteca)
    indice_piso       = 0
    indice_biblioteca = 0
    resultado_dado    = 0

    print("\nAhora al frente de ti hay un libro de " + str(alto_biblioteca) + " capitulos")
    print("de " + str(largo_piso) + " paginas cada capitulo. Al final de cada capitulo habra un formulario.")
    print("Tienes prisa, por lo tanto decides leer algunas paginas y verificar si aprendiste")
    print("lo necesario realizando el cuestionario.")
    print("Escoges las paginas que leeras tirando un dado de 4 caras (1, 2, 3 o 4).")
    print("Escribe 'info' para ver todos los comandos o 'stats' para ver tu progreso.\n")

    juego()


def juego():
    """Bucle principal de juego: recibe comandos del jugador y actualiza el estado."""
    global indice_piso, indice_biblioteca, resultado_dado
    global largo_piso, alto_biblioteca

    print("\nTienes ante ti un libro de " + str(alto_biblioteca) + " capitulos")
    print("con " + str(largo_piso) + " paginas cada uno.")
    print("Tiras un dado de 4 caras para decidir cuantas paginas avanzas.")
    print("Al final de cada capitulo hay un cuestionario sobre solarpunk.")
    print("Escribe 'info' para ver los comandos.\n")

    while True:
        cmd = input("> Comando: ")

        if cmd == "info":
            mostrar_info()

        elif cmd == "stats":
            mostrar_stats()

        elif cmd == "salir":
            print("\nCierras el libro. Tal vez otro dia...\n")
            break

        elif cmd == "tirar_dado":
            resultado_dado  = dado()
            indice_piso    += resultado_dado
            print("\nSacaste un " + str(resultado_dado) + ".")

            if indice_piso >= largo_piso:
                # Jugador llego al final del capitulo
                indice_piso = largo_piso - 1
                mostrar_pista()
                print("Llegaste al final del capitulo " + str(indice_biblioteca + 1) + ".")

                if cuestionario():
                    # Respuesta correcta: avanza al siguiente capitulo
                    indice_biblioteca += 1
                    indice_piso        = 0

                    if indice_biblioteca >= alto_biblioteca:
                        print("Terminaste el libro!")
                        print("Cerraste la ultima pagina con algo nuevo en tu cabeza.")
                        print("Ya sabes como pudo una sociedad tan rota convertirse en esto que te rodea.\n")
                        break
                    else:
                        print("Ahora en capitulo " + str(indice_biblioteca + 1) + ": " + titulos_capitulos[indice_biblioteca] + "\n")
                else:
                    # Respuesta incorrecta: retrocede un capitulo
                    if indice_biblioteca > 0:
                        indice_biblioteca -= 1
                        print("Vuelves al capitulo " + str(indice_biblioteca + 1) + " a repasar.\n")
                    else:
                        print("Estas en el primer capitulo. Repasas desde el principio.\n")
                    indice_piso = 0
            else:
                mostrar_pista()

        else:
            print("Comando '" + cmd + "' desconocido. Escribe 'info' para ayuda.")

# ---------------------------------------------------------------------------
# COMANDOS DE APOYO
# ---------------------------------------------------------------------------

def mostrar_info():
    """Imprime la lista de comandos disponibles durante la partida."""
    print("\n--- COMANDOS ---")
    print("tirar_dado  : avanzas paginas (dado de 4 caras)")
    print("stats       : ves tu progreso")
    print("info        : muestra esta ayuda")
    print("salir       : cierras el libro\n")


def mostrar_stats():
    """Muestra el capitulo actual, la pagina y el porcentaje de progreso del jugador."""
    global largo_piso, alto_biblioteca, indice_piso, indice_biblioteca, resultado_dado

    total  = largo_piso * alto_biblioteca
    leidas = indice_biblioteca * largo_piso + indice_piso

    if total > 0:
        pct = leidas * 100 // total
    else:
        pct = 0

    print("\n--- TUS STATS ---")
    print("Capitulo : " + str(indice_biblioteca + 1) + "/" + str(alto_biblioteca) + " - " + titulos_capitulos[indice_biblioteca])
    print("Pagina   : " + str(indice_piso) + "/" + str(largo_piso - 1))
    print("Progreso : " + str(pct) + "%")
    print("Ultimo dado: " + str(resultado_dado) + "\n")


def mostrar_pista():
    """
    Tira el dado de 4 caras y muestra esa cantidad de pistas del capitulo actual.
    Las pistas se toman desde la pagina actual hacia adelante sin salirse del rango.
    """
    global indice_piso, indice_biblioteca

    tiro         = dado()
    total_pistas = len(pistas[indice_biblioteca])

    print("\n  [Capitulo " + str(indice_biblioteca + 1) + " - " + titulos_capitulos[indice_biblioteca] + "]")
    print("  Tiraste el dado y sacaste " + str(tiro) + ". Lees " + str(tiro) + " pista(s):\n")

    pistas_mostradas = 0
    while pistas_mostradas < tiro:
        idx = indice_piso + pistas_mostradas
        if idx >= total_pistas:
            idx = total_pistas - 1
        print("  - Pista " + str(pistas_mostradas + 1) + ": " + pistas[indice_biblioteca][idx])
        pistas_mostradas += 1

    print("")


def cuestionario():
    """
    Hace hasta 7 preguntas del capitulo actual.
    - Si el jugador acumula 4 respuestas correctas: gana el cuestionario (True).
    - Si el jugador acumula 4 respuestas incorrectas: pierde el cuestionario (False).
    El cuestionario termina en cuanto se alcanza cualquiera de los dos limites.
    """
    global indice_biblioteca

    correctas   = 0
    incorrectas = 0
    numero      = 0

    print("\n=== CUESTIONARIO - Capitulo " + str(indice_biblioteca + 1) + " ===")
    print("7 preguntas. 4 correctas para avanzar, 4 incorrectas para retroceder.")
    print("Escribe 'pista' en cualquier momento para recibir una ayuda.\n")

    while numero < 7:
        pregunta  = cuestionarios[indice_biblioteca][numero][0]
        pista     = cuestionarios[indice_biblioteca][numero][1]
        respuesta = cuestionarios[indice_biblioteca][numero][2]

        print("Pregunta " + str(numero + 1) + "/7  |  Correctas: " + str(correctas) + "  Incorrectas: " + str(incorrectas))
        print(pregunta)

        while True:
            entrada = input("Tu respuesta: ")

            if entrada == "pista":
                print("Pista: " + pista + "\n")
            elif entrada == respuesta:
                correctas += 1
                print("Correcto! (" + str(correctas) + " buenas)\n")
                break
            else:
                incorrectas += 1
                print("Incorrecto. Era: " + respuesta + " (" + str(incorrectas) + " malas)\n")
                break

        if correctas >= 4:
            print("Superaste el cuestionario con " + str(correctas) + " correctas. Avanzas al siguiente capitulo.\n")
            return True

        if incorrectas >= 4:
            print("Demasiados errores (" + str(incorrectas) + " incorrectas). Vuelves a repasar.\n")
            return False

        numero += 1

    # Se terminaron las 7 preguntas sin llegar a 4 de ninguna clase
    # Gana quien tenga mas (en empate, se considera perdido)
    if correctas > incorrectas:
        print("Fin del cuestionario. " + str(correctas) + " correctas vs " + str(incorrectas) + " incorrectas. Avanzas!\n")
        return True
    else:
        print("Fin del cuestionario. " + str(correctas) + " correctas vs " + str(incorrectas) + " incorrectas. Vuelves a repasar.\n")
        return False


def dado():
    """Simula el lanzamiento de un dado de 4 caras. Devuelve un entero entre 1 y 4."""
    return random.randint(1, 4)

# ---------------------------------------------------------------------------
# UTILIDAD DE DEPURACION (no se usa en el flujo normal del juego)
# ---------------------------------------------------------------------------

def debug_estado():
    """Imprime todas las variables globales de estado. Util para depuracion."""
    global indice_piso, indice_biblioteca
    global dificultad_piso, dificultad_biblioteca
    global largo_piso, alto_biblioteca

    print("indice_piso      : " + str(indice_piso))
    print("indice_biblioteca: " + str(indice_biblioteca))
    print("dificultad_piso  : " + str(dificultad_piso))
    print("dificultad_biblio: " + str(dificultad_biblioteca))
    print("largo_piso       : " + str(largo_piso))
    print("alto_biblioteca  : " + str(alto_biblioteca))

# ---------------------------------------------------------------------------
# PUNTO DE ENTRADA
# ---------------------------------------------------------------------------

introduccion()
menu()
#dfcrgvthbyjnumkill