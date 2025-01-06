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

from nomad.datamodel.datamodel import EntryArchive
from nomad.parsing import MatchingParser

from pdi_nomad_plugin.mbe.instrument import (
    InstrumentMbePDI,
)
from pdi_nomad_plugin.utils import (
    create_archive,
)

class ParserEpicPDI(MatchingParser):
    def parse(
        self,
        mainfile: str,
        archive: EntryArchive,
        logger,
    ) -> None:
        data_file = mainfile.split('/')[-1]

        child_archives = {
            'experiment': EntryArchive(),
            'instrument': EntryArchive(),
            'process': EntryArchive(),
        }
        filetype = 'yaml'

        instrument_filename = f'{data_file[:-5]}.InstrumentMbePDI.archive.{filetype}'

        child_archives['instrument'].data = InstrumentMbePDI()
        child_archives['instrument'].data.name = f'{data_file} instrument'
        child_archives['instrument'].data.port_list = []

        create_archive(
            child_archives['instrument'].m_to_dict(),
            archive.m_context,
            instrument_filename,
            filetype,
            logger,
        )