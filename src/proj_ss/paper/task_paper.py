import shutil
import pytask
from pytask_latex import compilation_steps as cs
from proj_ss.config import BLD, PAPER_DIR
import os

latex_dir = BLD / "latex"
os.makedirs(latex_dir, exist_ok=True)
table_dir = BLD / "python"/"table"
os.makedirs(table_dir, exist_ok=True)

documents = ["proj_ss"]

for document in documents:

    @pytask.mark.depends_on({
        "document": PAPER_DIR / f"{document}.pdf"
    })
    @pytask.mark.produces(BLD / "latex")
    def task_copy_to_root(depends_on, produces):
        """Copy a document to the root directory for easier retrieval."""
        pdf_file = depends_on["document"]
        shutil.copyfile(pdf_file, produces / "Social_security_LZ.pdf")
        return produces / f"{document}.pdf"

    print("Social_security_LZ.pdf copied to BLD/latex")

@pytask.mark.depends_on({
        "table": PAPER_DIR / "table_results.tex"
    })
@pytask.mark.produces(BLD / "python"/"table")
def task_copy_to_root(depends_on, produces):
    """Copy a document to the root directory for easier retrieval."""
    table = depends_on["table"]
    shutil.copyfile(table, produces / "table_results.tex")
    return produces / "table_results.tex"

print("table_results.tex copied to BLD/python")