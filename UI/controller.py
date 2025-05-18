import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self.statoScelto = None

    def handleCalcola(self, e):
        anno = self._view._txtAnno.value

        try:
            year = int(anno)
        except ValueError:
            self._view._txt_result.controls.clear()
            self._view._txt_result.controls.append(ft.Text("Attenzione! Inserire un valore numerico", color='red'))
            self._view.update_page()
            return

        if year < 1816 or year > 2016:
            self._view._txt_result.controls.clear()
            self._view._txt_result.controls.append(ft.Text("Attenzione! Inserire un anno compreso nell'intervallo 1816 - 2016", color='red'))
            self._view.update_page()
            return

        self._model.buildGraph(year)
        self._view._txt_result.controls.clear()
        self._view._txt_result.controls.append(ft.Text("Grafo correttamente creato"))
        self._view._txt_result.controls.append(ft.Text(f"Il grafo ha {self._model.infoCompConnessa()} componenti connesse"))
        self._view._txt_result.controls.append(ft.Text("Di seguito le info sui paesi confinanti per ogni stato:"))
        for n in self._model.getNodes():
            self._view._txt_result.controls.append(ft.Text(f"{n} -- {self._model.getNumConfini(n)} vicini."))

        self._view._ddStato.disabled = False
        self._view._btnRaggiungibili.disabled = False
        self.fillDD()
        self._view.update_page()


    def fillDD(self):
        stati = self._model.getNodes()

        for s in stati:
            self._view._ddStato.options.append(ft.dropdown.Option(s.StateNme,
                                                                  data=s,
                                                                  on_click=self.readStati))

    def readStati(self,e):
        print("Stato called")
        if e.control.data is None:
            self.statoScelto = None
        else:
            self.statoScelto = e.control.data
        print(self.statoScelto)



    def handleRaggiungibili(self, e):
        raggiungibili = self._model.getRaggiungibili(self.statoScelto)
        self._view._txt_result.controls.clear()
        self._view._txt_result.controls.append(ft.Text(f"Dallo stato {self.statoScelto} è possibile raggiungere a piedi {len(raggiungibili)} stati"))
        self._view._txt_result.controls.append(ft.Text("Di seguito la lista degli stati raggiungibili:"))
        for n in raggiungibili:
            self._view._txt_result.controls.append(ft.Text(f"{n}"))
        self._view.update_page()