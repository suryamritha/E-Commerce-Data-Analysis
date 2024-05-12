import streamlit as st
import plotly.express as px
import pandas as pd
import os
import warnings
warnings.filterwarnings('ignore')

st.set_page_config(page_title="E-Comm", page_icon=":bar_chart:",layout="wide")

st.title(" :bar_chart: Analyzing Electronics Sales Trends in E-Commerce")
st.markdown('<style>div.block-container{padding-top:1rem;}</style>',unsafe_allow_html=True)

df = pd.read_csv("C:\\Users\\Varshini\\Downloads\\E-Commerce Survey (Responses) - Form responses 1 (1).csv")
total_rows, total_cols = df.shape
# Create a sidebar expander titled "Dataset Size"
with st.sidebar.expander("Dataset Size"):
    # Display total number of rows and columns
    st.write(f"Total number of rows: {total_rows}")
    st.write(f"Total number of columns: {total_cols}")
    
with st.sidebar.expander("Age Group"):
    age_group_counts = df['Which age group do you belong to?'].value_counts()
    st.write("Frequency distribution of age groups:")
    st.write(age_group_counts)

with st.sidebar.expander("Gender"):
    # Display frequency distribution of gender
    gender_counts = df['Gender'].value_counts()
    st.write("\nFrequency distribution of gender:")
    st.write(gender_counts)

import streamlit as st
import plotly.express as px
import pandas as pd


col1, col2 = st.columns(2)

# Plot pie chart for gender distribution
with col1:
    st.subheader("Gender Distribution")
    fig_gender = px.pie(names=gender_counts.index, values=gender_counts.values, hole=0.5)
    fig_gender.update_traces(textposition="inside", textinfo="percent+label")
    st.plotly_chart(fig_gender, use_container_width=True)
    


# Plot pie chart for age group distribution
with col2:
    st.subheader("Age Group Distribution")
    fig_age = px.pie(names=age_group_counts.index, values=age_group_counts.values, hole=0.5)
    fig_age.update_traces(textposition="inside", textinfo="percent+label")
    st.plotly_chart(fig_age, use_container_width=True)

col1, col2 = st.columns(2)
with col1:
    elec_counts = df['How do you purchase electronic items such as mobile phones, laptops, watches, and TVs?'].value_counts()
    st.subheader("Where do you purchase electronic items?")
    fig_elec = px.pie(names=elec_counts.index, values=elec_counts.values, hole=0.5)
    fig_elec.update_traces(textposition="inside", textinfo="percent")
    st.plotly_chart(fig_elec, use_container_width=True)
with col2:
    price_counts = df['How satisfied are you with the pricing of electronic items on e-commerce websites compared to offline stores?'].value_counts()
    st.subheader("Price satisfaction")
    fig_price = px.pie(names=price_counts.index, values=price_counts.values, hole=0.5)
    fig_price.update_traces(textposition="inside", textinfo="percent")
    st.plotly_chart(fig_price, use_container_width=True)


column_name = "What factors influence your decision to purchase electronic items from e-commerce websites or offline stores? (Select all that apply)"
factor_labels = df[column_name]
label_counts = factor_labels.str.split(', ', expand=True).stack().value_counts()
label_counts = label_counts[label_counts <= 250]
total_responses = label_counts.sum()
label_percentages = (label_counts / 387) * 100
fig = px.bar(x=label_counts.values, y=label_counts.index, orientation='h', text=label_counts.values,
             labels={'x': 'Number of Responses', 'y': 'Factors'},
             title='Factors influencing purchase decisions',
             color=label_counts.values,
             color_continuous_scale='Blues')
fig.update_xaxes(range=[0, 250])
text = [f"{count} ({percentage:.2f}%)" for count, percentage in zip(label_counts.values, label_percentages)]
fig.update_traces(text=text, textposition='outside')
st.plotly_chart(fig, use_container_width=True)

col1, col2 = st.columns(2)
with col1:
    mode_counts = df['Which channel do you find more convenient for purchasing electronic items?'].value_counts()
    st.subheader("Which mode is more convenient for purchasing electronic items?")
    fig_mode = px.pie(names=mode_counts.index, values=mode_counts.values, hole=0.5)
    fig_mode.update_traces(textposition="inside", textinfo="percent")
    st.plotly_chart(fig_mode, use_container_width=True)
with col2:
    exep_counts = df['How would you rate the overall shopping experience when purchasing electronic items from e-commerce websites compared to offline stores?'].value_counts()
    st.subheader("Overall shopping experience")
    fig_exep = px.pie(names=exep_counts.index, values=exep_counts.values, hole=0.5)
    fig_exep.update_traces(textposition="inside", textinfo="percent")
    st.plotly_chart(fig_exep, use_container_width=True)


