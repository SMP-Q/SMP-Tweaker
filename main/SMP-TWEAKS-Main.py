


kkjkjk
import math 
import sys
import os
import time
import subprocess
import ctypes
import platform
import random

try:
    import colorama
    from colorama import Fore, Style
except ImportError:
    import subprocess
    import sys
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'colorama'])
    import colorama
    from colorama import Fore, Style
colorama.init(autoreset=True)
import itertools
import threading

try:
    import psutil
except ImportError:
    import subprocess
    import sys
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'psutil'])
    import psutil

VALID_KEYS = [
    "admin",
]

ASCII_TITLE = r'''
  ____  __  __ ____    _______        _______    _    _  ______  
 / ___||  \/  |  _ \  |_   _\ \      / / ____|  / \  | |/ / ___| 
 \___ \| |\/| | |_) |   | |  \ \ /\ / /|  _|   / _ \ | ' /\___ \ 
  ___) | |  | |  __/    | |   \ V  V / | |___ / ___ \| . \ ___) |
 |____/|_|  |_|_|       |_|    \_/\_/  |_____/_/   \_\_|\_\____/ 
                                                                 
'''

CATEGORIES = [
    {"name": "Windows Tweaks", "func": "windows_tweaks_menu"},
    {"name": "test", "func": "test_menu"},
    {"name": "Remove Bloatware", "func": "bloatware_menu"},
    {"name": "Disable Services", "func": "services_menu"},
    {"name": "System Restore", "func": "restore_point_menu"},
    {"name": "Exit", "func": "exit_program"},
]

# Hilfsfunktionen für Farben

def print_colored(text, color=Fore.WHITE, end='\n'):
    print(color + text + Style.RESET_ALL, end=end)

def typing_effect(text, color=Fore.WHITE, delay=0.01):
    for char in text:
        print(color + char + Style.RESET_ALL, end='', flush=True)
        time.sleep(delay)
    print()

def loading_animation(text="Loading", duration=2, color=Fore.CYAN):
    spinner = itertools.cycle(['|', '/', '-', '\\'])
    end_time = time.time() + duration
    while time.time() < end_time:
        print(f"{color}{text} {next(spinner)}{Style.RESET_ALL}", end='\r', flush=True)
        time.sleep(0.1)
    print(' ' * (len(text) + 4), end='\r')

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def check_key():
    for _ in range(3):
        key = input("Please enter license key: ").strip()
        if key in VALID_KEYS:
            print("\n[+] License key accepted!\n")
            return True
        else:
            print("[ERROR] Invalid license key!\n")
    print("[ABORTED] Too many failed attempts.")
    return False

def main_menu():
    while True:
        print_title()
        print_colored("Main Menu:", Fore.CYAN)
        for idx, cat in enumerate(CATEGORIES, 1):
            print_colored(f"  [{idx}] {cat['name']}", Fore.YELLOW)
        try:
            choice = int(input("\nPlease select a category: "))
            animated_menu_switch()
            if 1 <= choice <= len(CATEGORIES):
                func = globals()[CATEGORIES[choice-1]["func"]]
                loading_animation("Loading menu", 1, color=Fore.CYAN)
                func()
            else:
                animated_warning("Invalid selection!")
                time.sleep(1)
        except (ValueError, KeyError):
            animated_warning("Invalid input!")
            time.sleep(1)

def windows_tweaks_menu():
    tweaks = [
        ("Enable Dark Mode", lambda: print("[+] Dark Mode aktiviert!")),
        ("Hide Taskbar Search", lambda: print("[+] Taskleiste Suche versteckt!")),
        ("Platzhalter 1", lambda: print("[+] Windows Tweaks Funktion 1 ausgeführt!")),
        ("Platzhalter 2", lambda: print("[+] Windows Tweaks Funktion 2 ausgeführt!")),
        ("Back to Main Menu", None)
    ]
    while True:
        clear()
        print_title(show_disclaimer=False)
        print_colored("Windows Tweaks:", Fore.CYAN)
        for idx, (name, _) in enumerate(tweaks, 1):
            print_colored(f"  [{idx}] {name}", Fore.YELLOW)
        try:
            choice = int(input("\nPlease select an option: "))
            if 1 <= choice < len(tweaks):
                tweaks[choice-1][1]()
                input("\nContinue with Enter...")
            elif choice == len(tweaks):
                return
            else:
                print_colored("Invalid selection!", Fore.RED)
                time.sleep(1)
        except ValueError:
            print_colored("Invalid input!", Fore.RED)
            time.sleep(1)

def test_menu():
    tweaks = [
        ("Platzhalter Test 1", lambda: print("[+] Test Funktion 1 ausgeführt!")),
        ("Platzhalter Test 2", lambda: print("[+] Test Funktion 2 ausgeführt!")),
        ("Back to Main Menu", None)
    ]
    while True:
        clear()
        print_title()
        print_colored("Test Menü:", Fore.CYAN)
        for idx, (name, _) in enumerate(tweaks, 1):
            print_colored(f"  [{idx}] {name}", Fore.YELLOW)
        try:
            choice = int(input("\nBitte wähle eine Option: "))
            if 1 <= choice < len(tweaks):
                tweaks[choice-1][1]()
                input("\nWeiter mit Enter...")
            elif choice == len(tweaks):
                return
            else:
                print_colored("Ungültige Auswahl!", Fore.RED)
                time.sleep(1)
        except ValueError:
            print_colored("Ungültige Eingabe!", Fore.RED)
            time.sleep(1)



    while True:
        clear()
        print_title()
        typing_effect("Remove Bloatware:", color=Fore.CYAN, delay=0.01)
        for idx, (name, _) in enumerate(apps, 1):
            typing_effect(f"  [{idx}] {name}", color=Fore.YELLOW, delay=0.002)
        try:
            choice = int(input("\nPlease select an option: "))
            if 1 <= choice < len(apps):
                animated_menu_switch()
                apps[choice-1][1]()
                input("\nWeiter mit Enter...")
            elif choice == len(apps):
                return
            else:
                animated_warning("Invalid selection!")
                time.sleep(1)
        except ValueError:
            animated_warning("Invalid input!")
            time.sleep(1)

