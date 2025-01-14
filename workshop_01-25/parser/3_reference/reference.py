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
        
        df_csv = pd.read_csv(mainfile, sep=",")  # , decimal=',', engine='python')

        # create archive function accepts either yaml or json as filetype
        filetype = "yaml"

        # filenames used later to create the archives
        main_archive_filename = f"main.archive.{filetype}"
        test_filename = f"test.archive.{filetype}"

        # EntryArchive is the root class that is used to store the data of the archive
        main_archive = EntryArchive()

        # the class filled in the "data" section must be an EntryData class
        main_archive.data = MyClassFive(
            name="experiment",
        )

        # EntryArchive is the root class that is used to store the data of the archive
        new_archive = EntryArchive()

        # the class filled in the "data" section must be an EntryData class
        new_archive.data = MyClassOne(
            my_name="stuff to be referenced",
            my_value=df_csv["ValueThree"],
            my_time=df_csv["ValueThree2"],
        )

        # copy-paste the code from the plugin where this is imported
        create_archive(
            new_archive.m_to_dict(),
            archive.m_context,
            test_filename,
            filetype,
            logger,
        )

        # hash function is not the python native one! It is imported from nomad.utils
        # it always generates an entry_id from upload_id and filename
        entry_id = hash(archive.m_context.upload_id, test_filename)

        # we use the fact that the archive passed to the parse function will have already an upload id defined
        # so we can take it and use it to create the reference string
        upload_id = archive.m_context.upload_id

        main_archive.data.reference = f"../uploads/{upload_id}/archive/{entry_id}#data"

        # the create archive returns automatically the reference string, so one can use directly the return value
        create_archive(
            main_archive.m_to_dict(),
            archive.m_context,
            main_archive_filename,
            filetype,
            logger,
        )

        # This archive is the parse function argument, so it is the archive that will be written to the archive folder 
        # (not in the raw folder like those created with create_archive function)
        # This archive will give rise to a non editable entry.
        archive.data = MyClassFive()
        archive.data.name = "My namy name"
        archive.data.reference = f"../uploads/{upload_id}/archive/{entry_id}#data"
