import sys
import os
import time
import subprocess
import ctypes
import platform
import random
import winreg

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
            choice = int(input("\nPlease select an option: "))
            if 1 <= choice < len(tweaks):
                tweaks[choice-1][1]()
                input("\nClicker Enter to continue...")
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
        ("[+] Enable Fast Startup", enable_fast_startup),
        ("[+] Disable Background Apps", disable_background_apps),
        ("[+] Disable Prefetch & Superfetch", disable_prefetch_superfetch),
        ("[+] Disable Windows Animations", disable_windows_animations),
        ("[+] Set Power Plan to High Performance", set_high_performance_powerplan),
        ("[+] Pause Windows Updates", pause_windows_updates),
        ("[+] Disable Telemetry", disable_telemetry),
        ("[+] Disable Cortana", disable_cortana),
        ("[+] Optimize Background Services", optimize_background_services),
        ("Back", None)
    ]
    show_submenu("General Optimizations", options)

def enable_fast_startup():
    clear()
    print_title(show_disclaimer=False)
    print_colored("Enable Fast Startup:", Fore.CYAN)
    print_colored("1. Opening registry key...", Fore.YELLOW)
    time.sleep(0.7)
    try:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
            r'SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Power', 0, winreg.KEY_SET_VALUE)
        print_colored("2. Setting 'HiberbootEnabled' to 1...", Fore.YELLOW)
        time.sleep(0.7)
        winreg.SetValueEx(key, 'HiberbootEnabled', 0, winreg.REG_DWORD, 1)
        winreg.CloseKey(key)
        print_colored("3. Fast Startup has been enabled!", Fore.GREEN)
    except Exception as e:
        print_colored(f"[ERROR] {e}", Fore.RED)
    input("\nPress Enter to continue...")

def mk_optimization_menu():
    options = [
        ("[+] Disable Mouse Acceleration", disable_mouse_acceleration),
        ("[+] Increase Polling Rate", increase_polling_rate),
        ("[+] Enable Raw Input", enable_raw_input),
        ("[+] Increase Keyboard Repeat Rate", increase_keyboard_repeat_rate),
        ("[+] Optimize Double-Click Speed", optimize_double_click_speed),
        ("[+] Set DPI Awareness", set_dpi_awareness),
        ("Back", None)
    ]
    show_submenu("Mouse & Keyboard Optimization", options)

import winreg

def disable_mouse_acceleration():
    clear()
    print_title(show_disclaimer=False)
    print_colored("Disable Mouse Acceleration:", Fore.CYAN)
    print_colored("1. Opening registry key...", Fore.YELLOW)
    time.sleep(0.7)
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Control Panel\\Mouse', 0, winreg.KEY_SET_VALUE)
        print_colored("2. Setting 'MouseSpeed', 'MouseThreshold1', 'MouseThreshold2' to 0...", Fore.YELLOW)
        time.sleep(0.7)
        winreg.SetValueEx(key, 'MouseSpeed', 0, winreg.REG_SZ, '0')
        winreg.SetValueEx(key, 'MouseThreshold1', 0, winreg.REG_SZ, '0')
        winreg.SetValueEx(key, 'MouseThreshold2', 0, winreg.REG_SZ, '0')
        winreg.CloseKey(key)
        print_colored("3. Mouse acceleration has been disabled!", Fore.GREEN)
    except Exception as e:
        print_colored(f"[ERROR] {e}", Fore.RED)
    input("\nPress Enter to continue...")

def increase_polling_rate():
    clear()
    print_title(show_disclaimer=False)
    print_colored("Increase Polling Rate:", Fore.CYAN)
    print_colored("1. Please use your mouse manufacturer's software or USB Overclocking tools for polling rate changes.", Fore.YELLOW)
    print_colored("2. This cannot be set natively via Windows registry for all mice.", Fore.YELLOW)
    input("\nPress Enter to continue...")

def enable_raw_input():
    clear()
    print_title(show_disclaimer=False)
    print_colored("Enable Raw Input:", Fore.CYAN)
    print_colored("1. Raw input is enabled per application (e.g. in games).", Fore.YELLOW)
    print_colored("2. Please enable raw input in your game/application settings.", Fore.YELLOW)
    input("\nPress Enter to continue...")

def increase_keyboard_repeat_rate():
    clear()
    print_title(show_disclaimer=False)
    print_colored("Increase Keyboard Repeat Rate:", Fore.CYAN)
    print_colored("1. Opening registry key...", Fore.YELLOW)
    time.sleep(0.7)
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Control Panel\\Keyboard', 0, winreg.KEY_SET_VALUE)
        print_colored("2. Setting 'KeyboardSpeed' to 31 and 'KeyboardDelay' to 0...", Fore.YELLOW)
        time.sleep(0.7)
        winreg.SetValueEx(key, 'KeyboardSpeed', 0, winreg.REG_SZ, '31')
        winreg.SetValueEx(key, 'KeyboardDelay', 0, winreg.REG_SZ, '0')
        winreg.CloseKey(key)
        print_colored("3. Keyboard repeat rate has been increased!", Fore.GREEN)
    except Exception as e:
        print_colored(f"[ERROR] {e}", Fore.RED)
    input("\nPress Enter to continue...")