def services_menu():
    services = [
        ("Disable DiagTrack", lambda: print("[+] DiagTrack deaktiviert!")),
        ("Disable Superfetch", lambda: print("[+] Superfetch deaktiviert!")),
        ("Platzhalter Service 1", lambda: print("[+] Service Funktion 1 ausgeführt!")),
        ("Platzhalter Service 2", lambda: print("[+] Service Funktion 2 ausgeführt!")),
        ("Back to Main Menu", None)
    ]
    while True:
        clear()
        print_title(show_disclaimer=False)
        print_colored("Disable Services:", Fore.CYAN)
        for idx, (name, _) in enumerate(services, 1):
            print_colored(f"  [{idx}] {name}", Fore.YELLOW)
        try:
            choice = int(input("\nPlease select an option: "))
            if 1 <= choice < len(services):
                services[choice-1][1]()
                input("\nContinue with Enter...")
            elif choice == len(services):
                return
            else:
                print_colored("Invalid selection!", Fore.RED)
                time.sleep(1)
        except ValueError:
            print_colored("Invalid input!", Fore.RED)
            time.sleep(1)

def restore_point_menu():
    print_colored("\nSystem Restore:", Fore.CYAN)
    while True:
        answer = input("Möchten Sie einen Wiederherstellungspunkt erstellen? (J/N): ").strip().lower()
        if answer in ("j", "y"):
            print_colored("Das Systemwiederherstellungsfenster wird jetzt geöffnet. Bitte folge den Anweisungen im Fenster.", Fore.YELLOW)
            loading_animation("Starte Systemwiederherstellung", 2, color=Fore.CYAN)
            input("Weiter mit Enter...")
            try:
                subprocess.run(["rstrui.exe"], check=True)
                animated_success("Systemwiederherstellung erfolgreich gestartet!")
            except Exception as e:
                animated_warning(f"[ERROR] Konnte die Systemwiederherstellung nicht starten: {e}")
            input("Weiter mit Enter...")
            break
        elif answer in ("n", "nein"):
            animated_success("Wiederherstellungspunkt wurde übersprungen.")
            time.sleep(1)
            break
        else:
            animated_warning("Ungültige Eingabe! Bitte J für Ja oder N für Nein eingeben.")

def exit_program():
    print_colored("\nGoodbye!", Fore.MAGENTA)
    loading_animation("Exiting", 1)
    sys.exit(0)

def ensure_admin():
    try:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin()
    except:
        is_admin = False
    if not is_admin:
        print("[INFO] Starte das Programm mit Administratorrechten neu...")
        # Starte das Skript mit erhöhten Rechten neu
        params = ' '.join([f'"{arg}"' for arg in sys.argv])
        try:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, params, None, 1)
        except Exception as e:
            print(f"[FEHLER] Konnte das Programm nicht als Administrator starten: {e}")
        sys.exit(0)

def get_system_info():
    info = {}
    # RAM
    try:
        ram = psutil.virtual_memory().total / (1024 ** 3)
        info['RAM'] = f"{ram:.1f} GB"
    except:
        info['RAM'] = "Unknown"
    # CPU
    try:
        cpu = subprocess.check_output(
            'powershell -Command "Get-CimInstance Win32_Processor | Select-Object -ExpandProperty Name"',
            shell=True, encoding='utf-8', errors='replace')
        cpu = cpu.strip()
        info['CPU'] = cpu if cpu else "Unknown"
    except:
        info['CPU'] = "Unknown"
    # GPU
    try:
        gpu = subprocess.check_output(
            'powershell -Command "Get-CimInstance Win32_VideoController | Select-Object -ExpandProperty Name"',
            shell=True, encoding='utf-8', errors='replace')
        lines = [l.strip() for l in gpu.split('\n') if l.strip()]
        if lines and any(len(l) > 2 for l in lines):
            info['GPU'] = ', '.join(lines)
        else:
            info['GPU'] = "Unknown"
    except:
        info['GPU'] = "Unknown"
    # Windows Version (e.g. 22H2)
    try:
        version = subprocess.check_output(
            'powershell -Command "(Get-ItemProperty \'HKLM:\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\').DisplayVersion"',
            shell=True, encoding='utf-8', errors='replace')
        version = version.strip()
        if version:
            info['Windows Version'] = version
        else:
            info['Windows Version'] = platform.platform()
    except:
        info['Windows Version'] = platform.platform()
    return info

def show_system_info():
    print_colored("\nSystem Information:", Fore.CYAN)
    info = get_system_info()
    for k, v in info.items():
        print_colored(f"{k}: {v}", Fore.YELLOW)
    print()

