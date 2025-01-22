import random
import string
import time
import sys
import curses

# Función para generar la contraseña aleatoria
def generar_contraseña(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(caracteres) for _ in range(longitud))

# Función para mostrar el radar y efectos visuales
def mostrar_efectos(window, longitud):
    window.clear()
    window.border(0)
    window.addstr(2, 2, "Generando contraseña...", curses.color_pair(1))
    window.addstr(4, 2, "🔴 [BUSCANDO CARACTERES...] 🔴", curses.color_pair(2))
    
    # Radar efecto
    for i in range(20):
        window.addstr(6, 2, f"🔘 {'.' * (i % 5 + 1)}", curses.color_pair(3))
        window.refresh()
        time.sleep(0.1)
    
    # Pantalla hackeada
    window.addstr(8, 2, "☠️ Escaneando patrones...", curses.color_pair(4))
    window.refresh()
    time.sleep(1)
    
    # Mostrar la contraseña
    contraseña = generar_contraseña(longitud)
    window.clear()
    window.border(0)
    window.addstr(2, 2, f"Contraseña generada: {contraseña}", curses.color_pair(5))
    window.addstr(4, 2, "Presione cualquier tecla para salir...", curses.color_pair(1))
    window.refresh()

    window.getch()

# Función principal
def main(stdscr):
    # Inicializar colores
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    curses.init_pair(5, curses.COLOR_YELLOW, curses.COLOR_BLACK)

    stdscr.clear()
    stdscr.refresh()

    # Solicitar longitud de la contraseña
    stdscr.addstr(2, 2, "Ingrese la longitud de la contraseña: ", curses.color_pair(1))
    stdscr.refresh()
    
    longitud = int(stdscr.getstr().decode())

    # Llamar a la función para mostrar los efectos
    mostrar_efectos(stdscr, longitud)

if __name__ == "__main__":
    curses.wrapper(main)
