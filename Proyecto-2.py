"""
=============================================================
  POST SOCIETY PUNK
  Taller de Programación - Biblioteca Anarquista
  Juego de terminal
  Kaleb Coto
  Tomás André 
=============================================================
"""
 
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
# TEMAS
# ---------------------------------------------------------------------------


TEMAS = [
    "Matriz energética sostenible",
    "Movilidad urbana",
    "Terceros espacios",
    "Agricultura sostenible",
    "Economías alternativas",
    "Vivienda bioclimática",
    "Manejo del agua",
    "Biodiversidad",
    "Tecnología apropiada",
    "Gestión de residuos",
    "Educación comunitaria",
    "Salud y bienestar",
    "Resiliencia ante desastres",
    "Gobernanza participativa",
    "Lunarpunk"
]
 
# =========================
# CÁPSULAS DE CONOCIMIENTO
# =========================
 
CAPSULAS = {
    0: [  # Tema: Matriz energética sostenible
        "La energía solar fotovoltaica convierte la luz del sol directamente en electricidad mediante paneles de silicio.",
        "Las redes eléctricas descentralizadas ('microgrids') permiten que comunidades generen y compartan su propia energía.",
        "La energía eólica es ya la fuente de electricidad más barata en muchas regiones del mundo.",
        "Los sistemas de almacenamiento con baterías de ion-litio permiten usar energía solar durante la noche.",
        "La cogeneración aprovecha el calor residual de producir electricidad para calentar hogares y edificios.",
        "Los aerogeneradores usan la fuerza del viento para producir electricidad renovable.",
        "La energía hidroeléctrica se genera usando el movimiento del agua de ríos o cascadas.",
        "La energía geotérmica aprovecha el calor natural que existe bajo la Tierra.",
        "Los restos de plantas y comida pueden convertirse en energía útil mediante biomasa.",
        "Las redes inteligentes distribuyen la electricidad de manera automática y eficiente.",
    ],
    1: [  # Tema: Movilidad urbana
        "Las ciudades con carriles bici bien diseñados reducen hasta un 40% el uso de automóviles privados.",
        "El tranvía moderno consume hasta 10 veces menos energía por pasajero que un auto particular.",
        "El diseño urbano '15 minutos' busca que todas las necesidades básicas estén a pie o en bici desde casa.",
        "Los sistemas de bicicletas compartidas reducen emisiones y congestión en ciudades medianas y grandes.",
        "Calles peatonales activas aumentan el comercio local y la cohesión social de los barrios.",
        "El transporte público eléctrico reduce significativamente las emisiones de carbono.",
        "Los vehículos compartidos optimizan el uso de la infraestructura vial.",
        "La infraestructura ciclista segura fomenta la movilidad activa.",
        "El diseño de ciudades sin autos mejora la calidad del aire y el espacio público.",
        "La movilidad sostenible es clave para reducir emisiones urbanas.",
    ],
    2: [  # Tema: Terceros espacios
        "Los 'terceros espacios' son lugares públicos fuera del hogar y el trabajo: parques, plazas, bibliotecas.",
        "Las bibliotecas comunitarias son uno de los terceros espacios más democráticos: accesibles a todas las personas.",
        "Los centros comunitarios autogestionados fomentan la participación ciudadana y la toma de decisiones colectiva.",
        "Los huertos urbanos comunitarios combinan producción de alimentos con espacio social y educativo.",
        "El diseño de espacios públicos inclusivos considera las necesidades de niñez, adultos mayores y personas con discapacidad.",
        "Los parques públicos mejoran la salud mental y física de las comunidades.",
        "Los centros culturales ofrecen espacios para el arte, música y expresión comunitaria.",
        "Los talleres compartidos permiten que la comunidad acceda a herramientas y equipos.",
        "Los cafés comunitarios son espacios de encuentro y convivencia.",
        "Las plazas públicas activas fortalecen la identidad comunitaria.",
    ],
    3: [  # Tema: Agricultura sostenible
        "La permacultura diseña sistemas agrícolas que imitan la diversidad y resiliencia de los ecosistemas naturales.",
        "La agroforestería combina árboles con cultivos y ganadería, mejorando suelos y capturando carbono.",
        "Los cultivos de cobertura previenen la erosión del suelo y aumentan su fertilidad de forma natural.",
        "La agricultura regenerativa busca devolver carbono al suelo, revertiendo parte del cambio climático.",
        "Las semillas criollas o nativas son más resistentes al clima local y no dependen de corporaciones.",
        "El compostaje convierte residuos orgánicos en abono para cultivos.",
        "La rotación de cultivos mantiene la salud del suelo de forma natural.",
        "Los cultivos hidropónicos producen alimentos usando menos agua.",
        "Los polinizadores como abejas y mariposas son esenciales para la agricultura.",
        "La captación de agua de lluvia reduce dependencia de sistemas centralizados.",
    ],
    4: [  # Tema: Economías alternativas
        "La economía del regalo se basa en dar sin esperar retribución directa, fortaleciendo lazos comunitarios.",
        "Las cooperativas son empresas propiedad de sus trabajadoras/es, que distribuyen beneficios de forma democrática.",
        "Las bibliotecas de herramientas permiten compartir objetos de uso poco frecuente, reduciendo consumo.",
        "El trueque comunitario organizado puede satisfacer necesidades sin usar dinero.",
        "La economía circular diseña productos para que sus materiales sean reutilizados indefinidamente.",
        "Los bancos de tiempo permiten intercambiar servicios sin dinero.",
        "La reutilización de objetos reduce la necesidad de producción nueva.",
        "La reparación comunitaria extiende la vida útil de productos.",
        "El intercambio de bienes fortalece la red comunitaria.",
        "Las monedas locales circulan beneficios dentro de la comunidad.",
    ],
    5: [  # Tema: Vivienda bioclimática
        "Los edificios bioclimáticos aprovechan el clima local para reducir el consumo energético.",
        "El aislamiento térmico evita que el calor escape durante los meses fríos.",
        "La madera sostenible procedente de bosques responsablemente gestionados almacena carbono.",
        "Los techos verdes regulan la temperatura interior y absorben agua de lluvia.",
        "La ventilación natural utiliza corrientes de aire para refrescar los edificios sin sistemas mecánicos.",
        "Los paneles solares integrados en el diseño arquitectónico generan electricidad localmente.",
        "El diseño pasivo aprovecha la orientación, sombra y ventilación para mantener confort.",
        "Las ventanas eficientes con doble acristalamiento reducen pérdidas de calor.",
        "Los espacios multifuncionales reducen la necesidad de construir más infraestructura.",
        "La construcción modular genera menos desperdicios.",
    ],
    6: [  # Tema: Manejo del agua
        "Los techos pueden recoger agua de lluvia y almacenarla para usos domésticos.",
        "Los depósitos de almacenamiento permiten disponer de agua durante periodos secos.",
        "Las aguas grises procedentes de duchas y lavamanos pueden reutilizarse para riego.",
        "Los filtros de arena y grava eliminan impurezas del agua de forma natural.",
        "Los humedales artificiales pueden tratar aguas residuales mediante procesos biológicos.",
        "Conservar bosques alrededor de ríos mejora la calidad del agua.",
        "Los sensores ayudan a detectar fugas y controlar el consumo de agua.",
        "Los dispositivos ahorradores reducen el desperdicio de agua.",
        "Los canales y estanques ayudan a gestionar el exceso de lluvia.",
        "La recarga de acuíferos permite que el agua vuelva al subsuelo de forma natural.",
    ],
    7: [  # Tema: Biodiversidad
        "La reforestación con especies nativas proporciona refugio a muchas especies locales.",
        "Los corredores biológicos conectan diferentes hábitats para que los animales se desplacen con seguridad.",
        "La protección de aves nativas como el kiwi y el kea es fundamental para su supervivencia.",
        "El control de especies invasoras ayuda a proteger especies nativas.",
        "La restauración de ecosistemas costeros reduce la erosión y proporciona hábitats importantes.",
        "Las áreas marinas protegidas ayudan a recuperar poblaciones de peces.",
        "Los humedales filtran agua, almacenan carbono y sirven de refugio para aves acuáticas.",
        "Los insectos polinizadores contribuyen a la reproducción de muchas plantas.",
        "El monitoreo ecológico permite tomar mejores decisiones sobre conservación.",
        "La agricultura amigable con la fauna permite coexistencia entre cultivos y vida silvestre.",
    ],
    8: [  # Tema: Tecnología apropiada
        "La tecnología apropiada busca soluciones fáciles de entender y reparar.",
        "Los productos pueden mantenerse funcionando durante años gracias a reparaciones sencillas.",
        "El software de código abierto permite que cualquiera estudie y mejore su funcionamiento.",
        "La producción local reduce dependencia de cadenas de suministro lejanas.",
        "Las impresoras 3D pueden fabricar piezas de repuesto cuando se necesitan.",
        "La comunidad puede compartir equipos en lugar de que cada persona compre los suyos.",
        "Los dispositivos modulares permiten reemplazar componentes dañados sin desechar todo.",
        "La tecnología apropiada prioriza un bajo consumo energético.",
        "Los sensores ayudan a monitorear calidad del aire, agua y consumo energético.",
        "Las comunidades pueden gestionar sus propias redes de comunicación.",
    ],
    9: [  # Tema: Gestión de residuos
        "La separación en origen permite clasificar residuos desde el momento en que se generan.",
        "Muchos materiales pueden transformarse en nuevos productos mediante reciclaje.",
        "Los residuos orgánicos pueden convertirse en abono para cultivos mediante compostaje.",
        "La economía circular mantiene los materiales en uso durante más tiempo.",
        "Los objetos pueden utilizarse nuevamente antes de desecharse mediante reutilización.",
        "Los talleres comunitarios ayudan a extender la vida útil de los productos.",
        "Menos envases significa menos residuos en el medio ambiente.",
        "Los aparatos electrónicos contienen materiales valiosos recuperables.",
        "Los centros de clasificación permiten separar materiales para facilitar su reciclaje.",
        "La estrategia de basura cero busca minimizar la cantidad de residuos enviados a vertederos.",
    ],
    10: [  # Tema: Educación comunitaria
        "Las comunidades solarpunk fomentan el aprendizaje colaborativo entre vecinos.",
        "Las bibliotecas comunitarias pueden ofrecer herramientas, semillas y materiales educativos.",
        "Los talleres vecinales permiten enseñar habilidades como carpintería, agricultura o reparación.",
        "Los habitantes aprenden cómo proteger los ecosistemas y utilizar recursos sosteniblemente.",
        "Los ciudadanos pueden colaborar en proyectos científicos registrando aves, plantas o datos climáticos.",
        "Las personas mayores pueden compartir experiencias valiosas con nuevas generaciones.",
        "La comunidad aprende a mantener sistemas de energía renovable y tecnologías locales.",
        "Todos los habitantes tienen acceso a conocimientos básicos sobre tecnología e internet.",
        "La educación continúa durante toda la vida y no termina al finalizar la escuela.",
        "Los huertos comunitarios sirven para enseñar agricultura sostenible.",
    ],
    11: [  # Tema: Salud y bienestar
        "Los parques y jardines mejoran la salud física y mental.",
        "Consumir alimentos frescos y locales favorece una mejor nutrición.",
        "Caminar, andar en bicicleta y practicar deportes fortalece la salud.",
        "Prevenir enfermedades suele ser más efectivo que tratarlas.",
        "La reducción de la contaminación mejora la calidad de vida.",
        "El bienestar emocional es tan importante como la salud física.",
        "Dormir bien favorece la recuperación del cuerpo y la mente.",
        "Las relaciones comunitarias ayudan a reducir el estrés.",
        "Las actividades recreativas mejoran el bienestar general.",
        "El contacto frecuente con la naturaleza tiene efectos positivos sobre la salud.",
    ],
    12: [  # Tema: Resiliencia ante desastres
        "Las comunidades preparan protocolos para terremotos, tormentas o inundaciones.",
        "Mantener reservas alimentarias ayuda durante interrupciones del suministro.",
        "Las baterías permiten mantener servicios esenciales durante emergencias.",
        "El almacenamiento de agua aumenta la seguridad hídrica.",
        "Los refugios ofrecen protección durante emergencias.",
        "Los sistemas de alerta permiten reaccionar rápidamente ante peligros.",
        "Los vecinos pueden coordinar ayuda mutua durante emergencias.",
        "Las infraestructuras se diseñan para resistir cambios climáticos.",
        "Practicar respuestas mejora la preparación ante emergencias.",
        "Varias fuentes energéticas reducen riesgos de apagones.",
    ],
    13: [  # Tema: Gobernanza participativa
        "Las decisiones importantes pueden discutirse públicamente en asambleas comunitarias.",
        "Los ciudadanos participan directamente en ciertas decisiones mediante democracia directa.",
        "La información pública fortalece la confianza en las instituciones.",
        "La comunidad decide cómo utilizar parte de los recursos mediante presupuestos participativos.",
        "Se buscan acuerdos aceptables para la mayoría mediante consenso.",
        "Los jóvenes aportan nuevas perspectivas a las decisiones comunitarias.",
        "La colaboración entre vecinos fortalece la comunidad.",
        "Los recursos pueden administrarse colectivamente mediante gestión compartida.",
        "Los desacuerdos se solucionan mediante diálogo y resolución de conflictos.",
        "Los líderes facilitan la organización local sin tomar decisiones unilaterales.",
    ],
    14: [  # Tema: Lunarpunk
        "La tecnología lunarpunk se integra al entorno sin ser visualmente dominante.",
        "Los sistemas energéticos pueden ocultarse dentro de edificios o paisajes.",
        "La eficiencia es más importante que exhibir tecnología.",
        "La naturaleza se considera una parte esencial de la vida cotidiana.",
        "Los ciclos lunares pueden utilizarse como referencia cultural.",
        "La observación del entorno fortalece la conexión comunitaria.",
        "Las actividades nocturnas reducen contaminación lumínica innecesaria.",
        "La iluminación eficiente protege ecosistemas nocturnos.",
        "La producción local evita dependencias externas excesivas.",
        "Los edificios se mezclan visualmente con el paisaje mediante arquitectura integrada.",
    ],
}


