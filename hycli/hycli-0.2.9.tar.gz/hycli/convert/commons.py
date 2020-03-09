def read_pdf(pdf_path):
    with open(pdf_path, "rb") as pdf:
        pdf = pdf.read()

    return (pdf_path, pdf)


class InvoiceExtractorException(Exception):
    """Raised when the Invoice Extractor service returns an error."""

    pass
