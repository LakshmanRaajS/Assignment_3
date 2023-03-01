import requests
import streamlit as st
from requests.exceptions import HTTPError
import time
from pages.Login import my_token

if 'access_token' not in st.session_state:
    st.session_state.access_token = ''

def goes18(my_token):
    headers = {"Authorization": f"Bearer {my_token}"}
    st.markdown("<h1 style='text-align: center;'>GOES-18</h1>", unsafe_allow_html=True)
    st.header("")
    st.header("Search by Fields")
    st.header("")

    BASE_URL = "http://localhost:8090"

    col1, col2, col3 = st.columns(3, gap="large")

    # Make a request to the endpoint to retrieve the list of years
    year_response = (requests.get(BASE_URL + '/list-years-goes', headers=headers)).json()
    year_list = year_response["year_list"]


    with col1:
        year = st.selectbox(
            'Select the Year :',
            (year_list))
        st.write('You selected :', year)


    # Make a request to the endpoint to retrieve the list of days for the selected year
    day_response = requests.post(BASE_URL + f'/list-days-goes?year={year}', headers=headers).json()
    day_list = day_response["days_list"]


    with col2:
        day = st.selectbox(
            'Select the Day :',
            (day_list))
        st.write('You selected :', day)
    

    # Make a request to the endpoint to retrieve the list of hours for the selected year and day
    hour_response = (requests.post(BASE_URL + f'/list-hours-goes?year={year}&day={day}', headers=headers)).json()
    hour_list = hour_response['hours_list']


    with col3:
        hour = st.selectbox(
            'Select the Hour :',
            (hour_list))
        st.write('You selected :', hour)
    st.header("")


    # Make a request to the endpoint to retrieve the list of files for the selected year, day and hour
    file_list_response = (requests.post(BASE_URL + f'/list-files-goes?year={year}&day={day}&hour={hour}', headers=headers)).json()
    file_list = file_list_response["file_list"]


    selected_file = st.selectbox("Select link for download", 
                (file_list),  
                key=None, help="select link for download")


    st.header("")


    if st.button('Generate using Filter'):

        headers = {"Authorization": f"Bearer {my_token}"}
        # Make a request to the endpoint to fetch the url for the selected file
        file_url_response = requests.post(BASE_URL + f'/fetch-url-goes?name={selected_file}', headers=headers).json()
        file_url = file_url_response["url"]

        # Display the url for the selected file
        st.write('Download Link : ', file_url)

        # Make a request to the endpoint to fetch the url for the selected file from the GOES18 bucket for validation
        validation_url_response = requests.post(BASE_URL + f'/validate-url-goes?name={selected_file}', headers=headers).json()
        validation_url = validation_url_response["url"]
        
        st.write("NOAA bucket path for verfication : ", validation_url)

    st.header("")
    st.header("Search by Filename")
    st.header("")


    filename = st.text_input('Enter Filename')
    st.header("")


    if st.button('Generate using Name'):

        # Set up the headers for authenticated requests
        headers = {"Authorization": f"Bearer {my_token}"}

        try:
            # Copies the file from GOES18 bucket to User bucket and generates download URL
            file_url_response = requests.post(BASE_URL + f'/fetch-url-goes-from-name?name={filename}', headers=headers).json()
            file_url = file_url_response["url"]    

            # Display the url for the selected file
            st.write('Download Link : ', file_url)
        
        except Exception as error:
            st.error(f"Error: {error}")
    
if "access_token" not in st.session_state or st.session_state['access_token']=='':
    st.title("Please sign-in to access this feature!")
else:
    goes18(st.session_state["access_token"])