# =========================
# PREGUNTAS Y RESPUESTAS
# =========================
 
PREGUNTAS = {
    0: [  # Tema: Matriz energética sostenible
        "¿Qué convierte la energía solar fotovoltaica?",
        "¿Cómo se llaman las redes eléctricas descentralizadas?",
        "¿Qué fuente de energía es la más barata en muchas regiones?",
        "¿Qué tecnología permite usar energía solar de noche?",
        "¿Qué aprovecha la cogeneración además de producir electricidad?",
    ],
    1: [  # Tema: Movilidad urbana
        "¿Cuánto pueden reducir los carriles bici el uso de autos?",
        "¿Cuántas veces menos energía consume el tranvía vs. el auto?",
        "¿Qué busca el diseño urbano de '15 minutos'?",
        "¿Qué efecto tienen las bicicletas compartidas?",
        "¿Qué beneficio tienen las calles peatonales?",
    ],
    2: [  # Tema: Terceros espacios
        "¿Qué son los 'terceros espacios'?",
        "¿Cuál es uno de los terceros espacios más democráticos?",
        "¿Qué fomentan los centros comunitarios autogestionados?",
        "¿Qué combinan los huertos urbanos comunitarios?",
        "¿A quiénes considera el diseño de espacios públicos inclusivos?",
    ],
    3: [  # Tema: Agricultura sostenible
        "¿Qué imita la permacultura?",
        "¿Qué combina la agroforestería?",
        "¿Para qué sirven los cultivos de cobertura?",
        "¿Qué busca la agricultura regenerativa?",
        "¿Qué ventaja tienen las semillas criollas?",
    ],
    4: [  # Tema: Economías alternativas
        "¿En qué se basa la economía del regalo?",
        "¿Qué son las cooperativas?",
        "¿Para qué sirven las bibliotecas de herramientas?",
        "¿Qué puede hacer el trueque comunitario?",
        "¿Qué diseña la economía circular?",
    ],
    5: [  # Tema: Vivienda bioclimática
        "¿Cómo aprovechan los edificios bioclimáticos el clima?",
        "¿Qué evita el aislamiento térmico?",
        "¿Qué beneficio tiene la madera sostenible?",
        "¿Qué hacen los techos verdes?",
        "¿Qué aprovecha el diseño pasivo?",
    ],
    6: [  # Tema: Manejo del agua
        "¿Qué recoge la captación de lluvia?",
        "¿Para qué sirven los tanques de almacenamiento?",
        "¿Qué son las aguas grises?",
        "¿Qué usan los filtros naturales?",
        "¿Qué hacen los humedales artificiales?",
    ],
    7: [  # Tema: Biodiversidad
        "¿Qué árboles se usan en reforestación nativa?",
        "¿Qué conectan los corredores biológicos?",
        "¿Cuál es un ave nativa de Nueva Zelanda?",
        "¿Qué problema causan las especies invasoras?",
        "¿Qué hacen las áreas marinas protegidas?",
    ],
    8: [  # Tema: Tecnología apropiada
        "¿Qué busca la tecnología apropiada?",
        "¿Qué permite el código abierto?",
        "¿Qué reduce la fabricación local?",
        "¿Qué pueden fabricar impresoras 3D?",
        "¿Qué promueven las herramientas compartidas?",
    ],
    9: [  # Tema: Gestión de residuos
        "¿Qué es la separación en origen?",
        "¿Qué produce el compostaje?",
        "¿Qué busca la economía circular?",
        "¿Qué significa reutilizar?",
        "¿Qué hacen los talleres de reparación?",
    ],
    10: [  # Tema: Educación comunitaria
        "¿Qué promueve el aprendizaje colaborativo?",
        "¿Qué pueden prestar las bibliotecas comunitarias?",
        "¿Qué enseñan los talleres vecinales?",
        "¿Qué es la ciencia ciudadana?",
        "¿Qué enseña un huerto educativo?",
    ],
    11: [  # Tema: Salud y bienestar
        "¿Qué mejoran los espacios verdes?",
        "¿Qué favorece la alimentación saludable?",
        "¿Qué beneficio tiene caminar?",
        "¿Qué busca la salud preventiva?",
        "¿Qué mejora el aire limpio?",
    ],
    12: [  # Tema: Resiliencia ante desastres
        "¿Para qué sirven los planes de emergencia?",
        "¿Por qué mantener reservas alimentarias?",
        "¿Qué función cumplen las baterías de respaldo?",
        "¿Por qué almacenar agua?",
        "¿Cuál es función de las alertas tempranas?",
    ],
    13: [  # Tema: Gobernanza participativa
        "¿Qué son las asambleas comunitarias?",
        "¿Qué caracteriza la democracia directa?",
        "¿Por qué importa la transparencia?",
        "¿Qué permiten los presupuestos participativos?",
        "¿Qué busca el consenso?",
    ],
    14: [  # Tema: Lunarpunk
        "¿Qué caracteriza la tecnología discreta?",
        "¿Qué prioriza el Lunarpunk?",
        "¿Qué papel tiene la naturaleza en lunarpunk?",
        "¿Qué reduce la contaminación lumínica?",
        "¿Cómo son los edificios lunarpunk?",
    ],
}
 


