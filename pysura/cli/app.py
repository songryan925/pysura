from pysura.pysura_types.root_cmd import RootCmd
from pysura.cli.google_root import GoogleRoot


class App(RootCmd):

    def __init__(self, *arg, **kwargs):
        super().__init__(*arg, **kwargs)
        self.intro = "Welcome to Pysura! Type help or ? to list commands."
        self.prompt = "(pysura_cli) >>> "

    def do_choose_provider(self, _):
        """
        Launches the chosen provider's CLI
        """
        provider = self.collect("Please choose a provider: [google,]: ", ["google"])
        if provider == "google":
            GoogleRoot().cmdloop()
        else:
            print("Invalid provider")


def cli():
    App().cmdloop()