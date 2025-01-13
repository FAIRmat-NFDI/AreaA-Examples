from nomad.config.models.plugins import ParserEntryPoint
from pydantic import Field


class MyParserThreeEntryPoint(ParserEntryPoint):
    parameter: int = Field(0, description="Custom configuration parameter")

    def load(self):
        from nomad_aa_plugin.parsers.parser import MyParserThree

        return MyParserThree(**self.dict())


parser_three_entry_point = MyParserThreeEntryPoint(
    name="MyParserThree",
    description="My parser entry point configuration.",
    mainfile_name_re=r".+\.csv",
    mainfile_mime_re="(?:text/plain|text/csv)",  # 'text/plain',
    mainfile_contents_dict={
        "__has_all_keys": ["ValueThree", "ValueThree2"],
        "__has_comment": "#",
    },
)