def manual_tweak_menu():
    menu_items = [
        ("1", "General Optimizations"),
        ("2", "M&K Optimization"),
        ("3", "Windows Tweaks"),
        ("4", "PC clean"),
        ("5", "Memory/RAM Optimization"),
        ("6", "Disable Startup Services"),
        ("7", "GPU Tweaks"),
        ("8", "CPU Tweaks"),
        ("9", "USB Tweaks"),
        ("10", "Power Tweaks"),
        ("11", "System Debloat"),
        ("12", "Storage Tweaks"),
        ("13", "Fix Corrupted Files"),
        ("14", "Set Full Screen Optimization"),
        ("15", "Uninstall Useless Apps"),
        ("16", "SMP Network Tweaking Utility"),
        ("P", "Use Restore Point"),
        ("X", "Exit"),
        ("E", "SMP Tweaks Discord"),
    ]
    columns = [
        menu_items[0:8],   # 1-8
        menu_items[8:16],  # 9-16
    ]
    special_row = [menu_items[16], menu_items[17], menu_items[18]]  # P, X, E

    # Mapping von Auswahl zu Untermenü-Funktionen
    submenu_functions = {
        "1": general_optimizations_menu,
        "2": mk_optimization_menu,
        "3": windows_tweaks_submenu,
        "4": pc_clean_menu,
        "5": memory_optimization_menu,
        "6": disable_startup_services_menu,
        "7": gpu_tweaks_menu,
        "8": cpu_tweaks_menu,
        "9": usb_tweaks_menu,
        "10": power_tweaks_menu,
        "11": system_debloat_menu,
        "12": storage_tweaks_menu,
        "13": fix_corrupted_files_menu,
        "14": fullscreen_optimization_menu,
        "15": uninstall_useless_apps_menu,
        "16": network_tweaking_menu,
    }

    while True:
        print_title()
        print_colored("\n" + ("-" * 70), Fore.CYAN)
        for i in range(8):
            left = columns[0][i]
            right = columns[1][i]
            print_colored(f"[{left[0]}] {left[1]:25}", Fore.CYAN, end=" ")
            print_colored(f"[{right[0]}] {right[1]}", Fore.CYAN)
        print_colored("\n" + ("-" * 70), Fore.CYAN)
        print_colored(f"[P] {special_row[0][1]:26} [X] {special_row[1][1]:26} [E] {special_row[2][1]}", Fore.CYAN)
        print_colored("\nMade and distributed by SMP TWEAKS, for Support or Questions add smp2908 on Discord!\n", Fore.CYAN)
        choice = input("Select an option (number or letter): ").strip().upper()
        if choice in submenu_functions:
            submenu_functions[choice]()
        elif choice == "P":
            restore_point_menu()
        elif choice == "X":
            exit_program()
        elif choice == "E":
            print_colored("Discord: smp2908", Fore.CYAN)
            input("Weiter mit Enter...")
        else:
            print_colored("Invalid selection!", Fore.RED)
            time.sleep(1)

# Untermenüs für jede Kategorie (jeweils mit Platzhalter-Optionen)
def general_optimizations_menu():
    options = [
        ("[-] Schnellstart aktivieren", lambda: print("[-] Schnellstart aktiviert!")),
        ("[-] Hintergrund-Apps deaktivieren", lambda: print("[-] Hintergrund-Apps deaktiviert!")),
        ("[-] Prefetch & Superfetch deaktivieren", lambda: print("[-] Prefetch & Superfetch deaktiviert!")),
        ("[-] Windows-Animationen deaktivieren", lambda: print("[-] Windows-Animationen deaktiviert!")),
        ("[-] Energieplan auf Höchstleistung setzen", lambda: print("[-] Energieplan auf Höchstleistung!")),
        ("[-] Windows-Updates pausieren", lambda: print("[-] Windows-Updates pausiert!")),
        ("[-] Telemetrie deaktivieren", lambda: print("[-] Telemetrie deaktiviert!")),
        ("[-] Cortana deaktivieren", lambda: print("[-] Cortana deaktiviert!")),
        ("[-] Hintergrunddienste optimieren", lambda: print("[-] Hintergrunddienste optimiert!")),
        ("Zurück", None)
    ]
    show_submenu("General Optimizations", options)

def mk_optimization_menu():
    options = [
        ("[-] Mausbeschleunigung deaktivieren", lambda: print("[-] Mausbeschleunigung deaktiviert!")),
        ("[-] Polling Rate erhöhen", lambda: print("[-] Polling Rate erhöht!")),
        ("[-] Raw Input aktivieren", lambda: print("[-] Raw Input aktiviert!")),
        ("[-] Tastatur-Repeat-Rate erhöhen", lambda: print("[-] Tastatur-Repeat-Rate erhöht!")),
        ("[-] Double-Click Speed optimieren", lambda: print("[-] Double-Click Speed optimiert!")),
        ("[-] DPI Awareness setzen", lambda: print("[-] DPI Awareness gesetzt!")),
        ("Zurück", None)
    ]
    show_submenu("M&K Optimization", options)

def windows_tweaks_submenu():
    options = [
        ("[-] Dark Mode aktivieren", lambda: print("[-] Dark Mode aktiviert!")),
        ("[-] Taskleiste anpassen", lambda: print("[-] Taskleiste angepasst!")),
        ("[-] Explorer-Start auf Dieser PC setzen", lambda: print("[-] Explorer-Start geändert!")),
        ("[-] Kontextmenü beschleunigen", lambda: print("[-] Kontextmenü beschleunigt!")),
        ("[-] Transparenzeffekte deaktivieren", lambda: print("[-] Transparenzeffekte deaktiviert!")),
        ("[-] Benachrichtigungen deaktivieren", lambda: print("[-] Benachrichtigungen deaktiviert!")),
        ("[-] Registry Tweaks anwenden", lambda: print("[-] Registry Tweaks angewendet!")),
        ("Zurück", None)
    ]
    show_submenu("Windows Tweaks", options)

