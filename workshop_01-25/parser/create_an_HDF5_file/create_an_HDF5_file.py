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

if TYPE_CHECKING:
    from nomad.datamodel.datamodel import (
        EntryArchive,
    )

from nomad.datamodel.datamodel import EntryArchive
from nomad.parsing import MatchingParser
from nomad.parsing.parser import MatchingParser
from pdi_nomad_plugin.utils import (
    create_archive,
)

from nomad_aa_plugin.schema_packages.schema_package import (
    MyClassOne,
    MyClassOneHDF5,
    MyClassTwoHDF5,
)

class MyParserFour(MatchingParser):
    def parse(
        self,
        mainfile: str,
        archive: EntryArchive,
        logger,
    ) -> None:
        
        data_file = mainfile.split('/')[-1]

        # other useful strings:
        # folder_name = mainfile.split('/')[-2]
        # upload_path = f"{mainfile.split('raw/')[0]}raw/"

        df_csv = pd.read_csv(mainfile, sep=',') #, decimal=',', engine='python')
    
        child_archives = {
            'experiment': EntryArchive(),
            'instrument': EntryArchive(),
            'process': EntryArchive(),
        }

        my_name = "And"
        filetype = 'yaml'

        # # # # # HDF5 FILE CREATION # # # # #
        hdf_filename = f'{data_file[:-4]}.h5'
        with archive.m_context.raw_file(hdf_filename, 'w') as newfile:
            with h5py.File(newfile.name, 'w') as hdf:
                group_name = f"my_group_{my_name}"
                group = hdf.create_group(group_name)
                group.create_dataset('value', data=df_csv["ValueFour"])
                group.create_dataset('time', data=df_csv["ValueFour2"])
                group.attrs['signal'] = 'value'
                group.attrs['axes'] = 'time'
                group.attrs['NX_class'] = 'NXdata'

        child_archives['process'].data = MyClassTwoHDF5()
        child_archives['process'].data.my_name = f'{my_name}'
        child_archives['process'].data.my_class_one = []

        child_archives['process'].data.my_class_one.append(MyClassOneHDF5())

        child_archives['process'].data.my_class_one[0].my_value = f'/uploads/{archive.m_context.upload_id}/raw/{hdf_filename}#/{group_name}/value'
        child_archives['process'].data.my_class_one[0].my_time = f'/uploads/{archive.m_context.upload_id}/raw/{hdf_filename}#/{group_name}/time'

        # other code ....

        # reopen the hdf5 file to add units
        with archive.m_context.raw_file(hdf_filename, 'a') as newfile:
            with h5py.File(newfile.name, 'a') as hdf:
                hdf[f"my_group_{my_name}/value"].attrs['units'] = 'K'
                hdf[f"my_group_{my_name}/time"].attrs['units'] = 'sec'
                
        
        example_filename = f'{my_name}_testHDF5.archive.{filetype}'

        create_archive(
            child_archives['process'].m_to_dict(),
            archive.m_context,
            example_filename,
            filetype,
            logger,
        )

        archive.data = MyClassOne()
