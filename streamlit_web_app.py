# streamlit run .\Desktop\python_tests\streamlit_web_app.py

import streamlit as st
import time
import requests
import json

import pandas as pd
import numpy as np
import plost
from PIL import Image

# ------------------------------ Page setting ------------------------------
st.set_page_config( page_title = "THE F.I.R.S.T",
					layout = "wide")
st.title("--- Ground Control Station ---")
st.markdown("#")

# ------------------------------ Initialization ------------------------------

# ------- Variables -------
usv_data = 0
print_data = 0

control_panel_header = st.empty()
display_header = st.empty()
control_board = st.empty()
display_section = st.empty()

mode = ""
lat = 0
lng = 0

# ------------------------------ Interactive content ------------------------------
with control_panel_header:
	st.header("Control panel")
# ---------------- Control board ----------------
control_board.empty()
with control_board.container():
	mode = st.selectbox('Mode',('Waypoints','Zigzac path'), key=1)
	st.write('Selected mode: ', mode)
	lat = st.number_input('Waypoint latitude', key=2)
	st.write('Selected latitude: ', lat)
	lng = st.number_input('Waypoint longitude', key=3)
	st.write('Selected longitude: ', lng)



# ---------------------------------------- WHILE LOOP ----------------------------------------
# ----------------------------------------............----------------------------------------
while True:

	# ----------------------------- Data requests -----------------------------
	rep_obj = requests.get("http://127.0.0.1:8000/get_data/motor")
	rep_content = rep_obj.json()[0]
	rep_text = json.dumps(rep_content) 

	# ----------------------------- Data manipulation -----------------------------
	print(rep_text)
	usv_data = int(rep_text)
	print_data = usv_data * 2 

	# ------------------------------ Read-only content ------------------------------
	with display_header:
		st.header("USV's Data")

	# ---------------- USV's states ----------------
	display_section.empty()
	with display_section.container():
		st.subheader("Motor 1 = {}".format(print_data))

