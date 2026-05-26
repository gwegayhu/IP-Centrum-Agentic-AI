"""
BizSignal — Business Development Intelligence Agent

Domain: Commercial growth
Risk tier: Low (intelligence output for commercial team review)

Monitors the EPO's public grants database continuously to identify commercial opportunities:
- Detects EP grants to non-clients
- Prioritizes leads by grant volume, technology area, applicant type
- Identifies high-volume patent attorney firms not using IP Centrum
- Tracks UPC opt-out activity (signal of active EP validation decisions)
- Monitors UK and EU regulatory developments
"""

from dataclasses import dataclass, field
from typing import Optional, List, Dict, Any
from enum import Enum
from datetime import datetime
import logging

logger = logging.getLogger(__name__)


class LeadPriority(Enum):
    """Lead priority for outreach."""
    TIER1 = "tier1"  # High-volume, high-value
    TIER2 = "tier2"  # Medium volume or value
    TIER3 = "tier3"  # Lower priority
    LOW = "low"


class OpportunityType(Enum):
    """Type of commercial opportunity."""
    NEW_CLIENT_LEAD = "new_client_lead"
    ATTORNEY_FIRM_OUTREACH = "attorney_firm_outreach"
    UPC_OPT_OUT_SIGNAL = "upc_opt_out_signal"
    TECHNOLOGY_EXPANSION = "technology_expansion"
    REGULATORY_CHANGE_OPPORTUNITY = "regulatory_change_opportunity"


@dataclass
class ClientLead:
    """Potential new client lead."""
    lead_id: str
    organization_name: str
    grant_volume_annual: int
    technology_areas: List[str]
    estimated_value: float  # EUR annual revenue potential
    contact_email: Optional[str]
    geographic_focus: List[str]  # Countries where they file
    priority: LeadPriority
    detected_date: datetime = field(default_factory=datetime.now)
    last_grant_date: Optional[datetime] = None


@dataclass
class AttorneyFirmLead:
    """Patent attorney firm that could benefit from IP Centrum services."""
    firm_id: str
    firm_name: str
    website: str
    high_volume_clients: int
    annual_ep_grants_managed: int
    geographic_coverage: List[str]
    estimated_annual_opportunity: float  # EUR
    priority: LeadPriority
    contact_info: Optional[str] = None


@dataclass
class UPCOptOutSignal:
    """UPC opt-out activity as signal of active EP validation."""
    signal_id: str
    applicant_name: str
    organization_type: str  # "corporation", "firm", "individual"
    opt_out_date: datetime
    patents_affected: int
    technology_areas: List[str]
    implies_classical_validation: bool


@dataclass
class BusinessOpportunity:
    """Business development opportunity detected by BizSignal."""
    opportunity_id: str
    opportunity_type: OpportunityType
    description: str
    lead_entity: str  # Organization or individual name
    estimated_annual_value: float  # EUR
    priority: LeadPriority
    recommended_action: str
    supporting_data: Dict[str, Any]
    detected_date: datetime = field(default_factory=datetime.now)


