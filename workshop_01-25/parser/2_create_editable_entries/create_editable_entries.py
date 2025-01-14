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
from pdi_nomad_plugin.utils import (
    create_archive,
)

from nomad_aa_plugin.schema_packages.schema_package import MyClassOne, MyClassTwo


class MyParserTwo(MatchingParser):
    def parse(
        self,
        mainfile: str,
        archive: EntryArchive,
        logger,
    ) -> None:
        df_csv = pd.read_csv(mainfile, sep=",")  # , decimal=',', engine='python')

        archive.data = MyClassOne()

        # this variable contains the root class of the archive that we will fill in
        child_archive = EntryArchive()

        my_name = "And"

        # create archive function accepts either yaml or json as filetype
        filetype = "yaml"

        # filenames used later to create the archives
        example_filename = f"{my_name}.archive.{filetype}"

        # we fill the archive, remember to instantiate classes before filling them in!
        child_archive.data = MyClassTwo()
        child_archive.data.my_name = f"{my_name}"

        my_class_one_subsec = MyClassOne()
        my_class_one_subsec.my_value = df_csv["ValueTwo"]
        my_class_one_subsec.my_time = df_csv["ValueTwo2"]

        # check which args the function m_add_subsection accepts: packages/nomad-FAIR/nomad/metainfo/metainfo.py
        # DO NOT use list.append() to add a subsection to a section!
        child_archive.data.m_add_sub_section(MyClassTwo.my_class_one, my_class_one_subsec)

        # the create archive returns automatically the reference string, so one can use directly the return value
        create_archive(
            child_archive.m_to_dict(),
            archive.m_context,
            example_filename,
            filetype,
            logger,
        )

        # This archive is the parse function argument, so it is the archive that will be written to the archive folder 
        # (not in the raw folder like those created with create_archive function)
        # This archive will give rise to a non editable entry.
        archive.data = MyClassOne()
