"""
Auto Loan Settlement Negotiator
 
Main Streamlit Application
"""
 
import asyncio
 
import streamlit as st
 
from agents.agent_team import AgentTeam
 
from components.sidebar import render_sidebar
 
from components.customer_summary import render_customer_summary
 
from components.loan_summary import render_loan_summary
 
from components.vehicle_summary import render_vehicle_summary
 
from components.financial_summary import render_financial_summary
 
from components.negotiation_summary import render_negotiation_summary
 
from components.emi_history import render_emi_history
 
from components.chat_window import render_chat_history
 
from components.offer_card import render_offer_card
 
from components.negotiation_panel import render_negotiation_panel
 
from components.approval_panel import render_approval_panel
 
from components.document_panel import render_document_panel
 
from components.metrics_dashboard import render_metrics_dashboard
 
 
# -----------------------------------------------------
# Page Configuration
# -----------------------------------------------------
 
st.set_page_config(
 
    page_title="Auto Loan Settlement Negotiator",
 
    page_icon="🚗",
 
    layout="wide",
 
    initial_sidebar_state="expanded"
 
)
 
 
# -----------------------------------------------------
# Session State
# -----------------------------------------------------
 
if "team" not in st.session_state:
 
    st.session_state.team = AgentTeam()
 
 
if "workflow" not in st.session_state:
 
    st.session_state.workflow = None
 
 
if "customer_loaded" not in st.session_state:
 
    st.session_state.customer_loaded = False
 
 
if "customer_id" not in st.session_state:
 
    st.session_state.customer_id = ""
 
 
if "chat_history" not in st.session_state:
 
    st.session_state.chat_history = []
 
 
# -----------------------------------------------------
# Header
# -----------------------------------------------------
 
st.title("🚗 Auto Loan Settlement Negotiator")
 
st.caption(
    "AI Powered Loan Settlement & Recovery Platform"
)
 
st.divider()
 
 
# -----------------------------------------------------
# Sidebar
# -----------------------------------------------------
 
render_sidebar(
 
    st.session_state.team
 
)
 
 
# -----------------------------------------------------
# Customer Validation
# -----------------------------------------------------
 
if not st.session_state.customer_loaded:
 
    st.info(
 
        "Please load a customer from the sidebar."
 
    )
 
    st.stop()
 
 
# -----------------------------------------------------
# Workflow
# -----------------------------------------------------
 
workflow = st.session_state.workflow
 
 
customer_context = workflow["customer"]
 
customer = customer_context.customer
 
loan = customer_context.loan
 
vehicle = customer_context.vehicle
 
 
vehicle_report = workflow["vehicle_report"]
 
financial_report = workflow["financial_report"]
 
settlement_strategy = workflow["settlement_strategy"]
 
approval = workflow["approval"]
 
emi_history = workflow["emi_history"]
 
 
# -----------------------------------------------------
# Metrics Dashboard
# -----------------------------------------------------
 
render_metrics_dashboard(
 
    workflow
 
)
 
st.divider()
 
 
# -----------------------------------------------------
# Customer Dashboard
# -----------------------------------------------------
 
tab1, tab2, tab3, tab4 = st.tabs(
 
    [
 
        "Customer",
 
        "Loan",
 
        "Vehicle",
 
        "Financial"
 
    ]
 
)

# -----------------------------------------------------
# Customer Tab
# -----------------------------------------------------
 
with tab1:
 
    render_customer_summary(customer)
 
    st.divider()
 
    render_negotiation_summary(
 
        settlement_strategy
 
    )
 
 
# -----------------------------------------------------
# Loan Tab
# -----------------------------------------------------
 
with tab2:
 
    render_loan_summary(
 
        loan
 
    )
 
    st.divider()
 
    render_emi_history(
 
        emi_history
 
    )
 
 
# -----------------------------------------------------
# Vehicle Tab
# -----------------------------------------------------
 
with tab3:
 
    render_vehicle_summary(
 
        vehicle,
 
        vehicle_report
 
    )
 
 
# -----------------------------------------------------
# Financial Tab
# -----------------------------------------------------
 
with tab4:
 
    render_financial_summary(
 
        financial_report
 
    )
 
 