# =========================
# OPCIONES DE RESPUESTAS
# =========================
 
OPCIONES = {
    0: [  # Tema: Matriz energética sostenible
        ["A) Calor en vapor", "B) Luz en electricidad", "C) Viento en movimiento"],
        ["A) Supergrids", "B) Microgrids", "C) Nanoredes"],
        ["A) Gas natural", "B) Nuclear", "C) Eólica"],
        ["A) Paneles bifaciales", "B) Baterías de ion-litio", "C) Turbinas de vapor"],
        ["A) El viento", "B) El agua", "C) El calor residual"],
    ],
    1: [  # Tema: Movilidad urbana
        ["A) 10%", "B) 20%", "C) 40%"],
        ["A) 2 veces", "B) 5 veces", "C) 10 veces"],
        ["A) Construir autopistas", "B) Necesidades accesibles a pie/bici", "C) Reducir semáforos"],
        ["A) Aumentan congestión", "B) Sin impacto real", "C) Reducen emisiones"],
        ["A) Aumentan comercio local", "B) Reducen presión del suelo", "C) Facilitan carga"],
    ],
    2: [  # Tema: Terceros espacios
        ["A) Oficinas de trabajo", "B) Lugares fuera del hogar y trabajo", "C) Espacios virtuales"],
        ["A) Club privado", "B) Biblioteca comunitaria", "C) Restaurante"],
        ["A) Competencia", "B) Participación ciudadana", "C) Consumo local"],
        ["A) Alimentos con espacio social", "B) Arte urbano con deporte", "C) Reciclaje con solar"],
        ["A) Solo adultos", "B) Niñez, adultos mayores y personas con discapacidad", "C) Turistas"],
    ],
    3: [  # Tema: Agricultura sostenible
        ["A) Fábricas modernas", "B) Ecosistemas naturales", "C) Jardines ornamentales"],
        ["A) Tecnología con cultivos", "B) Árboles con cultivos", "C) Solo ganadería"],
        ["A) Producir comida", "B) Prevenir erosión", "C) Atraer plagas"],
        ["A) Usar químicos", "B) Devolver carbono al suelo", "C) Monocultivos"],
        ["A) Son más fáciles de vender", "B) Requieren más fertilizantes", "C) Resistentes al clima local"],
    ],
    4: [  # Tema: Economías alternativas
        ["A) Dar esperando retribución", "B) Dar sin esperar retribución", "C) Intercambio igual"],
        ["A) Empresas del Estado", "B) Multinacionales", "C) Empresas de trabajadores"],
        ["A) Vender herramientas", "B) Compartir objetos poco frecuentes", "C) Reparar electrónicos"],
        ["A) Reemplazar gobierno", "B) Satisfacer necesidades sin dinero", "C) Generar ganancias"],
        ["A) Productos de un solo uso", "B) Fábricas sin trabajadores", "C) Materiales reutilizables"],
    ],
    5: [  # Tema: Vivienda bioclimática
        ["A) Ignorándolo", "B) Para reducir consumo energético", "C) Aumentando gasto"],
        ["A) Entrada de luz", "B) Escape de calor", "C) Ventilación"],
        ["A) Es la más barata", "B) Almacena carbono", "C) No necesita mantenimiento"],
        ["A) Solo decoran", "B) Regulan temperatura y absorben agua", "C) Aumentan peso"],
        ["A) Máquinas costosas", "B) Orientación y ventilación", "C) Energía nuclear"],
    ],
    6: [  # Tema: Manejo del agua
        ["A) Solo nieve", "B) Agua de lluvia", "C) Agua salada"],
        ["A) Decorar", "B) Disponer agua en periodos secos", "C) Guardar comida"],
        ["A) Agua de lluvia", "B) Agua contaminada", "C) De duchas y lavamanos"],
        ["A) Arena y grava", "B) Químicos", "C) Metales"],
        ["A) Atraen mosquitos", "B) Tratan aguas residuales", "C) Producen sal"],
    ],
    7: [  # Tema: Biodiversidad
        ["A) Exóticas únicamente", "B) Especies nativas", "C) Lo mismo siempre"],
        ["A) Carreteras", "B) Hábitats", "C) Ciudades"],
        ["A) Kiwi", "B) Loro", "C) Gallina"],
        ["A) Protegen ecosistemas", "B) Afectan fauna local", "C) Nada"],
        ["A) Reducen peces", "B) Recuperan poblaciones", "C) Aumentan pesca"],
    ],
    8: [  # Tema: Tecnología apropiada
        ["A) Complejidad extrema", "B) Soluciones fáciles de reparar", "C) Obsolescencia"],
        ["A) Guardar secretos", "B) Que cualquiera lo estudie", "C) Control corporativo"],
        ["A) Empleo", "B) Dependencia externa", "C) Contaminación"],
        ["A) Soles artificiales", "B) Piezas de repuesto", "C) Nada"],
        ["A) Uso eficiente de recursos", "B) Consumismo", "C) Aislamiento"],
    ],
    9: [  # Tema: Gestión de residuos
        ["A) Tirar todo junto", "B) Clasificar residuos al generarlos", "C) No separar nada"],
        ["A) Petróleo", "B) Abono", "C) Plástico"],
        ["A) Tirar más rápido", "B) Mantener materiales en uso", "C) Contaminar"],
        ["A) Tirar inmediatamente", "B) Quemar", "C) Usar nuevamente un objeto"],
        ["A) Desechan objetos", "B) Extienden vida útil", "C) Aumentan basura"],
    ],
    10: [  # Tema: Educación comunitaria
        ["A) Aislamiento", "B) Competencia extrema", "C) Conocimiento compartido"],
        ["A) Solo libros", "B) Herramientas y semillas", "C) Dinero"],
        ["A) Teoría pura", "B) Habilidades prácticas", "C) Nada útil"],
        ["A) Solo para científicos", "B) Participación pública en proyectos", "C) Ficción"],
        ["A) Geometría", "B) Agricultura sostenible", "C) Matemáticas"],
    ],
    11: [  # Tema: Salud y bienestar
        ["A) Contaminación", "B) Salud física y mental", "C) Tráfico"],
        ["A) Comida ultraprocesada", "B) Alimentos frescos locales", "C) Ayunar"],
        ["A) Solo pierde tiempo", "B) Mejora la salud", "C) Causa estrés"],
        ["A) Esperar enfermedad", "B) Evitar enfermedades", "C) Ignorar síntomas"],
        ["A) Enfermedad", "B) Contaminación", "C) Calidad de vida"],
    ],
    12: [  # Tema: Resiliencia ante desastres
        ["A) Crear pánico", "B) Protocolo ante desastres", "C) Perder tiempo"],
        ["A) Solo guardar", "B) Ayuda ante interrupciones", "C) Nunca se usan"],
        ["A) Decoración", "B) Mantener servicios esenciales", "C) Nada importante"],
        ["A) Por diversión", "B) Aumentar seguridad hídrica", "C) Atraer plagas"],
        ["A) Crear pánico", "B) Avisar con anticipación", "C) Retrasar reacción"],
    ],
    13: [  # Tema: Gobernanza participativa
        ["A) Entretenimiento", "B) Reuniones de decisiones", "C) Obligatorias siempre"],
        ["A) Un solo decididor", "B) Participación ciudadana", "C) Caos total"],
        ["A) Esconder información", "B) Fortalece confianza", "C) Causa problemas"],
        ["A) Solo gastar", "B) Comunidad decide recursos", "C) Robar dinero"],
        ["A) Imponer opinión", "B) Acuerdos aceptables", "C) Conflicto eterno"],
    ],
    14: [  # Tema: Lunarpunk
        ["A) Muy visible", "B) Integrada al entorno", "C) Desconectada"],
        ["A) Lujo", "B) Eficiencia", "C) Tecnología visible"],
        ["A) Secundario", "B) Central", "C) Ninguno"],
        ["A) Más luces", "B) Iluminación eficiente", "C) Oscuridad total"],
        ["A) Muy modernos", "B) Integrados al paisaje", "C) Aislados"],
    ],
}
 