def pc_clean_menu():
    options = [
        ("[-] Temporäre Dateien löschen", lambda: print("[-] Temporäre Dateien gelöscht!")),
        ("[-] Papierkorb leeren", lambda: print("[-] Papierkorb geleert!")),
        ("[-] Systemdateien bereinigen", lambda: print("[-] Systemdateien bereinigt!")),
        ("[-] Browser-Cache löschen", lambda: print("[-] Browser-Cache gelöscht!")),
        ("[-] Prefetch-Ordner leeren", lambda: print("[-] Prefetch-Ordner geleert!")),
        ("[-] Speicheroptimierung starten", lambda: print("[-] Speicheroptimierung gestartet!")),
        ("Zurück", None)
    ]
    show_submenu("PC clean", options)

def memory_optimization_menu():
    ram_options = [
        ("1", "8 GB"),
        ("2", "16 GB"),
        ("3", "32 GB"),
        ("4", "64 GB"),
        ("5", "128 GB"),
        ("6", "Zurück")
    ]
    while True:
        clear()
        print_title()
        print_colored("Memory/RAM Optimization:", Fore.CYAN)
        print_colored("Bitte wähle deinen RAM aus:", Fore.YELLOW)
        for idx, (_, name) in enumerate(ram_options, 1):
            print_colored(f"  [{idx}] {name}", Fore.YELLOW)
        try:
            choice = int(input("\nDeine Auswahl: "))
            if 1 <= choice <= 5:
                ram_size = ram_options[choice-1][1]
                show_ram_tweaks(ram_size)
                return
            elif choice == 6:
                return
            else:
                print_colored("Ungültige Auswahl!", Fore.RED)
                time.sleep(1)
        except ValueError:
            print_colored("Ungültige Eingabe!", Fore.RED)
            time.sleep(1)

def show_ram_tweaks(ram_size):
    tweaks_by_ram = {
        "8 GB": [
            ("[-] Auslagerungsdatei auf 4-8 GB setzen", lambda: print("[-] Auslagerungsdatei auf 4-8 GB gesetzt!")),
            ("[-] Superfetch deaktivieren", lambda: print("[-] Superfetch deaktiviert!")),
            ("[-] Hintergrund-Apps minimieren", lambda: print("[-] Hintergrund-Apps minimiert!")),
            ("[-] RAM-Optimierungsdienst starten", lambda: print("[-] RAM-Optimierungsdienst gestartet!")),
            ("Zurück", None)
        ],
        "16 GB": [
            ("[-] Auslagerungsdatei auf 2-4 GB setzen", lambda: print("[-] Auslagerungsdatei auf 2-4 GB gesetzt!")),
            ("[-] Memory Compression deaktivieren", lambda: print("[-] Memory Compression deaktiviert!")),
            ("[-] Standby Memory leeren", lambda: print("[-] Standby Memory geleert!")),
            ("[-] RAM-Optimierungsdienst starten", lambda: print("[-] RAM-Optimierungsdienst gestartet!")),
            ("Zurück", None)
        ],
        "32 GB": [
            ("[-] Auslagerungsdatei deaktivieren", lambda: print("[-] Auslagerungsdatei deaktiviert!")),
            ("[-] Memory Compression deaktivieren", lambda: print("[-] Memory Compression deaktiviert!")),
            ("[-] Standby Memory leeren", lambda: print("[-] Standby Memory geleert!")),
            ("[-] RAM-Optimierungsdienst starten", lambda: print("[-] RAM-Optimierungsdienst gestartet!")),
            ("Zurück", None)
        ],
        "64 GB": [
            ("[-] Auslagerungsdatei deaktivieren", lambda: print("[-] Auslagerungsdatei deaktiviert!")),
            ("[-] Memory Compression deaktivieren", lambda: print("[-] Memory Compression deaktiviert!")),
            ("[-] Standby Memory leeren", lambda: print("[-] Standby Memory geleert!")),
            ("[-] RAM-Optimierungsdienst starten", lambda: print("[-] RAM-Optimierungsdienst gestartet!")),
            ("Zurück", None)
        ],
        "128 GB": [
            ("[-] Auslagerungsdatei deaktivieren", lambda: print("[-] Auslagerungsdatei deaktiviert!")),
            ("[-] Memory Compression deaktivieren", lambda: print("[-] Memory Compression deaktiviert!")),
            ("[-] Standby Memory leeren", lambda: print("[-] Standby Memory geleert!")),
            ("[-] RAM-Optimierungsdienst starten", lambda: print("[-] RAM-Optimierungsdienst gestartet!")),
            ("Zurück", None)
        ],
    }
    while True:
        clear()
        print_title(show_disclaimer=False)
        print_colored(f"RAM-Größe: {ram_size}", Fore.CYAN)
        print_colored("Empfohlene RAM-Tweaks:", Fore.YELLOW)
        tweaks = tweaks_by_ram.get(ram_size, [])
        for idx, (name, _) in enumerate(tweaks, 1):
            print_colored(f"  [{idx}] {name}", Fore.YELLOW)
        try:
            choice = int(input("\nBitte wähle eine Option: "))
            if 1 <= choice < len(tweaks):
                tweaks[choice-1][1]()
                input("\nWeiter mit Enter...")
            elif choice == len(tweaks):
                return
            else:
                print_colored("Ungültige Auswahl!", Fore.RED)
                time.sleep(1)
        except ValueError:
            print_colored("Ungültige Eingabe!", Fore.RED)
            time.sleep(1)