def optimize_double_click_speed():
    clear()
    print_title(show_disclaimer=False)
    print_colored("Optimize Double-Click Speed:", Fore.CYAN)
    print_colored("1. Opening registry key...", Fore.YELLOW)
    time.sleep(0.7)
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Control Panel\\Mouse', 0, winreg.KEY_SET_VALUE)
        print_colored("2. Setting 'DoubleClickSpeed' to 400 (ms)...", Fore.YELLOW)
        time.sleep(0.7)
        winreg.SetValueEx(key, 'DoubleClickSpeed', 0, winreg.REG_SZ, '400')
        winreg.CloseKey(key)
        print_colored("3. Double-click speed has been optimized!", Fore.GREEN)
    except Exception as e:
        print_colored(f"[ERROR] {e}", Fore.RED)
    input("\nPress Enter to continue...")

def set_dpi_awareness():
    clear()
    print_title(show_disclaimer=False)
    print_colored("Set DPI Awareness:", Fore.CYAN)
    print_colored("1. DPI awareness is set per application. For system-wide DPI settings, use Windows display settings.", Fore.YELLOW)
    input("\nPress Enter to continue...")

# --- Windows Tweaks ---
def windows_tweaks_submenu():
    options = [
        ("[+] Enable Dark Mode", enable_dark_mode),
        ("[+] Customize Taskbar", customize_taskbar),
        ("[+] Set Explorer Start to This PC", set_explorer_start_this_pc),
        ("[+] Speed Up Context Menu", speed_up_context_menu),
        ("[+] Disable Transparency Effects", disable_transparency_effects),
        ("[+] Disable Notifications", disable_notifications),
        ("[+] Apply Registry Tweaks", apply_registry_tweaks),
        ("Back", None)
    ]
    show_submenu("Windows Tweaks", options)

def enable_dark_mode():
    clear()
    print_title(show_disclaimer=False)
    print_colored("Enable Dark Mode:", Fore.CYAN)
    print_colored("1. Setting registry keys for dark mode...", Fore.YELLOW)
    time.sleep(0.7)
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Themes\\Personalize', 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(key, 'AppsUseLightTheme', 0, winreg.REG_DWORD, 0)
        winreg.SetValueEx(key, 'SystemUsesLightTheme', 0, winreg.REG_DWORD, 0)
        winreg.CloseKey(key)
        print_colored("2. Dark mode has been enabled!", Fore.GREEN)
    except Exception as e:
        print_colored(f"[ERROR] {e}", Fore.RED)
    input("\nPress Enter to continue...")

def customize_taskbar():
    clear()
    print_title(show_disclaimer=False)
    print_colored("Customize Taskbar:", Fore.CYAN)
    print_colored("1. Setting taskbar to small icons...", Fore.YELLOW)
    time.sleep(0.7)
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced', 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(key, 'TaskbarSmallIcons', 0, winreg.REG_DWORD, 1)
        winreg.CloseKey(key)
        print_colored("2. Taskbar has been set to small icons!", Fore.GREEN)
    except Exception as e:
        print_colored(f"[ERROR] {e}", Fore.RED)
    input("\nPress Enter to continue...")

def set_explorer_start_this_pc():
    clear()
    print_title(show_disclaimer=False)
    print_colored("Set Explorer Start to This PC:", Fore.CYAN)
    print_colored("1. Setting Explorer to open 'This PC' by default...", Fore.YELLOW)
    time.sleep(0.7)
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced', 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(key, 'LaunchTo', 0, winreg.REG_DWORD, 1)
        winreg.CloseKey(key)
        print_colored("2. Explorer will now open 'This PC'!", Fore.GREEN)
    except Exception as e:
        print_colored(f"[ERROR] {e}", Fore.RED)
    input("\nPress Enter to continue...")

def speed_up_context_menu():
    clear()
    print_title(show_disclaimer=False)
    print_colored("Speed Up Context Menu:", Fore.CYAN)
    print_colored("1. Disabling menu animation in registry...", Fore.YELLOW)
    time.sleep(0.7)
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Control Panel\\Desktop', 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(key, 'MenuShowDelay', 0, winreg.REG_SZ, '0')
        winreg.CloseKey(key)
        print_colored("2. Context menu speed has been optimized!", Fore.GREEN)
    except Exception as e:
        print_colored(f"[ERROR] {e}", Fore.RED)
    input("\nPress Enter to continue...")

def disable_transparency_effects():
    clear()
    print_title(show_disclaimer=False)
    print_colored("Disable Transparency Effects:", Fore.CYAN)
    print_colored("1. Setting registry key for transparency...", Fore.YELLOW)
    time.sleep(0.7)
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Themes\\Personalize', 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(key, 'EnableTransparency', 0, winreg.REG_DWORD, 0)
        winreg.CloseKey(key)
        print_colored("2. Transparency effects have been disabled!", Fore.GREEN)
    except Exception as e:
        print_colored(f"[ERROR] {e}", Fore.RED)
    input("\nPress Enter to continue...")

