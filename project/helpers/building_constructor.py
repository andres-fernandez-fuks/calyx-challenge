from project.models.building import Building


class BuildingConstructor:
    """
    Clase borde, que conoce tanto el formato en el que entra el archivo como la clase Building de models
    Recibe los datos con el formato de entrada y los transforma a un objeto Building
    """

    TRANSLATOR = {
        "cod_loc": "location_code",
        "idprovincia": "province_id",
        "iddepartamento": "department_id",
        "categoria": "category",
        "provincia": "province",
        "localidad": "location",
        "nombre": "name",
        "direccion": "address",
        "cp": "zip_code",
        "telefono": "phone",
        "mail": "email",
        "web": "website",
    }

    INT_FIELDS = {"location_code", "province_id", "department_id"}

    @classmethod
    def clean_key(cls, key):
        return (
            key.lower()
            .replace("á", "a")
            .replace("é", "e")
            .replace("í", "i")
            .replace("ó", "o")
            .replace("ú", "u")
        )

    @classmethod
    def translate_key(cls, key):
        key = cls.clean_key(key)
        return cls.TRANSLATOR.get(key, key)

    @classmethod
    def convert_integer_fields(cls, building_data):
        for field in cls.INT_FIELDS:
            building_data[field] = int(building_data[field])

    @classmethod
    def is_building_field(cls, key):
        return cls.clean_key(key) in cls.TRANSLATOR

    @classmethod
    def create_building(cls, raw_building_data, building_type):
        building_data = cls.translate_keys(raw_building_data)
        cls.convert_integer_fields(building_data)
        building_data["category"] = building_type
        return Building(**building_data)

    @classmethod
    def translate_keys(cls, building_data):
        building_data = {
            cls.translate_key(key): value
            for key, value in building_data.items()
            if cls.is_building_field(key)
        }
        return building_data

