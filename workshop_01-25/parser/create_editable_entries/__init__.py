from nomad.config.models.plugins import ParserEntryPoint
from pydantic import Field

class MyParserTwoEntryPoint(ParserEntryPoint):
    parameter: int = Field(0, description='Custom configuration parameter')

    def load(self):
        from nomad_aa_plugin.parsers.parser import MyParserTwo

        return MyParserTwo(**self.dict())


parser_two_entry_point = MyParserTwoEntryPoint(
    name='MyParserTwo',
    description='My parser entry point configuration.',
    mainfile_name_re=r'.+\.csv',
    mainfile_mime_re="(?:text/plain|text/csv)",  # 'text/plain',  
    mainfile_contents_dict={
        '__has_all_keys': ['Value', 'Value2'],
        '__has_comment': '#',
    },
)