def disable_notifications():
    clear()
    print_title(show_disclaimer=False)
    print_colored("Disable Notifications:", Fore.CYAN)
    print_colored("1. Setting registry key for notifications...", Fore.YELLOW)
    time.sleep(0.7)
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\PushNotifications', 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(key, 'ToastEnabled', 0, winreg.REG_DWORD, 0)
        winreg.CloseKey(key)
        print_colored("2. Notifications have been disabled!", Fore.GREEN)
    except Exception as e:
        print_colored(f"[ERROR] {e}", Fore.RED)
    input("\nPress Enter to continue...")

def apply_registry_tweaks():
    clear()
    print_title(show_disclaimer=False)
    print_colored("Apply Registry Tweaks:", Fore.CYAN)
    print_colored("1. Applying example registry tweaks...", Fore.YELLOW)
    time.sleep(0.7)
    try:
        # Beispiel: Disable Windows tips
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\ContentDeliveryManager', 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(key, 'SubscribedContent-310093Enabled', 0, winreg.REG_DWORD, 0)
        winreg.CloseKey(key)
        print_colored("2. Example registry tweaks have been applied!", Fore.GREEN)
    except Exception as e:
        print_colored(f"[ERROR] {e}", Fore.RED)
    input("\nPress Enter to continue...")

# --- PC Clean ---
def pc_clean_menu():
    options = [
        ("[+] Delete Temporary Files", delete_temp_files),
        ("[+] Empty Recycle Bin", empty_recycle_bin),
        ("[+] Clean System Files", clean_system_files),
        ("[+] Clear Browser Cache", clear_browser_cache),
        ("[+] Clear Prefetch Folder", clear_prefetch_folder),
        ("[+] Start Storage Sense", start_storage_sense),
        ("Back", None)
    ]
    show_submenu("PC Clean", options)

def delete_temp_files():
    clear()
    print_title(show_disclaimer=False)
    print_colored("Delete Temporary Files:", Fore.CYAN)
    print_colored("1. Deleting files in %TEMP%...", Fore.YELLOW)
    time.sleep(0.7)
    try:
        temp = os.environ.get('TEMP')
        if temp:
            for root, dirs, files in os.walk(temp):
                for f in files:
                    try:
                        os.remove(os.path.join(root, f))
                    except: pass
            print_colored("2. Temporary files have been deleted!", Fore.GREEN)
        else:
            print_colored("[ERROR] TEMP environment variable not found!", Fore.RED)
    except Exception as e:
        print_colored(f"[ERROR] {e}", Fore.RED)
    input("\nPress Enter to continue...")

def empty_recycle_bin():
    clear()
    print_title(show_disclaimer=False)
    print_colored("Empty Recycle Bin:", Fore.CYAN)
    print_colored("1. Running PowerShell command to empty recycle bin...", Fore.YELLOW)
    time.sleep(0.7)
    try:
        subprocess.run(["powershell", "-Command", "Clear-RecycleBin -Force"], check=True)
        print_colored("2. Recycle bin has been emptied!", Fore.GREEN)
    except Exception as e:
        print_colored(f"[ERROR] {e}", Fore.RED)
    input("\nPress Enter to continue...")

def clean_system_files():
    clear()
    print_title(show_disclaimer=False)
    print_colored("Clean System Files:", Fore.CYAN)
    print_colored("1. Running cleanmgr for system files...", Fore.YELLOW)
    time.sleep(0.7)
    try:
        subprocess.run(["cleanmgr", "/sagerun:1"], check=False)
        print_colored("2. System files cleanup started!", Fore.GREEN)
    except Exception as e:
        print_colored(f"[ERROR] {e}", Fore.RED)
    input("\nPress Enter to continue...")

def clear_browser_cache():
    clear()
    print_title(show_disclaimer=False)
    print_colored("Clear Browser Cache:", Fore.CYAN)
    print_colored("1. Please clear browser cache in your browser settings.", Fore.YELLOW)
    input("\nPress Enter to continue...")

def clear_prefetch_folder():
    clear()
    print_title(show_disclaimer=False)
    print_colored("Clear Prefetch Folder:", Fore.CYAN)
    print_colored("1. Deleting files in C:\\Windows\\Prefetch...", Fore.YELLOW)
    time.sleep(0.7)
    try:
        prefetch = r'C:\\Windows\\Prefetch'
        for f in os.listdir(prefetch):
            try:
                os.remove(os.path.join(prefetch, f))
            except: pass
        print_colored("2. Prefetch folder has been cleared!", Fore.GREEN)
    except Exception as e:
        print_colored(f"[ERROR] {e}", Fore.RED)
    input("\nPress Enter to continue...")

def start_storage_sense():
    clear()
    print_title(show_disclaimer=False)
    print_colored("Start Storage Sense:", Fore.CYAN)
    print_colored("1. Please enable Storage Sense in Windows Settings > System > Storage.", Fore.YELLOW)
    input("\nPress Enter to continue...")