def disable_startup_services_menu():
    options = [
        ("[-] Autostart für OneDrive deaktivieren", lambda: print("[-] OneDrive Autostart deaktiviert!")),
        ("[-] Autostart für Cortana deaktivieren", lambda: print("[-] Cortana Autostart deaktiviert!")),
        ("[-] Autostart für Xbox deaktivieren", lambda: print("[-] Xbox Autostart deaktiviert!")),
        ("[-] Nicht benötigte Dienste deaktivieren", lambda: print("[-] Nicht benötigte Dienste deaktiviert!")),
        ("[-] Taskplaner-Aufgaben deaktivieren", lambda: print("[-] Taskplaner-Aufgaben deaktiviert!")),
        ("Zurück", None)
    ]
    show_submenu("Disable Startup Services", options)

def gpu_tweaks_menu():
    gpu_options = [
        ("1", "NVIDIA"),
        ("2", "RADEON"),
        ("3", "INTEL"),
        ("4", "Zurück")
    ]
    while True:
        clear()
        print_title()
        print_colored("GPU Tweaks:", Fore.CYAN)
        print_colored("Bitte wähle deinen GPU-Typ aus:", Fore.YELLOW)
        for idx, (_, name) in enumerate(gpu_options, 1):
            print_colored(f"  [{idx}] {name}", Fore.YELLOW)
        try:
            choice = int(input("\nDeine Auswahl: "))
            if 1 <= choice <= 3:
                gpu_type = gpu_options[choice-1][1]
                show_gpu_tweaks(gpu_type)
                return
            elif choice == 4:
                return
            else:
                print_colored("Ungültige Auswahl!", Fore.RED)
                time.sleep(1)
        except ValueError:
            print_colored("Ungültige Eingabe!", Fore.RED)
            time.sleep(1)

def show_gpu_tweaks(gpu_type):
    tweaks_by_gpu = {
        "NVIDIA": [
            ("[-] NVIDIA Treiber aktualisieren", lambda: print("[-] NVIDIA Treiber aktualisiert!")),
            ("[-] G-Sync aktivieren", lambda: print("[-] G-Sync aktiviert!")),
            ("[-] Low Latency Mode aktivieren", lambda: print("[-] Low Latency Mode aktiviert!")),
            ("[-] Shader Cache leeren", lambda: print("[-] Shader Cache geleert!")),
            ("[-] Power Management auf Maximum setzen", lambda: print("[-] Power Management auf Maximum!")),
            ("[-] Image Scaling aktivieren", lambda: print("[-] Image Scaling aktiviert!")),
            ("Zurück", None)
        ],
        "RADEON": [
            ("[-] Radeon Treiber aktualisieren", lambda: print("[-] Radeon Treiber aktualisiert!")),
            ("[-] Radeon Anti-Lag aktivieren", lambda: print("[-] Radeon Anti-Lag aktiviert!")),
            ("[-] Radeon Boost aktivieren", lambda: print("[-] Radeon Boost aktiviert!")),
            ("[-] Shader Cache leeren", lambda: print("[-] Shader Cache geleert!")),
            ("[-] Chill deaktivieren", lambda: print("[-] Radeon Chill deaktiviert!")),
            ("[-] Power Management auf Maximum setzen", lambda: print("[-] Power Management auf Maximum!")),
            ("Zurück", None)
        ],
        "INTEL": [
            ("[-] Intel Treiber aktualisieren", lambda: print("[-] Intel Treiber aktualisiert!")),
            ("[-] Adaptive Helligkeit deaktivieren", lambda: print("[-] Adaptive Helligkeit deaktiviert!")),
            ("[-] Panel Self Refresh deaktivieren", lambda: print("[-] Panel Self Refresh deaktiviert!")),
            ("[-] Power Management auf Maximum setzen", lambda: print("[-] Power Management auf Maximum!")),
            ("[-] V-Sync deaktivieren", lambda: print("[-] V-Sync deaktiviert!")),
            ("Zurück", None)
        ],
    }
    while True:
        clear()
        print_title(show_disclaimer=False)
        print_colored(f"GPU-Typ: {gpu_type}", Fore.CYAN)
        print_colored("Empfohlene GPU-Tweaks:", Fore.YELLOW)
        tweaks = tweaks_by_gpu.get(gpu_type, [])
        for idx, (name, _) in enumerate(tweaks, 1):
            print_colored(f"  [{idx}] {name}", Fore.YELLOW)
        try:
            choice = int(input("\nBitte wähle eine Option: "))
            if 1 <= choice < len(tweaks):
                tweaks[choice-1][1]()
                input("\nWeiter mit Enter...")
            elif choice == len(tweaks):
                return
            else:
                print_colored("Ungültige Auswahl!", Fore.RED)
                time.sleep(1)
        except ValueError:
            print_colored("Ungültige Eingabe!", Fore.RED)
            time.sleep(1)

