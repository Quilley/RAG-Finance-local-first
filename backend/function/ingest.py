from pathlib import Path
from unstructured.partition.auto import partition

def parse_document(file_path: str) -> str:
    elements = partition(filename=file_path)
    text = "\n".join(el.text for el in elements if el.text)
    return text

