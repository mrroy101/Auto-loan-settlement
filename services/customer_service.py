from services.cutomer_master_service import CustomerMasterService
from services.customer_workbook_service import CustomerWorkbookService
from services.customer_workbook_parser import CustomerWorkbookParser
from services.emi_history_parser import EMIHistoryParser
from services.data_validator import DataValidator
from services.loan_analysis_service import LoanAnalysisService
from services.risk_analysis_service import RiskAnalysisService
from services.repayment_capacity_service import RepaymentCapacityService
from services.financial_summary_service import FinancialSummaryService
from services.negotiation_context_builder import NegotiationContextBuilder


class CustomerService:
    def load_customer(self, customer_id):
        workbook = CustomerWorkbookService()
        validator = DataValidator()
        parser = CustomerWorkbookParser()
        emi_parser = EMIHistoryParser()

        customer_sheet, emi_sheet = workbook.load(customer_id)
        validator.validate_customer_sheet(customer_sheet)
        validator.validate_emi_sheet(emi_sheet)

        customer, vehicle, loan = parser.parse(customer_sheet)
        emi_history = emi_parser.parse(emi_sheet)

        summary = FinancialSummaryService().build(customer, vehicle, loan, emi_history)
        context = NegotiationContextBuilder().build(
            customer,
            loan,
            summary["vehicle"],
            emi_history,
            summary,
            0,
        )
        return context
