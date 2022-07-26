# IMPORT ALL FILE
import formasi_query
import text_processing

# Mencari kata kunci
import itertools
from itertools import product
from collections import defaultdict
import random

"""# Query Jawaban"""

def jwbjawaban(pertanyaan):
  hasil_tag = text_processing.proses_pertanyaan(pertanyaan)
  kata_kunci = text_processing.identifikasi_kunci(hasil_tag)
  kata_objek = text_processing.identifikasi_objek(hasil_tag)
  kata_properti = text_processing.identifikasi_properti(hasil_tag)

  hasil_query = []
  for cari_properti in kata_properti:
    # Jika Kata Kunci ada 2
    if (len(kata_kunci) >= 2):
        listcoba = []
        for subset in itertools.permutations(kata_kunci, 2):
          listcoba.append(subset)
        for que, ue in listcoba:
          if (kata_objek == []):
            i = formasi_query.query_duakey(que, ue, cari_properti)
            if (i == []):
              continue;
            else:
              hasil_query.append(i);

          elif (kata_objek != []):
            for cari_objek in kata_objek: 
              i = formasi_query.query_duakey_obj(que, ue, cari_properti, cari_objek)
              if (i == []):
                continue;
              else:
                hasil_query.append(i);

        # jika masih kosong, coba cari tanpa ada relasi
        if (hasil_query == []):
          i = formasi_query.query_duakey(que, ue, cari_properti)
          if (i == []):
            continue;
          else:
            hasil_query.append(i);

  #  Jika Kata Kunci ada 1
    if (len(kata_kunci) == 1):
      # Jika Kata Objek Kosong
      if (kata_objek == []):
        i = formasi_query.query_data(kata_kunci[0], cari_properti)
        if (i == []):
          continue;
        else:
          hasil_query.append(i);
      # Jika Kata Objek Berisi
      elif (kata_objek != []):
        for cari_objek in kata_objek:
          i = formasi_query.query_obj(kata_kunci[0], cari_properti, cari_objek)
          if (i == []):
            continue;
          else: 
            hasil_query.append(i)
        
        # Jika hasil masih kosong, coba tanpa memasukkan kata objek
        if(hasil_query == []):
          i = formasi_query.query_data(kata_kunci[0], cari_properti)
          if (i == []):
            continue;
          else:
            hasil_query.append(i);

    # Jika Kata Kunci null
    if(kata_kunci == []):
      for katakata, tagtag in hasil_tag:
        i = formasi_query.query_list(katakata, cari_properti)
        if (i == []):
          continue;
        else: 
          hasil_query.append(i)
          break;

  jawaban = []
  for z in hasil_query:
    for link, info in z:
      jawaban.append(info);

  jawaban = list(dict.fromkeys(jawaban))
  if ('nama' in kata_properti):
    hasil_gelar = []
    for jwb in jawaban:
      gelar = formasi_query.query_data(jwb.lower(), 'gelar')
      if gelar != []:
        for ge in range(len(gelar)):
          gelar = gelar[ge][1]
          hasil_gelar.append(jwb +" punya nama lain/gelar " + gelar)
          break;
      else:
        hasil_gelar.append(jwb)

    if hasil_gelar != []:
      jawaban = hasil_gelar

  # Jika jawaban lebih dari 1
  if isinstance(jawaban, str):
    jawaban = jawaban
  elif (len(jawaban) > 1):
    jawaban = ", ".join(jawaban)
  elif (len(jawaban) == 1):
    jawaban = " ".join(jawaban)
  else:
    jawaban = "jawaban tidak ditemukan"

  return jawaban