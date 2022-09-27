from small_table import SmallTable
from medium_table import MediumTable
from big_table import BigTable

class TableFactory:

    @staticmethod
    def get_table(table):

        try:
            if table == 'BigTable':
                return BigTable()
            if table == 'MediumTable':
                return MediumTable()
            if table == 'SmallTable':
                return SmallTable()

            raise Exception('Table Not Found')
        except Exception as _e:
            print(_e)
        return None