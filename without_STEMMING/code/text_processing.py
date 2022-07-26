# IMPORT ALL FILE
import import_kelola_data

# Library
import pandas as pd
import nltk

# Case Folding
import re

#StopWord
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from Sastrawi.Dictionary.ArrayDictionary import ArrayDictionary
from Sastrawi.StopWordRemover.StopWordRemover import StopWordRemover

#Tokenizing
nltk.download('punkt')
from nltk.tokenize import word_tokenize

#POS Tagging
from nltk.tag import CRFTagger
import pycrfsuite

# Mencari kata kunci
import itertools
from itertools import product
from collections import defaultdict
import random

"""Text Processing"""

def proses_pertanyaan (pertanyaan):
  # Case Folding
  pertanyaan = pertanyaan.lower() #lower the text even unicode given
  pertanyaan = re.sub(r'[^a-z0-9 -]', ' ', pertanyaan, flags = re.IGNORECASE|re.MULTILINE)
  pertanyaan = re.sub(r'( +)', ' ', pertanyaan, flags = re.IGNORECASE|re.MULTILINE)
  pertanyaan = pertanyaan.replace('-', ' ')
  pertanyaan = pertanyaan.strip()

  #stopword removal (Sastrawi)
  factory = StopWordRemoverFactory()
  stopword_list = factory.get_stop_words()
  exclude_stopword = ['setelah', 'telah', 'sebelum', 'belum', 'kedua', 'dua', 'mengapa', 'dimana']
  for i in exclude_stopword:
    if i in stopword_list:
      stopword_list.remove(i)

  dictionary = ArrayDictionary(stopword_list)
  stopWordRemover = StopWordRemover(dictionary)

  # Proses Stopword Removal dan Tokenize
  hasil = []
  hasil.append(word_tokenize((stopWordRemover.remove(pertanyaan))))

  # Proses Pos Tagging
  pos_tag = pd.DataFrame(columns=['kata','tag'])

  ct = CRFTagger()
  # ct.set_model_file('drive/MyDrive/Proposal dan TA/import/all_indo_man_tag_corpus_model.crf.tagger')
  ct.set_model_file(r'F:\Documents\Semester_8\Tugas_Akhir\import\without_STEMMING\all_indo_man_tag_corpus_model.crf.tagger')
  pos = ct.tag_sents(hasil)
  pos = pos[0]

  for kata_pos, tag_pos in pos:
    for kata, tag in import_kelola_data.katatag:
      if kata_pos == kata:
        tag_pos = tag;
    pos_tag = pos_tag.append({'kata':kata_pos, "tag":tag_pos}, ignore_index=True)

  pos_tag = pos_tag.values.tolist()

  return pos_tag

"""Identifikasi Kata

Identifikasi Kata Kunci
"""
def identifikasi_kunci(hasil_tag):
  potensi_kunci = []

  for kata, tag in hasil_tag:
    if (tag == "NN" or tag == "OD" or tag == "NNP"  or tag == "CD"):
      potensi_kunci.append(kata);

  identifikasi_kunci = []
  for k in range(len(potensi_kunci)):
    for pair in itertools.permutations(potensi_kunci, k+1):
      sebuah = ' '.join(pair);
      if sebuah in import_kelola_data.list_katakunci:
        identifikasi_kunci.append(sebuah);

  identifikasi_kunci = list(dict.fromkeys(identifikasi_kunci))

  daftar =[]
  # Memanggil Fungsi List Kunci
  link_kunci = import_kelola_data.q_listkunci()
  for j,k in link_kunci:
    if k in identifikasi_kunci:
      daftar.append([j,k])

  d = defaultdict(set)
  for k, v in daftar:
      d[k].add(v)

  identifikasi_kunci = []
  for i, j in sorted(d.items()):
    # if (len(j) > 1):
    identifikasi_kunci.append(random.choice(list(j)))
  return identifikasi_kunci

"""## Identifikas Kata Objek (kata_objek)"""

def identifikasi_objek(hasil_tag):
  potensi_objek = []

  for kata, tag in hasil_tag:
    if kata in list(import_kelola_data.df_objek['kata']):
      potensi_objek.append(kata);

  # objek = []
  q_objek = []
  for o in potensi_objek:
    if potensi_objek == []:
      break;
    else:
      for kata, dataobjek in import_kelola_data.list_objek:
        if o == kata:
          #untuk hasil
          # objek.append(o);
          #untuk query
          q_objek.append(dataobjek)
          
  #Untuk QUERY
  q_objek = list(dict.fromkeys(q_objek))

  return q_objek

"""Identifikasi Kata Properti (kata_properti)"""

def identifikasi_properti(hasil_tag):
  potensi_properti = []

  for kata, tag in hasil_tag:
    if kata in list(import_kelola_data.df_properti['kata']):
      potensi_properti.append(kata);
    
  # properti = []
  q_properti = []

  if (potensi_properti == []) or ('memindahkan_ke' in identifikasi_objek(hasil_tag)) or ('dijadikan_ibukota' in identifikasi_objek(hasil_tag)):
      # properti.append('nama');
      q_properti.append('nama');

  if (potensi_properti != []):
    for d in potensi_properti:
      # if potensi_properti == [] or objek == 'pindah' or objek == 'ibukota pindah' :
      for kata, dataproperti in import_kelola_data.list_properti:
        if d == kata:
          #untuk hasil
          # properti.append(kata)
          #untuk query
          q_properti.append(dataproperti)

  #untuk hasil
  # data = list(dict.fromkeys(data))
  # for d in data:
  #   if (d == 'tahun'):
  #     data = d;
  # data = " ".join(data)
      
  # data

  #untuk query
  q_properti = list(dict.fromkeys(q_properti))
  return q_properti