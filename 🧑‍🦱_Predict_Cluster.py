import streamlit as st
import pickle
import numpy as np

st.set_page_config(
    page_title="Predict Customer Cluster",
    page_icon="🧑‍🦱",
)

with open('models/kmeans.pickle', 'rb') as f:
    model = pickle.load(f)

def show_cluster():
    st.title('🧑‍🦱 Customer Personality Clustering')

    with st.container(border=True):
        st.info('📢 Untuk keperluan demo, nilai inputan digenerate secara random jika tidak diisi. Tujuannya supaya memudahkan jika ingin mencoba-coba sistem prediksi ini.')

        if "rand_init" not in st.session_state:
            st.session_state.rand_education = np.random.randint(0, 3)
            st.session_state.rand_marital_status = np.random.randint(0, 2)
            st.session_state.rand_income = np.random.randint(0, 100000)
            st.session_state.rand_recency = np.random.randint(0, 100)
            st.session_state.rand_wine = np.random.randint(0, 1000)
            st.session_state.rand_fruit = np.random.randint(0, 150)
            st.session_state.rand_meat = np.random.randint(0, 900)
            st.session_state.rand_fish = np.random.randint(0, 200)
            st.session_state.rand_sweet = np.random.randint(0, 200)
            st.session_state.rand_gold = np.random.randint(0, 200)
            st.session_state.rand_deals = np.random.randint(0, 10)
            st.session_state.rand_web = np.random.randint(0, 10)
            st.session_state.rand_catalog = np.random.randint(0, 10)
            st.session_state.rand_store = np.random.randint(0, 15)
            st.session_state.rand_web_visits = np.random.randint(0, 10)
            st.session_state.rand_days_since_last_registration = np.random.randint(3000, 4250)
            st.session_state.rand_age = np.random.randint(15, 80)
            st.session_state.rand_children = np.random.randint(0, 5)
            st.session_state.rand_init = True

        education = st.selectbox('Education', ("Undergraduate", "Graduate", "Post Graduate"), index=st.session_state.rand_education)
        if education == 'Undergraduate':
            education = 2
        elif education == 'Graduate':
            education = 0
        elif education == 'Post Graduate':
            education = 1

        marital_status = st.selectbox('Status', ("Not Single", "Single"), index=st.session_state.rand_marital_status)
        if marital_status == 'Not Single':
            marital_status = 0
        elif marital_status == 'Single':
            marital_status = 1

        # rand_income = np.random.randint(0, 100000)
        income = st.number_input('Income (in USD per year)', value=st.session_state.rand_income, step=2000, min_value=0, placeholder="e.g. 50000")

        # rand_recency = np.random.randint(0, 100)
        Recency = st.number_input("Number of days since customer's last purchase", value=st.session_state.rand_recency, step=1, min_value=0, placeholder="e.g. 40")

        # rand_wine = np.random.randint(0, 1000)
        MntWines = st.number_input('Money Spent for Wine (in USD)', value=st.session_state.rand_wine, step=1, min_value=0, placeholder="e.g. 300")

        # rand_fruit = np.random.randint(0, 150)
        MntFruits = st.number_input('Money Spent for Fruits', value=st.session_state.rand_fruit, step=1, min_value=0, placeholder="e.g. 70")

        # rand_meat = np.random.randint(0, 900)
        MntMeatProducts = st.number_input('Money Spent for Meat', value=st.session_state.rand_meat, step=1, min_value=0, placeholder="e.g. 200")

        # rand_fish = np.random.randint(0, 200)
        MntFishProducts = st.number_input('Money Spent for Fish', value=st.session_state.rand_fish, step=1, min_value=0, placeholder="e.g. 100")

        # rand_sweet = np.random.randint(0, 200)
        MntSweetProducts = st.number_input('Money Spent for Sweet', value=st.session_state.rand_sweet, step=1, min_value=0, placeholder="e.g. 100")

        # rand_gold = np.random.randint(0, 200)
        MntGoldProds = st.number_input('Money Spent for Gold', value=st.session_state.rand_gold, step=1, min_value=0, placeholder="e.g. 100")

        # rand_deals = np.random.randint(0, 10)
        NumDealsPurchases = st.number_input('Number of Purchases with Discount', value=st.session_state.rand_deals, step=1, min_value=0, placeholder="e.g. 3")

        # rand_web = np.random.randint(0, 10)
        NumWebPurchases = st.number_input('Number of Purchases via Web', value=st.session_state.rand_web, step=1, min_value=0, placeholder="e.g. 3")

        # rand_catalog = np.random.randint(0, 10)
        NumCatalogPurchases = st.number_input('Number of Purchases via Catalog', value=st.session_state.rand_catalog, step=1, min_value=0, placeholder="e.g. 3")

        # rand_store = np.random.randint(0, 15)
        NumStorePurchases = st.number_input('Number of Purchases via Store', value=st.session_state.rand_store, step=1, min_value=0, placeholder="e.g. 3")

        # rand_web_visits = np.random.randint(0, 10)
        NumWebVisitsMonth = st.number_input('Number of Visits to Web', value=st.session_state.rand_web_visits, step=1, min_value=0, placeholder="e.g. 5")

        # rand_days_since_last_registration = np.random.randint(3000, 4250)
        days_since_last_registration = st.number_input('Days Since Registration', value=st.session_state.rand_days_since_last_registration, step=1, min_value=0, placeholder="e.g. 200")

        # rand_age = np.random.randint(1, 80)
        Age = st.select_slider('Age', options=[i for i in range(1, 110)], value=st.session_state.rand_age)

        # rand_children = np.random.randint(0, 5)
        Total_Children = st.select_slider('Total Children', options=[i for i in range(0, 10)], value=st.session_state.rand_children)

        col1, col2 = st.columns([0.197,0.7])

        with col1:
            ok = st.button("🔍 Show Cluster")
        
        with col2:
            if st.button('🔄 Generate Another Random Data'):
                st.session_state.clear()
                st.experimental_rerun()

        if ok:
            Total_Spent = MntWines + MntFruits + MntMeatProducts + MntFishProducts + MntSweetProducts + MntGoldProds
            Total_Purchases = NumDealsPurchases + NumWebPurchases + NumCatalogPurchases + NumStorePurchases

            X = np.array([education, marital_status, income, Recency, MntWines, MntFruits, MntMeatProducts, MntFishProducts, MntSweetProducts, MntGoldProds, NumDealsPurchases, NumWebPurchases, NumCatalogPurchases, NumStorePurchases, NumWebVisitsMonth, days_since_last_registration, Age, Total_Children, Total_Spent, Total_Purchases])

            cluster = model.predict([X])

            # st.write(Total_Children)

            if cluster == 0:
                st.markdown(f"<h3>Customer Cluster: <span style='color: green'>0</span></h3>", unsafe_allow_html=True)
                st.write('**Karakteristik Cluster 0:**')
                st.write('- Income menengah bawah (25000-50000)')
                st.write('- Hemat dalam berbelanja')
                st.write('- Mayoritas memiliki anak')
                st.write('- Jarang membeli barang via katalog')
            elif cluster == 1:
                st.markdown(f"<h3>Customer Cluster: <span style='color: green'>1</span></h3>", unsafe_allow_html=True)
                st.write('**Karakteristik Cluster 1:**')
                st.write('- Income menengah atas (50000-75000)')
                st.write('- Lebih boros dalam berbelanja')
                st.write('- Suka membeli wine')
            elif cluster == 2:
                st.markdown(f"<h3>Customer Cluster: <span style='color: green'>2</span></h3>", unsafe_allow_html=True)
                st.write('**Karakteristik Cluster 2:**')
                st.write('- Income rendah (< 25000)')
                st.write('- Jarang berbelanja')
                st.write('- Orang berusia lebih muda')
                st.write('- Hampir tidak pernah membeli daging')
                st.write('- Membeli barang ketika ada diskon')
            elif cluster == 3:
                st.markdown(f"<h3>Customer Cluster: <span style='color: green'>3</span></h3>", unsafe_allow_html=True)
                st.write('**Karakteristik Cluster 3:**')
                st.write('- Income tinggi (> 75000)')
                st.write('- Mengeluarkan paling banyak uang ketika berbelanja')
                st.write('- Mayoritas tidak memiliki anak')
                st.write('- Suka membeli berbagai macam variasi produk')
                st.write('- Tidak menunggu diskon untuk membeli barang')
            st.info('📢 Silakan klik tombol "Generate Another Random Data" untuk mencoba variasi inputan lainnya.')

show_cluster()