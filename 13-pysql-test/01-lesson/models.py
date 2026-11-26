class City:
    def __init__(self, city_id, name, country_code, district, population):
        self.id = city_id
        self.name = name
        self.country_code = country_code
        self.district = district
        self.population = population

    @staticmethod
    def clean_name(value):
        name = value.strip()
        if not 1 <= len(name) <= 35:
            raise ValueError("Use 1 to 35 characters.")
        return name

    @staticmethod
    def clean_country_code(value):
        country_code = value.strip().upper()
        if (
            len(country_code) != 3
            or not country_code.isascii()
            or not country_code.isalpha()
        ):
            raise ValueError("Use exactly 3 ASCII letters.")

        return country_code

    @staticmethod
    def clean_district(value):
        district = value.strip()
        if not len(district) <= 20:
            raise ValueError("Maximum 20 characters allowed.")
        return district

    @staticmethod
    def clean_population(value):
        population = int(value)
        if not population >= 0:
            raise ValueError("Population must be a non-negative integer.")
        return population
