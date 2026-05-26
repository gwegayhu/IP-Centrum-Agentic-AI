"""
QuoteAdvisor — Intelligent Quote Optimization Agent

Domain: Sales & client advisory
Risk tier: Low (advisory recommendations; client retains decision authority)

Moves beyond quote generation to quote intelligence:
- Advises on optimal validation strategy by technology area
- Models UP vs. classical validation pathways
- Analyzes applicant type for risk tolerance signals
- Uses historical validation patterns
- Performs cost-benefit analysis
- Provides renewal trajectory recommendations
"""

from dataclasses import dataclass, field
from typing import Optional, List, Dict, Any, Tuple
from enum import Enum
from datetime import datetime
import logging

logger = logging.getLogger(__name__)


class ValidationType(Enum):
    """Type of validation pathway."""
    UP_ONLY = "up_only"
    CLASSICAL_ONLY = "classical_only"
    UP_PLUS_CLASSICAL = "up_plus_classical"


@dataclass
class ValidationPathway:
    """A complete validation pathway with cost and coverage."""
    pathway_type: ValidationType
    states: List[str]  # List of state codes
    total_cost: float  # EUR
    first_year_cost: float  # EUR
    renewal_annual_cost_range: Tuple[float, float]  # (min, max) EUR
    territorial_coverage: float  # % of major markets
    up_coverage_percentage: float  # % covered by UP
    classical_coverage_percentage: float  # % covered by classical
    estimated_grant_probability: float  # 0.0-1.0
    risk_level: str  # "low", "medium", "high"


@dataclass
class QuoteRecommendation:
    """Recommendation for optimal validation strategy."""
    quote_id: str
    ep_number: str
    client_id: str
    technology_area: str
    applicant_type: str  # "individual", "sme", "large_corporation"
    recommended_pathway: ValidationPathway
    alternative_pathways: List[ValidationPathway]
    rationale: str
    cost_benefit_analysis: Dict[str, Any]
    historical_context: Dict[str, Any]  # Historical patterns for same tech area
    renewal_trajectory: Dict[str, float]  # Projected costs by year
    confidence_score: float  # 0.0-1.0
    generated_date: datetime = field(default_factory=datetime.now)


@dataclass
class HistoricalPattern:
    """Historical validation pattern for a technology area."""
    technology_area: str
    total_validations: int
    avg_states_selected: float
    up_adoption_rate: float  # % of UP-eligible patents choosing UP
    avg_cost_per_state: float
    most_common_states: List[Tuple[str, float]]  # (state_code, selection_percentage)
    renewal_completion_rate: float  # % maintained to term