class BizSignal:
    """
    Business Development Intelligence Agent.
    
    Monitors EPO and UPC public data to identify commercial opportunities
    for IP Centrum's services, enabling proactive business development.
    """
    
    def __init__(self):
        """Initialize BizSignal agent."""
        self.detected_leads: Dict[str, ClientLead] = {}
        self.attorney_firm_leads: Dict[str, AttorneyFirmLead] = {}
        self.upc_opt_out_signals: Dict[str, UPCOptOutSignal] = {}
        self.opportunities: Dict[str, BusinessOpportunity] = {}
        self.existing_clients: set = set()  # Set of known client names
    
    def monitor_ep_grants(self, grants_data: List[Dict[str, Any]]) -> List[ClientLead]:
        """
        Monitor EPO grants database for new client leads.
        
        Args:
            grants_data: List of recent EP grant data
            
        Returns:
            List of new ClientLead opportunities
        """
        new_leads = []
        
        try:
            for grant in grants_data:
                applicant = grant.get("applicant_name", "")
                
                # Skip if already a client
                if applicant in self.existing_clients:
                    continue
                
                # Check if we already have this lead
                lead_key = f"LEAD_{applicant}"
                if lead_key in self.detected_leads:
                    existing_lead = self.detected_leads[lead_key]
                    existing_lead.grant_volume_annual += 1
                    existing_lead.last_grant_date = datetime.now()
                else:
                    # Create new lead
                    lead = self._create_client_lead(applicant, grant)
                    self.detected_leads[lead_key] = lead
                    new_leads.append(lead)
                    
                    logger.info(f"Detected new lead: {applicant} (Priority: {lead.priority.value})")
            
            return new_leads
            
        except Exception as e:
            logger.error(f"Error monitoring EP grants: {str(e)}")
            return []
    
    def _create_client_lead(self, applicant_name: str, grant_data: Dict[str, Any]) -> ClientLead:
        """Create a new ClientLead record."""
        technology_areas = grant_data.get("technology_areas", [])
        
        # Assess priority based on characteristics
        priority = self._assess_lead_priority(
            grant_data.get("organization_type", ""),
            technology_areas,
            grant_data.get("geographic_focus", [])
        )
        
        # Estimate annual value based on typical patterns
        estimated_value = self._estimate_lead_value(priority, len(technology_areas))
        
        lead = ClientLead(
            lead_id=f"LEAD_{applicant_name}_{datetime.now().timestamp()}",
            organization_name=applicant_name,
            grant_volume_annual=1,
            technology_areas=technology_areas,
            estimated_value=estimated_value,
            contact_email=grant_data.get("contact_email"),
            geographic_focus=grant_data.get("geographic_focus", []),
            priority=priority,
            last_grant_date=datetime.now(),
        )
        
        return lead
    
    def _assess_lead_priority(
        self,
        organization_type: str,
        technology_areas: List[str],
        geographic_focus: List[str]
    ) -> LeadPriority:
        """Assess priority of a potential lead."""
        score = 0
        
        # Organization type scoring
        if organization_type == "large_corporation":
            score += 40
        elif organization_type == "sme":
            score += 20
        elif organization_type == "individual":
            score += 5
        
        # Technology area scoring (high-value areas)
        high_value_areas = ["pharma", "software", "biotech"]
        score += sum(10 for area in technology_areas if area in high_value_areas)
        
        # Geographic coverage scoring
        key_markets = ["DE", "FR", "GB", "IT", "CH"]
        score += sum(5 for market in geographic_focus if market in key_markets)
        
        if score >= 50:
            return LeadPriority.TIER1
        elif score >= 30:
            return LeadPriority.TIER2
        elif score >= 10:
            return LeadPriority.TIER3
        else:
            return LeadPriority.LOW
    
    def _estimate_lead_value(self, priority: LeadPriority, tech_area_count: int) -> float:
        """Estimate annual revenue potential from lead."""
        base_values = {
            LeadPriority.TIER1: 50000,
            LeadPriority.TIER2: 20000,
            LeadPriority.TIER3: 5000,
            LeadPriority.LOW: 1000,
        }
        
        base = base_values.get(priority, 10000)
        
        # Increase value with technology area diversity
        multiplier = 1.0 + (tech_area_count * 0.1)
        
        return base * multiplier
    
    def identify_high_volume_attorney_firms(self) -> List[AttorneyFirmLead]:
        """
        Identify patent attorney firms with high-volume EP filing.
        
        Returns:
            List of AttorneyFirmLead opportunities
        """
        new_firm_leads = []
        
        try:
            # Mock data: would query EPO and attorney databases
            sample_firms = [
                {
                    "name": "Patent Services GmbH",
                    "website": "https://patentservices.de",
                    "high_volume_clients": 15,
                    "annual_ep_grants": 500,
                    "coverage": ["DE", "FR", "IT"],
                },
                {
                    "name": "European IP Solutions",
                    "website": "https://euiplaw.fr",
                    "high_volume_clients": 25,
                    "annual_ep_grants": 800,
                    "coverage": ["FR", "NL", "BE"],
                },
            ]
            
            for firm_data in sample_firms:
                firm = AttorneyFirmLead(
                    firm_id=f"FIRM_{firm_data['name']}_{datetime.now().timestamp()}",
                    firm_name=firm_data["name"],
                    website=firm_data["website"],
                    high_volume_clients=firm_data["high_volume_clients"],
                    annual_ep_grants_managed=firm_data["annual_ep_grants"],
                    geographic_coverage=firm_data["coverage"],
                    estimated_annual_opportunity=firm_data["annual_ep_grants"] * 1500,  # Mock: EUR per grant
                    priority=LeadPriority.TIER1 if firm_data["annual_ep_grants"] > 500 else LeadPriority.TIER2,
                )
                
                self.attorney_firm_leads[firm.firm_id] = firm
                new_firm_leads.append(firm)
                logger.info(f"Identified attorney firm: {firm.firm_name}")
            
            return new_firm_leads
            
        except Exception as e:
            logger.error(f"Error identifying attorney firms: {str(e)}")
            return []
    
    def track_upc_opt_outs(self, opt_out_data: List[Dict[str, Any]]) -> List[UPCOptOutSignal]:
        """
        Track UPC opt-out registrations as signal of active EP validation.
        
        UP opt-out indicates applicant is actively making validation decisions.
        
        Args:
            opt_out_data: List of recent opt-out registrations
            
        Returns:
            List of UPCOptOutSignal records
        """
        signals = []
        
        try:
            for opt_out in opt_out_data:
                signal = UPCOptOutSignal(
                    signal_id=f"SIGNAL_{opt_out['ep_number']}_{datetime.now().timestamp()}",
                    applicant_name=opt_out.get("applicant_name", ""),
                    organization_type=opt_out.get("organization_type", "corporation"),
                    opt_out_date=datetime.now(),
                    patents_affected=opt_out.get("patents_affected", 1),
                    technology_areas=opt_out.get("technology_areas", []),
                    implies_classical_validation=True,
                )
                
                self.upc_opt_out_signals[signal.signal_id] = signal
                signals.append(signal)
                logger.info(f"Tracked UPC opt-out: {signal.applicant_name}")
            
            return signals
            
        except Exception as e:
            logger.error(f"Error tracking UPC opt-outs: {str(e)}")
            return []
    
    def generate_business_opportunity(
        self,
        opportunity_type: OpportunityType,
        lead_entity: str,
        description: str,
        estimated_value: float,
        supporting_data: Dict[str, Any]
    ) -> BusinessOpportunity:
        """
        Generate a business opportunity record.
        
        Args:
            opportunity_type: Type of opportunity
            lead_entity: Entity name
            description: Opportunity description
            estimated_value: Annual value in EUR
            supporting_data: Supporting information
            
        Returns:
            BusinessOpportunity record
        """
        opportunity = BusinessOpportunity(
            opportunity_id=f"OPP_{lead_entity}_{datetime.now().timestamp()}",
            opportunity_type=opportunity_type,
            description=description,
            lead_entity=lead_entity,
            estimated_annual_value=estimated_value,
            priority=self._assess_opportunity_priority(opportunity_type, estimated_value),
            recommended_action=self._generate_recommended_action(opportunity_type),
            supporting_data=supporting_data,
        )
        
        self.opportunities[opportunity.opportunity_id] = opportunity
        logger.info(f"Generated opportunity: {opportunity.opportunity_id}")
        
        return opportunity
    
    def _assess_opportunity_priority(
        self,
        opportunity_type: OpportunityType,
        estimated_value: float
    ) -> LeadPriority:
        """Assess priority of an opportunity."""
        if estimated_value > 50000:
            return LeadPriority.TIER1
        elif estimated_value > 20000:
            return LeadPriority.TIER2
        elif estimated_value > 5000:
            return LeadPriority.TIER3
        else:
            return LeadPriority.LOW
    
    def _generate_recommended_action(self, opportunity_type: OpportunityType) -> str:
        """Generate recommended action for opportunity."""
        actions = {
            OpportunityType.NEW_CLIENT_LEAD: "Outreach campaign targeting high-volume grantees",
            OpportunityType.ATTORNEY_FIRM_OUTREACH: "White-label partnership proposal",
            OpportunityType.UPC_OPT_OUT_SIGNAL: "Contact regarding classical validation needs",
            OpportunityType.TECHNOLOGY_EXPANSION: "Develop specialized service offering",
            OpportunityType.REGULATORY_CHANGE_OPPORTUNITY: "Position IP Centrum as compliance partner",
        }
        return actions.get(opportunity_type, "Evaluate partnership opportunity")
    
    def get_tier1_opportunities(self) -> List[BusinessOpportunity]:
        """Get all Tier 1 priority opportunities."""
        return [
            opp for opp in self.opportunities.values()
            if opp.priority == LeadPriority.TIER1
        ]


