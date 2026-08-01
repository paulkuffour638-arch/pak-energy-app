from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from screens import (
    HomeScreen,
    ToolsScreen,
    AboutScreen,
    PressureScreen,
    HydrostaticScreen,
    PorosityScreen,
    PermeabilityScreen,
    WaterCutScreen,
    DatabaseScreen,
    ReportScreen,
)


class PAKEnergyApp(App):

    def build(self):

        sm = ScreenManager()

        sm.add_widget(HomeScreen(name="home"))
        sm.add_widget(ToolsScreen(name="tools"))

        sm.add_widget(PressureScreen(name="pressure"))
        sm.add_widget(HydrostaticScreen(name="hydrostatic"))
        sm.add_widget(PorosityScreen(name="porosity"))
        sm.add_widget(PermeabilityScreen(name="permeability"))
        sm.add_widget(WaterCutScreen(name="watercut"))
        sm.add_widget(DatabaseScreen(name="database"))
        sm.add_widget(ReportScreen(name="report"))

        sm.add_widget(AboutScreen(name="about"))

        return sm


if __name__ == "__main__":
    PAKEnergyApp().run()