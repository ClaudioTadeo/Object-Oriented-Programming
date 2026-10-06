import tkinter as tk
from tkinter import ttk
from abc import ABC, abstractmethod


# =====================================================================
# 1. BASE CLASS & POLYMORPHIC METHODS
# =====================================================================
class SmartDevice(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def turn_on(self) -> str:
        pass

    # REQUIREMENT 1: Added second polymorphic behavior
    @abstractmethod
    def turn_off(self) -> str:
        pass


# =====================================================================
# DEVICE CLASSES
# =====================================================================
class SmartLight(SmartDevice):
    def __init__(self):
        super().__init__("Living Room Smart Light")

    def turn_on(self) -> str:
        return f"💡 {self.name}: Turned ON with 100% brightness."

    def turn_off(self) -> str:
        return f"🌑 {self.name}: Turned OFF."


class SmartSpeaker(SmartDevice):
    def __init__(self):
        super().__init__("Alexa Speaker")

    def turn_on(self) -> str:
        return f"🔊 {self.name}: Playing Lofi music."

    def turn_off(self) -> str:
        return f"🔇 {self.name}: Music stopped."


class SmartThermostat(SmartDevice):
    def __init__(self):
        super().__init__("Ecobee Thermostat")

    def turn_on(self) -> str:
        return f"🌡️ {self.name}: Climate control active (Set to 22°C)."

    def turn_off(self) -> str:
        return f"❄️ {self.name}: Climate control deactivated."


# REQUIREMENT 2: Added a new device class to test scalability
class SmartCamera(SmartDevice):
    def __init__(self):
        super().__init__("Front Door Security Camera")

    def turn_on(self) -> str:
        return f"🛡️ {self.name}: Live feed active & recording."

    def turn_off(self) -> str:
        return f"💤 {self.name}: Recording paused (Privacy mode)."


# =====================================================================
# 3. UPGRADED TKINTER GUI
# =====================================================================
class SmartHomeApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Lab 6.1: Smart Home Upgrade")
        self.geometry("600x600")  # Increased height to fit the Activity Log
        self.resizable(True, True)

        # Added the new camera device into the system dictionary
        self.devices = {
            "Smart Light": SmartLight(),
            "Smart Speaker": SmartSpeaker(),
            "Smart Thermostat": SmartThermostat(),
            "Security Camera": SmartCamera()  
        }

        self._build_interface()

    def _build_interface(self):
        # Header Label
        lbl_header = tk.Label(
            self,
            text="SMART HOME CENTER",
            font=("Arial", 15, "bold"),
            fg="#2c3e50"
        )
        lbl_header.pack(pady=12)

        # Device Selection Container
        group_box = tk.LabelFrame(
            self,
            text=" Select Device ",
            font=("Arial", 10, "bold"),
            padx=15,
            pady=10
        )
        group_box.pack(fill="x", padx=20, pady=5)

        first_key = list(self.devices.keys())[0]
        self.selected_key = tk.StringVar(value=first_key)

        for key in self.devices.keys():
            rb = ttk.Radiobutton(
                group_box,
                text=key,
                value=key,
                variable=self.selected_key
            )
            rb.pack(anchor="w", pady=3)

        # REQUIREMENT 3: Horizontal layout container for action buttons
        frame_buttons = tk.Frame(self)
        frame_buttons.pack(pady=15)

        btn_on = tk.Button(
            frame_buttons,
            text="TURN ON DEVICE",
            command=lambda: self._handle_action("on"),
            bg="#2980b9",
            fg="white",
            font=("Arial", 10, "bold"),
            relief="raised",
            cursor="hand2",
            padx=12,
            pady=6
        )
        btn_on.pack(side="left", padx=10)

        # REQUIREMENT 3: Added Turn Off button
        btn_off = tk.Button(
            frame_buttons,
            text="TURN OFF DEVICE",
            command=lambda: self._handle_action("off"),
            bg="#c0392b",
            fg="white",
            font=("Arial", 10, "bold"),
            relief="raised",
            cursor="hand2",
            padx=12,
            pady=6
        )
        btn_off.pack(side="left", padx=10)

        # Real-time Display Label
        self.lbl_output = tk.Label(
            self,
            text="Select a device above and use the buttons to interact.",
            font=("Arial", 10, "italic"),
            bg="#ecf0f1",
            fg="#34495e",
            relief="groove",
            height=3,
            wraplength=420,
            justify="center"
        )
        self.lbl_output.pack(fill="x", padx=20, pady=5)

        # REQUIREMENT 3: Activity Log (Listbox with scrollbar)
        log_frame = tk.LabelFrame(
            self,
            text=" Activity Log ",
            font=("Arial", 10, "bold"),
            padx=5,
            pady=5
        )
        log_frame.pack(fill="both", expand=True, padx=20, pady=15)

        scrollbar = tk.Scrollbar(log_frame)
        scrollbar.pack(side="right", fill="y")

        self.log_listbox = tk.Listbox(
            log_frame,
            font=("Courier", 10),
            yscrollcommand=scrollbar.set
        )
        self.log_listbox.pack(side="left", fill="both", expand=True)
        scrollbar.config(command=self.log_listbox.yview)

    def _handle_action(self, action_type: str):
        chosen_key = self.selected_key.get()
        active_device: SmartDevice = self.devices[chosen_key]
        
        # Polymorphic call matching the action type
        if action_type == "on":
            result_message = active_device.turn_on()
        else:
            result_message = active_device.turn_off()
            
        # Update main status display
        self.lbl_output.config(text=result_message, font=("Arial", 10, "normal"))
        
        # Append action details into the Activity Log Listbox and auto-scroll down
        self.log_listbox.insert(tk.END, result_message)
        self.log_listbox.yview(tk.END)


if __name__ == "__main__":
    app = SmartHomeApp()
    app.mainloop()
