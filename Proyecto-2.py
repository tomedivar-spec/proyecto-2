import time
import random

dificultad_piso = 10
dificultad_biblioteca = 10
largo_piso = 0
alto_biblioteca = 0
mapa = 0
indice_piso = 0
indice_biblioteca = 0
resultado_dado = 0

def introduccion():
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
    while True:
        AC = input("Lo lees? (y/n): ")
        
        if AC == "y":
            menu1()
            break
        elif AC == "n":
            print("Recuerda: todo pueblo que no conozca su historia esta condenado a repetirla.")
            break
        else:
            print("Entrada no valida. Por favor, ingresa 'y' para si o 'n' para no.")

def menu1():
    print("--- MENU PRINCIPAL ---")
    print("1. Jugar")
    print("2. Dificultad")
    print("3. Creditos")

    SE = input("Selecciona una opcion del menu: ")
    ME = int(SE)
        
    if ME == 1:
        genrador_alzar_de_juego()
        
    elif ME == 2:
        dificultad()

    elif ME == 3:
        creditos()

    else:
        menu1()

def genrador_alzar_de_juego():
    global dificultad_piso
    global dificultad_biblioteca
    global largo_piso
    global alto_biblioteca
    global mapa

    largo_piso = random.randint(5, dificultad_piso)
    alto_biblioteca = random.randint(5, dificultad_biblioteca)
    mapa = creador_de_mapa(largo_piso, largo_piso, alto_biblioteca, alto_biblioteca)

    print("\nAhora al frente de ti hay un libro de", alto_biblioteca, "capitulos\n"
    "de", largo_piso, " paginas cada capitulo, al final de cada capitulo habra un formulario\n"
    "tienes prisa por lo tanto decides leer algunas paginas y verificar si aprendiste lo necesario realizando el cuestionario\n"
    "escoges las paginas que leeras tirando un dado de 4 caras donde las opciones pueden ser 1, 2, 3 y 4\n"
    "por lo tanto debes tirar los dados (con tirar_dado) para saber que pagina leer\n"
    "si escribes (info) te apareceran todos los comandos para jugar mas fluido\n"
    "y con (stats) tu situacion en la historia: por que capitulo vas, en que pagina, etc\n")

    juego()

def creador_de_mapa(largo, stopl, stopa, alto):
    piso = creador_de_piso(largo, stopl)
    resultado = []
    while alto > 0:
        resultado += [piso]
        alto -= 1
    return resultado

def creador_de_piso(largo, stopl):
    resultado = []
    valor = [0]
    while largo > 0:
        resultado += valor 
        valor[0] += 1
        largo -= 1
    return resultado

def dificultad():
    global dificultad_piso
    global dificultad_biblioteca
    print("--- VAMOS A VER QUE TAN CURIOSO ERES ---\n")
    print("1. Mucho texto, dame algo corto\n")
    print("2. Me interesa pero quiero una experiencia casual\n")
    print("3. Tengo curiosidad y quiero aprender del tema\n")
    print("4. Quiero leer todo el libro y aprender del sistema de esta segunda sociedad\n")
    SE = input("Selecciona que tanta curiosidad tienes para leer el libro: \n")
    ME = int(SE)

    if ME == 1:
        dificultad_piso = 5
        dificultad_biblioteca = 5
        menu1()
    
    elif ME == 2:
        dificultad_piso = 10
        dificultad_biblioteca = 10
        menu1()
        
    elif ME == 3:
        dificultad_piso = 13
        dificultad_biblioteca = 13
        menu1()
    
    elif ME == 4:
        dificultad_piso = 15
        dificultad_biblioteca = 15
        menu1()
    
    else:
        print("Demasiada curiosidad para un solo libro, por favor digita un numero mas tranquilo")
        dificultad()

def creditos():
    print("Idea de Prof. Aurelio")
    print("Disenado por Tomas Andre Medina y Kaleb Coto")
    print("By CodeGaming")
    menu1()

# Titulos y pistas definidos una sola vez para usar en todo el programa
titulos_capitulos = [
    "Que es el solarpunk",
    "Economia y ciudad solarpunk",
    "Politica y educacion solarpunk",
    "Tecnologia y resistencia solarpunk",
    "Cultura y futuro solarpunk",
]

pistas = [
    ["Pista cap1 pag1", "Pista cap1 pag2", "Pista cap1 pag3", "Pista cap1 pag4", "Pista cap1 pag5"],
    ["Pista cap2 pag1", "Pista cap2 pag2", "Pista cap2 pag3", "Pista cap2 pag4", "Pista cap2 pag5"],
    ["Pista cap3 pag1", "Pista cap3 pag2", "Pista cap3 pag3", "Pista cap3 pag4", "Pista cap3 pag5"],
    ["Pista cap4 pag1", "Pista cap4 pag2", "Pista cap4 pag3", "Pista cap4 pag4", "Pista cap4 pag5"],
    ["Pista cap5 pag1", "Pista cap5 pag2", "Pista cap5 pag3", "Pista cap5 pag4", "Pista cap5 pag5"],
]

