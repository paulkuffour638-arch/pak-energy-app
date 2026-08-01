from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from pdf_report import generate_report

from calculators import (
    calculate_pressure,
    calculate_hydrostatic,
    calculate_porosity,
    calculate_permeability,
    calculate_water_cut
)

from database import save_record


# ---------------------------------------------------------
# HOME SCREEN
# ---------------------------------------------------------

class HomeScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(
            orientation="vertical",
            spacing=20,
            padding=20
        )

        logo = Image(
            source="pak_logo.png",
            size_hint=(1, 0.5)
        )

        title = Label(
            text="PAK ENERGY & TECH HUB",
            font_size=28,
            bold=True
        )

        welcome = Label(
            text="Petroleum Engineering Toolkit",
            font_size=18
        )

        start = Button(
            text="START",
            size_hint=(1, 0.2)
        )

        start.bind(
            on_press=self.open_tools
        )

        layout.add_widget(logo)
        layout.add_widget(title)
        layout.add_widget(welcome)
        layout.add_widget(start)

        self.add_widget(layout)


    def open_tools(self, instance):
        self.manager.current = "tools"


# ---------------------------------------------------------
# TOOLS SCREEN (DASHBOARD)
# ---------------------------------------------------------

class ToolsScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(
            orientation="vertical",
            spacing=10,
            padding=20
        )

        title = Label(
            text="ENGINEERING TOOLS DASHBOARD",
            font_size=24,
            bold=True
        )

        layout.add_widget(title)

        tools = [
            ("Pressure Calculator", "pressure"),
            ("Hydrostatic Pressure", "hydrostatic"),
            ("Porosity Calculator", "porosity"),
            ("Permeability Calculator", "permeability"),
            ("Water Cut Calculator", "watercut"),
            ("Reservoir Database", "database"),
            ("Generate PDF Report", "report"),
            ("About", "about")
        ]

        for text, screen_name in tools:

            button = Button(
                text=text,
                size_hint=(1, 0.1)
            )

            button.bind(
                on_press=lambda instance, s=screen_name:
                self.change_screen(s)
            )

            layout.add_widget(button)

        self.add_widget(layout)


    def change_screen(self, screen_name):
        self.manager.current = screen_name


# ---------------------------------------------------------
# ABOUT SCREEN
# ---------------------------------------------------------

class AboutScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(
            orientation="vertical",
            padding=20
        )

        text = Label(
            text=
            "PAK ENERGY & TECH HUB\n\n"
            "Petroleum Engineering Mobile Toolkit\n\n"
            "Version 1.0\n"
            "Developed by Paul",
            font_size=20
        )

        back = Button(
            text="Back Home",
            size_hint=(1, 0.2)
        )

        back.bind(
            on_press=self.go_back
        )

        layout.add_widget(text)
        layout.add_widget(back)

        self.add_widget(layout)


    def go_back(self, instance):
        self.manager.current = "home"


# ---------------------------------------------------------
# BASE CLASS FOR ALL CALCULATOR SCREENS
# ---------------------------------------------------------

class BaseCalculatorScreen(Screen):

    def create_back_button(self):

        back = Button(
            text="Back to Tools",
            size_hint=(1, 0.15)
        )

        back.bind(
            on_press=self.go_back
        )

        return back


    def go_back(self, instance):
        self.manager.current = "tools"


# ---------------------------------------------------------
# PRESSURE CALCULATOR
# ---------------------------------------------------------

