import streamlit as st
import pickle
import numpy as np

with open('models/kmeans.pickle', 'rb') as f:
    model = pickle.load(f)

def show_cluster():
    st.title('🧑‍🦱 Customer Personality Clustering')

    education = st.selectbox('Education', ("Undergraduate", "Graduate", "Post Graduate"))
    if education == 'Undergraduate':
        education = 2
    elif education == 'Graduate':
        education = 0
    elif education == 'Post Graduate':
        education = 1

    marital_status = st.selectbox('Status', ("Not Single", "Single"))
    if marital_status == 'Not Single':
        marital_status = 0
    elif marital_status == 'Single':
        marital_status = 1

    income = st.number_input('Income (in USD per year)', value=None, step=2000, min_value=0, placeholder="e.g. 50000")

    Recency = st.number_input("Number of days since customer's last purchase", value=None, step=1, min_value=0, placeholder="e.g. 40")

    MntWines = st.number_input('Money Spent for Wine (in USD)', value=None, step=1, min_value=0, placeholder="e.g. 100")

    MntFruits = st.number_input('Money Spent for Fruits', value=None, step=1, min_value=0, placeholder="e.g. 100")

    MntMeatProducts = st.number_input('Money Spent for Meat', value=None, step=1, min_value=0, placeholder="e.g. 100")

    MntFishProducts = st.number_input('Money Spent for Fish', value=None, step=1, min_value=0, placeholder="e.g. 100")

    MntSweetProducts = st.number_input('Money Spent for Sweet', value=None, step=1, min_value=0, placeholder="e.g. 100")

    MntGoldProds = st.number_input('Money Spent for Gold', value=None, step=1, min_value=0, placeholder="e.g. 100")

    NumDealsPurchases = st.number_input('Number of Purchases with Discount', value=None, step=1, min_value=0, placeholder="e.g. 3")

    NumWebPurchases = st.number_input('Number of Purchases via Web', value=None, step=1, min_value=0, placeholder="e.g. 3")

    NumCatalogPurchases = st.number_input('Number of Purchases via Catalog', value=None, step=1, min_value=0, placeholder="e.g. 3")

    NumStorePurchases = st.number_input('Number of Purchases via Store', value=None, step=1, min_value=0, placeholder="e.g. 3")

    NumWebVisitsMonth = st.number_input('Number of Visits to Web', value=None, step=1, min_value=0, placeholder="e.g. 5")

    days_since_last_registration = st.number_input('Days Since Registration', value=None, step=1, min_value=0, placeholder="e.g. 200")

    Age = st.select_slider('Age', options=[i for i in range(1, 110)])

    Total_Children = st.select_slider('Total Children', options=[i for i in range(0, 10)])

    ok = st.button('Show Cluster')
    if ok:
        Total_Spent = MntWines + MntFruits + MntMeatProducts + MntFishProducts + MntSweetProducts + MntGoldProds
        Total_Purchases = NumDealsPurchases + NumWebPurchases + NumCatalogPurchases + NumStorePurchases
        
        X = np.array([education, marital_status, income, Recency, MntWines, MntFruits, MntMeatProducts, MntFishProducts, MntSweetProducts, MntGoldProds, NumDealsPurchases, NumWebPurchases, NumCatalogPurchases, NumStorePurchases, NumWebVisitsMonth, days_since_last_registration, Age, Total_Children, Total_Spent, Total_Purchases])

        cluster = model.predict([X])

        if cluster == 0:
            st.subheader('Customer Cluster: 0')
            st.write('**Karakteristik Cluster 0:**')
            st.write('- Income menengah bawah (25000-50000)')
            st.write('- Hemat dalam berbelanja')
            st.write('- Mayoritas memiliki anak')
            st.write('- Jarang membeli barang via katalog')
        elif cluster == 1:
            st.subheader('Customer Cluster: 1')
            st.write('**Karakteristik Cluster 1:**')
            st.write('- Income menengah atas (50000-75000)')
            st.write('- Lebih boros dalam berbelanja')
            st.write('- Suka membeli wine')
        elif cluster == 2:
            st.subheader('Customer Cluster: 2')
            st.write('**Karakteristik Cluster 2:**')
            st.write('- Income rendah (< 25000)')
            st.write('- Jarang berbelanja')
            st.write('- Orang berusia lebih muda')
            st.write('- Hampir tidak pernah membeli daging')
            st.write('- Membeli barang ketika ada diskon')
        elif cluster == 3:
            st.subheader('Customer Cluster: 3')
            st.write('**Karakteristik Cluster 3:**')
            st.write('- Income tinggi (> 75000)')
            st.write('- Mengeluarkan paling banyak uang ketika berbelanja')
            st.write('- Mayoritas tidak memiliki anak')
            st.write('- Suka membeli berbagai macam variasi produk')
            st.write('- Tidak menunggu diskon untuk membeli barang')
        

show_cluster()