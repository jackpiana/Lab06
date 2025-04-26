import flet as ft

class Controller:
    def __init__(self, view, model):
        self._lv = None
        self._retailer = None
        self._brand = None
        self._anno = None
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def fillAnni(self):
        anni = self._model.get_anni()
        self._view._dropdownAnno.options.append(ft.dropdown.Option(key=None,
                                                                   text="Nessun filtro",
                                                                   on_click=self.read_anno))
        for anno in anni:
            self._view._dropdownAnno.options.append(ft.dropdown.Option(key= anno,
                                                                       text=anno,
                                                                       data= anno,
                                                                       on_click=self.read_anno))

    def fillBrand(self):
        prodotti = self._model.get_products()
        usati = []
        self._view._dropdownBrand.options.append(ft.dropdown.Option(key=None,
                                                                   text="Nessun filtro",
                                                                   on_click=self.read_brand))
        for prodotto in prodotti:
            if prodotto.Product_brand not in usati:
                self._view._dropdownBrand.options.append(ft.dropdown.Option(key= prodotto.Product_brand,
                                                                            text=prodotto.Product_brand,
                                                                            data=prodotto.Product_brand,
                                                                            on_click=self.read_brand))
                usati.append(prodotto.Product_brand)

    def fillRetailer(self):
        reatilers = self._model.get_retailers()
        usati = []
        self._view._dropdownRetailer.options.append(ft.dropdown.Option(key=None,
                                                                   text="Nessun filtro",
                                                                    data= None,
                                                                   on_click=self.read_retailer))
        for retailer in reatilers:
            if retailer.code not in usati:
                self._view._dropdownRetailer.options.append(ft.dropdown.Option(key=retailer.code,
                                                                               text=retailer.name,
                                                                               data=retailer.code,
                                                                                on_click=self.read_retailer))
                usati.append(retailer.code)

    def read_retailer(self, e):
        self._retailer = e.control.data

    def read_anno(self, e):
        self._anno = e.control.data

    def read_brand(self, e):
        self._brand = e.control.data

    def top(self):
        parametri = (self._anno, self._retailer, self._brand)
        top5 = self._model.get_top(parametri)
        self._view.update_lvTop5(top5)

    def analisi(self):
        parametri = (self._anno, self._retailer, self._brand)
        analisi = self._model.analisi(self._model.get_vendite(parametri))
        self._view.print_analisi(analisi)



