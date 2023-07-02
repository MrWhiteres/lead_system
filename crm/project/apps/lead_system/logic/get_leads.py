from .. import models
from ..security.encryption import decrypt


def get_all_leads() -> dict:
    all_leads = models.Lead.objects.all()
    return {
        'phones': [decrypt(lead.phone, lead.leadsettings.phone) for lead in all_leads],
        'emails': [decrypt(lead.email, lead.leadsettings.email) for lead in all_leads],
    }
