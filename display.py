def print_result(principal, rate, years, ci, si):
    print("\n===== HASIL PERHITUNGAN TABUNGAN =====")
    print(f"Saldo Awal           : ¥{principal:,.1f}")
    print(f"Bunga Tahunan        : {rate * 100:.1f}%")
    print(f"Lama Menabung        : {years} tahun")
    print("-" * 52)
    print(f"Nilai Akhir (Bunga Majemuk)  : ¥{ci:,.2f}")
    print(f"Nilai Akhir (Bunga Sederhana): ¥{si:,.2f}")
    print("====================================================")