# Example usage
if __name__ == "__main__":
    agent = BizSignal()
    
    # Monitor EP grants
    sample_grants = [
        {
            "applicant_name": "Tech Innovations Ltd",
            "technology_areas": ["software", "electronics"],
            "organization_type": "sme",
            "geographic_focus": ["DE", "FR", "GB"],
        }
    ]
    
    leads = agent.monitor_ep_grants(sample_grants)
    print(f"New leads detected: {len(leads)}")
    for lead in leads:
        print(f"  - {lead.organization_name} (Priority: {lead.priority.value}, Value: €{lead.estimated_value:.0f})")
    
    # Identify attorney firms
    firms = agent.identify_high_volume_attorney_firms()
    print(f"\nHigh-volume attorney firms: {len(firms)}")
    
    # Generate opportunity
    opp = agent.generate_business_opportunity(
        opportunity_type=OpportunityType.NEW_CLIENT_LEAD,
        lead_entity="Tech Innovations Ltd",
        description="Growing software company with regular EP grants",
        estimated_value=75000,
        supporting_data={"grant_volume": 25}
    )
    
    print(f"\nOpportunity: {opp.opportunity_id}")
    print(f"Value: €{opp.estimated_annual_value:.0f}")
    print(f"Action: {opp.recommended_action}")
