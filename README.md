# tools_remote
tools remote ping ip and curl 
# tools ini berguna untuk ping beberapa ip secara bersamaan
# tools ini berguna untuk get request code web ( curl )

#syarat :
python 3.x.x

cara penggunaan aplikasi ini :
1. buat database di postgreSQL dengan nama bebas tinggal sesuaikan dengan codingan
2. buat 2 table 1 untuk ping tools 1 untuk request code ( CURL ) katakanlah
   - table ping = ( id, ip, status, tanggal )
   - table request = ( id, req, status,  tanggal )
3. cocokan struktur database anda dengan codingan
4. run ( jalankan )

