import streamlit as st

def show_insight_perusahaan():
    st.title('🏭 Insights for Company')
    st.write('Berdasarkan page Cluster Analysis, berikut ada beberapa insight dan masukan untuk perusahaan:')
    st.write('1. Memberikan diskon pada daging untuk menarik minat customer yang memiliki income rendah, seperti cluster 2.')
    st.write('2. Perlu ada evaluasi dari perusahaan terkait produk manis karena kurang diminati oleh cluster 0 dan 2.')
    st.write('3. Perlu dilakukan evaluasi terkait strategi pemasaran via katalog karena beberapa cluster jarang membeli barang via katalog.')
    st.write('4. Menambah variasi wine karena termasuk produk yang paling banyak diminati.')
    st.write('5. Menambah produk yang berkaitan dengan konsumsi anak karena sebagian besar customer memiliki anak.')
    st.write('6. Memberikan promo pada customer yang loyal karena sebagian besar customer sudah menjadi pelanggan dalam waktu yang lama.')
    st.write('7. Memberikan promo pada customer yang memiliki income rendah karena mereka mengeluarkan uang paling sedikit ketika berbelanja.')
    st.write('8. Memaksimalkan pemasaran via web karena mayoritas customer mengunjungi web 0-10 kali setiap bulan.')
    st.write('9. Perlu merencanakan strategi pemasaran untuk menarik customer baru karena mayoritas customer sudah menjadi pelanggan dalam waktu yang lama.')

show_insight_perusahaan()