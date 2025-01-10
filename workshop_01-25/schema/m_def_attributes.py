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


from typing import TYPE_CHECKING

from nomad.datamodel.metainfo.annotations import (
    ELNAnnotation,
    Filter,
    SectionProperties,
)
from nomad.metainfo import Section
from transmission.schema import (
    UVVisNirTransmissionResult,
)

from nomad.datamodel.metainfo.annotations import (
    H5WebAnnotation,
)
from nomad_ikz_plugin.general.schema import (
    IKZCategory,
)

if TYPE_CHECKING:
    pass


from nomad.datamodel.data import (
    ArchiveSection,
)
from nomad.datamodel.hdf5 import HDF5Reference
from nomad.metainfo import (
    Quantity,
    SubSection,
)



from typing import (
    TYPE_CHECKING,
)

from nomad.datamodel.data import (
    EntryDataCategory,
)
from nomad.metainfo.metainfo import (
    Category,
)

if TYPE_CHECKING:
    pass


class MyCategory(EntryDataCategory):
    m_def = Category(
        label='IKZ Pulsed Laser Deposition', categories=[EntryDataCategory]
    )


class MyExampleClass(ArchiveSection):
    """
    A specialized section for IKZ based on the `UVVisNirTransmissionResult` section.
    """

    m_def = Section(
        categories=[MyCategory],
        label='IKZ UV-Vis-NIR Transmission',
        label_quantity='lab_id',  # "growth_id",
        a_template={
            'measurement_identifiers': {},
        },
        a_eln=ELNAnnotation(
            lane_width='800px',
            properties=SectionProperties(
                order=[
                    'transmittance',
                    'absorbance',
                    'wavelength',
                    'extinction_coefficient',
                ],
                visible=Filter(
                    exclude=[
                        'array_index',
                    ],
                ),
                hide=[
                    "instruments",
                    "steps",
                    "samples",
                    "description",
                    "location",
                    "lab_id",
                ],
            )
        ),
    )

    name = Quantity(
        type=str,
        description='The name of the heater',
    )
    temperature = SubSection(
        section_def=HeaterTemperature,
    )

