"""Plugin for executing JavaScript code."""


from mkdocs import plugins
from mkdocs.config import base, config_options
from mkdocs.structure import files, pages

from mkdocs_code_runner import lib


class CodeRunner(plugins.BasePlugin):
    """Plugin for executing JavaScript code."""

    config_scheme = (("selector", config_options.Type(str, default="div.code-runner")),)

    def on_page_markdown(
        self, markdown: str, page: pages.Page, config: base.Config, files: files.Files
    ) -> str:
        """Edit page copying JavaScript code into script element."""

        return lib.runner(markdown, self.config["selector"])
