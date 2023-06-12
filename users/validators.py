import datetime

from jsonschema.exceptions import ValidationError


class AgeValidator:
    def __init__(self, min_reg_age):
        self.today = datetime.date.today()
        self.min_reg_age = min_reg_age
    def __call__(self, value):
        age = (self.today.year - value.year - 1) + ((self.today.month, self.today.day) >= (value.month, value.day))
        if age <= self.min_reg_age:
            raise ValidationError(f'ваш возраст {age} слишком мал для регистрации!')


class EmailDomainValidator:
    def __init__(self, forbidden_domains):
        self.forbidden_domains = forbidden_domains

    def __call__(self, value):
        domain = value.split('@')[-1]
        if domain in self.forbidden_domains:
            raise ValidationError(f'регистрация с почтового домена {domain} запрещена!')
