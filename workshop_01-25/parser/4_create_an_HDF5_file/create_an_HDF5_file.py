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
import h5py

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

# copy the code from here: https://github.com/PDI-Berlin/pdi-nomad-plugin/blob/main/src/pdi_nomad_plugin/utils.py
from pdi_nomad_plugin.utils import (
    create_archive,
)

# find these classes in the schema/schema_packages python file
from nomad_aa_plugin.schema_packages.schema_package import (
    MyClassOne,
    MyClassOneHDF5,
    MyClassTwoHDF5,
)


class MyParserFour(MatchingParser):
    def parse(
        self,
        mainfile: str,  # expliciting the type of the variable required makes it easier to understand the code
        archive: "EntryArchive",  # expliciting the type of the variable required makes it easier to understand the code
        logger: "BoundLogger",  # expliciting the type of the variable required makes it easier to understand the code
    ) -> None:
        data_file = mainfile.split("/")[-1]

        # other useful strings:
        # (print them if you want to check how they look like)

        # folder_name = mainfile.split('/')[-2]
        # upload_path = f"{mainfile.split('raw/')[0]}raw/"

        df_csv = pd.read_csv(mainfile, sep=",")  # , decimal=',', engine='python')

        # create archive function accepts either yaml or json as filetype
        filetype = "yaml"

        my_name = "And"

        # this variable contains the root class of the archive EntryArchive that we will fill in
        child_archive = EntryArchive()

        # # # # # HDF5 FILE CREATION # # # # #
        # check docs https://nomad-lab.eu/prod/v1/staging/docs/reference/annotations.html#h5web
        hdf_filename = f"{data_file[:-4]}.h5"
        with archive.m_context.raw_file(hdf_filename, "w") as newfile:
            with h5py.File(newfile.name, "w") as hdf:
                group_name = f"my_group_{my_name}"
                group = hdf.create_group(group_name)
                group.create_dataset("value", data=df_csv["ValueFour"])
                group.create_dataset("time", data=df_csv["ValueFour2"])
                group.attrs["signal"] = "value"
                group.attrs["axes"] = "time"
                group.attrs["NX_class"] = "NXdata"

        # this variable contains the root class of the archive EntryArchive that we will fill in
        # remember to instantiate it'S subsections (if present) before filling them in!
        child_archive.data = MyClassTwoHDF5()
        child_archive.data.name = f"{my_name}"

        # instantiate a subsection
        my_class_one_subsec = MyClassOneHDF5()

        # fill subsection with data
        # set the paths to the data in the HDF5 file
        my_class_one_subsec.my_value = f"/uploads/{archive.m_context.upload_id}/raw/{hdf_filename}#/{group_name}/value"
        my_class_one_subsec.my_time = f"/uploads/{archive.m_context.upload_id}/raw/{hdf_filename}#/{group_name}/time"

        # check which args the function m_add_subsection accepts: packages/nomad-FAIR/nomad/metainfo/metainfo.py
        # DO NOT use list.append() to add a subsection to a section!
        child_archive.data.m_add_sub_section(
            MyClassTwoHDF5.my_class_one, my_class_one_subsec
        )

        # reopen the hdf5 file as many times as you want
        # this time it was reopened to add units
        with archive.m_context.raw_file(hdf_filename, "a") as newfile:
            with h5py.File(newfile.name, "a") as hdf:
                hdf[f"my_group_{my_name}/value"].attrs["units"] = "K"
                hdf[f"my_group_{my_name}/time"].attrs["units"] = "sec"

        example_filename = f"{my_name}_testHDF5.archive.{filetype}"
        create_archive(
            child_archive.m_to_dict(),
            archive.m_context,
            example_filename,
            filetype,
            logger,
        )

        # make use of the logger so you will see these messages in the log lane of your Entry in the GUI
        logger.info("Alles Gut")
        logger.warn("Some warny warn")
        if 1 < 0:
            logger.error("Something went wrong")

        archive.data = MyClassOne()