column_name = "What type of electronic gadgets do you typically purchase online? (Select all that apply)"
factor_labels = df[column_name]
label_counts = factor_labels.str.split(', ', expand=True).stack().value_counts()
total_responses = label_counts.sum()
label_percentages = (label_counts / 387) * 100
fig = px.bar(x=label_counts.values, y=label_counts.index, orientation='h', text=label_counts.values,
             labels={'x': 'Number of Responses', 'y': 'Gadgets'},
             title='Type of electronic gadgets typically purchased online',
             color=label_counts.values,
             color_continuous_scale='Peach')
fig.update_xaxes(range=[0, 300])
text = [f"{count} ({percentage:.2f}%)" for count, percentage in zip(label_counts.values, label_percentages)]
fig.update_traces(text=text, textposition='outside')
st.plotly_chart(fig, use_container_width=True)


selected_columns = ["How satisfied are you with the pricing of electronic items on e-commerce websites compared to offline stores?", "Which channel do you find more convenient for purchasing electronic items?", "How would you rate the overall shopping experience when purchasing electronic items from e-commerce websites compared to offline stores?", "How frequently do you purchase electronic gadgets online?", "How would you rate your overall satisfaction with the variety of electronic gadgets available on e-commerce website?", "How likely are you to recommend e-commerce website to others for purchasing electronic gadgets?", "How important are customer reviews and ratings in influencing your decision to purchase electronic gadgets online?", "How often do you rely on comparison tools or features to compare different electronic gadgets before making a purchase decision?"]
def plot_pie_chart(selected_column):
    selected_data = df[selected_column].dropna()
    response_counts = selected_data.value_counts()

    fig = px.pie(names=response_counts.index, values=response_counts.values, hole=0.5)
    fig.update_traces(textinfo='percent', textposition='inside')
    st.plotly_chart(fig, use_container_width=True)

selected_column = st.selectbox("All about Electronics on E-Commerce:", selected_columns)

if selected_column:
    st.subheader(f"{selected_column}")
    plot_pie_chart(selected_column)

column_name = "During which occasions or festivals do you prefer to purchase electronic items from e-commerce websites or offline stores? (Select all that apply)"
factor_labels = df[column_name]
label_counts = factor_labels.str.split(', ', expand=True).stack().value_counts()
total_responses = label_counts.sum()
label_percentages = (label_counts / 387) * 100
fig = px.bar(x=label_counts.values, y=label_counts.index, orientation='h', text=label_counts.values,
             labels={'x': 'Number of Responses', 'y': 'Ocassions'},
             title='Occasions or festivals for purchasing electronic items',
             color=label_counts.values,
             color_continuous_scale='Peach')
fig.update_xaxes(range=[0, 300])
text = [f"{count} ({percentage:.2f}%)" for count, percentage in zip(label_counts.values, label_percentages)]
fig.update_traces(text=text, textposition='outside')
st.plotly_chart(fig, use_container_width=True)

column_name = "During which occasions or festivals do you prefer to purchase electronic items from e-commerce websites or offline stores? (Select all that apply)"
factor_labels = df[column_name]
label_counts = factor_labels.str.split(', ', expand=True).stack().value_counts()

# Select top 5 gadgets
top_5_gadgets = label_counts.head(5)

# Plot pie chart for top 5 gadgets
fig = px.pie(names=top_5_gadgets.index, values=top_5_gadgets.values, hole=0.5,
             title='Top 5 ocassions')
fig.update_traces(textinfo='percent', textposition='inside')
st.plotly_chart(fig, use_container_width=True)

import streamlit as st
import pandas as pd
import plotly.express as px

column_name = "Which e-commerce website do you prefer the most for purchasing electronic gadgets?"
factor_labels = df[column_name].dropna()

# Count the occurrences of each label
label_counts = factor_labels.value_counts()

# Calculate total number of responses
total_responses = label_counts.sum()

# Calculate percentage for each label
label_percentages = (label_counts / total_responses) * 100

# Combine number of responses and percentage for hover text
hover_text = [f"Responses: {count}<br>Percentage: {percentage:.2f}%" 
              for count, percentage in zip(label_counts.values, label_percentages)]

# Plot line graph
fig = px.line(x=label_counts.index, y=label_counts.values, 
              labels={'x': 'E-commerce Website', 'y': 'Number of Responses'},
              title='Preferences for Purchasing Electronic Gadgets by E-commerce Website',
              hover_data={"y": label_counts.values, "y_percent": label_percentages},
              hover_name=hover_text)
st.plotly_chart(fig, use_container_width=True)


