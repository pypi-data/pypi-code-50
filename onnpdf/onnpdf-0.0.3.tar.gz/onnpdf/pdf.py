import os
from weasyprint import HTML
import jinja2


def create_pdf(template_dir, template_filename, template_assets_dir, output_file_path, **kv_pairs):
    """Converts Jinja2 templates to PDF"""

    output_dir = os.path.dirname(output_file_path)
    os.makedirs(output_dir, exist_ok=True)

    template_loader = jinja2.FileSystemLoader(searchpath=template_dir)
    template_env = jinja2.Environment(loader=template_loader)
    template_html = template_env.get_template(template_filename)
    rendered_html = template_html.render(**kv_pairs)

    HTML(string=rendered_html, base_url=template_assets_dir).write_pdf(output_file_path)