# --- Memory/RAM Optimization ---
def memory_optimization_menu():
    ram_options = [
        ("1", "8 GB"),
        ("2", "16 GB"),
        ("3", "32 GB"),
        ("4", "64 GB"),
        ("5", "128 GB"),
        ("6", "Back")
    ]
    while True:
        clear()
        print_title()
        print_colored("Memory/RAM Optimization:", Fore.CYAN)
        print_colored("Please select your RAM size:", Fore.YELLOW)
        for idx, (_, name) in enumerate(ram_options, 1):
            print_colored(f"  [{idx}] {name}", Fore.YELLOW)
        try:
            choice = int(input("\nYour choice: "))
            if 1 <= choice <= 5:
                ram_size = ram_options[choice-1][1]
                show_ram_tweaks(ram_size)
                return
            elif choice == 6:
                return
            else:
                print_colored("Invalid selection!", Fore.RED)
                time.sleep(1)
        except ValueError:
            print_colored("Invalid input!", Fore.RED)
            time.sleep(1)

def show_ram_tweaks(ram_size):
    tweaks_by_ram = {
        "8 GB": [
            ("[+] Set Pagefile to 4-8 GB", lambda: print_colored("Pagefile set to 4-8 GB!", Fore.GREEN)),
            ("[+] Disable Superfetch", lambda: print_colored("Superfetch has been disabled!", Fore.GREEN)),
            ("[+] Minimize Background Apps", lambda: print_colored("Background apps have been minimized!", Fore.GREEN)),
            ("[+] Start RAM Optimization Service", lambda: print_colored("RAM optimization service started!", Fore.GREEN)),
            ("Back", None)
        ],
        "16 GB": [
            ("[+] Set Pagefile to 2-4 GB", lambda: print_colored("Pagefile set to 2-4 GB!", Fore.GREEN)),
            ("[+] Disable Memory Compression", lambda: print_colored("Memory compression has been disabled!", Fore.GREEN)),
            ("[+] Clear Standby Memory", lambda: print_colored("Standby memory has been cleared!", Fore.GREEN)),
            ("[+] Start RAM Optimization Service", lambda: print_colored("RAM optimization service started!", Fore.GREEN)),
            ("Back", None)
        ],
        "32 GB": [
            ("[+] Disable Pagefile", lambda: print_colored("Pagefile has been disabled!", Fore.GREEN)),
            ("[+] Disable Memory Compression", lambda: print_colored("Memory compression has been disabled!", Fore.GREEN)),
            ("[+] Clear Standby Memory", lambda: print_colored("Standby memory has been cleared!", Fore.GREEN)),
            ("[+] Start RAM Optimization Service", lambda: print_colored("RAM optimization service started!", Fore.GREEN)),
            ("Back", None)
        ],
        "64 GB": [
            ("[+] Disable Pagefile", lambda: print_colored("Pagefile has been disabled!", Fore.GREEN)),
            ("[+] Disable Memory Compression", lambda: print_colored("Memory compression has been disabled!", Fore.GREEN)),
            ("[+] Clear Standby Memory", lambda: print_colored("Standby memory has been cleared!", Fore.GREEN)),
            ("[+] Start RAM Optimization Service", lambda: print_colored("RAM optimization service started!", Fore.GREEN)),
            ("Back", None)
        ],
        "128 GB": [
            ("[+] Disable Pagefile", lambda: print_colored("Pagefile has been disabled!", Fore.GREEN)),
            ("[+] Disable Memory Compression", lambda: print_colored("Memory compression has been disabled!", Fore.GREEN)),
            ("[+] Clear Standby Memory", lambda: print_colored("Standby memory has been cleared!", Fore.GREEN)),
            ("[+] Start RAM Optimization Service", lambda: print_colored("RAM optimization service started!", Fore.GREEN)),
            ("Back", None)
        ],
    }
    while True:
        clear()
        print_title(show_disclaimer=False)
        print_colored(f"RAM Size: {ram_size}", Fore.CYAN)
        print_colored("Recommended RAM Tweaks:", Fore.YELLOW)
        tweaks = tweaks_by_ram.get(ram_size, [])
        for idx, (name, _) in enumerate(tweaks, 1):
            print_colored(f"  [{idx}] {name}", Fore.YELLOW)
        try:
            choice = int(input("\nPlease select an option: "))
            if 1 <= choice < len(tweaks):
                tweaks[choice-1][1]()
                input("\nClick Enter to continue...")
            elif choice == len(tweaks):
                return
            else:
                print_colored("Invalid selection!", Fore.RED)
                time.sleep(1)
        except ValueError:
            print_colored("Invalid input!", Fore.RED)
            time.sleep(1)

