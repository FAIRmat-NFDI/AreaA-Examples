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

# The if TYPE_CHECKING: statement is a special construct provided by the typing module. 
# It allows you to include imports that are only necessary for type hinting and static analysis, 
# without actually importing those modules at runtime.
if TYPE_CHECKING:
    from nomad.datamodel.datamodel import (
        EntryArchive,
    )
    from structlog.stdlib import (
        BoundLogger,
    )

from nomad.datamodel.datamodel import EntryArchive
from nomad.parsing import MatchingParser
from nomad.utils import hash

# copy the code from here: https://github.com/PDI-Berlin/pdi-nomad-plugin/blob/main/src/pdi_nomad_plugin/utils.py
from pdi_nomad_plugin.utils import (
    create_archive,
)

# find these classes in the schema/schema_packages python file
from nomad_aa_plugin.schema_packages.schema_package import MyClassFive, MyClassOne

class MyParserThree(MatchingParser):
    def parse(
        self,
        mainfile: str, # expliciting the type of the variable required makes it easier to understand the code
        archive: EntryArchive, # expliciting the type of the variable required makes it easier to understand the code
        logger: 'BoundLogger', # expliciting the type of the variable required makes it easier to understand the code
    ) -> None:
        
        df_csv = pd.read_csv(mainfile, sep=",")  # , decimal=',', engine='python')

        # create archive function accepts either yaml or json as filetype
        filetype = "yaml"

        my_name = "And child archive"
        my_new_name = "And new child archive"

        # this variable contains the root class of the archive EntryArchive that we will fill in
        child_archive = EntryArchive()

        # the class filled in the "data" section must be an EntryData class
        child_archive.data = MyClassFive(
            name=my_name,
        )

        # this variable contains the root class of the archive EntryArchive that we will fill in
        new_child_archive = EntryArchive()

        # the class filled in the "data" section must be an EntryData class
        new_child_archive.data = MyClassOne(
            name=my_new_name,
            my_value=df_csv["ValueThree"],
            my_time=df_csv["ValueThree2"],
        )

        test_filename = f"test.archive.{filetype}"
        # copy-paste the code from the plugin where this is imported
        create_archive(
            new_child_archive.m_to_dict(),
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

        child_archive.data.reference = f"../uploads/{upload_id}/archive/{entry_id}#data"

        main_archive_filename = f"main.archive.{filetype}"
        # the create archive returns automatically the reference string, so one can use directly the return value
        create_archive(
            child_archive.m_to_dict(),
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

        # make use of the logger so you will see these messages in the log lane of your Entry in the GUI
        logger.info(f"Alles Gut")
        logger.warn(f"Some warny warn")
        if 1 < 0:
            logger.error(f"Something went wrong")