def cpu_tweaks_menu():
    cpu_options = [
        ("1", "AMD"),
        ("2", "INTEL"),
        ("3", "Back")
    ]
    while True:
        clear()
        print_title()
        print_colored("CPU Tweaks:", Fore.CYAN)
        print_colored("Please select your CPU type:", Fore.YELLOW)
        for idx, (_, name) in enumerate(cpu_options, 1):
            print_colored(f"  [{idx}] {name}", Fore.YELLOW)
        try:
            choice = int(input("\nYour choice: "))
            if 1 <= choice <= 2:
                cpu_type = cpu_options[choice-1][1]
                show_cpu_tweaks(cpu_type)
                return
            elif choice == 3:
                return
            else:
                print_colored("Invalid selection!", Fore.RED)
                time.sleep(1)
        except ValueError:
            print_colored("Invalid input!", Fore.RED)
            time.sleep(1)

def show_cpu_tweaks(cpu_type):
    def with_warning(func, note):
        def wrapper():
            print_colored(note, Fore.YELLOW)
            proceed = input("Do you want to continue? (y/n): ").strip().lower()
            if proceed != 'y':
                print_colored("Action cancelled.", Fore.CYAN)
                return
            func()
        return wrapper
    tweaks_by_cpu = {
        "AMD": [
            ("[-] Set power plan to High Performance", with_warning(lambda: print("[-] Power plan set to High Performance!"), "Note: This tweak may cause your PC to run warmer or use more power.")),
            ("[-] Adjust CPU priority", lambda: print("[-] CPU priority adjusted!")),
            ("[-] Enable CPPC (Ryzen)", lambda: print("[-] CPPC enabled!")),
            ("[-] Control SMT", with_warning(lambda: print("[-] SMT controlled!"), "Note: This tweak may affect system stability in rare cases.")),
            ("[-] Optimize timer resolution", lambda: print("[-] Timer resolution optimized!")),
            ("[-] Disable CPU Parking", with_warning(lambda: print("[-] CPU Parking disabled!"), "Note: This tweak may cause your PC to run warmer or use more power.")),
            ("[-] Enable Hidden Cores", with_warning(lambda: print("[-] Hidden Cores enabled!"), "Note: This tweak may affect system stability in rare cases.")),
            ("Back", None)
        ],
        "INTEL": [
            ("[-] Set power plan to High Performance", with_warning(lambda: print("[-] Power plan set to High Performance!"), "Note: This tweak may cause your PC to run warmer or use more power.")),
            ("[-] Adjust CPU priority", lambda: print("[-] CPU priority adjusted!")),
            ("[-] Control Hyperthreading", with_warning(lambda: print("[-] Hyperthreading controlled!"), "Note: This tweak may affect system stability in rare cases.")),
            ("[-] Enable/Disable Turbo Boost", with_warning(lambda: print("[-] Turbo Boost changed!"), "Note: This tweak may cause your PC to run warmer or use more power.")),
            ("[-] Optimize timer resolution", lambda: print("[-] Timer resolution optimized!")),
            ("[-] Disable CPU Parking", with_warning(lambda: print("[-] CPU Parking disabled!"), "Note: This tweak may cause your PC to run warmer or use more power.")),
            ("[-] Enable Hidden Cores", with_warning(lambda: print("[-] Hidden Cores enabled!"), "Note: This tweak may affect system stability in rare cases.")),
            ("Back", None)
        ],
    }
    while True:
        clear()
        print_title(show_disclaimer=False)
        print_colored(f"CPU type: {cpu_type}", Fore.CYAN)
        print_colored("Recommended CPU tweaks:", Fore.YELLOW)
        tweaks = tweaks_by_cpu.get(cpu_type, [])
        for idx, (name, _) in enumerate(tweaks, 1):
            print_colored(f"  [{idx}] {name}", Fore.YELLOW)
        try:
            choice = int(input("\nPlease select an option: "))
            if 1 <= choice < len(tweaks):
                tweaks[choice-1][1]()
                input("\nPress Enter to continue...")
            elif choice == len(tweaks):
                return
            else:
                print_colored("Invalid selection!", Fore.RED)
                time.sleep(1)
        except ValueError:
            print_colored("Invalid input!", Fore.RED)
            time.sleep(1)

def usb_tweaks_menu():
    options = [
        ("[-] USB-Energiesparmodus deaktivieren", lambda: print("[-] USB-Energiesparmodus deaktiviert!")),
        ("[-] USB-Selective Suspend deaktivieren", lambda: print("[-] USB-Selective Suspend deaktiviert!")),
        ("[-] USB-Ports zurücksetzen", lambda: print("[-] USB-Ports zurückgesetzt!")),
        ("[-] USB-Root Hub optimieren", lambda: print("[-] USB-Root Hub optimiert!")),
        ("Zurück", None)
    ]
    show_submenu("USB Tweaks", options)

def power_tweaks_menu():
    options = [
        ("[-] Schnellstart deaktivieren", lambda: print("[-] Schnellstart deaktiviert!")),
        ("[-] Energiesparoptionen optimieren", lambda: print("[-] Energiesparoptionen optimiert!")),
        ("[-] Adaptive Helligkeit deaktivieren", lambda: print("[-] Adaptive Helligkeit deaktiviert!")),
        ("[-] USB Selective Suspend deaktivieren", lambda: print("[-] USB Selective Suspend deaktiviert!")),
        ("[-] PCI Express Energiesparmodus deaktivieren", lambda: print("[-] PCI Express Energiesparmodus deaktiviert!")),
        ("Zurück", None)
    ]
    show_submenu("Power Tweaks", options)

