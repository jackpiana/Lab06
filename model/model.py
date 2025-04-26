from database.DAO import DAO

class Model:
    def __init__(self):
        pass
    def get_products(self):
        return DAO.get_products()
    def get_retailers(self):
        return DAO.get_retailers()
    def get_anni(self):
        return DAO.get_anni()
    def get_prodNums(self):
        return DAO.get_prodNums()
    def get_retailerCodes(self):
        return DAO.get_retailerCodes()
    def get_top(self, parametri):
        return DAO.get_top(parametri)
    def get_vendite(self, parametri):
        return DAO.get_vendite(parametri)

    def analisi(self, vendite):
        totRicavi = 0
        totRetailers = 0
        totProdotti = 0
        usatiRet = []
        usatiProd = []
        for vendita in vendite:
            totRicavi += vendita["Ricavo"]
            if vendita["Retailer_code"] not in usatiRet:
                totRetailers += 1
                usatiRet.append(vendita["Retailer_code"])
            if vendita["Product_number"] not in usatiProd:
                totProdotti += 1
                usatiProd.append(vendita["Product_number"])

        analisi = (f"Statistiche: \n"
                   f"Giro d'affari: {totRicavi}$\n"
                   f"Numero vendite: {len(vendite)}\n"
                   f"Numero retailers coinvolti: {totRetailers}\n"
                   f"Numero prodotti coinvolti: {totProdotti}\n")
        return analisi





