"""
ClientComms — Client Communication Agent

Domain: Client-facing communication
Risk tier: Low (draft generation; human review for non-routine communications)

Generates proactive, personalized case status communications:
- Automatic status update drafts triggered by case milestones
- Intelligent calibration to client communication preferences
- Exception notifications (human authorization required)
- Portfolio summary reports
- UP-specific communications
- White-label communication support for partner firms
"""

from dataclasses import dataclass, field
from typing import Optional, List, Dict, Any
from enum import Enum
from datetime import datetime
import logging

logger = logging.getLogger(__name__)


class CommunicationFrequency(Enum):
    """Client communication preference frequency."""
    EXCEPTION_ONLY = "exception_only"
    WEEKLY = "weekly"
    AT_MILESTONE = "at_milestone"
    DETAILED = "detailed"


class CaseMilestone(Enum):
    """Case processing milestones."""
    INSTRUCTION_RECEIVED = "instruction_received"
    TRANSLATION_ASSIGNED = "translation_assigned"
    TRANSLATION_COMPLETE = "translation_complete"
    FILED_STATE = "filed_state"
    FILING_CONFIRMED = "filing_confirmed"
    CERTIFICATE_RECEIVED = "certificate_received"
    UP_REGISTERED = "up_registered"
    CASE_COMPLETE = "case_complete"


@dataclass
class ClientPreferences:
    """Client communication preferences."""
    client_id: str
    client_name: str
    is_white_label_client: bool
    white_label_firm_name: Optional[str] = None
    white_label_firm_tone: Optional[str] = None  # "formal", "casual", "technical"
    communication_frequency: CommunicationFrequency = CommunicationFrequency.AT_MILESTONE
    contact_email: str = ""
    contact_name: str = ""
    preferred_language: str = "en"
    include_portfolio_analytics: bool = False
    up_specific_notifications: bool = False


@dataclass
class CommunicationDraft:
    """Draft communication to client."""
    draft_id: str
    client_id: str
    case_id: str
    communication_type: str  # "milestone_update", "exception", "portfolio_report"
    subject: str
    body: str
    is_white_label: bool = False
    white_label_firm_name: Optional[str] = None
    requires_approval: bool = True
    approval_status: str = "pending"  # pending, approved, rejected, sent
    created_date: datetime = field(default_factory=datetime.now)
    approved_date: Optional[datetime] = None
    sent_date: Optional[datetime] = None
    recipient_email: str = ""


@dataclass
class ExceptionNotification:
    """Exception notification for client."""
    notification_id: str
    case_id: str
    client_id: str
    exception_type: str  # "deadline_risk", "translation_delay", "filing_error"
    severity: str  # "warning", "alert", "critical"
    description: str
    recommended_action: str
    requires_client_action: bool


