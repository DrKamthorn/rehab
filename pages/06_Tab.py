import os
import bs4 as bs
import urllib.request as url

import streamlit as st

# so we can see the output side by side
st.set_page_config(layout="wide")

# i made these just to hold the test_input box so
# the rest of the output can match up below and we can
# compare easier
col1,col2 = st.beta_columns(2)
with col2:
    text = st.text_input('http://sigj.atwebpages.com/rehab/fr')

    st.write('the link:')
    st.write(text)

# thses columns will hold the comparison side-by-side
col3,col4 = st.beta_columns(2)

# your original code
with col3:
    st.subheader('Original code (1st 4 lines)')
    source = url.urlopen('https://www.yelp.com/search?cflt=beaches&find_loc=Los%20Angeles%2C%20CA&start=90')
    st.write('source')
    st.write(source)

    page_soup = bs.BeautifulSoup(source, 'html.parser')
    st.write('page soup done')
    #st.write(page_soup)

    #For Main Attributes
    mains = page_soup.find_all("div", {"class": "mainAttributes__09f24__26-vh arrange-unit__09f24__1gZC1 arrange-unit-fill__09f24__O6JFU border-color--default__09f24__R1nRO"})
    st.text('mains')
    st.write(mains)

    main = mains[0] #First item of mains
    st.write('fist item in mains')
    st.write(main)

# now im going to use that text field we created above
# as a input text to the urlopen command
with col4:
    st.subheader('Switch the url from hardcoded to text input')

    # make sure the user has actually put something in the text field
    if len(text) > 1:
        source_new = url.urlopen(text)
        st.write('source')
        st.write(source_new)

        soup_new = bs.BeautifulSoup(source_new, "html.parser")
        st.write('page soup done')

        main_new = soup_new.find_all("div", {"class": "mainAttributes__09f24__26-vh arrange-unit__09f24__1gZC1 arrange-unit-fill__09f24__O6JFU border-color--default__09f24__R1nRO"})
        st.text('mains')
        st.write(main_new)

        first_main = main_new[0]
        st.write('fist item in mains')
        st.write(first_main)

       # check if your original code creates the same soup as my new code 
        if main == first_main:
            st.write('True')