st.divider()
 
 
# -----------------------------------------------------
# Negotiation Section
# -----------------------------------------------------
 
st.header("🤝 AI Settlement Negotiation")
 
left_column, right_column = st.columns(
 
    [3, 2]
 
)
 
 
# -----------------------------------------------------
# Left Column
# -----------------------------------------------------
 
with left_column:
 
    render_chat_history()
 
    st.divider()
 
    render_negotiation_panel()
 
 
# -----------------------------------------------------
# Right Column
# -----------------------------------------------------
 
with right_column:
 
    render_offer_card(
 
        settlement_strategy
 
    )
 
    st.divider()
 
    render_approval_panel(
 
        approval
 
    )
 
    st.divider()
 
    render_document_panel(
 
        approval
 
    )
 
 
st.divider()
 
# -----------------------------------------------------
# Footer Actions
# -----------------------------------------------------
 
st.header("⚙ Actions")
 
col1, col2, col3 = st.columns(3)
 
# -----------------------------------------------------
# Refresh Customer
# -----------------------------------------------------
 
with col1:
 
    if st.button("🔄 Refresh Customer Data"):
 
        with st.spinner("Refreshing customer information..."):
 
            workflow = asyncio.run(
 
                st.session_state.team.start_workflow(
 
                    customer_id=st.session_state.customer_id
 
                )
 
            )
 
            st.session_state.workflow = workflow
 
        st.success("Customer information refreshed.")
 
        st.rerun()
 
 
# -----------------------------------------------------
# Clear Negotiation
# -----------------------------------------------------
 
with col2:
 
    if st.button("🗑 Clear Negotiation"):
 
        st.session_state.chat_history = []
 
        st.success("Negotiation history cleared.")
 
        st.rerun()
 
 
# -----------------------------------------------------
# Reset Application
# -----------------------------------------------------
 
with col3:
 
    if st.button("🚪 Logout"):
 
        st.session_state.customer_loaded = False
 
        st.session_state.customer_id = ""
 
        st.session_state.workflow = None
 
        st.session_state.chat_history = []
 
        st.success("Logged out successfully.")
 
        st.rerun()
 
 
# -----------------------------------------------------
# Negotiation Timeline
# -----------------------------------------------------
 
st.divider()
 
st.subheader("📈 Negotiation Timeline")
 
if len(st.session_state.chat_history) == 0:
 
    st.info("Negotiation has not started.")
 
else:
 
    for index, message in enumerate(
 
        st.session_state.chat_history,
 
        start=1
 
    ):
 
        role = message["role"].upper()
 
        st.write(
 
            f"{index}. {role} : {message['message']}"
 
        )
 
 
# -----------------------------------------------------
# Current Settlement Status
# -----------------------------------------------------
 
st.divider()
 
status = approval.get(
 
    "status",
 
    "UNKNOWN"
 
)
 
if status == "APPROVED":
 
    st.success(
 
        "✅ Settlement Successfully Approved"
 
    )
 
elif status == "PENDING_RM":
 
    st.warning(
 
        "🟡 Awaiting Relationship Manager Approval"
 
    )
 
elif status == "REJECTED":
 
    st.error(
 
        "❌ Settlement Rejected"
 
    )
 
else:
 
    st.info(
 
        "Negotiation is currently in progress."
 
    )
 
 
# -----------------------------------------------------
# Debug Section
# -----------------------------------------------------
 
with st.expander(
 
    "Developer Debug Information"
 
):
 
    st.json(
 
        {
 
            "Customer ID":
 
                st.session_state.customer_id,
 
            "Workflow Loaded":
 
                st.session_state.customer_loaded,
 
            "Chat Messages":
 
                len(st.session_state.chat_history),
 
            "Approval Status":
 
                approval,
 
            "Settlement Strategy":
 
                settlement_strategy
 
        }
 
    )
 
 
# -----------------------------------------------------
# Footer
# -----------------------------------------------------
 
st.divider()
 
st.markdown(
 
"""
<center>
 
### 🚗 Auto Loan Settlement Negotiator
 
Powered by
 
**Microsoft AutoGen**
 
**Azure OpenAI**
 
**Streamlit**
 
</center>
""",
 
unsafe_allow_html=True
 
)