def system_debloat_menu():
    options = [
        ("[-] Xbox entfernen", lambda: print("[-] Xbox entfernt!")),
        ("[-] OneDrive entfernen", lambda: print("[-] OneDrive entfernt!")),
        ("[-] Cortana entfernen", lambda: print("[-] Cortana entfernt!")),
        ("[-] 3D Viewer entfernen", lambda: print("[-] 3D Viewer entfernt!")),
        ("[-] Paint 3D entfernen", lambda: print("[-] Paint 3D entfernt!")),
        ("[-] Bloatware-Apps entfernen", lambda: print("[-] Bloatware-Apps entfernt!")),
        ("Zurück", None)
    ]
    show_submenu("System Debloat", options)

def storage_tweaks_menu():
    options = [
        ("[-] Laufwerk defragmentieren", lambda: print("[-] Laufwerk defragmentiert!")),
        ("[-] Speicheroptimierung aktivieren", lambda: print("[-] Speicheroptimierung aktiviert!")),
        ("[-] ReadyBoost aktivieren", lambda: print("[-] ReadyBoost aktiviert!")),
        ("[-] SSD-Trim ausführen", lambda: print("[-] SSD-Trim ausgeführt!")),
        ("[-] Indizierung deaktivieren", lambda: print("[-] Indizierung deaktiviert!")),
        ("Zurück", None)
    ]
    show_submenu("Storage Tweaks", options)

def fix_corrupted_files_menu():
    options = [
        ("[-] Systemdateien überprüfen (sfc /scannow)", lambda: print("[-] Systemdateien überprüft!")),
        ("[-] Windows Reparatur starten (DISM)", lambda: print("[-] Windows Reparatur gestartet!")),
        ("[-] Festplattenprüfung (chkdsk)", lambda: print("[-] Festplattenprüfung gestartet!")),
        ("[-] Windows-Komponentenstore bereinigen", lambda: print("[-] Komponentenstore bereinigt!")),
        ("Zurück", None)
    ]
    show_submenu("Fix Corrupted Files", options)

def fullscreen_optimization_menu():
    options = [
        ("[-] Vollbildoptimierung aktivieren", lambda: print("[-] Vollbildoptimierung aktiviert!")),
        ("[-] DPI-Einstellungen anpassen", lambda: print("[-] DPI-Einstellungen angepasst!")),
        ("[-] Game Mode aktivieren", lambda: print("[-] Game Mode aktiviert!")),
        ("[-] Variable Refresh Rate aktivieren", lambda: print("[-] VRR aktiviert!")),
        ("Zurück", None)
    ]
    show_submenu("Set Full Screen Optimization", options)

def uninstall_useless_apps_menu():
    options = [
        ("[-] Candy Crush deinstallieren", lambda: print("[-] Candy Crush deinstalliert!")),
        ("[-] 3D Viewer deinstallieren", lambda: print("[-] 3D Viewer deinstalliert!")),
        ("[-] Groove Music deinstallieren", lambda: print("[-] Groove Music deinstalliert!")),
        ("[-] Filme & TV deinstallieren", lambda: print("[-] Filme & TV deinstalliert!")),
        ("[-] Xbox Game Bar deinstallieren", lambda: print("[-] Xbox Game Bar deinstalliert!")),
        ("Zurück", None)
    ]
    show_submenu("Uninstall Useless Apps", options)

def network_tweaking_menu():
    options = [
        ("[-] Netzwerkadapter zurücksetzen", lambda: print("[-] Netzwerkadapter zurückgesetzt!")),
        ("[-] QoS deaktivieren", lambda: print("[-] QoS deaktiviert!")),
        ("[-] TCP/IP Stack optimieren", lambda: print("[-] TCP/IP Stack optimiert!")),
        ("[-] DNS-Cache leeren", lambda: print("[-] DNS-Cache geleert!")),
        ("[-] MTU-Wert optimieren", lambda: print("[-] MTU-Wert optimiert!")),
        ("[-] Netzwerkpriorität für Spiele setzen", lambda: print("[-] Netzwerkpriorität für Spiele gesetzt!")),
        ("Zurück", None)
    ]
    show_submenu("SMP Network Tweaking Utility", options)

def show_submenu(title, options):
    while True:
        clear()
        print_title(show_disclaimer=False)
        print_colored(f"{title}:", Fore.CYAN)
        for idx, (name, _) in enumerate(options, 1):
            print_colored(f"  [{idx}] {name}", Fore.YELLOW)
        try:
            choice = int(input("\nBitte wähle eine Option: "))
            if 1 <= choice < len(options):
                options[choice-1][1]()
                input("\nWeiter mit Enter...")
            elif choice == len(options):
                return
            else:
                print_colored("Ungültige Auswahl!", Fore.RED)
                time.sleep(1)
        except ValueError:
            print_colored("Ungültige Eingabe!", Fore.RED)
            time.sleep(1)

# Passe tweak_mode_menu an, damit bei Auswahl 2 das neue Menü aufgerufen wird

def tweak_mode_menu():
    while True:
        print_colored("\nPlease select a mode:", Fore.CYAN)
        print_colored("  [1] One-Click Tweak", Fore.CYAN)
        print_colored("  [2] Manual Tweak (recommended)", Fore.CYAN)
        choice = input("\nYour choice: ").strip()
        if choice == "1":
            loading_animation("Detecting system information", 2)
            show_system_info()
            while True:
                auto_tweak = input("Do you want SMP Tweaks to analyze your system and apply the best tweaks? (y/n): ").strip().lower()
                if auto_tweak == "y":
                    loading_animation("Applying tweaks", 2, color=Fore.GREEN)
                    animated_success("[Placeholder] Automatic tweaks are being applied...")
                    input("Done! Continue with Enter...")
                    return
                elif auto_tweak == "n":
                    print_colored("You can now select tweaks manually.", Fore.YELLOW)
                    input("Continue with Enter...")
                    manual_tweak_menu()
                    return
                else:
                    animated_warning("Invalid input! Please enter 'y' or 'n'.")
            break
        elif choice == "2":
            manual_tweak_menu()
            return
        else:
            animated_warning("Invalid selection!")
            time.sleep(1)