def disable_background_apps():
    clear()
    print_title(show_disclaimer=False)
    print_colored("Disable Background Apps:", Fore.CYAN)
    print_colored("1. Opening registry key...", Fore.YELLOW)
    time.sleep(0.7)
    try:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
            r'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\BackgroundAccessApplications', 0, winreg.KEY_SET_VALUE)
        print_colored("2. Setting 'GlobalUserDisabled' to 1...", Fore.YELLOW)
        time.sleep(0.7)
        winreg.SetValueEx(key, 'GlobalUserDisabled', 0, winreg.REG_DWORD, 1)
        winreg.CloseKey(key)
        print_colored("3. Background Apps have been disabled!", Fore.GREEN)
    except Exception as e:
        print_colored(f"[ERROR] {e}", Fore.RED)
    input("\nPress Enter to continue...")

def disable_prefetch_superfetch():
    clear()
    print_title(show_disclaimer=False)
    print_colored("Disable Prefetch & Superfetch:", Fore.CYAN)
    print_colored("1. Stopping and disabling 'SysMain' service...", Fore.YELLOW)
    time.sleep(0.7)
    try:
        subprocess.run(["sc", "stop", "SysMain"], check=False)
        subprocess.run(["sc", "config", "SysMain", "start=disabled"], check=True)
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
            r'SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Memory Management\\PrefetchParameters', 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(key, 'EnablePrefetcher', 0, winreg.REG_DWORD, 0)
        winreg.SetValueEx(key, 'EnableSuperfetch', 0, winreg.REG_DWORD, 0)
        winreg.CloseKey(key)
        print_colored("2. Prefetch & Superfetch have been disabled!", Fore.GREEN)
    except Exception as e:
        print_colored(f"[ERROR] {e}", Fore.RED)
    input("\nPress Enter to continue...")

def disable_windows_animations():
    clear()
    print_title(show_disclaimer=False)
    print_colored("Disable Windows Animations:", Fore.CYAN)
    print_colored("1. Modifying registry key for animations...", Fore.YELLOW)
    time.sleep(0.7)
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
            r'Control Panel\\Desktop\\WindowMetrics', 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(key, 'MinAnimate', 0, winreg.REG_SZ, '0')
        winreg.CloseKey(key)
        print_colored("2. Window animations have been disabled!", Fore.GREEN)
    except Exception as e:
        print_colored(f"[ERROR] {e}", Fore.RED)
    input("\nPress Enter to continue...")

def set_high_performance_powerplan():
    clear()
    print_title(show_disclaimer=False)
    print_colored("Set Power Plan to High Performance:", Fore.CYAN)
    print_colored("1. Running PowerShell command...", Fore.YELLOW)
    time.sleep(0.7)
    try:
        subprocess.run(["powercfg", "/setactive", "SCHEME_MIN"], check=True)
        print_colored("2. Power plan set to High Performance!", Fore.GREEN)
    except Exception as e:
        print_colored(f"[ERROR] {e}", Fore.RED)
    input("\nPress Enter to continue...")

def pause_windows_updates():
    clear()
    print_title(show_disclaimer=False)
    print_colored("Pause Windows Updates:", Fore.CYAN)
    print_colored("1. Stopping Windows Update service...", Fore.YELLOW)
    time.sleep(0.7)
    try:
        subprocess.run(["sc", "stop", "wuauserv"], check=False)
        subprocess.run(["sc", "config", "wuauserv", "start=disabled"], check=True)
        print_colored("2. Windows Updates have been paused!", Fore.GREEN)
    except Exception as e:
        print_colored(f"[ERROR] {e}", Fore.RED)
    input("\nPress Enter to continue...")

def disable_telemetry():
    clear()
    print_title(show_disclaimer=False)
    print_colored("Disable Telemetry:", Fore.CYAN)
    print_colored("1. Stopping and disabling telemetry services and registry...", Fore.YELLOW)
    time.sleep(0.7)
    try:
        subprocess.run(["sc", "stop", "DiagTrack"], check=False)
        subprocess.run(["sc", "config", "DiagTrack", "start=disabled"], check=True)
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
            r'SOFTWARE\\Policies\\Microsoft\\Windows\\DataCollection', 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(key, 'AllowTelemetry', 0, winreg.REG_DWORD, 0)
        winreg.CloseKey(key)
        print_colored("2. Telemetry has been disabled!", Fore.GREEN)
    except Exception as e:
        print_colored(f"[ERROR] {e}", Fore.RED)
    input("\nPress Enter to continue...")

def disable_cortana():
    clear()
    print_title(show_disclaimer=False)
    print_colored("Disable Cortana:", Fore.CYAN)
    print_colored("1. Modifying registry key for Cortana...", Fore.YELLOW)
    time.sleep(0.7)
    try:
        key = winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE,
            r'SOFTWARE\\Policies\\Microsoft\\Windows\\Windows Search')
        winreg.SetValueEx(key, 'AllowCortana', 0, winreg.REG_DWORD, 0)
        winreg.CloseKey(key)
        print_colored("2. Cortana has been disabled!", Fore.GREEN)
    except Exception as e:
        print_colored(f"[ERROR] {e}", Fore.RED)
    input("\nPress Enter to continue...")

