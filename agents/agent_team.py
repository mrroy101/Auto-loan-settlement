"""
Agent Team

Orchestrates the complete
Auto Loan Settlement Negotiation workflow.
"""

from agents.coordinator_agent import CoordinatorAgent
from agents.data_collection_agent import data_collection_agent
from agents.vehicle_research_agent import vehicle_research_agent
from agents.financial_analysis_agent import financial_analysis_agent
from agents.settlement_strategy_agent import settlement_strategy_agent
from agents.negotiation_agent import negotiation_agent
from agents.approval_agent import approval_agent
from agents.document_agent import document_agent


class AgentTeam:

    def __init__(self):
        self.coordinator = CoordinatorAgent()
        self.data_agent = data_collection_agent
        self.vehicle_agent = vehicle_research_agent
        self.financial_agent = financial_analysis_agent
        self.strategy_agent = settlement_strategy_agent
        self.negotiation_agent = negotiation_agent
        self.approval_agent = approval_agent
        self.document_agent = document_agent

    async def start_workflow(
        self,
        customer_id,
        customer_offer=None,
        hardship_reason=None
    ):
        print("=" * 60)
        print("AUTO LOAN SETTLEMENT NEGOTIATOR")
        print("=" * 60)

        customer_context = await self.coordinator.start(customer_id)
        print("✔ Customer Data Loaded")

        vehicle_report = await self.vehicle_agent.run(customer_context)
        print("✔ Vehicle Research Completed")

        financial_report = await self.financial_agent.run(customer_context, vehicle_report)
        print("✔ Financial Analysis Completed")

        settlement_strategy = await self.strategy_agent.run(
            financial_report,
            vehicle_report,
            customer_context,
        )
        print("✔ Settlement Strategy Generated")

        if customer_offer is None:
            return settlement_strategy

        negotiation_result = await self.negotiation_agent.run(
            customer_offer,
            settlement_strategy,
            hardship_reason,
        )
        print("✔ Negotiation Completed")

        approval = await self.approval_agent.run(customer_offer, settlement_strategy)
        print("✔ Approval Decision Completed")

        if approval["status"] == "APPROVED":
            letter = await self.document_agent.run(
                customer_name=customer_context.customer.customer_name,
                loan_id=customer_context.loan.loan_id,
                vehicle=f"{customer_context.vehicle.brand} {customer_context.vehicle.model}",
                settlement_amount=customer_offer,
            )
            approval["letter"] = letter

        return {
            "customer": customer_context,
            "vehicle_report": vehicle_report,
            "financial_report": financial_report,
            "settlement_strategy": settlement_strategy,
            "negotiation": negotiation_result,
            "approval": approval,
            "emi_history": customer_context.emi_history,
        }
