#
# Copyright The NOMAD Authors.
#
# This file is part of NOMAD. See https://nomad-lab.eu for further info.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#


from nomad.config.models.plugins import ParserEntryPoint


#
# https://github.com/FAIRmat-NFDI/nomad-measurements/blob/main/src/nomad_measurements/xrd/__init__.py
#


class XRDParserEntryPoint(ParserEntryPoint):
    def load(self):
        from nomad_measurements.xrd.parser import XRDParser

        return XRDParser(**self.dict())


parser = XRDParserEntryPoint(
    name="XRD Parser",
    description="Parser for several kinds of raw files from XRD measurements.",
    mainfile_name_re=r"^.*\.xrdml$|^.*\.rasx$|^.*\.brml$",
    mainfile_mime_re="text/.*|application/zip",
)


#
# https://github.com/IKZ-Berlin/lakeshore-nomad-plugin/blob/main/src/lakeshore_nomad_plugin/hall/measurement_parser/__init__.py
#


class HallMeasurementParserEntryPoint(ParserEntryPoint):
    def load(self):
        from lakeshore_nomad_plugin.hall.measurement_parser.parser import (
            HallMeasurementsParser,
        )

        return HallMeasurementsParser(**self.dict())


measurement_parser = HallMeasurementParserEntryPoint(
    name="HallMeasurementsParser",
    description="Parse Hall measurement file from Lakeshore.",
    mainfile_name_re=".+\.txt",
    mainfile_mime_re="(?:text/plain|application/x-wine-extension-ini)",
    mainfile_contents_re=r"(?s)\[Sample parameters\].*?\[Measurements\]",
)

#
# https://github.com/IKZ-Berlin/nomad-ikz-plugin/blob/main/src/nomad_ikz_plugin/movpe/movpe1/growth_excel/__init__.py
#

class Movpe1ParserEntryPoint(ParserEntryPoint):
    def load(self):
        from nomad_ikz_plugin.movpe.movpe1.growth_excel.parser import ParserMovpe1IKZ

        return ParserMovpe1IKZ(**self.dict())


parser = Movpe1ParserEntryPoint(
    name="Movpe1Parser",
    description="Parse excel files containing growth process parameters logged manually.",
    mainfile_name_re=r".+\.xlsx",
    mainfile_mime_re=r"application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    mainfile_contents_dict={
        "Deposition Control": {
            "__has_all_keys": ["Constant Parameters ID", "Sample ID", "Date", "number"]
        },
        "Precursors": {"__has_all_keys": ["Sample ID"]},
        "__has_comment": "#",
    },
)
