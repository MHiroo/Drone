# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 12:19:25 2023

@author: hiroo
"""
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


# Fonction pour définir la vitesse du moteur (avec calibration simulée)
def set_motor_speed(speed_percent):
    # Convertir le pourcentage en microsecondes (1000-2000 us)
    pwm_us = 1000 + (speed_percent * 10)  # Convertir en microsecondes
    # Normaliser en une plage de devoir cyclique (0.0-100.0)
    duty_cycle = (pwm_us - 1000) / 10.0
    pwm.ChangeDutyCycle(duty_cycle)
    time.sleep(3)  # Laisser le signal PWM actif pendant quelques secondes

# Calibration simulée
try:
    # Gaz minimum (1000 us) pour quelques secondes
    set_motor_speed(0)
    time.sleep(5)

    # Gaz maximum (2000 us) pour quelques secondes
    set_motor_speed(100)
    time.sleep(5)

    # Point neutre (1500 us)
    set_motor_speed(50)
    time.sleep(1)

except KeyboardInterrupt:
    pass