# =========================
# RESPUESTAS CORRECTAS
# =========================
 
RESPUESTAS = {
    0: ["B", "B", "C", "B", "C"],
    1: ["C", "C", "B", "C", "A"],
    2: ["B", "B", "B", "A", "B"],
    3: ["B", "B", "B", "B", "C"],
    4: ["B", "C", "B", "B", "C"],
    5: ["B", "B", "B", "B", "B"],
    6: ["B", "B", "C", "A", "B"],
    7: ["B", "B", "A", "B", "B"],
    8: ["B", "B", "B", "B", "A"],
    9: ["B", "B", "B", "C", "B"],
    10: ["C", "B", "B", "B", "B"],
    11: ["B", "B", "B", "B", "C"],
    12: ["B", "B", "B", "B", "B"],
    13: ["B", "B", "B", "B", "B"],
    14: ["B", "B", "B", "B", "B"],
}
 

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

titulos_capitulos = [
    "Que es el solarpunk",
    "Principios del solarpunk",
    "Solarpunk y el capitalismo",
    "Politica y organizacion solarpunk",
    "Cultura e imaginario solarpunk",
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
    print("Escoges las paginas que leeras tirando un dado de 4 caras (0, 1, 2 o 3).")
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
                mostrar_capsulas()
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
                mostrar_capsulas()

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


def mostrar_capsulas():
    """
    Tira el dado de 4 caras y muestra esa cantidad de cápsulas del capítulo actual.
    Las cápsulas se toman desde la página actual hacia adelante sin salirse del rango.
    """
    global indice_piso, indice_biblioteca

    tiro = dado()
    total_capsulas = len(CAPSULAS[indice_biblioteca])

    print("\n  [Capitulo " + str(indice_biblioteca + 1) + " - " +
          titulos_capitulos[indice_biblioteca] + "]")

    print("  Tiraste el dado y sacaste " + str(tiro) +
          ". Lees " + str(tiro) + " cápsula(s):\n")

    capsulas_mostradas = 0

    while capsulas_mostradas < tiro:
        idx = indice_piso + capsulas_mostradas

        if idx >= total_capsulas:
            idx = total_capsulas - 1

        print("  - Cápsula " + str(capsulas_mostradas + 1) +
              ": " + CAPSULAS[indice_biblioteca][idx])

        capsulas_mostradas += 1

    print("")


def cuestionario():
    """
    Hace hasta 5 preguntas del capítulo actual.
    - Si el jugador acumula 5 respuestas correctas: gana.
    - Si acumula 1 incorrectas: pierde.
    """
    global indice_biblioteca

    correctas = 0
    incorrectas = 0
    numero = 0

    print("\n=== CUESTIONARIO - Capitulo " +
          str(indice_biblioteca + 1) + " ===")
    print("7 preguntas. 4 correctas para avanzar, 4 incorrectas para retroceder.")
    print("Escribe 'capsula' en cualquier momento para recibir una ayuda.\n")

    while numero < 5:

        pregunta = PREGUNTAS[indice_biblioteca][numero]
        ayuda = cuestionarios[indice_biblioteca][numero][1]
        respuesta = RESPUESTAS[indice_biblioteca][numero]
        opciones0 = OPCIONES[indice_biblioteca][numero][0]
        opciones1 = OPCIONES[indice_biblioteca][numero][1]
        opciones2 = OPCIONES[indice_biblioteca][numero][2]

        print("Pregunta " + str(numero + 1) +
              "/5  |  Correctas: " + str(correctas) +
              "  Incorrectas: " + str(incorrectas))

        print(pregunta + "\n" + opciones0 + "\n" + opciones1 + "\n" + opciones2)

        while True:

            entrada = input("Tu respuesta: ").strip().lower()

            if entrada == "capsula":
                print("Cápsula de ayuda: " + ayuda + "\n")

            elif entrada == respuesta.lower():
                correctas += 1
                print("Correcto! (" + str(correctas) + " buenas)\n")
                break

            else:
                incorrectas += 1
                print("Incorrecto. Era: " + respuesta +
                      " (" + str(incorrectas) + " malas)\n")
                break

        if correctas >= 5:
            print("Superaste el cuestionario con " +
                  str(correctas) +
                  " correctas. Avanzas al siguiente capítulo.\n")
            return True

        if incorrectas >= 5:
            print("Demasiados errores (" +
                  str(incorrectas) +
                  " incorrectas). Vuelves a repasar.\n")
            return False

        numero += 1

    if correctas > incorrectas:
        print("Fin del cuestionario. " +
              str(correctas) +
              " correctas vs " +
              str(incorrectas) +
              " incorrectas. Avanzas!\n")
        return True

    print("Fin del cuestionario. " +
          str(correctas) +
          " correctas vs " +
          str(incorrectas) +
          " incorrectas. Vuelves a repasar.\n")

    return False

def dado():
    """Simula el lanzamiento de un dado de 4 caras. Devuelve un entero entre 1 y 4."""
    return random.randint(0, 3)

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