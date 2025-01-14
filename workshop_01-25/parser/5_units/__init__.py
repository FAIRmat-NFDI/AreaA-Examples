from nomad.config.models.plugins import ParserEntryPoint
from pydantic import Field


class MyParserFiveEntryPoint(ParserEntryPoint):
    parameter: int = Field(0, description='Custom configuration parameter')

    def load(self):
        from nomad_aa_plugin.parsers.parser import MyParserFive 

        return MyParserFive(**self.dict())


parser_five_entry_point = MyParserFiveEntryPoint(
    name='MyParserFive',
    description='My parser entry point configuration.',
    mainfile_name_re=r'.+\.csv',
    mainfile_mime_re="(?:text/plain|text/csv)",  # 'text/plain',  
    mainfile_contents_dict={
        '__has_all_keys': ['ValueFive', 'ValueFive2'],
        '__has_comment': '#',
    },
)

