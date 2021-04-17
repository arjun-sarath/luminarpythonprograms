class Pycharm:
    def open(self):
        print("open method in pycharm")

    def run(self):
        print("run method in pycharm")

    def debug(self):
        print("debug method in pycharm")


class Vscode:
    def open(self):
        print("open method in vscode")

    def run(self):
        print("run method in vscode")

    def debug(self):
        print("debug method in vscode")


class Programmer:
    def coding(self, ide):
        ide.open()
        ide.run()
        ide.debug()

py = Pycharm()
vs = Vscode()
pg = Programmer()
# pg.coding(py)
pg.coding(vs)
