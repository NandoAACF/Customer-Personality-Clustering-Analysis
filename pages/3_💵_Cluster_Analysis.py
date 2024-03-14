import streamlit as st

st.set_page_config(
    page_title="Cluster Analysis",
    page_icon="💵"
)

def show_visualisasi():
    st.title('💵 Cluster Analysis')

    st.subheader('- Income')
    st.image('images/kmeans/3.png')
    st.write('Cluster 0: Income menengah bawah (25000-50000)')
    st.write('Cluster 1: Income menengah atas (50000-75000)')
    st.write('Cluster 2: Income rendah (< 25000)')
    st.write('Cluster 3: Income tinggi (> 75000)')

    st.subheader('- Total Spent')
    st.image('images/kmeans/19.png')
    st.write('Customer pada cluster 2 (income rendah) mengeluarkan uang paling sedikit ketika berbelanja.')
    st.write('Sebaliknya, customer pada cluster 3 (income tinggi) mengeluarkan uang paling banyak ketika berbelanja.')
    st.write('Walaupun cluster 0 dan 1 memiliki income yang sama (income menengah), namun cluster 0 lebih hemat dalam berbelanja dibandingkan cluster 1.')

    st.subheader('- Total Purchases')
    st.image('images/kmeans/20.png')
    st.write('Customer pada cluster 2 (income rendah) paling jarang berbelanja.')
    st.write('Sebaliknya, customer pada cluster 3 (income tinggi) cukup sering berbelanja.')
    st.write('Cluster 0 juga sering berbelanja, namun mereka membeli barang-barang murah')
    st.write('Cluster 1 sering berbelanja, namun sering membeli barang-barang mahal')

    st.subheader('- Total Children')
    st.image('images/kmeans/18.png')
    st.write('Mayoritas customer pada cluster 3 tidak memiliki anak. Sebaliknya, customer pada cluster 0, 1, dan 2 mayoritas memiliki 1-3 anak.')

    st.subheader('- Education')
    st.image('images/kmeans/1.png')
    st.write('Pada setiap cluster, tingkat pendidikan para customer bervariasi, yaitu undergraduate, graduate, dan post graduate.')

    st.subheader('- Status')
    st.image('images/kmeans/2.png')
    st.write('Pada setiap cluster, status para customer juga bervariasi, yaitu single dan not single.')

    st.subheader('- Recency')
    st.image('images/kmeans/4.png')
    st.write('Rata-rata sudah 50 hari sejak customer terakhir berbelanja. Maka, perusahaan perlu membuat strategi pemasaran untuk menarik minat customer agar berbelanja kembali.')

    st.subheader('- Wines')
    st.image('images/kmeans/5.png')
    st.write('Wine termasuk produk yang banyak dibeli oleh customer.')
    st.write('Cluster 1 dan cluster 3 tampak suka membeli wine.')

    st.subheader('- Fruits')
    st.image('images/kmeans/6.png')
    st.write('Tampak bahwa buah buahan juga cukup diminati oleh cluster 1 dan 3')

    st.subheader('- Meat')
    st.image('images/kmeans/7.png')
    st.write('Cluster 2 hampir tidak pernah membeli daging.')
    st.write('Perusahaan perlu membuat strategi pemasaran daging agar bisa menarik minat cluster 2.')

    st.subheader('- Fish')
    st.image('images/kmeans/8.png')
    st.write('Ikan cukup diminati oleh cluster 1 dan 3.')
    st.write('Bisa dilakukan penambahan jenis ikan agar customer tidak bosan.')

    st.subheader('- Sweet')
    st.image('images/kmeans/9.png')
    st.write('Produk manis kurang diminati oleh cluster 0 dan 2.')
    st.write('Perlu ada evaluasi dari perusahaan terkait produk ini.')

    st.subheader('- Gold')
    st.image('images/kmeans/10.png')
    st.write('Emas cukup diminati oleh cluster 0, 1, dan 3.')

    st.subheader('- Purchase with Discount')
    st.image('images/kmeans/11.png')
    st.write('Tampak bahwa cluster 3 tidak menunggu diskon untuk membeli barang.')

    st.subheader('- Purchase via Web')
    st.image('images/kmeans/12.png')
    st.write('Jumlah pembelian produk via web cukup imbang antar cluster. Web cukup efektif untuk digunakan sebagai media pemasaran.')

    st.subheader('- Purchase via Catalog')
    st.image('images/kmeans/13.png')
    st.write('Cluster 0 dan 2 sangat jarang membeli barang via katalog. Perlu dilakukan evaluasi terkait strategi pemasaran via katalog.')

    st.subheader('- Purchase via Store')
    st.image('images/kmeans/14.png')
    st.write('Tampak bahwa cluster 1 dan 3 sering membeli barang via toko.')

    st.subheader('- Web Visits')
    st.image('images/kmeans/15.png')
    st.write('Customer rata-rata mengunjungi web 0-10 kali setiap bulan.')

    st.subheader('- Days Since Registration')
    st.image('images/kmeans/16.png')
    st.write('Mayoritas customer sudah menjadi pelanggan dalam waktu yang lama.')
    st.write('Perlu ada strategi pemasaran untuk menarik customer baru.')
    
    st.subheader('- Age')
    st.image('images/kmeans/17.png')
    st.write('Customer pada cluster 2 memiliki usia yang lebih muda dibandingkan dengan cluster lainnya.')
    st.write('Rata-rata customer antara 30-80 tahun.')

show_visualisasi()
