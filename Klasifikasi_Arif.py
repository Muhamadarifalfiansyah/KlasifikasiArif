import pickle
import numpy as np
import streamlit as st

model = pickle.load(open('ekspedisi.sav', 'rb'))

st.title('prediksi kedatangan paket')
kolom1, kolom2 = st.columns(2)

with kolom1:
    Warehouse_block = st.number_input('blok gudang')
    Customer_care_calls = st.number_input('jumlah panggilan dari konsumen')
    Cost_of_the_Product = st.number_input('harga produk')
    Product_importance = st.number_input('Tingkat kepentingan produk')
    Weight_in_gms = st.number_input('berat barang')

with kolom2:
   Mode_of_Shipment = st.number_input('jalur pengiriman')
   Customer_rating = st.number_input('penilaian konsumen')
   Prior_purchases = st.number_input('jumlah transaksi sebelumnya')
   Discount_offered = st.number_input('discount yang di tawrkan')
   
prediksi = ''
if st.button('Hasil Prediksi'):
    prediksi= model.predict([[Warehouse_block, Mode_of_Shipment, Customer_care_calls, Customer_rating, 
                              Cost_of_the_Product, Prior_purchases, Product_importance, Discount_offered, Weight_in_gms]])
    
    if (prediksi [0] == 0):
        prediksi= 'paket ini datang tepat waktu'
    else:
        prediksi= 'paket ini datang terlambat'
st.success(prediksi)