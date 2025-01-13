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

        child_archive = EntryArchive()

        my_name = "And"
        filetype = "yaml"

        example_filename = f"{my_name}.archive.{filetype}"

        child_archive.data = MyClassTwo()
        child_archive.data.my_name = f"{my_name}"
        child_archive.data.my_class_one = []

        child_archive.data.my_class_one.append(MyClassOne())

        child_archive.data.my_class_one[0].my_value = df_csv["Value"]
        child_archive.data.my_class_one[0].my_time = df_csv["Value2"]

        create_archive(
            child_archive.m_to_dict(),
            archive.m_context,
            example_filename,
            filetype,
            logger,
        )

        archive.data = MyClassOne()