class PressureScreen(BaseCalculatorScreen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(
            orientation="vertical",
            spacing=10,
            padding=20
        )

        layout.add_widget(
            Label(
                text="Pressure Calculator",
                font_size=24
            )
        )

        self.force = TextInput(
            hint_text="Force (N)",
            multiline=False
        )

        self.area = TextInput(
            hint_text="Area (m²)",
            multiline=False
        )

        button = Button(text="Calculate")
        button.bind(on_press=self.calculate)

        self.result = Label(text="Result")

        layout.add_widget(self.force)
        layout.add_widget(self.area)
        layout.add_widget(button)
        layout.add_widget(self.result)
        layout.add_widget(self.create_back_button())

        self.add_widget(layout)


    def calculate(self, instance):

        self.result.text = calculate_pressure(
            self.force.text,
            self.area.text
        )


# ---------------------------------------------------------
# HYDROSTATIC PRESSURE CALCULATOR
# ---------------------------------------------------------

class HydrostaticScreen(BaseCalculatorScreen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(
            orientation="vertical",
            spacing=10,
            padding=20
        )

        layout.add_widget(
            Label(
                text="Hydrostatic Pressure Calculator",
                font_size=22
            )
        )

        self.density = TextInput(
            hint_text="Density kg/m³",
            multiline=False
        )

        self.depth = TextInput(
            hint_text="Depth (m)",
            multiline=False
        )

        button = Button(text="Calculate")
        button.bind(on_press=self.calculate)

        self.result = Label(text="Result")

        layout.add_widget(self.density)
        layout.add_widget(self.depth)
        layout.add_widget(button)
        layout.add_widget(self.result)
        layout.add_widget(self.create_back_button())

        self.add_widget(layout)


    def calculate(self, instance):

        self.result.text = calculate_hydrostatic(
            self.density.text,
            self.depth.text
        )


# ---------------------------------------------------------
# POROSITY CALCULATOR
# ---------------------------------------------------------

class PorosityScreen(BaseCalculatorScreen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(
            orientation="vertical",
            spacing=10,
            padding=20
        )

        layout.add_widget(
            Label(
                text="Porosity Calculator",
                font_size=24
            )
        )

        self.pore = TextInput(
            hint_text="Pore Volume",
            multiline=False
        )

        self.bulk = TextInput(
            hint_text="Bulk Volume",
            multiline=False
        )

        button = Button(text="Calculate")
        button.bind(on_press=self.calculate)

        self.result = Label(text="Result")

        layout.add_widget(self.pore)
        layout.add_widget(self.bulk)
        layout.add_widget(button)
        layout.add_widget(self.result)
        layout.add_widget(self.create_back_button())

        self.add_widget(layout)


    def calculate(self, instance):

        self.result.text = calculate_porosity(
            self.pore.text,
            self.bulk.text
        )


# ---------------------------------------------------------
# PERMEABILITY CALCULATOR
# ---------------------------------------------------------

class PermeabilityScreen(BaseCalculatorScreen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(
            orientation="vertical",
            spacing=10,
            padding=20
        )

        layout.add_widget(
            Label(
                text="Permeability Calculator",
                font_size=24
            )
        )

        self.flow = TextInput(
            hint_text="Flow Rate",
            multiline=False
        )

        self.pressure = TextInput(
            hint_text="Pressure Difference",
            multiline=False
        )

        button = Button(text="Calculate")
        button.bind(on_press=self.calculate)

        self.result = Label(text="Result")

        layout.add_widget(self.flow)
        layout.add_widget(self.pressure)
        layout.add_widget(button)
        layout.add_widget(self.result)
        layout.add_widget(self.create_back_button())

        self.add_widget(layout)


    def calculate(self, instance):

        self.result.text = calculate_permeability(
            self.flow.text,
            self.pressure.text
        )


# ---------------------------------------------------------
# WATER CUT CALCULATOR
# ---------------------------------------------------------

class WaterCutScreen(BaseCalculatorScreen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(
            orientation="vertical",
            spacing=10,
            padding=20
        )

        layout.add_widget(
            Label(
                text="Water Cut Calculator",
                font_size=24
            )
        )

        self.water = TextInput(
            hint_text="Water Production",
            multiline=False
        )

        self.total = TextInput(
            hint_text="Total Production",
            multiline=False
        )

        button = Button(text="Calculate")
        button.bind(on_press=self.calculate)

        self.result = Label(text="Result")

        layout.add_widget(self.water)
        layout.add_widget(self.total)
        layout.add_widget(button)
        layout.add_widget(self.result)
        layout.add_widget(self.create_back_button())

        self.add_widget(layout)


    def calculate(self, instance):

        self.result.text = calculate_water_cut(
            self.water.text,
            self.total.text
        )


# ---------------------------------------------------------
# RESERVOIR DATABASE SCREEN
# ---------------------------------------------------------

class DatabaseScreen(BaseCalculatorScreen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(
            orientation="vertical",
            spacing=10,
            padding=20
        )

        layout.add_widget(
            Label(
                text="Reservoir Database",
                font_size=24
            )
        )

        self.record = TextInput(
            hint_text="Enter reservoir information",
            multiline=True
        )

        save = Button(
            text="Save Record"
        )

        save.bind(
            on_press=self.save_data
        )

        self.result = Label(
            text=""
        )

        layout.add_widget(self.record)
        layout.add_widget(save)
        layout.add_widget(self.result)
        layout.add_widget(self.create_back_button())

        self.add_widget(layout)


    def save_data(self, instance):

        message = save_record(
            self.record.text
        )

        self.result.text = message
        # ---------------------------------------------------------
# PDF REPORT SCREEN
# ---------------------------------------------------------

class ReportScreen(BaseCalculatorScreen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(
            orientation="vertical",
            spacing=10,
            padding=20
        )

        layout.add_widget(
            Label(
                text="Generate PDF Report",
                font_size=24
            )
        )

        self.title_input = TextInput(
            hint_text="Report Title",
            multiline=False
        )

        self.content_input = TextInput(
            hint_text="Report Content",
            multiline=True
        )

        button = Button(text="Create PDF")
        button.bind(on_press=self.create_pdf)

        self.result = Label(text="")

        layout.add_widget(self.title_input)
        layout.add_widget(self.content_input)
        layout.add_widget(button)
        layout.add_widget(self.result)
        layout.add_widget(self.create_back_button())

        self.add_widget(layout)


    def create_pdf(self, instance):

        message = generate_report(
            self.title_input.text,
            self.content_input.text
        )

        self.result.text = message