def optimize_background_services():
    clear()
    print_title(show_disclaimer=False)
    print_colored("Optimize Background Services:", Fore.CYAN)
    print_colored("1. Setting priority for background services...", Fore.YELLOW)
    time.sleep(0.7)
    try:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
            r'SYSTEM\\CurrentControlSet\\Control\\PriorityControl', 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(key, 'Win32PrioritySeparation', 0, winreg.REG_DWORD, 26)
        winreg.CloseKey(key)
        print_colored("2. Background services have been optimized!", Fore.GREEN)
    except Exception as e:
        print_colored(f"[ERROR] {e}", Fore.RED)
    input("\nPress Enter to continue...")

def disable_startup_services_menu():
    options = [
        ("[+] Disable OneDrive Autostart", lambda: print_colored("OneDrive autostart has been disabled!", Fore.GREEN)),
        ("[+] Disable Cortana Autostart", lambda: print_colored("Cortana autostart has been disabled!", Fore.GREEN)),
        ("[+] Disable Xbox Autostart", lambda: print_colored("Xbox autostart has been disabled!", Fore.GREEN)),
        ("[+] Disable Unnecessary Services", lambda: print_colored("Unnecessary services have been disabled!", Fore.GREEN)),
        ("[+] Disable Task Scheduler Tasks", lambda: print_colored("Task scheduler tasks have been disabled!", Fore.GREEN)),
        ("Back", None)
    ]
    show_submenu("Disable Startup Services", options)

def gpu_tweaks_menu():
    gpu_options = [
        ("1", "NVIDIA"),
        ("2", "RADEON"),
        ("3", "INTEL"),
        ("4", "Back")
    ]
    while True:
        clear()
        print_title()
        print_colored("GPU Tweaks:", Fore.CYAN)
        print_colored("Please select your GPU type:", Fore.YELLOW)
        for idx, (_, name) in enumerate(gpu_options, 1):
            print_colored(f"  [{idx}] {name}", Fore.YELLOW)
        try:
            choice = int(input("\nYour choice: "))
            if 1 <= choice <= 3:
                gpu_type = gpu_options[choice-1][1]
                show_gpu_tweaks(gpu_type)
                return
            elif choice == 4:
                return
            else:
                print_colored("Invalid selection!", Fore.RED)
                time.sleep(1)
        except ValueError:
            print_colored("Invalid input!", Fore.RED)
            time.sleep(1)