class QuoteAdvisor:
    """
    Intelligent Quote Optimization Agent.
    
    Provides quote intelligence and validation pathway recommendations
    based on patent characteristics, market analysis, and historical data.
    """
    
    def __init__(self):
        """Initialize QuoteAdvisor agent."""
        self.historical_patterns: Dict[str, HistoricalPattern] = {}
        self.cost_database: Dict[str, float] = {}  # state -> cost mapping
        self.recommendations: Dict[str, QuoteRecommendation] = {}
        
        # Load mock historical data
        self._load_historical_patterns()
    
    def _load_historical_patterns(self) -> None:
        """Load historical validation patterns from database."""
        # Mock data - would load from actual database
        self.historical_patterns = {
            "software": HistoricalPattern(
                technology_area="software",
                total_validations=2500,
                avg_states_selected=8.5,
                up_adoption_rate=0.72,
                avg_cost_per_state=850,
                most_common_states=[
                    ("DE", 0.95),
                    ("FR", 0.92),
                    ("GB", 0.85),
                    ("IT", 0.68),
                ],
                renewal_completion_rate=0.68,
            ),
            "pharma": HistoricalPattern(
                technology_area="pharma",
                total_validations=1200,
                avg_states_selected=18.2,
                up_adoption_rate=0.58,
                avg_cost_per_state=1200,
                most_common_states=[
                    ("DE", 0.98),
                    ("FR", 0.96),
                    ("IT", 0.89),
                    ("ES", 0.78),
                ],
                renewal_completion_rate=0.85,
            ),
            "chemistry": HistoricalPattern(
                technology_area="chemistry",
                total_validations=1800,
                avg_states_selected=12.1,
                up_adoption_rate=0.62,
                avg_cost_per_state=950,
                most_common_states=[
                    ("DE", 0.93),
                    ("FR", 0.90),
                    ("GB", 0.75),
                ],
                renewal_completion_rate=0.72,
            ),
        }
        
        # Mock cost database
        self.cost_database = {
            "DE": 800,
            "FR": 950,
            "GB": 750,
            "IT": 650,
            "ES": 600,
            "NL": 700,
            "SE": 700,
            "CH": 1200,
        }
    
    def generate_recommendation(
        self,
        ep_number: str,
        client_id: str,
        technology_area: str,
        applicant_type: str,
        is_up_eligible: bool,
        target_states: Optional[List[str]] = None
    ) -> Optional[QuoteRecommendation]:
        """
        Generate a quote recommendation with optimal validation pathway.
        
        Args:
            ep_number: European Patent Number
            client_id: Client ID
            technology_area: Technology classification
            applicant_type: Type of applicant (individual, sme, corporation)
            is_up_eligible: Whether patent is UP-eligible
            target_states: Optional list of preferred states
            
        Returns:
            QuoteRecommendation or None
        """
        try:
            quote_id = f"QUOTE_{ep_number}_{datetime.now().timestamp()}"
            
            # Get historical patterns for this technology
            pattern = self.historical_patterns.get(technology_area, None)
            
            # Generate validation pathways
            pathways = self._generate_pathways(
                ep_number,
                technology_area,
                is_up_eligible,
                applicant_type,
                target_states,
                pattern
            )
            
            if not pathways:
                logger.error(f"Failed to generate pathways for {ep_number}")
                return None
            
            # Sort pathways by recommendation score
            pathways.sort(key=lambda p: self._score_pathway(p, applicant_type))
            
            recommended = pathways[0]
            alternatives = pathways[1:]
            
            # Perform cost-benefit analysis
            cost_benefit = self._perform_cost_benefit_analysis(pathways, pattern)
            
            # Project renewal trajectory
            renewal_trajectory = self._project_renewal_trajectory(
                recommended.states,
                pattern
            )
            
            # Build rationale
            rationale = self._build_rationale(
                recommended,
                applicant_type,
                technology_area,
                pattern
            )
            
            recommendation = QuoteRecommendation(
                quote_id=quote_id,
                ep_number=ep_number,
                client_id=client_id,
                technology_area=technology_area,
                applicant_type=applicant_type,
                recommended_pathway=recommended,
                alternative_pathways=alternatives,
                rationale=rationale,
                cost_benefit_analysis=cost_benefit,
                historical_context=self._get_historical_context(pattern),
                renewal_trajectory=renewal_trajectory,
                confidence_score=self._calculate_confidence(pattern),
            )
            
            self.recommendations[quote_id] = recommendation
            logger.info(f"Generated recommendation: {quote_id}")
            
            return recommendation
            
        except Exception as e:
            logger.error(f"Error generating recommendation: {str(e)}")
            return None
    
    def _generate_pathways(
        self,
        ep_number: str,
        technology_area: str,
        is_up_eligible: bool,
        applicant_type: str,
        target_states: Optional[List[str]],
        pattern: Optional[HistoricalPattern]
    ) -> List[ValidationPathway]:
        """Generate alternative validation pathways."""
        pathways = []
        
        # Define major markets
        major_markets = ["DE", "FR", "GB", "IT", "ES", "NL", "SE", "CH"]
        
        if target_states:
            states_to_consider = target_states
        else:
            # Use historical pattern to select most valuable states
            if pattern:
                states_to_consider = [s[0] for s in pattern.most_common_states[:6]]
            else:
                states_to_consider = major_markets[:6]
        
        # Pathway 1: UP only (if eligible)
        if is_up_eligible:
            up_cost = 2500  # UP filing and prosecution cost
            up_pathway = ValidationPathway(
                pathway_type=ValidationType.UP_ONLY,
                states=["UP"],
                total_cost=up_cost,
                first_year_cost=up_cost,
                renewal_annual_cost_range=(500, 800),
                territorial_coverage=0.75,
                up_coverage_percentage=1.0,
                classical_coverage_percentage=0.0,
                estimated_grant_probability=0.85,
                risk_level="medium" if applicant_type == "individual" else "low"
            )
            pathways.append(up_pathway)
        
        # Pathway 2: Classical validation
        classical_cost = sum(
            self.cost_database.get(state, 800)
            for state in states_to_consider
        )
        classical_pathway = ValidationPathway(
            pathway_type=ValidationType.CLASSICAL_ONLY,
            states=states_to_consider,
            total_cost=classical_cost,
            first_year_cost=classical_cost,
            renewal_annual_cost_range=(
                len(states_to_consider) * 500,
                len(states_to_consider) * 1000
            ),
            territorial_coverage=0.85,
            up_coverage_percentage=0.0,
            classical_coverage_percentage=1.0,
            estimated_grant_probability=0.82,
            risk_level="low"
        )
        pathways.append(classical_pathway)
        
        # Pathway 3: UP + selective classical (if eligible)
        if is_up_eligible:
            additional_states = [s for s in states_to_consider if s not in ["DE", "FR"]][:2]
            hybrid_cost = 2500 + sum(
                self.cost_database.get(state, 800)
                for state in additional_states
            )
            hybrid_pathway = ValidationPathway(
                pathway_type=ValidationType.UP_PLUS_CLASSICAL,
                states=["UP"] + additional_states,
                total_cost=hybrid_cost,
                first_year_cost=hybrid_cost,
                renewal_annual_cost_range=(
                    500 + len(additional_states) * 500,
                    800 + len(additional_states) * 1000
                ),
                territorial_coverage=0.92,
                up_coverage_percentage=0.75,
                classical_coverage_percentage=0.25,
                estimated_grant_probability=0.84,
                risk_level="low"
            )
            pathways.append(hybrid_pathway)
        
        return pathways
    
    def _score_pathway(self, pathway: ValidationPathway, applicant_type: str) -> float:
        """
        Score a validation pathway for recommendation.
        Higher score = better recommendation.
        """
        score = 0.0
        
        # Cost factor (30%)
        max_cost = 8000
        cost_score = 1.0 - (pathway.total_cost / max_cost)
        score += cost_score * 0.30
        
        # Coverage factor (40%)
        score += pathway.territorial_coverage * 0.40
        
        # Grant probability (20%)
        score += pathway.estimated_grant_probability * 0.20
        
        # Risk factor (10%)
        risk_penalty = {
            "low": 0,
            "medium": 0.1,
            "high": 0.2
        }
        score -= risk_penalty.get(pathway.risk_level, 0)
        
        # Applicant-specific adjustments
        if applicant_type == "individual" and pathway.risk_level == "high":
            score -= 0.15
        
        return score
    
    def _perform_cost_benefit_analysis(
        self,
        pathways: List[ValidationPathway],
        pattern: Optional[HistoricalPattern]
    ) -> Dict[str, Any]:
        """Perform cost-benefit analysis comparing pathways."""
        return {
            "pathways_compared": len(pathways),
            "cost_range": {
                "min": min(p.total_cost for p in pathways),
                "max": max(p.total_cost for p in pathways),
            },
            "coverage_range": {
                "min": min(p.territorial_coverage for p in pathways),
                "max": max(p.territorial_coverage for p in pathways),
            },
            "cost_per_coverage_point": [
                p.total_cost / max(p.territorial_coverage, 0.1)
                for p in pathways
            ]
        }
    
    def _project_renewal_trajectory(
        self,
        states: List[str],
        pattern: Optional[HistoricalPattern]
    ) -> Dict[str, float]:
        """Project renewal costs over 20-year patent term."""
        trajectory = {}
        
        for year in [1, 3, 5, 7, 10, 15, 20]:
            # Mock: escalate costs by 3% per year
            base_cost = sum(
                self.cost_database.get(state, 800) * 0.5
                for state in states
            )
            trajectory[f"year_{year}"] = base_cost * (1.03 ** year)
        
        return trajectory
    
    def _build_rationale(
        self,
        pathway: ValidationPathway,
        applicant_type: str,
        technology_area: str,
        pattern: Optional[HistoricalPattern]
    ) -> str:
        """Build narrative rationale for recommendation."""
        rationale = f"For {applicant_type} applicants in {technology_area}, "
        rationale += f"this pathway provides optimal balance of cost (€{pathway.total_cost}) "
        rationale += f"and territorial coverage ({pathway.territorial_coverage*100:.0f}%). "
        
        if pathway.pathway_type == ValidationType.UP_ONLY:
            rationale += "UP-only approach minimizes prosecution costs and simplifies management. "
        elif pathway.pathway_type == ValidationType.UP_PLUS_CLASSICAL:
            rationale += "Hybrid approach combines UP efficiency with targeted classical validation in key markets. "
        
        if pattern:
            rationale += f"Historically, {pattern.up_adoption_rate*100:.0f}% of similar patents in this field choose UP pathway."
        
        return rationale
    
    def _calculate_confidence(self, pattern: Optional[HistoricalPattern]) -> float:
        """Calculate confidence score for recommendation."""
        if pattern and pattern.total_validations > 100:
            return min(0.95, 0.7 + (pattern.total_validations / 5000) * 0.25)
        return 0.7
    
    def _get_historical_context(self, pattern: Optional[HistoricalPattern]) -> Dict[str, Any]:
        """Get historical context data for this technology area."""
        if pattern:
            return {
                "total_validations": pattern.total_validations,
                "avg_states": pattern.avg_states_selected,
                "up_adoption_rate": pattern.up_adoption_rate,
                "renewal_completion_rate": pattern.renewal_completion_rate,
            }
        return {}


# Example usage
if __name__ == "__main__":
    agent = QuoteAdvisor()
    
    recommendation = agent.generate_recommendation(
        ep_number="EP2123456",
        client_id="CLIENT_001",
        technology_area="software",
        applicant_type="sme",
        is_up_eligible=True,
    )
    
    if recommendation:
        print(f"Quote ID: {recommendation.quote_id}")
        print(f"Recommended: {recommendation.recommended_pathway.pathway_type.value}")
        print(f"Cost: €{recommendation.recommended_pathway.total_cost}")
        print(f"Coverage: {recommendation.recommended_pathway.territorial_coverage*100:.0f}%")
        print(f"Rationale: {recommendation.rationale}")