selected_columns = ["How often do you rely on comparison tools or features to compare different electronic gadgets before making a purchase decision?","How important are customer reviews and ratings in influencing your decision to purchase electronic gadgets online?", "Which payment method do you prefer when purchasing electronic gadgets online?"]
def plot_pie_chart(selected_column):
    selected_data = df[selected_column].dropna()
    response_counts = selected_data.value_counts()

    fig = px.pie(names=response_counts.index, values=response_counts.values, hole=0.5)
    fig.update_traces(textinfo='percent', textposition='inside')
    st.plotly_chart(fig, use_container_width=True)

selected_column = st.selectbox("How users compare products.", selected_columns)

if selected_column:
    st.subheader(f"{selected_column}")
    plot_pie_chart(selected_column)


column_index = 14

# Filter the column to include only numeric values between 1 and 10
ratings_column = df.iloc[:, column_index]
valid_ratings = ratings_column[ratings_column.between(1, 10)]

# Count the occurrences of each rating
rating_counts = valid_ratings.value_counts().sort_index()

# Calculate percentage for each rating
total_responses = rating_counts.sum()
rating_percentages = (rating_counts / total_responses) * 100

# Plot vertical bar chart
fig = px.bar(x=rating_counts.index, y=rating_counts.values, 
             labels={'x': 'Rating', 'y': 'Count'},
             title='How satisfied are the users with the user experience (navigation, search functionality, checkout process, etc.) when browsing electronic gadgets on website?',
             color=rating_counts.index,
             color_continuous_scale='Purp')

# Set the layout for the bar chart
fig.update_layout(xaxis={'title': 'Rating', 'tickmode': 'linear', 'dtick': 1},
                  yaxis={'title': 'Count'})

# Add count and percentage text on top of each bar
text = [f"Count: {count}<br>Percentage: {percentage:.2f}%" 
        for count, percentage in zip(rating_counts.values, rating_percentages)]
fig.update_traces(text=text, textposition='outside')

# Display the plot
st.plotly_chart(fig, use_container_width=True)


gadgets_df = df['What type of electronic gadgets do you typically purchase online? (Select all that apply)'].str.split(', ', expand=True)

# Add the 'Gender' column to the gadgets DataFrame
gadgets_df['Gender'] = df['Gender']

# Melt the DataFrame to convert columns into rows
gadgets_df = gadgets_df.melt(id_vars=['Gender'], value_name='Gadget').dropna()

# Count the occurrences of each gadget category within each gender
gadget_counts = gadgets_df.groupby(['Gender', 'Gadget']).size().reset_index(name='Count')

# Define a function to create bar plots for top 5 products
def plot_top_5_products(df, selected_genders):
    for gender in selected_genders:
        subset = df[df['Gender'] == gender]
        top_5 = subset.nlargest(5, 'Count')
        fig = px.bar(top_5, x='Count', y='Gadget', color='Gadget', 
                     labels={'Count': 'Count', 'Gadget': 'Product'},
                     title=f'Top 5 Products Bought by {gender}',
                     orientation='h')
        st.plotly_chart(fig)

# Get unique genders
unique_genders = gadgets_df['Gender'].unique()

# Display multiselect widget for choosing genders
selected_genders = st.multiselect("Top 5 products purchased by: (gender)", unique_genders)

# Plot the top 5 products for each selected gender
if selected_genders:
    plot_top_5_products(gadget_counts, selected_genders)



gadgets_df = df['What type of electronic gadgets do you typically purchase online? (Select all that apply)'].str.split(', ', expand=True)

# Add the column at index 2 to the gadgets DataFrame
gadgets_df['Column_2'] = df.iloc[:, 1]  # Assuming the column is unnamed or you know the name

# Melt the DataFrame to convert columns into rows
gadgets_df = gadgets_df.melt(id_vars=['Column_2'], value_name='Gadget').dropna()

# Count the occurrences of each gadget category within each unique value in column index 2
gadget_counts = gadgets_df.groupby(['Column_2', 'Gadget']).size().reset_index(name='Count')

# Define a function to create bar plots for top 5 products
def plot_top_5_products(df, selected_values):
    for value in selected_values:
        subset = df[df['Column_2'] == value]
        top_5 = subset.nlargest(5, 'Count')
        fig = px.bar(top_5, x='Count', y='Gadget', color='Gadget', 
                     labels={'Count': 'Count', 'Gadget': 'Product'},
                     title=f'Top 5 Products Bought by {value}',
                     orientation='h')
        st.plotly_chart(fig)

# Get unique values from column index 2
unique_values = gadgets_df['Column_2'].unique()

# Display multiselect widget for choosing unique values
selected_values = st.multiselect("Top 5 products purchased by: (age )", unique_values)

# Plot the top 5 products for each selected unique value
if selected_values:
    plot_top_5_products(gadget_counts, selected_values)