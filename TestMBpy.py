pip install RPi.GPIO

import RPi.GPIO as GPIO
import time

# Configuration de la broche GPIO en numérotation BOARD
PWM_PIN_BOARD = 12  # Broche 12 en numérotation BOARD (GPIO 18 en numérotation BCM)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PWM_PIN_BOARD, GPIO.OUT)

# Configuration du signal PWM
pwm_frequency = 50  # Fréquence PWM en Hertz
pwm = GPIO.PWM(PWM_PIN_BOARD, pwm_frequency)
pwm.start(0)  # Démarrer avec un rapport cyclique de 0 (vitesse nulle)

# Fonction pour définir la vitesse du moteur
def set_motor_speed(speed_percent):
    duty_cycle = speed_percent * 10  # Convertir en devoir cyclique (0-100% -> 0-1000)
    pwm.ChangeDutyCycle(duty_cycle)

try:
    # Démarrer le moteur à 50% de vitesse
    set_motor_speed(50)

    # Laisser le moteur tourner pendant 10 secondes
    time.sleep(10)

    # Arrêter le moteur en mettant le rapport cyclique à 0
    set_motor_speed(0)

except KeyboardInterrupt:
    pass

# Arrêter le signal PWM et nettoyer les broches GPIO
pwm.stop()
GPIO.cleanup()
