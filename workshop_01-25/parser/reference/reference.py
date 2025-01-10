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

from typing import (
    TYPE_CHECKING,
)

import pandas as pd

if TYPE_CHECKING:
    from nomad.datamodel.datamodel import (
        EntryArchive,
    )

from nomad.datamodel.datamodel import EntryArchive
from nomad.parsing import MatchingParser
from nomad.parsing.parser import MatchingParser
from nomad.utils import hash
from pdi_nomad_plugin.utils import (
    create_archive,
)

from nomad_aa_plugin.schema_packages.schema_package import MyClassFive, MyClassOne


class MyParserThree(MatchingParser):
    def parse(
        self,
        mainfile: str, 
        archive: EntryArchive,
        logger,
    ) -> None:
        
        df_csv = pd.read_csv(mainfile, sep=',') #, decimal=',', engine='python')

        filetype = 'yaml'
        main_archive_filename = f'main.archive.{filetype}'
        test_filename = f'test.archive.{filetype}'
        
        main_archive = EntryArchive()
        main_archive.data = MyClassFive(
            name="experiment",
        )

        new_archive = EntryArchive()
        new_archive.data = MyClassOne(
            my_name="stuff to be referenced",
            my_value = df_csv["ValueThree"],
            my_time = df_csv["ValueThree2"],
        )

        create_archive(
            new_archive.m_to_dict(),
            archive.m_context,
            test_filename,
            filetype,
            logger,
        )

        entry_id = hash(archive.m_context.upload_id, test_filename)
        upload_id = archive.m_context.upload_id

        main_archive.data.reference = f"../uploads/{upload_id}/archive/{entry_id}#data"

        create_archive(
            main_archive.m_to_dict(),
            archive.m_context,
            main_archive_filename,
            filetype,
            logger,
        )
        
        archive.data = MyClassFive()
        archive.data.name = "My namy name"
        archive.data.reference = f"../uploads/{upload_id}/archive/{entry_id}#data"
        