# English greetings
GREETINGS = [
    "Welcome, power user! 🚀",
    "Ready for maximum performance? 💻",
    "SMP Tweaker – Your system, your style!",
    "Let's tweak it! 🔧",
    "Performance incoming..."
]

def print_greeting():
    greeting = random.choice(GREETINGS)
    typing_effect(greeting, color=Fore.CYAN, delay=0.03)
    print()

# Progress bar and animation texts in English
def progress_bar(task="", duration=2, color=Fore.GREEN):
    bar_length = 30
    start = time.time()
    while (time.time() - start) < duration:
        percent = (time.time() - start) / duration
        hashes = '#' * int(percent * bar_length)
        spaces = ' ' * (bar_length - len(hashes))
        print(f"{color}{task} [{hashes}{spaces}] {int(percent*100)}%{Style.RESET_ALL}", end='\r', flush=True)
        time.sleep(0.05)
    print(f"{color}{task} [{'#'*bar_length}] 100%{Style.RESET_ALL}")

SUCCESS_COLORS = [Fore.GREEN, Fore.YELLOW, Fore.CYAN]
WARNING_COLORS = [Fore.RED, Fore.YELLOW]

def animated_success(text):
    for _ in range(3):
        for color in SUCCESS_COLORS:
            print_colored(text, color)
            time.sleep(0.1)
            print("\033[F", end='')  # Cursor up
    print_colored(text, Fore.GREEN)

def animated_warning(text):
    for _ in range(3):
        for color in WARNING_COLORS:
            print_colored(text, color)
            time.sleep(0.1)
            print("\033[F", end='')
    print_colored(text, Fore.RED)

def animated_menu_switch():
    loading_animation("Switching menu", 2, color=Fore.MAGENTA)

def animated_action(task="Action running..."):
    progress_bar(task, duration=2, color=Fore.BLUE)
    animated_success(f"{task} completed!")

# Integration in bestehende Menüs und Aktionen
# Begrüßung beim Start
# ...
def print_title(show_disclaimer=True):
    clear()
    typing_effect(ASCII_TITLE, color=Fore.BLUE, delay=0.001)
    print_greeting()
    if show_disclaimer:
        print_colored("Developed by SMP\n", Fore.MAGENTA)
        print_colored("DISCLAIMER: SMP is not responsible for any damage. You use this tool at your own risk.\n", Fore.RED)

# Beispielhafte Integration in bloatware_menu
# ...
def bloatware_menu():
    apps = [
        ("[-] Remove Xbox", lambda: animated_action("Xbox entfernen")),
        ("[-] Remove OneDrive", lambda: animated_action("OneDrive entfernen")),
        ("[-] Remove all default bloatware", lambda: animated_action("Alle Bloatware entfernen")),
        ("[-] Platzhalter Bloatware 1", lambda: animated_action("Bloatware Funktion 1")),
        ("[-] Platzhalter Bloatware 2", lambda: animated_action("Bloatware Funktion 2")),
        ("Back to Main Menu", None)
    ]
    while True:
        clear()
        print_title(show_disclaimer=False)
        typing_effect("Remove Bloatware:", color=Fore.CYAN, delay=0.01)
        for idx, (name, _) in enumerate(apps, 1):
            typing_effect(f"  [{idx}] {name}", color=Fore.YELLOW, delay=0.002)
        try:
            choice = int(input("\nPlease select an option: "))
            if 1 <= choice < len(apps):
                animated_menu_switch()
                loading_animation("Running action", 1, color=Fore.GREEN)
                apps[choice-1][1]()
                animated_success("Aktion erfolgreich abgeschlossen!")
                input("\nWeiter mit Enter...")
            elif choice == len(apps):
                return
            else:
                animated_warning("Invalid selection!")
                time.sleep(1)
        except ValueError:
            animated_warning("Invalid input!")
            time.sleep(1)

if __name__ == "__main__":
    ensure_admin()
    print_title()
    # Lizenzschlüssel-Abfrage
    for _ in range(3):
        key = input("Please enter license key: ").strip()
        if key in VALID_KEYS:
            print("\n[+] License key accepted!\n")
            break
        else:
            print("[ERROR] Invalid license key!\n")
    else:
        print("[ABORTED] Too many failed attempts.")
        sys.exit(1)
    # Restore-Point-Abfrage
    while True:
        answer = input("Would you like to create a system restore point? (Y/N): ").strip().lower()
        if answer in ("y", "yes"):
            print("The System Restore window will now open. Please follow the instructions in the window.")
            input("Press Enter to continue...")
            try:
                subprocess.run(["rstrui.exe"], check=True)
                print("[+] System Restore started successfully!")
            except Exception as e:
                print(f"[ERROR] Could not start System Restore: {e}")
            input("Press Enter to continue...")
            break
        elif answer in ("n", "no"):
            print("System restore point creation was skipped.")
            break
        else:
            print("Invalid input! Please enter Y for Yes or N for No.")
    tweak_mode_menu()
    main_menu()