from project.models.total import Total


class TotalConstructor:
    """
    Recibe una lista de longitud n y la transforma en un objeto Total
    """
    @classmethod
    def create_total(cls, raw_total, category_name):
        category = category_name + "_" + ("_").join(raw_total[:-1])
        value = raw_total[-1]
        return Total(category=category, value=value)

