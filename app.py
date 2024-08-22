import streamlit as st
import json
import os

# File to store user profiles
PROFILE_STORAGE = "profiles.json"

# Load existing profiles
def load_profiles():
    if os.path.exists(PROFILE_STORAGE):
        with open(PROFILE_STORAGE, "r") as file:
            return json.load(file)
    return {}

# Save profiles
def save_profiles(profiles):
    with open(PROFILE_STORAGE, "w") as file:
        json.dump(profiles, file, indent=4)

# Main app function
def main():
    st.title("Student Profile Management")

    # Load profiles
    profiles = load_profiles()

    # Menu
    menu = ["Create Profile", "Edit Profile", "Delete Profile"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Create Profile":
        st.subheader("Create Profile")
        name = st.text_input("Enter Name")
        enrollment = st.text_input("Enter Enrollment Number")
        section = st.selectbox("Select Section", ["A", "B", "C"])
        subjects = st.multiselect(
            "Select Subjects",
            [
                "Innovation, Entrepreneurship and Start-ups (IES)",
                "Know yourself (KY)",
                "Professional Ethics (PE)",
                "Bibliophiles (Bibl)",
                "Psychology in Business (PB-A)",
                "International Business (IB)",
                "Project Management (PM)",
                "E-Business (E.Bus)",
                "Consumer Behaviour (CB)",
                "Integrated Marketing Communication (IMC)",
                "Sales & Distribution Management (S&DM)",
                "Marketing Analytics (Man)",
                "Strategic Brand Management (SBM)",
                "Financial Statement Analysis (FSA)",
                "Business Valuation (BussV)",
                "Security and Portfolio Management (SPM)",
                "International Finance (IF)",
                "Management of Banks (MoB)",
                "Programming for Analytics (PA)",
                "Text Mining and Sentiment Analytics (TM&SA)",
                "Data Mining and Visualization (DMV)",
                "Analytics for Service Operations (ASO)",
                "AI and Machine Learning (AIML)",
                "Digital Media (DM)",
                "Media Production and Consumption (MPC)",
                "Media and Sports Industry (MSI)",
                "Media Research Tools and Analytics (MRTA)",
                "Media Cost Management & Control (MCMC)",
                "Performance Management System (PMS)",
                "Talent Acquisition (TA)",
                "Learnings & Development (L&D)",
                "Compensation & Reward Management (C&RM)",
                "Purchasing & Inventory Management (P&IM)",
                "Supply Chain Management (SCM)",
                "Transportation & Distribution Management (TDM)",
                "Warehousing & Distribution Facilities Management (W&DFM)"
            ]
        )
        if st.button("Save Profile"):
            profiles[enrollment] = {
                "name": name,
                "section": section,
                "subjects": subjects
            }
            save_profiles(profiles)
            st.success("Profile Saved!")

    elif choice == "Edit Profile":
        st.subheader("Edit Profile")
        enrollment = st.selectbox("Select Enrollment Number", list(profiles.keys()))
        if enrollment:
            profile = profiles[enrollment]
            name = st.text_input("Enter Name", profile["name"])
            section = st.selectbox("Select Section", ["A", "B", "C"], index=["A", "B", "C"].index(profile["section"]))
            subjects = st.multiselect(
                "Select Subjects",
                [
                    "Innovation, Entrepreneurship and Start-ups (IES)",
                    "Know yourself (KY)",
                    "Professional Ethics (PE)",
                    "Bibliophiles (Bibl)",
                    "Psychology in Business (PB-A)",
                    "International Business (IB)",
                    "Project Management (PM)",
                    "E-Business (E.Bus)",
                    "Consumer Behaviour (CB)",
                    "Integrated Marketing Communication (IMC)",
                    "Sales & Distribution Management (S&DM)",
                    "Marketing Analytics (Man)",
                    "Strategic Brand Management (SBM)",
                    "Financial Statement Analysis (FSA)",
                    "Business Valuation (BussV)",
                    "Security and Portfolio Management (SPM)",
                    "International Finance (IF)",
                    "Management of Banks (MoB)",
                    "Programming for Analytics (PA)",
                    "Text Mining and Sentiment Analytics (TM&SA)",
                    "Data Mining and Visualization (DMV)",
                    "Analytics for Service Operations (ASO)",
                    "AI and Machine Learning (AIML)",
                    "Digital Media (DM)",
                    "Media Production and Consumption (MPC)",
                    "Media and Sports Industry (MSI)",
                    "Media Research Tools and Analytics (MRTA)",
                    "Media Cost Management & Control (MCMC)",
                    "Performance Management System (PMS)",
                    "Talent Acquisition (TA)",
                    "Learnings & Development (L&D)",
                    "Compensation & Reward Management (C&RM)",
                    "Purchasing & Inventory Management (P&IM)",
                    "Supply Chain Management (SCM)",
                    "Transportation & Distribution Management (TDM)",
                    "Warehousing & Distribution Facilities Management (W&DFM)"
                ],
                default=profile["subjects"]
            )
            if st.button("Update Profile"):
                profiles[enrollment] = {
                    "name": name,
                    "section": section,
                    "subjects": subjects
                }
                save_profiles(profiles)
                st.success("Profile Updated!")

    elif choice == "Delete Profile":
        st.subheader("Delete Profile")
        enrollment = st.selectbox("Select Enrollment Number", list(profiles.keys()))
        if st.button("Delete Profile"):
            if enrollment in profiles:
                del profiles[enrollment]
                save_profiles(profiles)
                st.success("Profile Deleted!")

if __name__ == "__main__":
    main()