class ClientComms:
    """
    Client Communication Agent.
    
    Generates and manages proactive, personalized client communications
    across case milestones, exceptions, and portfolio events.
    """
    
    def __init__(self):
        """Initialize ClientComms agent."""
        self.client_preferences: Dict[str, ClientPreferences] = {}
        self.communication_templates: Dict[str, str] = {}
        self.drafts: Dict[str, CommunicationDraft] = {}
        self.sent_communications: List[CommunicationDraft] = []
        
        # Load default templates
        self._load_default_templates()
    
    def register_client(self, preferences: ClientPreferences) -> bool:
        """Register client communication preferences."""
        try:
            self.client_preferences[preferences.client_id] = preferences
            logger.info(f"Registered client preferences for {preferences.client_name}")
            return True
        except Exception as e:
            logger.error(f"Error registering client: {str(e)}")
            return False
    
    def _load_default_templates(self) -> None:
        """Load default communication templates."""
        self.communication_templates = {
            "instruction_received": """
Dear {client_name},

Thank you for your patent validation instruction. We confirm receipt of your request for EP patent {ep_number}.

Case Reference: {case_id}
Filing Deadline: {filing_deadline}

Our team is now processing your application. We will keep you updated at each major milestone.

Best regards,
IP Centrum Team
""",
            "translation_assigned": """
Dear {client_name},

Your patent translation has been assigned to our specialist in {technical_domain}.

Translator: {translator_name}
Expected Delivery: {expected_delivery_date}
Language Pair: {source_language} → {target_language}

Best regards,
IP Centrum Team
""",
            "translation_complete": """
Dear {client_name},

We're pleased to inform you that the translation for your patent {ep_number} has been completed and approved.

Next Step: Filing with national agent
Filing Deadline: {filing_deadline}

Best regards,
IP Centrum Team
""",
            "filed_state": """
Dear {client_name},

Your patent validation has been successfully filed in {jurisdiction}.

Filing Number: {filing_number}
Filing Date: {filing_date}
Expected Confirmation: {confirmation_date}

Best regards,
IP Centrum Team
""",
            "exception_alert": """
Dear {client_name},

We need to alert you to the following issue with your patent validation case {case_id}:

Issue: {exception_description}
Impact: {impact_description}
Action Required: {recommended_action}

Please respond within 48 hours to ensure we can proceed as planned.

Best regards,
IP Centrum Team
""",
        }
    
    def generate_milestone_communication(
        self,
        case_id: str,
        ep_number: str,
        client_id: str,
        milestone: CaseMilestone,
        case_data: Dict[str, Any]
    ) -> Optional[CommunicationDraft]:
        """
        Generate a milestone communication for the client.
        
        Args:
            case_id: Case ID
            ep_number: EP patent number
            client_id: Client ID
            milestone: Milestone type
            case_data: Case information dictionary
            
        Returns:
            CommunicationDraft or None
        """
        try:
            client_prefs = self.client_preferences.get(client_id)
            if not client_prefs:
                logger.warning(f"No client preferences found for {client_id}")
                return None
            
            # Check communication frequency
            if client_prefs.communication_frequency == CommunicationFrequency.EXCEPTION_ONLY:
                logger.info(f"Skipping milestone communication for {client_id} (exception-only preference)")
                return None
            
            # Select template
            template_key = milestone.value
            template = self.communication_templates.get(template_key, "")
            
            if not template:
                logger.warning(f"No template found for milestone {milestone.value}")
                return None
            
            # Build context for template substitution
            context = {
                "client_name": client_prefs.contact_name or client_prefs.client_name,
                "ep_number": ep_number,
                "case_id": case_id,
                "filing_deadline": case_data.get("filing_deadline", "TBD"),
                "technical_domain": case_data.get("technical_domain", "patent"),
                "translator_name": case_data.get("translator_name", "specialist"),
                "expected_delivery_date": case_data.get("expected_delivery_date", "TBD"),
                "source_language": case_data.get("source_language", "EN"),
                "target_language": case_data.get("target_language", "TBD"),
                "jurisdiction": case_data.get("jurisdiction", "TBD"),
                "filing_number": case_data.get("filing_number", "TBD"),
                "filing_date": case_data.get("filing_date", "TBD"),
                "confirmation_date": case_data.get("confirmation_date", "TBD"),
            }
            
            # Substitute template variables
            body = template
            for key, value in context.items():
                placeholder = "{" + key + "}"
                body = body.replace(placeholder, str(value))
            
            # Handle white-label formatting
            subject = f"Patent Validation Update: {ep_number}"
            if client_prefs.is_white_label_client and client_prefs.white_label_firm_name:
                subject = f"{client_prefs.white_label_firm_name}: Patent Validation Update"
            
            # Create draft
            draft = CommunicationDraft(
                draft_id=f"DRAFT_{case_id}_{milestone.value}_{datetime.now().timestamp()}",
                client_id=client_id,
                case_id=case_id,
                communication_type="milestone_update",
                subject=subject,
                body=body,
                is_white_label=client_prefs.is_white_label_client,
                white_label_firm_name=client_prefs.white_label_firm_name,
                requires_approval=False,  # Templated communications don't require approval
                recipient_email=client_prefs.contact_email,
            )
            
            self.drafts[draft.draft_id] = draft
            logger.info(f"Generated milestone communication: {draft.draft_id}")
            
            return draft
            
        except Exception as e:
            logger.error(f"Error generating milestone communication: {str(e)}")
            return None
    
    def generate_exception_notification(
        self,
        case_id: str,
        client_id: str,
        exception_type: str,
        severity: str,
        description: str,
        recommended_action: str,
        requires_client_action: bool = False
    ) -> Optional[CommunicationDraft]:
        """
        Generate an exception notification for the client.
        
        Args:
            case_id: Case ID
            client_id: Client ID
            exception_type: Type of exception
            severity: Severity level
            description: Exception description
            recommended_action: Recommended action
            requires_client_action: Whether client needs to take action
            
        Returns:
            CommunicationDraft or None
        """
        try:
            client_prefs = self.client_preferences.get(client_id)
            if not client_prefs:
                logger.warning(f"No client preferences found for {client_id}")
                return None
            
            # Build exception notification email
            subject = f"ACTION REQUIRED: Issue with case {case_id}"
            if severity == "critical":
                subject = f"URGENT: Critical issue with case {case_id}"
            
            body = f"""
Dear {client_prefs.contact_name or client_prefs.client_name},

We are writing to alert you to the following issue with your patent validation case {case_id}:

Issue Type: {exception_type}
Severity: {severity.upper()}
Description: {description}

Recommended Action: {recommended_action}

{'PLEASE RESPOND WITHIN 48 HOURS to help us resolve this issue.' if requires_client_action else 'We are actively working to resolve this matter.'}

If you have any questions, please contact us immediately.

Best regards,
IP Centrum Team
"""
            
            # Create draft - always requires approval for exceptions
            draft = CommunicationDraft(
                draft_id=f"DRAFT_EXC_{case_id}_{datetime.now().timestamp()}",
                client_id=client_id,
                case_id=case_id,
                communication_type="exception",
                subject=subject,
                body=body,
                is_white_label=client_prefs.is_white_label_client,
                white_label_firm_name=client_prefs.white_label_firm_name,
                requires_approval=True,  # Always requires approval
                recipient_email=client_prefs.contact_email,
            )
            
            self.drafts[draft.draft_id] = draft
            logger.info(f"Generated exception notification: {draft.draft_id}")
            
            return draft
            
        except Exception as e:
            logger.error(f"Error generating exception notification: {str(e)}")
            return None
    
    def approve_draft(self, draft_id: str) -> bool:
        """
        Approve a communication draft.
        
        Args:
            draft_id: Draft ID
            
        Returns:
            True if approved successfully
        """
        try:
            draft = self.drafts.get(draft_id)
            if not draft:
                logger.error(f"Draft {draft_id} not found")
                return False
            
            draft.approval_status = "approved"
            draft.approved_date = datetime.now()
            logger.info(f"Approved draft {draft_id}")
            return True
            
        except Exception as e:
            logger.error(f"Error approving draft: {str(e)}")
            return False
    
    def send_draft(self, draft_id: str) -> bool:
        """
        Send an approved communication draft to client.
        
        Args:
            draft_id: Draft ID
            
        Returns:
            True if sent successfully
        """
        try:
            draft = self.drafts.get(draft_id)
            if not draft:
                logger.error(f"Draft {draft_id} not found")
                return False
            
            if draft.approval_status != "approved":
                logger.error(f"Cannot send unapproved draft {draft_id}")
                return False
            
            # Mock: would send email via SMTP
            draft.approval_status = "sent"
            draft.sent_date = datetime.now()
            
            self.sent_communications.append(draft)
            logger.info(f"Sent communication {draft_id} to {draft.recipient_email}")
            
            return True
            
        except Exception as e:
            logger.error(f"Error sending draft: {str(e)}")
            return False
    
    def get_pending_approvals(self) -> List[CommunicationDraft]:
        """Get communications pending approval."""
        return [d for d in self.drafts.values() if d.approval_status == "pending"]


# Example usage
if __name__ == "__main__":
    agent = ClientComms()
    
    # Register client
    client = ClientPreferences(
        client_id="CLIENT_001",
        client_name="Acme Corporation",
        is_white_label_client=False,
        communication_frequency=CommunicationFrequency.AT_MILESTONE,
        contact_email="ip@acmecorp.com",
        contact_name="John Smith",
    )
    agent.register_client(client)
    
    # Generate milestone communication
    draft = agent.generate_milestone_communication(
        case_id="CASE_001",
        ep_number="EP2123456",
        client_id="CLIENT_001",
        milestone=CaseMilestone.INSTRUCTION_RECEIVED,
        case_data={
            "filing_deadline": "2025-12-15",
            "technical_domain": "software"
        }
    )
    
    if draft:
        print(f"Draft: {draft.draft_id}")
        print(f"Subject: {draft.subject}")
        print(f"Body preview: {draft.body[:100]}...")
