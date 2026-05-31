import time
import random

dificultad_piso = 10
dificultad_biblioteca = 10
largo_piso = 0
alto_biblioteca = 0
mapa = 0
indice_piso = 0
indice_biblioteca = 0

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
    print("2. dificultad")
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
    juego(1)

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
    print("--- VAMOS A VER QUE TAN CURIOSO ERES---")
    print("1. Mucho texto dame algo corto")
    print("2. Me interasa pero quiero una experiencia casual")
    print("3. Tengo curosidad y quiero aprender del tema")
    print("4. Quieres leer todo el libro y aprender del sistema de esta segunda sociedad")
    SE = input("Selecciona que tanta curiosidad tienes para leer el libro: ")
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
        print("demaciada curiosidad para un solo libro porfavor digita un numero mas tranquilo")

def creditos():
    print("Idea de Prof.Aurelio")
    print("disenado por Tomas Andre Medina y Kaleb Coto")
    print("By CodeGaming")
    menu1()
        
def juego(intro = 0):
    global mapa
    global indice_piso
    global indice_biblioteca
    global dificultad_piso
    global dificultad_biblioteca
    global largo_piso
    global alto_biblioteca
    if intro == 1:
        print("Ahora al frente de ti hay un libro de", alto_biblioteca, "capitulos")
        print("de", largo_piso, " paginas cada capitulo, al final de cada capitulo habra un formulario")
        print("tienes prisa porlotanto decides leer algunas paginas y verificar si aprendiste lo nesesario realizando el cuestionario")
        print("escoges las paginas que leeras tirando un dado de 4 caras donde las opciones pueden ser 1, 2, 3 y 4")
        print("porlotanto debes tirar los dados (con t.tirar dados) para saber que pagina leer")
        print("si escribes (info) te apareseran todos los comandos para jugar mas fuido")
        print("y con (stats) tu situacion en la historia por que capitulo vas en que pagina etc")
        juego()

    elif intro == 0:
        TD = input()
        if TD == "t.tirar dados":
            largo_piso + dado()
            


def que_esta_pasando():
    global mapa
    global indice_piso
    global indice_biblioteca
    global dificultad_piso
    global dificultad_biblioteca
    global largo_piso
    global alto_biblioteca

    print("mapa", mapa)
    print("inidice piso", indice_piso)
    print("indice_biblioteca", indice_biblioteca)
    print("dificultad piso", dificultad_piso)
    print("dificultad bibloteca", dificultad_biblioteca)
    print("largopiso", largo_piso)
    print("alto biblioteca", alto_biblioteca)
    print(mapa[indice_biblioteca][indice_piso])

def dado():
    TD = random.randint(1, 4)
    return TD


# introduccion()
# menu()
# while True:

#     print(num)
#     if num == 11:
#         num = 0 
#     else:
#         num += 1