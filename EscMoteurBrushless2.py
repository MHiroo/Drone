import time
import RPi.GPIO as GPIO

# Configuration des broches GPIO
pin_pwm = 7  # Remplacez par le numéro de votre broche PWM
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin_pwm, GPIO.OUT)

# Configuration de la fréquence PWM (50 Hz est typique pour les ESC)
pwm_frequency = 50

# Initialisation du PWM
pwm = GPIO.PWM(pin_pwm, pwm_frequency)

try:
    pwm.start(0)  # Démarrage avec un rapport cyclique de 0%

    print("Moteur à l'arrêt")
    input("Appuyez sur Entrée pour démarrer...")

    pwm.ChangeDutyCycle(5)  # Réglage du rapport cyclique à 5%
    print("Moteur en marche à 5% de sa vitesse maximale.")
    input("Appuyez sur Entrée pour arrêter le moteur...")

except KeyboardInterrupt:
    pass

finally:
    pwm.stop()
    GPIO.cleanup()
