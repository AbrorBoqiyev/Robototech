# Ovoz's Python code
# POTENSIOMETR ishlatish kodi

import Entry
import ArduinoExt


def when_start():
    while True:
        Entry.print(ArduinoExt.analogRead("A0"))
        if ((ArduinoExt.analogRead("A0") > 0) and (ArduinoExt.analogRead("A0") < 200)):
            Entry.change_shape("Ovoz_1")
        if ((ArduinoExt.analogRead("A0") > 201) and (ArduinoExt.analogRead("A0") < 400)):
            Entry.change_shape("Ovoz_2")
        if ((ArduinoExt.analogRead("A0") > 401) and (ArduinoExt.analogRead("A0") < 600)):
            Entry.change_shape("Ovoz_3")
        if ((ArduinoExt.analogRead("A0") > 601) and (ArduinoExt.analogRead("A0") < 800)):
            Entry.change_shape("Ovoz_4")
        if ((ArduinoExt.analogRead("A0") > 801) and (ArduinoExt.analogRead("A0") < 1001)):
            Entry.change_shape("Ovoz_4")

def when_start():
    while True:
        if ((ArduinoExt.analogRead("A0") > 0) and (ArduinoExt.analogRead("A0") < 200)):
            Entry.play_sound("Kuchukning hurish")
        if ((ArduinoExt.analogRead("A0") > 201) and (ArduinoExt.analogRead("A0") < 400)):
            Entry.play_sound("Elektron ovozi2")
        if ((ArduinoExt.analogRead("A0") > 401) and (ArduinoExt.analogRead("A0") < 600)):
            Entry.play_sound("Elektron ovozi3")
        if ((ArduinoExt.analogRead("A0") > 601) and (ArduinoExt.analogRead("A0") < 800)):
            Entry.play_sound("Robot2")
        if ((ArduinoExt.analogRead("A0") > 801) and (ArduinoExt.analogRead("A0") < 1001)):
            Entry.play_sound("nimw")
            
            
            
            
# Entrybot's Python code
# tugma yordamida led chiroqlarini yoqish

import Entry
import ArduinoExt


def when_start():
    while True:
        if ArduinoExt.digitalRead(2):
            ArduinoExt.digitalWrite(4, "HIGH")
            ArduinoExt.digitalWrite(3, "LOW")
        else:
            ArduinoExt.digitalWrite(4, "LOW")
            ArduinoExt.digitalWrite(3, "HIGH")

def when_start():
    while True:
        if ArduinoExt.digitalRead(2):
            Entry.play_sound("Qor usti qadam tashlash ovozi")
            while ArduinoExt.digitalRead(2):
                Entry.show()
            Entry.hide()
            
            
            
# Entrybot's Python code
# tugmalar yordamida pionino yasash

import Entry

def when_start():
    while True:
        if ArduinoExt.digitalRead(3):
            Entry.play_sound("Pianino_04 do")
            while ArduinoExt.digitalRead(3):
                Entry.show()
            Entry.hide()
        if ArduinoExt.digitalRead(4):
            Entry.play_sound("Pianino_05re")
            while ArduinoExt.digitalRead(4):
                Entry.show()
            Entry.hide()
        if ArduinoExt.digitalRead(5):
            Entry.play_sound("Pianino_16mi")
            while ArduinoExt.digitalRead(5):
                Entry.show()
            Entry.hide()
        if ArduinoExt.digitalRead(6):
            Entry.play_sound("Pianino_08fa")
            while ArduinoExt.digitalRead(6):
                Entry.show()
            Entry.hide()
        if ArduinoExt.digitalRead(12):
            Entry.play_sound("Pianino_08sol")
            while ArduinoExt.digitalRead(12):
                Entry.show()
            Entry.hide()
            
            
            
# mator Yurayotgan ko'rinish's Python code

import Entry
import ArduinoExt


def when_press_key("A"):
    while True:
        ArduinoExt.analogWrite(5, 255)
        ArduinoExt.analogWrite(3, 0)

def when_press_key("S"):
    while True:
        ArduinoExt.analogWrite(5, 0)
        ArduinoExt.analogWrite(3, 0)

def when_press_key("D"):
    while True:
        ArduinoExt.analogWrite(5, 0)
        ArduinoExt.analogWrite(3, 255)