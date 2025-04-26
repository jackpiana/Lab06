import flet as ft

class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Lab06 - analisi vendite"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.txt_name = None
        self.btn_hello = None
        self.txt_result = None
        self.txt_container = None

        self._lv = None
        self._analisiTxt = None



    def load_interface(self):
        # title
        self._title = ft.Text("Analizza Vendite", color="blue", size=24)
        self._page.controls.append(self._title)

        #servono 3 menu drop down
        # ANNO BRAND RETAILER
        # 2 bottoni
        #TOP VENDITE, ANALIZZA

        self._dropdownAnno = ft.Dropdown(
            label= "Anno"
        )
        self._controller.fillAnni()

        self._dropdownBrand = ft.Dropdown(
            label="Brand"
        )
        self._controller.fillBrand()

        self._dropdownRetailer = ft.Dropdown(
                label= "Retailer"
                #options=
                #on_chenge=
            )
        self._controller.fillRetailer()


        row1 = ft.Row([self._dropdownAnno, self._dropdownBrand, self._dropdownRetailer], alignment=ft.MainAxisAlignment.CENTER)

        self._btnTop = ft.ElevatedButton(
            text="TOP VENDITE",
            on_click= lambda e: self._controller.top()
        )
        self._btnAnalisi = ft.ElevatedButton(
            text="ANALIZZA VENDITE",
            on_click= lambda e: self._controller.analisi()
        )

        row2 = ft.Row([self._btnTop, self._btnAnalisi], alignment=ft.MainAxisAlignment.CENTER)

        self._page.add(row1, row2)
        self._page.update()

    def update_lvTop5(self, top5):
        if self._analisiTxt is not None:
            self._page.controls.remove(self._analisiTxt)
            self._analisiTxt = None
        if self._lv is not None:
            self._page.controls.remove(self._lv)
            self._lv = None
        self._lv = ft.ListView(expand=True, spacing=10, padding=10)
        if not top5:
            self._lv.controls.append(ft.Text("Nessun dato trovato."))
        else:
            for sale in top5:
                self._lv.controls.append(ft.Text(f"Prodotto: {sale[3]} - Ricavo: {sale[1]}$ - Retailer: {sale[2]} - Data: {sale[0]}"))
        self._page.controls.append(self._lv)
        self._page.update()

    def print_analisi(self, analisi):
        if self._analisiTxt is not None:
            self._page.controls.remove(self._analisiTxt)
            self._analisiTxt = None
        self._analisiTxt = ft.Text(analisi)
        if self._lv is not None:
            self._page.controls.remove(self._lv)
            self._lv = None
        self._page.controls.append(self._analisiTxt)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
