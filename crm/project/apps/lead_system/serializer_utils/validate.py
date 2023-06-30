import ipaddress
import re

from ..models import Lead


def check_empty_fields(data: dict) -> tuple:
    result = {
        key: ['This field is required']
        for key, value in data.items()
        if not value
    }
    for key in ['name', 'email', 'phone', 'ip_address']:
        if not data.get(key):
            result[key] = ['This field is required']
    return (result, len(result) > 0) if len(result) > 0 else (data, False)


def check_email(data: str, emails: list) -> dict:
    email = re.match(r"^[\w.%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", (data := data.strip()))
    if not email:
        return {'email': ["This field must be a valid email address"]}
    if data in emails:
        return {'email': ["This email address is already exists"]}
    return {}


def check_phone(data: str, phones: list) -> dict:
    phone = re.fullmatch(r'^(?!.*(\d)\1{6})\d{8,}$', re.sub(r'\D', '', str(data)))
    phone = phone.group(0) if phone else None
    if not phone:
        return {'phone': ["This field must be a valid phone number"]}
    if str(data) in phones:
        return {'phone': ["This phone number is already exists"]}
    return {}


def check_ip(data: str) -> dict:
    try:
        ipaddress.ip_address(data)
        if Lead.objects.filter(ip_address=data).exists():
            return {'ip_address': ["This ip address is already exists"]}
        return {}
    except (ipaddress.AddressValueError, ValueError):
        return {'ip_address': ["This field must be a valid ip address"]}


def validate_fields(data: dict, leads) -> dict:
    return {
        **check_email(data['email'], leads['emails']),
        **check_phone(data['phone'], leads['phones']),
        **check_ip(data['ip_address'])
    }


def validator_lead(data: dict, leads: dict) -> tuple:
    data, have_error = check_empty_fields(data)
    if have_error:
        return data, have_error
    validate_errors = validate_fields(data, leads)
    return (validate_errors, len(validate_errors) > 0) if len(validate_errors) > 0 else (data, False)
