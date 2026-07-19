class SmartDevice:
    def __init__(self, uid, state, name):
        self._uid, self._state, self.name = uid, state, name

    @property
    def state(self): return self._state
    @state.setter
    def state(self, s): self._state = s.upper() if s.upper() in ["ON", "OFF"] else print("Invalid")

    def toggle(self, stat): 
        self._state = stat
        print(f"[{self.name}] is now {stat}")

    def show(self): print(f"  | ID: {self._uid}\n  | State: {self._state}\n  | Name: {self.name}")

class TemperatureSensor(SmartDevice):
    def __init__(self, uid, state, name, temp):
        super().__init__(uid, state, name)
        self.temp = temp
    def show(self): super().show(); print(f"  | Temp: {self.temp}°C")

class SecurityCamera(SmartDevice):
    def __init__(self, uid, state, name, rec):
        super().__init__(uid, state, name)
        self.rec = rec
    def show(self): super().show(); print(f"  | Recording: {self.rec}")

class SmartLight(SmartDevice):
    def __init__(self, uid, state, name, bright):
        super().__init__(uid, state, name)
        self.bright = bright
    def show(self): super().show(); print(f"  | Brightness: {self.bright}%")

# Setup devices
devices = {
    "sensor": TemperatureSensor("T101", "OFF", "Living Room Temp", 25),
    "light": SmartLight("L202", "OFF", "Kitchen Light", 0),
    "camera": SecurityCamera("C303", "OFF", "Front Door Cam", "Stopped")
}

while True:
    print("\n=== SYSTEM MENU ===\n1. Info | 2. On | 3. Off | 4. Temp | 5. Bright | 6. Record | 7. Exit")
    try: choice = int(input("Action: "))
    except ValueError: continue

    match choice:
        case 1: [print(f"\n[{k.upper()}]") or v.show() for k, v in devices.items()]
        case 2 | 3:
            dev = input("Target (sensor/light/camera): ").strip().lower()
            devices[dev].toggle("ON" if choice == 2 else "OFF") if dev in devices else print("Unknown device")
        case 4: print(f"Reading: {devices['sensor'].temp}°C")
        case 5:
            val = input("Brightness (0-100): ")
            if val.isdigit() and 0 <= int(val) <= 100: 
                devices['light'].bright = int(val)
                print("Updated.")
        case 6:
            devices['camera'].rec = "Recording"
            print("Recording started.")
        case 7: print("Exiting..."); break
        case _: print("Invalid option.")
