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

# find these classes in the schema/schema_packages python file
from nomad_aa_plugin.schema_packages.schema_package import MyClassOne


class MyParserOne(MatchingParser):
    def parse(
        self,
        mainfile: str,  # expliciting the type of the variable required makes it easier to understand the code
        archive: EntryArchive,  # expliciting the type of the variable required makes it easier to understand the code
        logger: "BoundLogger",  # expliciting the type of the variable required makes it easier to understand the code
    ) -> None:
        df_csv = pd.read_csv(mainfile, sep=",")  # , decimal=',', engine='python')

        my_name = "And"

        # This "archive" variable is the parse function argument,
        # it is the archive that will be written to the archive folder
        # (not in the raw folder like those created with create_archive function in next examples)
        # This archive will give rise to a non editable entry.
        # it's type is already EntryArchive, so we only need to define it's data section
        archive.data = MyClassOne()

        # we fill in values depending on the ones available in the schema
        archive.data.name = my_name
        archive.data.my_value = df_csv["Value"]
        archive.data.my_time = df_csv["Value2"]

        # make use of the logger so you will see these messages in the log lane of your Entry in the GUI
        logger.info("Alles Gut")
        logger.warn("Some warny warn")
        if 1 < 0:
            logger.error("Something went wrong")
