from dataclasses import dataclass


@dataclass
class LeadDataclass:
    name: str
    email: str
    phone: str
    ip_address: str
