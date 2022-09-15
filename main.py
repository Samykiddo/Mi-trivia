GREEN = '\033[32m'
RESET = '\033[39m'

score = 0
i_trivia = True
intentos = 0

print (GREEN+"Hola colega! yo se por qué estas aqui, tú tambien quieres poder participar en el sorteo de 2 entradas dobles al concierto de Travis Scott. Felicidades! estas en el lugar indicado, pero antes debes responderme algunas preguntas para saber si realmente mereces ganarte esos boletos."+RESET)
nombre = input("\nVaya, de tanta emocion olvide decirte mi nombre. Soy BotFrank y tú, como te llamas?: ")
print ("\nMuy bien " + nombre + ", quiero poner a prueba tus conocimientos sobre nuestro artista favorito, las preguntas son faciles para un verdadero fan, Suerte!\n")
#instrucciones de como jugar:
print ("*Responde las siguientes preguntas escribiendo la letra de la alternativa y presionando 'Enter' para enviar tu respuesta:\n Tienes", score, "puntos")

class Preguntas:
  def __init__(self, orden, respuesta):
          self.orden = orden
          self.respuesta = respuesta
preguntas_rptas = ["¿Cuál es el verdadero nombre de Travis Scott?\na) Carlton Douglas Ridenhour \nb) Jacques Berman Webster II \nc) Marshall Mathers III \nd) Chancelor Johnathan Bennett","¿Por quién se llamó a sí mismo Travis?\na) The Scottish band \nb) His uncle \nc) The baseball player Travis Hafner \nd) Travis Barker from blink-182","¿En qué universidad estudió antes de seguir una carrera musical?\na) University of Chicago \nb) Columbia University \nc) Stanford University \nd) University of Texas San Antonio","Lanzó su tercer álbum en 2018. ¿Cómo se llamaba?\na) Megaworld \nb) Starworld \nc) Astroworld \nd) Rapworld","¿En qué juego realizó Travis Scott conciertos virtuales en vivo en 2020?\na) Minecraft \nb) Fortnite Battle Royale \nc) Apex Legend \nd) Animal Crossing: New Horizons","¿Travis tiene una hija con qué celebridad?\na) Khloé Kardashian \nb) Kourtney Kardashian \nc) Kylie Jenner \nd) Kendall Jenner"]
preguntaz = [Preguntas(preguntas_rptas[0], "b"),Preguntas(preguntas_rptas[1], "b"),Preguntas(preguntas_rptas[2], "d"),Preguntas(preguntas_rptas[3], "c"),Preguntas(preguntas_rptas[4], "b"),Preguntas(preguntas_rptas[5], "c")]
def correr_trivia(preguntaz):
       score = 0
       for pregunta in preguntaz:
            respuesta = input(pregunta.orden)
            if respuesta == pregunta.respuesta:
                 score += 1
       print("conseguiste", score, "de", len(preguntaz))
while i_trivia == True:
  intentos += 1
  score = 0

  print("\nEste es tu intento:", intentos)
  input("Presiona Enter para continuar")

  print(correr_trivia(preguntaz))
  
  score = score +20 
  print("Excelente, has obtenido", score, "puntos")

  print("\n¿Deseas intentar la trivia nuevamente?")
  repetir_trivia = input("Ingresa 'si' para repetir, o cualquier tecla para finalizar: ").lower()
  if repetir_trivia != "si":  
   print("\nEspero ", nombre , "que lo hayas pasado bien, hasta pronto!")
   i_trivia = False  