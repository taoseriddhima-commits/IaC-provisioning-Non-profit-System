import streamlit as st
import sys
import os

# Allow frontend to access backend modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from backend.agents.orchestrator import TriageOrchestrator

# Page Config

st.set_page_config(
    page_title="Non-Profit Triage AI",
    layout="wide"
)

# Initialize Session State

if "history" not in st.session_state:
    st.session_state.history = []


# Custom Styling

st.markdown("""
<style>
.main {
    background-color: #f5f7fb;
}

.card {
    background-color: #000000;
    color: white;
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.4);
    margin-bottom: 15px;
    line-height: 1.2;
}
</style>
""", unsafe_allow_html=True
)



# Title

st.title("📬 Non-Profit Support Triage Agent")


# Top Navigation Tabs

tab1, tab2, tab3 = st.tabs(["Triage", "History", "Analytics"])


# TRIAGE TAB

with tab1:
    st.header("Message Triage")

    user_input = st.text_area("Incoming Support Message", height=150)

    if st.button("Run Triage"):
        if not user_input.strip():
            st.warning("Please enter a message.")
        else:
            orchestrator = TriageOrchestrator()

            with st.spinner("Processing with AI Agents..."):
                result = orchestrator.run(user_input)

            st.success("Triage Complete!")

                        
            # Create short summary (first 120 chars of user message)
            summary = user_input.strip()[:120]
            if len(user_input.strip()) > 120:
                summary += "..."

            # Store everything properly
            st.session_state.history.append({
                "original_message": user_input,
                "summary": summary,
                "classification": result["classification"],

            })

            col1, col2 = st.columns(2)

            with col1:
                st.subheader("📊 Classification")
                classification = result["classification"]
                urgency = classification.get("urgency", "Unknown")
                intent = classification.get("intent", "Unknown")
                
                st.markdown(f"""
                <div style="
                    background-color:#000000;
                    padding:20px;
                    border-radius:12px;
                    color:white;
                    margin-bottom:15px;
                    box-shadow:0px 4px 10px rgba(0,0,0,0.3);
                ">
                    <div style="font-size:16px; font-weight:600;">
                        Urgency: {urgency}
                    </div>
                    <div style="margin-top:8px; font-size:16px;">
                        Intent: {intent}
                    </div>
                </div>
                """, unsafe_allow_html=True)
                

                st.subheader("🔎 Extracted Entities")
                
                entities = result["entities"]

                person = entities.get("person_name", "Not found")
                amount = entities.get("donation_amount", "Not found")
                date = entities.get("date", "Not found")
                organization = entities.get("organization", "Not found")
                email = entities.get("email", "Not found")
                phone = entities.get("phone_number", "Not found")
                
                st.markdown(
                f"""

                <div class="card">
                <b> Person:</b> {person}<br>
                <b> Donation Amount:</b> {amount}<br>
                <b> Date:</b> {date}<br>
                <b> Organization:</b> {organization}<br>
                <b> Email:</b> {email}<br>
                <b> Phone:</b> {phone}
                </div>
                """,
                unsafe_allow_html=True
                )


            with col2:
                st.subheader("✉ Generated Response")

                response_text = result["response_text"].strip()
                response_text = "\n".join(line.strip() for line in response_text.splitlines())

                st.markdown(
                    f'<div class="card">{response_text}</div>',
                    unsafe_allow_html=True
                )            

# HISTORY TAB


# HISTORY TAB (Dashboard Style - Part 1)

with tab2:
    st.header("Triage History")
    st.caption("View and manage processed messages")

    history = st.session_state.history

    if not history:
        st.info("No messages processed yet.")
    else:
        
        # METRIC CARDS
        
        total_cases = len(history)
        high_count = sum(1 for x in history if x["classification"].get("urgency","").lower() == "high")
        medium_count = sum(1 for x in history if x["classification"].get("urgency","").lower() == "medium")
        low_count = sum(1 for x in history if x["classification"].get("urgency","").lower() == "low")

        col1, col2, col3, col4 = st.columns(4)

        col1.metric("Total Cases", total_cases)
        col2.metric("High Urgency", high_count)
        col3.metric("Medium", medium_count)
        col4.metric("Low", low_count)

        st.markdown("")
        
        # SEARCH + FILTERS ROW
        
        col_s, col_f1, col_f2 = st.columns([2,1,1])

        search_query = col_s.text_input("Search messages")
        urgency_filter = col_f1.selectbox(
            "Filter by Urgency",
            ["All", "High", "Medium", "Low"]
        )

        intent_filter = col_f2.selectbox(
            "Filter by Intent",
            ["All"] + list(set(
                x["classification"].get("intent","Unknown") for x in history
            ))
        )

        st.markdown("---")
        
        # FILTER LOGIC
        
        filtered_history = history

        # Search filter
        if search_query:
            filtered_history = [
                x for x in filtered_history
                if search_query.lower() in x["original_message"].lower()
            ]

        # Urgency filter
        if urgency_filter != "All":
            filtered_history = [
                x for x in filtered_history
                if x["classification"].get("urgency", "").lower() == urgency_filter.lower()
            ]

        # Intent filter
        if intent_filter != "All":
            filtered_history = [
                x for x in filtered_history
                if x["classification"].get("intent", "") == intent_filter
            ]

        
        # DISPLAY HISTORY CARDS
        
        for item in filtered_history:
            urgency = item["classification"].get("urgency", "Unknown")
            intent = item["classification"].get("intent", "Unknown")

            st.markdown(f"""
            <div class="card">
                <b>Urgency:</b> {urgency} &nbsp;&nbsp; | &nbsp;&nbsp;
                <b>Intent:</b> {intent}
                <br><br>        
                {item["summary"]}
            </div>
            """, unsafe_allow_html=True)



# ANALYTICS TAB

with tab3:
    st.header("Analytics Dashboard")

    history = st.session_state.history

    if not history:
        st.info("No data available yet.")
    else:
        
        # Prepare Data
        
        urgency_counts = {}
        intent_counts = {}

        for item in history:
            urgency = item["classification"].get("urgency", "Unknown")
            intent = item["classification"].get("intent", "Unknown")

            urgency_counts[urgency] = urgency_counts.get(urgency, 0) + 1
            intent_counts[intent] = intent_counts.get(intent, 0) + 1

        
        # Display Charts
        
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Cases by Urgency")
            st.bar_chart(urgency_counts)

        with col2:
            st.subheader("Cases by Intent")
            st.bar_chart(intent_counts)

        st.markdown("---")

        
        # Trend Chart
        
        st.subheader("Cases Processed Over Time")

        trend_data = list(range(1, len(history) + 1))
        st.line_chart(trend_data)

        st.markdown("---")

        
        # Urgency Distribution Table
        
        import pandas as pd
        import matplotlib.pyplot as plt

        st.subheader("Urgency Distribution")

        urgency_df = pd.DataFrame({
            "Urgency": list(urgency_counts.keys()),
            "Count": list(urgency_counts.values())
        })

        col1, col2 = st.columns(2)
        
        # Pie Chart
        with col1:
            fig, ax = plt.subplots()
            ax.pie(
                urgency_df["Count"],
                labels=urgency_df["Urgency"],
                autopct="%1.1f%%",
            )
            ax.set_title("Urgency Breakdown")
            st.pyplot(fig)        

        # Table View
        with col2:
            st.dataframe(urgency_df, use_container_width=True)

