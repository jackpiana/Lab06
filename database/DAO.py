from database.DB_connect import DBConnect
from model.Product import Product
from model.Retailer import Retailer


class DAO():
    @staticmethod
    def get_products():
        conn = DBConnect.get_connection()
        prodotti = []
        if conn is None:
            print("Connection failed")
        else:
            cursor = conn.cursor(dictionary=True)
            query = """SELECT *
                        FROM go_products
                        order by Product_brand
                        """
            cursor.execute(query)
            for row in cursor:
                prodotti.append(Product(**row))  #**row è un operatore di unpacking (espansione) di un dizionario. nb: serve che tutti i nomi degli attributi combacino
            cursor.close()
            conn.close()
        return prodotti

    @staticmethod
    def get_retailers():
        conn = DBConnect.get_connection()
        retailers = []
        if conn is None:
            print("Connection failed")
        else:
            cursor = conn.cursor(dictionary=True)
            query = """SELECT *
                        FROM go_retailers
                        order by Retailer_name
                        """
            cursor.execute(query)
            retailers_dizs = cursor.fetchall()
            for ret in retailers_dizs:
                retailers.append(Retailer(ret["Retailer_code"],
                                          ret["Retailer_name"],
                                          ret["Type"],
                                          ret["Country"]))   #ocio alle maiuscole dio cane

            cursor.close()
            conn.close()
        return retailers

    @staticmethod
    def get_anni():
        conn = DBConnect.get_connection()
        anni = []
        if conn is None:
            print("Connection failed")
        else:
            cursor = conn.cursor()
            query = """select distinct year(date)
                    from go_daily_sales  """
            cursor.execute(query)
            for anno in cursor:
                anni.append(anno[0])
            cursor.close()
            conn.close()
        return anni

    @staticmethod
    def get_prodNums():
        conn = DBConnect.get_connection()
        prodNum = []
        if conn is None:
            print("Connection failed")
        else:
            cursor = conn.cursor(dictionary=True)
            query = """SELECT Product_number 
                        FROM go_products"""
            cursor.execute(query)
            nums = cursor.fetchall()
            for num in nums:
                prodNum.append(num['Product_number'])
            cursor.close()
            conn.close()
        return prodNum

#in questo metodo non ho usato dictionary=True, ho lavorato con la tupla
    @staticmethod
    def get_retailerCodes():
        conn = DBConnect.get_connection()
        codes = []
        if conn is None:
            print("Connection failed")
        else:
            cursor = conn.cursor()
            query = """SELECT Retailer_code 
                        FROM go_retailers"""
            cursor.execute(query)
            res = cursor.fetchall()
            for code in res:
                codes.append(code[0])
            cursor.close()
            conn.close()
        return codes

    @staticmethod
    def get_top(parametri):
        anno = parametri[0]
        retailer = parametri[1]
        brand = parametri[2]
        params = []
        conn = DBConnect.get_connection()
        if conn is None:
            print("Connection failed")
            return []
        else:
            cursor = conn.cursor()
            query = """select `Date`, Quantity*Unit_sale_price as Ricavo, Retailer_code, gds.Product_number 
                        from go_daily_sales gds 
                        join go_products gp on gds.Product_number = gp.Product_number
                        where 1=1
                        """
            if anno is not None:
                query += "and YEAR(gds.Date) = %s\n"
                params.append(anno)
            if retailer is not None:
                query += "and gds.Retailer_code = %s\n"
                params.append(retailer)
            if brand is not None:
                query += "and Product_brand= %s\n"
                params.append(brand)
            query += "order by Ricavo desc\nlimit 5"
            cursor.execute(query, params)
            top5 = cursor.fetchall()
            cursor.close()
            conn.close()
        return top5

    @staticmethod
    def get_vendite(parametri):
        anno = parametri[0]
        retailer = parametri[1]
        brand = parametri[2]
        conn = DBConnect.get_connection()
        if conn is None:
            print("Connection failed")
            return []
        else:
            cursor = conn.cursor(dictionary=True)
            query = """SELECT `Date`, Quantity * Unit_sale_price AS Ricavo, Retailer_code, gds.Product_number
                        FROM go_daily_sales gds
                        JOIN go_products gp ON gds.Product_number = gp.Product_number
                        WHERE YEAR(gds.Date) = COALESCE(%s, YEAR(gds.Date))
                        AND gds.Retailer_code = COALESCE(%s, gds.Retailer_code)
                        AND Product_brand = COALESCE(%s, Product_brand)
                        ORDER BY Ricavo DESC
                        LIMIT 5
                        """

            """
            WHERE product_number = COALESCE(%s, product_number)
            vuol dire:
            Se %s ha un valore (cioè NON è NULL), confronta product_number = valore.
            **Se %s è NULL**, allora confronta product_number = product_number`, cioè sempre vero.
            """

            cursor.execute(query, (anno, retailer, brand))
            vendite = cursor.fetchall()
            cursor.close()
            conn.close()
        return vendite

#se faccio runnare questo file .py entro nella clausola if UTILE PER TESTING
if __name__ == "__main__":
    for j in DAO.get_top((2015, 1213, "Alpha")):
        print(j)

"""""
select `Date`, Quantity*Unit_sale_price as Ricavo, Retailer_code, gds.Product_number
                        from go_daily_sales gds
                        join go_products gp on gds.Product_number = gp.Product_number
                        where YEAR(gds.Date) = %s
                        and gds.Retailer_code = %s
                        and Product_brand= %s
                        order by Ricavo desc
                        limit 5
                        

query = select Quantity*Unit_sale_price as Ricavo, Retailer_code, gds.Product_number 
            from go_daily_sales gds 
            join go_products gp on gds.Product_number = gp.Product_number
            where 1=1
            if anno is not None:
                query += "and YEAR(gds.Date) = %s\n"
                params.append(anno)
            if retailer is not None:
                query += "and gds.Retailer_code = %s\n"
                params.append(retailer)
            if brand is not None:
                query += "and Product_brand= %s\n"
                params.append(brand)
"""""




