from nomad.config.models.plugins import ParserEntryPoint
from pydantic import Field

class MyParserFourEntryPoint(ParserEntryPoint):
    parameter: int = Field(0, description='Custom configuration parameter')

    def load(self):
        from nomad_aa_plugin.parsers.parser import MyParserFour

        return MyParserFour(**self.dict())


parser_four_entry_point = MyParserFourEntryPoint(
    name='MyParserFour',
    description='My parser entry point configuration.',
    mainfile_name_re=r'.+\.csv',
    mainfile_mime_re="(?:text/plain|text/csv)",  # 'text/plain',  
    mainfile_contents_dict={
        '__has_all_keys': ['Value', 'Value2'],
        '__has_comment': '#',
    },
)
