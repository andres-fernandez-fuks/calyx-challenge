from datetime import datetime


class DateHelper:
    @classmethod
    def now(cls):
        return datetime.now()

    @classmethod
    def get_full_month_from_date(cls, date=datetime.now()):
        months = [
            "enero",
            "febrero",
            "marzo",
            "abril",
            "mayo",
            "junio",
            "julio",
            "agosto",
            "septiembre",
            "octubre",
            "noviembre",
            "diciembre",
        ]
        return months[date.month - 1]

    @classmethod
    def format_date(cls, format, date=datetime.now()):
        return date.strftime(format)