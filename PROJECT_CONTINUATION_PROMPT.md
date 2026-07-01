MASTER CONTINUATION PROMPT

I am building a production-level AI application called Auto Loan Settlement Negotiator using Microsoft AutoGen, Azure OpenAI, Streamlit, and Python.

Do NOT redesign the architecture. Continue from the current progress.

Project Objective

This application is an AI-powered loan settlement negotiation platform for banks.

The bank has customers who have defaulted on vehicle loans.

Instead of directly auctioning the vehicle, the customer is given an AI chatbot where they can negotiate their settlement.

The chatbot uses multiple AutoGen agents.

The goal is to maximize recovery while giving suitable offers to genuine customers.

Tech Stack

Python

Microsoft AutoGen

Azure OpenAI

Streamlit

Pandas

OpenPyXL

python-dotenv

ReportLab (future)

Environment Variables

.env contains

AZURE_OPENAI_API_KEY

AZURE_OPENAI_ENDPOINT

AZURE_OPENAI_DEPLOYMENT

AZURE_OPENAI_API_VERSION

Project Structure

Auto-Loan-Settlement-Negotiator/

 

│

├── .env

├── .gitignore

├── requirements.txt

├── README.md

│

├── streamlit_app.py

│

├── config/

│      settings.py

│      prompts.py

│

├── llm/

│      azure_openai.py

│

├── agents/

│      coordinator_agent.py

│      data_collection_agent.py

│      vehicle_research_agent.py

│      financial_analysis_agent.py

│      settlement_strategy_agent.py

│      negotiation_agent.py

│      approval_agent.py

│      document_agent.py

│      agent_team.py

│

├── services/

│      customer_service.py

│      customer_workbook_service.py

│      customer_master_service.py

│      excel_reader.py

│      emi_history_parser.py

│      dashboard_service.py

│      data_validator.py

│      financial_summary_service.py

│      loan_analysis_service.py

│      negotiation_context_builder.py

│      repayment_capacity_service.py

│      risk_analysis_service.py

│      settlement_engine.py

│      vehicle_valuation_service.py

│

├── models/

│      customer.py

│      loan.py

│      vehicle.py

│      emi.py

│      settlement.py

│      negotiation_context.py

│

├── components/

│      sidebar.py

│      customer_summary.py

│      negotiation_summary.py

│      loan_summary.py

│      vehicle_summary.py

│      financial_summary.py

│      emi_history.py

│      chat_window.py

│      message_bubble.py

│      offer_card.py

│      negotiation_panel.py

│      approval_panel.py

│      document_panel.py

│      metrics_dashboard.py

│

├── data/

│

└── reports/

Excel Structure

There are TWO Excel files.

Excel 1

Master Customer Excel

Contains all customers.

Columns

Customer ID

Customer Name

DOB

Age

Mobile

Email

Aadhaar

PAN

Address

Employment Type

Company Name

Job Description

Monthly Income

CIBIL Score

Credit Risk

Existing Loans Count

Existing EMI Amount

Vehicle ID

Vehicle Details

Registration Number

Loan ID

Loan Amount

Loan Sanction Date

Down Payment

Interest Rate

Loan Tenure

EMI Amount

First EMI Date

Last EMI Date

Outstanding Principal

Outstanding Interest

Days Past Due

Missed EMI Count

Loan Status

Excel 2

Each customer has ONE workbook.

Inside that workbook

Sheet1

Contains

Field

Value

Where value stores one customer's details.

Sheet2

Contains EMI History

Columns

Installment Number

Due Date

Paid Date

EMI Amount

Principal

Interest

Late Fees

Status

AI Workflow

Coordinator Agent

↓

Data Collection Agent

↓

Vehicle Research Agent

↓

Financial Analysis Agent

↓

Settlement Strategy Agent

↓

Negotiation Agent

↓

Approval Agent

↓

Document Agent

Agent Responsibilities

Coordinator

Controls workflow.

Data Collection

Loads Excel

Builds Negotiation Context.

Vehicle Research

Researches internet

Predicts

Market Value

Auction Value

Dealer Value

Confidence

Reasoning

Financial Analysis

Uses

Loan Analysis

Risk Analysis

Repayment Capacity

Financial Summary

Settlement Strategy

Calculates

LES

MID

HES

Negotiation Strategy

Moratorium Eligibility

Restructure Eligibility

Negotiation

Talks with customer.

Offers

Settlement

EMI restructuring

Moratorium

Approval

Rules

Offer >= HES

Auto Approval

Offer within 2%

Send RM Approval

Offer < LES

Reject

Document

Creates

Settlement Letter

Approval Letter

RM Request

Rejection Letter

Negotiation Logic

Example

Outstanding

10,00,000

LES

8,20,000

MID

8,85,000

HES

9,50,000

Customer offers

9,50,000

↓

Auto Approve

Customer offers

9,35,000

↓

RM Approval

Customer offers

8,70,000

↓

Offer

Moratorium

EMI Restructure

Customer offers

7,00,000

↓

Reject

If customer recently lost job

Offer

6 month moratorium

or

Increase loan tenure

Vehicle Research

Vehicle Research Agent must search internet.

Estimate

Current Market Value

Dealer Value

Auction Value

Based on

Year

Variant

Brand

Location

Past trends

Streamlit UI

Contains

Sidebar

Customer Dashboard

Loan Dashboard

Vehicle Dashboard

Financial Dashboard

Negotiation Summary

EMI History

Chat Window

Offer Card

Negotiation Panel

Approval Panel

Metrics Dashboard

Document Download

Current Status

Completed

Project Structure

Services

Models

Azure OpenAI

Prompts

All AutoGen Agents

Agent Team

All Streamlit Components

Final streamlit_app.py

Not yet verified

Imports

AutoGen compatibility

Model field names

Return types

Excel parsing

Vehicle internet research

RM dashboard

PDF generation

Integration testing

Current Task

Do NOT redesign the project.

Do NOT rewrite architecture.

Continue only from current progress.

Help debug errors one by one until the application runs successfully.

Whenever I paste a traceback, identify the exact file and line causing the issue, explain the cause briefly, and provide the corrected code with minimal changes.

We are now entering the Integration & Debugging phase. The focus is to make the existing project run successfully, not to redesign or simplify it.

This prompt contains the full context of your project and is sufficient to continue development in a fresh chat without losing progress.
