# Libraries

from pathlib import Path
from markitdown import MarkItDown


def convert_to_markdown(path:Path)-> str:
    
    """Convert a file to Markdown text."""

    md = MarkItDown()
    result = md.convert(path)
    
    return result.markdown

if __name__ == "__main__":


    file = Path.home() / "projekt/test/protokoll.docx"
    print(convert_to_markdown(file))