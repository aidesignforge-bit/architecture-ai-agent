import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Architecture AI Agent", page_icon="🏗️", layout="wide")

st.title("🏗️ Architecture Layout & Project Data AI Agent")
st.caption("V1 • Layout processing • Project data • Dimensions • Canva-ready workflow")

if "project" not in st.session_state:
    st.session_state.project = {}

tabs = st.tabs([
    "① Project Search",
    "② Layout / Brochure",
    "③ Dimensions",
    "④ Project Details",
    "⑤ Canva Templates",
    "⑥ Export"
])

with tabs[0]:
    st.subheader("Project Information")
    c1, c2 = st.columns(2)
    with c1:
        project = st.text_input("Project Name", placeholder="e.g. ABC Heights")
        builder = st.text_input("Builder / Developer")
        location = st.text_input("City / Location")
    with c2:
        rera = st.text_input("RERA Number")
        address = st.text_input("Address")
        source_url = st.text_input("Official Project Website")

    if st.button("Save Project"):
        st.session_state.project = {
            "project": project, "builder": builder, "location": location,
            "rera": rera, "address": address, "source_url": source_url
        }
        st.success("Project information saved.")

    st.info("Verification rule: if a reliable source cannot confirm a field, the final value should be NOT FOUND — never guessed.")

with tabs[1]:
    st.subheader("Upload Layout / Brochure")
    uploaded = st.file_uploader(
        "Upload JPG, PNG or PDF",
        type=["jpg", "jpeg", "png", "pdf"],
        accept_multiple_files=True
    )
    if uploaded:
        st.success(f"{len(uploaded)} file(s) uploaded.")
        for f in uploaded:
            st.write(f"• {f.name} — {f.size:,} bytes")

    st.markdown("### Brochure workflow")
    st.code("""PDF
 ↓
Detect pages
 ↓
Detect every layout on each page
 ↓
Separate Layout A / B / C / ...
 ↓
Preserve geometry + labels
 ↓
Clean / enhance
 ↓
Dimension verification
 ↓
Export each layout separately""")

    st.checkbox("Keep original geometry and room labels", value=True)
    st.checkbox("Remove unnecessary visual noise", value=True)
    st.checkbox("Prepare high-resolution output", value=True)

with tabs[2]:
    st.subheader("Dimension Converter")
    c1, c2, c3 = st.columns(3)
    with c1:
        value = st.number_input("Value", min_value=0.0, value=3600.0)
    with c2:
        unit = st.selectbox("Original Unit", ["mm", "cm", "m", "inch", "ft"])
    with c3:
        output = st.selectbox("Output", ["Feet + Inches", "Feet", "Inches"])

    factors = {"mm": 0.03937007874, "cm": 0.3937007874, "m": 39.37007874,
               "inch": 1.0, "ft": 12.0}
    inches = value * factors[unit]

    feet = int(inches // 12)
    rem = inches - feet * 12
    st.metric("Converted Dimension", f"{feet}'-{rem:.2f}\"")

    st.warning("If the original dimension is unreadable or ambiguous, mark it NEEDS REVIEW instead of guessing.")

    status = st.selectbox("Dimension Status",
                          ["VERIFIED", "SOURCE CHECK", "NEEDS REVIEW", "NOT FOUND"])
    st.write("Status:", status)

with tabs[3]:
    st.subheader("Project Detail Extraction")
    fields = [
        "Project Name", "Builder", "Location", "Address", "RERA No.",
        "Towers", "Floors", "Apartments", "Units / Tower", "Lifts",
        "BHK", "Apartment Size", "Carpet Area", "Super Area",
        "Launch Date", "Possession", "Project Status", "Amenities",
        "Project Logo", "Builder Logo"
    ]

    cols = st.columns(2)
    for i, field in enumerate(fields):
        with cols[i % 2]:
            val = st.text_input(field, placeholder="Enter verified value or NOT FOUND",
                                key=f"field_{i}")
            if not val:
                st.caption("Status: NOT FOUND")

with tabs[4]:
    st.subheader("Canva Template & Page Size")
    template = st.selectbox("Template", [
        "Template 01 — Layout",
        "Template 02 — Project Presentation"
    ])

    size = st.selectbox("Page Size Preset", [
        "A4 Portrait", "A4 Landscape", "A3", "A2", "A1", "Custom"
    ])

    if size == "Custom":
        c1, c2, c3 = st.columns(3)
        with c1:
            w = st.number_input("Width", min_value=1.0, value=297.0)
        with c2:
            h = st.number_input("Height", min_value=1.0, value=210.0)
        with c3:
            u = st.selectbox("Unit", ["mm", "cm", "inch", "px", "ft"])

    st.markdown("### Required template behavior")
    st.checkbox("Project name at top", value=True)
    st.checkbox("Project logo placement", value=True)
    st.checkbox("Builder logo placement", value=True)
    st.checkbox("Automatic layout title", value=True)
    st.checkbox("Feet + inches dimensions", value=True)

    st.info("Actual Canva editing/API connection is an integration step for V2. This prototype stores the required settings so the connector can use them.")

with tabs[5]:
    st.subheader("Export Package")
    resolution = st.selectbox("Resolution", ["4K", "8K"])
    formats = st.multiselect("Formats", ["PNG", "JPG", "PDF"], default=["PNG", "PDF"])

    st.markdown("### Output package")
    items = [
        "Project Summary",
        "Verified Project Details",
        "Master Layout",
        "Individual BHK Layouts",
        "Individual Brochure Layouts",
        "Feet + Inches Dimension Version",
        "Project Logo",
        "Builder Logo",
        "Verification / NOT FOUND Report"
    ]
    for x in items:
        st.checkbox(x, value=True, key="out_"+x)

    if st.button("Prepare Export Checklist"):
        st.success(f"Export configuration saved: {resolution} • {', '.join(formats)}")
        st.write("The final production agent will generate the selected files after the uploaded source/template is processed.")

st.divider()
st.caption("Architecture-safe principle: preserve original geometry. Never invent a dimension that cannot be verified.")