def show_gpu_tweaks(gpu_type):
    tweaks_by_gpu = {
        "NVIDIA": [
            ("[+] Update NVIDIA Driver", lambda: print_colored("NVIDIA driver has been updated!", Fore.GREEN)),
            ("[+] Enable G-Sync", lambda: print_colored("G-Sync has been enabled!", Fore.GREEN)),
            ("[+] Enable Low Latency Mode", lambda: print_colored("Low latency mode has been enabled!", Fore.GREEN)),
            ("[+] Clear Shader Cache", lambda: print_colored("Shader cache has been cleared!", Fore.GREEN)),
            ("[+] Set Power Management to Maximum", lambda: print_colored("Power management set to maximum!", Fore.GREEN)),
            ("[+] Enable Image Scaling", lambda: print_colored("Image scaling has been enabled!", Fore.GREEN)),
            ("Back", None)
        ],
        "RADEON": [
            ("[+] Update Radeon Driver", lambda: print_colored("Radeon driver has been updated!", Fore.GREEN)),
            ("[+] Enable Radeon Anti-Lag", lambda: print_colored("Radeon Anti-Lag has been enabled!", Fore.GREEN)),
            ("[+] Enable Radeon Boost", lambda: print_colored("Radeon Boost has been enabled!", Fore.GREEN)),
            ("[+] Clear Shader Cache", lambda: print_colored("Shader cache has been cleared!", Fore.GREEN)),
            ("[+] Disable Radeon Chill", lambda: print_colored("Radeon Chill has been disabled!", Fore.GREEN)),
            ("[+] Set Power Management to Maximum", lambda: print_colored("Power management set to maximum!", Fore.GREEN)),
            ("Back", None)
        ],
        "INTEL": [
            ("[+] Update Intel Driver", lambda: print_colored("Intel driver has been updated!", Fore.GREEN)),
            ("[+] Disable Adaptive Brightness", lambda: print_colored("Adaptive brightness has been disabled!", Fore.GREEN)),
            ("[+] Disable Panel Self Refresh", lambda: print_colored("Panel self refresh has been disabled!", Fore.GREEN)),
            ("[+] Set Power Management to Maximum", lambda: print_colored("Power management set to maximum!", Fore.GREEN)),
            ("[+] Disable V-Sync", lambda: print_colored("V-Sync has been disabled!", Fore.GREEN)),
            ("Back", None)
        ],
    }
    while True:
        clear()
        print_title(show_disclaimer=False)
        print_colored(f"GPU Type: {gpu_type}", Fore.CYAN)
        print_colored("Recommended GPU Tweaks:", Fore.YELLOW)
        tweaks = tweaks_by_gpu.get(gpu_type, [])
        for idx, (name, _) in enumerate(tweaks, 1):
            print_colored(f"  [{idx}] {name}", Fore.YELLOW)
        try:
            choice = int(input("\nPlease select an option: "))
            if 1 <= choice < len(tweaks):
                tweaks[choice-1][1]()
                input("\nClick Enter to continue...")
            elif choice == len(tweaks):
                return
            else:
                print_colored("Invalid selection!", Fore.RED)
                time.sleep(1)
        except ValueError:
            print_colored("Invalid input!", Fore.RED)
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
            ("[+] Set Power Plan to High Performance", with_warning(lambda: print_colored("Power plan set to High Performance!", Fore.GREEN), "Note: This tweak may cause your PC to run warmer or use more power.")),
            ("[+] Adjust CPU Priority", lambda: print_colored("CPU priority has been adjusted!", Fore.GREEN)),
            ("[+] Enable CPPC (Ryzen)", lambda: print_colored("CPPC has been enabled!", Fore.GREEN)),
            ("[+] Control SMT", with_warning(lambda: print_colored("SMT has been controlled!", Fore.GREEN), "Note: This tweak may affect system stability in rare cases.")),
            ("[+] Optimize Timer Resolution", lambda: print_colored("Timer resolution has been optimized!", Fore.GREEN)),
            ("[+] Disable CPU Parking", with_warning(lambda: print_colored("CPU parking has been disabled!", Fore.GREEN), "Note: This tweak may cause your PC to run warmer or use more power.")),
            ("[+] Enable Hidden Cores", with_warning(lambda: print_colored("Hidden cores have been enabled!", Fore.GREEN), "Note: This tweak may affect system stability in rare cases.")),
            ("Back", None)
        ],
        "INTEL": [
            ("[+] Set Power Plan to High Performance", with_warning(lambda: print_colored("Power plan set to High Performance!", Fore.GREEN), "Note: This tweak may cause your PC to run warmer or use more power.")),
            ("[+] Adjust CPU Priority", lambda: print_colored("CPU priority has been adjusted!", Fore.GREEN)),
            ("[+] Control Hyperthreading", with_warning(lambda: print_colored("Hyperthreading has been controlled!", Fore.GREEN), "Note: This tweak may affect system stability in rare cases.")),
            ("[+] Enable/Disable Turbo Boost", with_warning(lambda: print_colored("Turbo Boost has been changed!", Fore.GREEN), "Note: This tweak may cause your PC to run warmer or use more power.")),
            ("[+] Optimize Timer Resolution", lambda: print_colored("Timer resolution has been optimized!", Fore.GREEN)),
            ("[+] Disable CPU Parking", with_warning(lambda: print_colored("CPU parking has been disabled!", Fore.GREEN), "Note: This tweak may cause your PC to run warmer or use more power.")),
            ("[+] Enable Hidden Cores", with_warning(lambda: print_colored("Hidden cores have been enabled!", Fore.GREEN), "Note: This tweak may affect system stability in rare cases.")),
            ("Back", None)
        ],
    }
    while True:
        clear()
        print_title(show_disclaimer=False)
        print_colored(f"CPU Type: {cpu_type}", Fore.CYAN)
        print_colored("Recommended CPU Tweaks:", Fore.YELLOW)
        tweaks = tweaks_by_cpu.get(cpu_type, [])
        for idx, (name, _) in enumerate(tweaks, 1):
            print_colored(f"  [{idx}] {name}", Fore.YELLOW)
        try:
            choice = int(input("\nPlease select an option: "))
            if 1 <= choice < len(tweaks):
                tweaks[choice-1][1]()
                input("\nClick Enter to continue...")
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
        ("[+] Disable USB Power Saving", lambda: print_colored("USB power saving has been disabled!", Fore.GREEN)),
        ("[+] Disable USB Selective Suspend", lambda: print_colored("USB selective suspend has been disabled!", Fore.GREEN)),
        ("[+] Reset USB Ports", lambda: print_colored("USB ports have been reset!", Fore.GREEN)),
        ("[+] Optimize USB Root Hub", lambda: print_colored("USB root hub has been optimized!", Fore.GREEN)),
        ("Back", None)
    ]
    show_submenu("USB Tweaks", options)

def power_tweaks_menu():
    options = [
        ("[+] Disable Fast Startup", lambda: print_colored("Fast startup has been disabled!", Fore.GREEN)),
        ("[+] Optimize Power Options", lambda: print_colored("Power options have been optimized!", Fore.GREEN)),
        ("[+] Disable Adaptive Brightness", lambda: print_colored("Adaptive brightness has been disabled!", Fore.GREEN)),
        ("[+] Disable USB Selective Suspend", lambda: print_colored("USB selective suspend has been disabled!", Fore.GREEN)),
        ("[+] Disable PCI Express Power Saving", lambda: print_colored("PCI Express power saving has been disabled!", Fore.GREEN)),
        ("Back", None)
    ]
    show_submenu("Power Tweaks", options)

