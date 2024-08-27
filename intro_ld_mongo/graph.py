import gzip
import logging
from rdflib import Graph, Literal
from rdflib.namespace import XSD
from rdflib.term import _toPythonMapping

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s:%(message)s')

# Custom function to handle invalid date literals
def safe_parse_date(lexical):
	try:
		return _toPythonMapping[XSD.date](lexical)
	except ValueError as e:
		logging.error(f"Invalid date literal: {lexical} - {e}")
		return None

# Override the default date parser with the custom one
_toPythonMapping[XSD.date] = safe_parse_date

g = Graph()

try:
	with gzip.open('data/01-nobelprize-data.nt.gz', 'rt', encoding='utf-8') as f:
		print("Starting to parse the RDF data.")
		g.parse(f, format='nt')
		print("Finished parsing the RDF data.")
except Exception as e:
	print(f"An error occurred: {e}")

# Print the number of triples parsed
print(f"Graph has {len(g)} triples.")

# Optionally, print some triples to verify
for stmt in list(g)[:5]:  # Print first 5 triples
	print(stmt)