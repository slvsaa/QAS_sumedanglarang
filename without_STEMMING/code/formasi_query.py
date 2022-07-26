# IMPORT ALL FILE
import import_kelola_data

"""# Formasi Kueri SPARQL"""

#Query Jawaban (DATA PROPERTY)
def query_data(katakunci, kataproperti):
  q = """
      PREFIX table: <http://www.semanticweb.org/asus/ontologies/2022/3/sumedanglarang#>
      SELECT *
        WHERE { ?individu rdf:type  owl:NamedIndividual .
                ?individu ?properti  ?info . 
                ?individu table:kata_kunci  ?kata_kunci .
                ?properti a          owl:DatatypeProperty .
                FILTER(STR(?kata_kunci)= '"""+katakunci+"""')
                 FILTER(STR(?properti)= 'http://www.semanticweb.org/asus/ontologies/2022/3/sumedanglarang#"""+kataproperti+"""')
              }
  """
  # Iterasi mendapatkan hasil
  q_data = []
  for r in import_kelola_data.ontology.query(q):
    isi = (str(r["properti"]), str(r["info"]))
    q_data.append(isi)
  return q_data

#Query Jawaban (OBJECT PROPERTY)
def query_obj(katakunci, kataproperti, kataobjek):
  q = """
      PREFIX table: <http://www.semanticweb.org/asus/ontologies/2022/3/sumedanglarang#>
      SELECT *
        WHERE { ?individu rdf:type  owl:NamedIndividual .
                ?individu ?object  ?info . 
                ?individu table:kata_kunci  ?kata_kunci .
                ?object a          owl:ObjectProperty .
                ?info	table:"""+kataproperti+"""	?atribut .
                FILTER(STR(?kata_kunci)= '"""+katakunci+"""')
                FILTER(STR(?object)= 'http://www.semanticweb.org/asus/ontologies/2022/3/sumedanglarang#"""+kataobjek+"""')
              }
  """
  # Iterasi mendapatkan hasil
  q_obj = []
  for r in import_kelola_data.ontology.query(q):
    # return (str(r["properti"]), str(r["info"]))
    isi = (str(r["object"]), str(r["atribut"]))
    q_obj.append(isi)
  return q_obj

#Query Jawaban (DUA KATA KUNCI)
def query_duakey(katakunci_1, katakunci_2, kataproperti):
  q = """
      PREFIX table: <http://www.semanticweb.org/asus/ontologies/2022/3/sumedanglarang#>
      SELECT DISTINCT *
        WHERE { 	?individu	?predikat	?individu_2 .
                  ?individu	table:kata_kunci	?kata_kunci .
                  ?individu_2	table:kata_kunci	?kata_kunci_2 .
                  ?individu_2	table:"""+kataproperti+"""	?properti .
                  FILTER(STR(?kata_kunci) = '"""+katakunci_1+"""') .
                  FILTER(STR(?kata_kunci_2) =  '"""+katakunci_2+"""') 
              }
  """
  # Iterasi mendapatkan hasil
  q_obj = []
  for r in import_kelola_data.ontology.query(q):
    # return (str(r["properti"]), str(r["info"]))
    isi = (str(r["individu_2"]), str(r["properti"]))
    q_obj.append(isi)
  return q_obj

#Query Jawaban (DUA KATA KUNCI)
def query_duakey_obj(katakunci_1, katakunci_2, kataproperti, kataobjek):
  q = """
      PREFIX table: <http://www.semanticweb.org/asus/ontologies/2022/3/sumedanglarang#>
      SELECT DISTINCT *
        WHERE { 	?individu	?predikat	?individu_2 .
                  ?individu	table:kata_kunci	?kata_kunci .
                  ?individu_2	table:kata_kunci	?kata_kunci_2 .
                  ?individu_2	table:"""+kataproperti+"""	?properti .
                  FILTER(STR(?kata_kunci) = '"""+katakunci_1+"""') .
                  FILTER(STR(?kata_kunci_2) =  '"""+katakunci_2+"""') .
                  FILTER(STR(?predikat)= 'http://www.semanticweb.org/asus/ontologies/2022/3/sumedanglarang#"""+kataobjek+"""')
              }
  """
  # Iterasi mendapatkan hasil
  q_obj = []
  for r in import_kelola_data.ontology.query(q):
    # return (str(r["properti"]), str(r["info"]))
    isi = (str(r["individu_2"]), str(r["properti"]))
    q_obj.append(isi)
  return q_obj

#Query Jawaban (DUA KATA KUNCI)
def query_list(kata, kataproperti):
  q = """
      PREFIX table: <http://www.semanticweb.org/asus/ontologies/2022/3/sumedanglarang#>
      SELECT *
        WHERE { 	?subjek	rdf:type	table:"""+kata+""" .
		              ?subjek table:"""+kataproperti+"""	?objek .
              }
  """
  # Iterasi mendapatkan hasil
  q_list = []
  for r in import_kelola_data.ontology.query(q):
    isi = (str(r["subjek"]), str(r["objek"]))
    q_list.append(isi)
  return q_list