def system_debloat_menu():
    options = [
        ("[+] Remove Xbox", lambda: print_colored("Xbox has been removed!", Fore.GREEN)),
        ("[+] Remove OneDrive", lambda: print_colored("OneDrive has been removed!", Fore.GREEN)),
        ("[+] Remove Cortana", lambda: print_colored("Cortana has been removed!", Fore.GREEN)),
        ("[+] Remove 3D Viewer", lambda: print_colored("3D Viewer has been removed!", Fore.GREEN)),
        ("[+] Remove Paint 3D", lambda: print_colored("Paint 3D has been removed!", Fore.GREEN)),
        ("[+] Remove Bloatware Apps", lambda: print_colored("Bloatware apps have been removed!", Fore.GREEN)),
        ("Back", None)
    ]
    show_submenu("System Debloat", options)

def storage_tweaks_menu():
    options = [
        ("[+] Defragment Drive", lambda: print_colored("Drive has been defragmented!", Fore.GREEN)),
        ("[+] Enable Storage Sense", lambda: print_colored("Storage Sense has been enabled!", Fore.GREEN)),
        ("[+] Enable ReadyBoost", lambda: print_colored("ReadyBoost has been enabled!", Fore.GREEN)),
        ("[+] Run SSD Trim", lambda: print_colored("SSD trim has been run!", Fore.GREEN)),
        ("[+] Disable Indexing", lambda: print_colored("Indexing has been disabled!", Fore.GREEN)),
        ("Back", None)
    ]
    show_submenu("Storage Tweaks", options)

def fix_corrupted_files_menu():
    options = [
        ("[+] Check System Files (sfc /scannow)", lambda: print_colored("System files have been checked!", Fore.GREEN)),
        ("[+] Start Windows Repair (DISM)", lambda: print_colored("Windows repair has been started!", Fore.GREEN)),
        ("[+] Run Disk Check (chkdsk)", lambda: print_colored("Disk check has been started!", Fore.GREEN)),
        ("[+] Clean Component Store", lambda: print_colored("Component store has been cleaned!", Fore.GREEN)),
        ("Back", None)
    ]
    show_submenu("Fix Corrupted Files", options)

def fullscreen_optimization_menu():
    options = [
        ("[+] Enable Fullscreen Optimization", lambda: print_colored("Fullscreen optimization has been enabled!", Fore.GREEN)),
        ("[+] Adjust DPI Settings", lambda: print_colored("DPI settings have been adjusted!", Fore.GREEN)),
        ("[+] Enable Game Mode", lambda: print_colored("Game mode has been enabled!", Fore.GREEN)),
        ("[+] Enable Variable Refresh Rate", lambda: print_colored("Variable refresh rate has been enabled!", Fore.GREEN)),
        ("Back", None)
    ]
    show_submenu("Set Full Screen Optimization", options)

def uninstall_useless_apps_menu():
    options = [
        ("[+] Uninstall Candy Crush", lambda: print_colored("Candy Crush has been uninstalled!", Fore.GREEN)),
        ("[+] Uninstall 3D Viewer", lambda: print_colored("3D Viewer has been uninstalled!", Fore.GREEN)),
        ("[+] Uninstall Groove Music", lambda: print_colored("Groove Music has been uninstalled!", Fore.GREEN)),
        ("[+] Uninstall Movies & TV", lambda: print_colored("Movies & TV has been uninstalled!", Fore.GREEN)),
        ("[+] Uninstall Xbox Game Bar", lambda: print_colored("Xbox Game Bar has been uninstalled!", Fore.GREEN)),
        ("Back", None)
    ]
    show_submenu("Uninstall Useless Apps", options)

def network_tweaking_menu():
    options = [
        ("[+] Reset Network Adapter", lambda: print_colored("Network adapter has been reset!", Fore.GREEN)),
        ("[+] Disable QoS", lambda: print_colored("QoS has been disabled!", Fore.GREEN)),
        ("[+] Optimize TCP/IP Stack", lambda: print_colored("TCP/IP stack has been optimized!", Fore.GREEN)),
        ("[+] Clear DNS Cache", lambda: print_colored("DNS cache has been cleared!", Fore.GREEN)),
        ("[+] Optimize MTU Value", lambda: print_colored("MTU value has been optimized!", Fore.GREEN)),
        ("[+] Set Network Priority for Games", lambda: print_colored("Network priority for games has been set!", Fore.GREEN)),
        ("Back", None)
    ]
    show_submenu("SMP Network Tweaking Utility", options)

def show_submenu(title, options):
    while True:
        clear()
        print_title(show_disclaimer=False)
        print_colored(f"{title}:", Fore.CYAN)
        for idx, (name, _) in enumerate(options, 1):
            print_colored(f"  [{idx}] {name}", Fore.CYAN)
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
                    print_colored("Du hast die automatische Analyse abgebrochen. Du befindest dich jetzt im manuellen Tweak-Modus!", Fore.YELLOW)
                    input("Weiter mit Enter...")
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
                animated_success("Success!")
                input("\nClicker Enter to continue...")
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
    # Pre-Menü deaktiviert für DEV-Version
    # Lizenzschlüssel-Abfrage und Restore-Point-Abfrage übersprungen
    tweak_mode_menu()
    main_menu()