def juego():
    global mapa
    global indice_piso
    global indice_biblioteca
    global dificultad_piso
    global dificultad_biblioteca
    global largo_piso
    global alto_biblioteca
    global resultado_dado

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
            resultado_dado = dado()
            indice_piso   += resultado_dado
            print("\nSacaste un " + str(resultado_dado) + ".")
 
            if indice_piso >= largo_piso:
                indice_piso = largo_piso - 1
                mostrar_pista()
                print("Llegaste al final del capitulo " + str(indice_biblioteca + 1) + ".")
 
                if cuestionario():
                    indice_biblioteca += 1
                    indice_piso        = 0
 
                    if indice_biblioteca >= alto_biblioteca:
                        print("Terminaste el libro!")
                        print("Cerraste la ultima pagina con algo nuevo en tu cabeza.")
                        print("Ya sabes como pudo una sociedad tan rota convertirse en esto que te rodea.\n")
                        break
                    else:
                        cap_titulo = indice_biblioteca % len(titulos_capitulos)
                        print("Ahora en capitulo " + str(indice_biblioteca + 1) + ": " + titulos_capitulos[cap_titulo] + "\n")
                else:
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

def mostrar_info():
    print("\n--- COMANDOS ---")
    print("tirar_dado  : avanzas paginas (dado de 4 caras)")
    print("stats       : ves tu progreso")
    print("info        : muestra esta ayuda")
    print("salir       : cierras el libro\n")
 
def mostrar_stats():
    global largo_piso, alto_biblioteca, indice_piso, indice_biblioteca, resultado_dado
    total   = largo_piso * alto_biblioteca
    leidas  = indice_biblioteca * largo_piso + indice_piso
    if total > 0:
        pct = leidas * 100 // total
    else:
        pct = 0
    cap = indice_biblioteca % len(titulos_capitulos)
    print("\n--- TUS STATS ---")
    print("Capitulo : " + str(indice_biblioteca + 1) + "/" + str(alto_biblioteca) + " - " + titulos_capitulos[cap])
    print("Pagina   : " + str(indice_piso) + "/" + str(largo_piso - 1))
    print("Progreso : " + str(pct) + "%")
    print("Ultimo dado: " + str(resultado_dado) + "\n")
 
def mostrar_pista():
    global indice_piso, indice_biblioteca
    cap = indice_biblioteca % len(pistas)
    idx = indice_piso
    if idx >= len(pistas[cap]):
        idx = len(pistas[cap]) - 1
    print("\n  [Capitulo " + str(indice_biblioteca + 1) + " - " + titulos_capitulos[cap] + "]")
    # FIX: pistas[cap][idx] ya es un string, no una lista dentro de lista
    print("  Pagina " + str(indice_piso) + ": " + pistas[cap][idx] + "\n")

def cuestionario():
    preguntas = [
        "Segun el solarpunk, la tecnologia debe trabajar _____ la naturaleza (con / contra):",
        "El movimiento solarpunk nacio en cual pais alrededor del 2012:",
        "La base economica del solarpunk son las _____ (cooperativas / empresas):",
        "En el solarpunk la toma de decisiones se hace por _____ (asambleas / presidentes):",
        "El solarpunk dice que la esperanza es un acto _____ (politico / religioso):",
    ]

    pistas_cuestionario = [
        "Piensa en como el solarpunk ve a la naturaleza: como aliada o enemiga?",
        "Pista: pais de America del Sur famoso por su biodiversidad",
        "Pista: organizaciones donde todos son duenos y trabajadores a la vez",
        "Pista: reunion donde todos pueden hablar y votar",
        "Pista: tiene que ver con cambiar el mundo, no con la fe",
    ]

    respuestas = ["con", "brasil", "cooperativas", "asambleas", "politico"]

    global indice_biblioteca
    # FIX: usar % para que siempre haya una pregunta sin importar cuantos capitulos haya
    cap = indice_biblioteca % len(preguntas)

    print("\n=== CUESTIONARIO - Capitulo " + str(indice_biblioteca + 1) + " ===")
    print(preguntas[cap])
    print("(escribe 'pista' si la necesitas)\n")
 
    while True:
        respuesta = input("Tu respuesta: ").strip().lower()
        if respuesta == "pista":
            # FIX: pistas_cuestionario[cap] ya es un string directo
            print("Pista: " + pistas_cuestionario[cap] + "\n")
        elif respuesta == respuestas[cap]:
            print("Correcto! Avanzas al siguiente capitulo.\n")
            return True
        else:
            print("Incorrecto. La respuesta era: " + respuestas[cap] + "\n")
            return False

def que_esta_pasando():
    global mapa, indice_piso, indice_biblioteca
    global dificultad_piso, dificultad_biblioteca
    global largo_piso, alto_biblioteca

    print("mapa", mapa)
    print("indice piso", indice_piso)
    print("indice_biblioteca", indice_biblioteca)
    print("dificultad piso", dificultad_piso)
    print("dificultad biblioteca", dificultad_biblioteca)
    print("largo piso", largo_piso)
    print("alto biblioteca", alto_biblioteca)
    print(mapa[indice_biblioteca][indice_piso])

def dado():
    TD = random.randint(1, 4)
    return TD

introduccion()
menu()
