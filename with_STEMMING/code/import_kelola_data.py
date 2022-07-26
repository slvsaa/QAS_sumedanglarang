# Library
import pandas as pd
import nltk

#Ontology/RDF
from rdflib import Graph, Literal, RDF, URIRef
from rdflib.namespace import FOAF, OWL, RDF, RDFS, VOID, XMLNS, XSD

""" Import Data"""
# from google.colab import drive
# drive.mount('/content/drive')
# from google.colab import files
# file = files.upload()

""" Kelola Data """

"""Ontology"""
ontology = Graph()
ontology.parse(r'F:\Documents\Semester_8\Tugas_Akhir\import\with_STEMMING\sumedanglarangv2.owl')

"""Data Kata Tag"""
katatag = pd.read_csv(r'F:\Documents\Semester_8\Tugas_Akhir\import\with_STEMMING\kunci.csv')
katatag = katatag.values.tolist()
katatag[:5]

""" Data Kata kunci"""
#Fungsi Kata Kunci
def q_listkunci():
  q = """
      PREFIX table: <http://www.semanticweb.org/asus/ontologies/2022/3/sumedanglarang#>
      SELECT DISTINCT *
        WHERE { 
                ?individu	rdf:type	owl:NamedIndividual .
	              ?individu	table:kata_kunci	?kata_kunci .
        }
      ORDER BY ASC(?individu) ASC(?kata_kunci)
"""
  q_listkunci = []
  for r in ontology.query(q):
      isi = (str(r["individu"]), str(r["kata_kunci"]))
      q_listkunci.append(isi)
  return q_listkunci

#List Kata Kunci
list_katakunci = []
for indi, kk in q_listkunci():
  list_katakunci.append(kk)

list_katakunci[:5]

""" Data Objek"""
df_objek = pd.read_csv(r'F:\Documents\Semester_8\Tugas_Akhir\import\with_STEMMING\objek.csv')
list_objek = df_objek.values.tolist()
list_objek[:5]

""" Data Properti"""
df_properti = pd.read_csv(r'F:\Documents\Semester_8\Tugas_Akhir\import\with_STEMMING\data.csv')
list_properti = df_properti.values.tolist()
list_properti[:5]
