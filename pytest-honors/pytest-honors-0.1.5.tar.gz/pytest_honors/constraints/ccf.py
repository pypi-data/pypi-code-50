"""
Define controls found in Adobe's Common Controls Framework.

Adobe released this framework
https://www.adobe.com/security/compliance.html

"""

from . import ConstraintsGroup

# https://blogs.adobe.com/security/2019/12/open-source-common-controls-framework-ccf-v3-0-now-available.html
# https://adobe.allegiancetech.com/cgi-bin/qwebcorporate.dll?idx=VM6HD7


class AssetManagementFamily(ConstraintsGroup):
    pass


DeviceAndMediaInventory
DeviceAndMediaTransportation
ComponentInstallationAndMaintenance


class BusinessContinuityFamily(ConstraintsGroup):
    pass

Business Continuity Planning
Capacity Management

class BackupManagementFamily(ConstraintsGroup):
    pass


class Backup(BackupManagementFamily):
    BackupConfiguration = (
        "[The organization] configures redundant systems or performs data backups [in accordance "
        "with the organization-defined frequency] to resume system operations in the event of a "
        "system failure."
    )
    ResilienceTesting = (
        "[The organization] performs backup restoration or failover tests [in accordance with the "
        "organization-defined frequency] to confirm the reliability and integrity of system "
        "backups or recovery operations."
    )
    AlternateStorage = (
        "[The organization] backups are securely stored in an alternate location from source data."
    )


class ConfigurationManagementFamily(ConstraintsGroup):
    pass

Baseline Configurations


class ChangeManagementFamily(ConstraintsGroup):
    pass
Change Management
Segregation of Duties
Change Communication


class DataManagementFamily(ConstraintsGroup):
    pass

Data Classification
Choice and Consent
Data Handling
Data Encryption
Data Storage
Data Integrity
Data Removal
Social Media


class EntityManagementFamily(ConstraintsGroup):
    pass

Board of Directors
Strategic Planning
Internal Audit Oversight
Information Security Oversight



class IdentityAndAccessManagementFamily(ConstraintsGroup):
    pass


Logical Access Account Lifecycle
Authentication
Authentication Maintenance
Role-Based Logical Access
Remote Access
End-user Authentication
Key Management
Key Storage and Distribution


class IncidentResponseFamily(ConstraintsGroup):
    pass

Incident Response
Incident Communication



class MobileDeviceManagementFamily(ConstraintsGroup):
    pass
Mobile Device Security


class NetworkOperationsFamily(ConstraintsGroup):
    pass

Perimeter Security
Network Segmentation
Wireless Security


class PeopleResourcesFamily(ConstraintsGroup):
    pass

On-boarding
Compliance
Business Ethics
Personnel Screening


class RiskManagementFamily(ConstraintsGroup):
    pass

Risk Assessment
Internal and External Audit
Controls Implementation


class SystemDesignDocumentationFamily(ConstraintsGroup):
    pass
Internal System Documentation
Customer-facing System Documentation

class SecurityGovernanceFamily(ConstraintsGroup):
    pass
Policy Governance
Security Documentation
Privacy Program
Privacy Documentation
Workforce Agreements
Information Security Management System


class ServiceLifecycleFamily(ConstraintsGroup):
    pass
Release Management
Source Code Management


class SystemsMonitoringFamily(ConstraintsGroup):
    pass
Logging
Security Monitoring
Availability Monitoring


class SiteOperationsFamily(ConstraintsGroup):
    pass
Physical Security
Physical Access Account Lifecycle
Environmental Security


class TrainingAndAwarenessFamily(ConstraintsGroup):
    pass
General Awareness Training
Role-Based Training


class ThirdPartyManagementFamily(ConstraintsGroup):
    pass

Vendor Assessments
Vendor Agreements
Vendor Procurement


class VulnerabilityManagementFamily(ConstraintsGroup):
    pass

Production Scanning
Penetration Testing
Patch Management
Malware Protection
Code Security
External Advisories and Inquiries
Program Management