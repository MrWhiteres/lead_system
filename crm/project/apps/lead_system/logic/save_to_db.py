from django.db.models import Model

from .dataclass_lead import LeadDataclass
from ..models import Lead, LeadSettings
from ..security.encryption import generate_key, encrypt


def save_lead_to_db(data: dict) -> dict:
    for lead in data['leads']:
        lead = LeadDataclass(**lead)
        email_key, email = encrypt_data(lead.email)
        phone_key, phone = encrypt_data(lead.phone)
        lead = create_model(
            Lead,
            dict(name=lead.name, email=email, phone=phone, ip_address=lead.ip_address)
        )
        create_model(LeadSettings, dict(lead=lead, email=email_key, phone=phone_key))
    return dict(new_leads=len(data['leads']))


def create_model(model: Model, data: dict) -> Model:
    model = model.objects.create(**data)
    model.save()
    return model


def encrypt_data(field: str) -> tuple:
    key = generate_key()
    return key, encrypt(str(field), key)
