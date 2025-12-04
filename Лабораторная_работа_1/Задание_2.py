# TODO Найдите количество книг, которое можно разместить на дискете

one_kb_in_b = 1024
one_mb_in_kb = 1024
one_gb_in_mb = 1024
one_tb_in_gb = 1024


v_disk_mb = 1.44
n_paige = 100
n_str_paige = 50
n_sim_in_str = 25
one_code_in_sim_b = 4

v_sim = one_code_in_sim_b * n_sim_in_str
v_str = v_sim * n_str_paige
v_one_book = v_str * n_paige

v_one_book_kb = v_one_book / one_kb_in_b
v_one_book_mb = v_one_book_kb / one_mb_in_kb
n_book_in_disk = int(v_disk_mb / v_one_book_mb)

print("Количество книг, помещающихся на дискету:", n_book_in_disk)
