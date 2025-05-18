from database.DB_connect import DBConnect
from model.arco import Border
from model.country import Country


class DAO():
    def __init__(self):
        pass


    @staticmethod
    def getNodes(year):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)

        res = []
        query = """SELECT co.StateAbb, co.CCode, co.StateNme
                from contiguity c, country co
                where c.`year` <= %s
                and c.state1no = co.CCode
                group by c.state1no ORDER BY StateAbb"""
        cursor.execute(query, (year,))

        for row in cursor:
            res.append(Country(**row))

        cursor.close()
        conn.close()
        return res

    @staticmethod
    def getEdges(idMap, year):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)

        res = []
        query = """select c.state1no , c.state2no 
                    from contiguity c 
                    where c.conttype = 1 and c.`year` <= %s"""
        cursor.execute(query, (year,))

        for row in cursor:
            res.append(Border(idMap[row['state1no']], idMap[row['state2no']]))

        cursor.close()
        conn.close()
        return res