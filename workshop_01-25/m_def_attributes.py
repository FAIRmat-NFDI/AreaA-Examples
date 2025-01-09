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



class HeaterTemperature(ArchiveSection):
    """
    The temperature of a heater.
    """

    m_def = Section(
        a_h5web=H5WebAnnotation(axes='time', signal='value', long_name='Temperature')
    )

    value = Quantity(
        type=HDF5Reference,
        unit='K',
        shape=[],
    )
    time = Quantity(
        type=HDF5Reference,
        description='The process time when each of the values were recorded.',
        unit='second',
        shape=[],
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
        a_plotly_express={
            'method': 'line',
            'x': '#step_number',
            'y': '#h1_soll_p',
            'label': 'Example Express Plot',
            'index': 0,
            'layout': {
                'title': {'text': 'Example Express Plot'},
                'xaxis': {'title': {'text': 'x axis'}},
                'yaxis': {'title': {'text': 'y axis'}},
            },
        },
        a_plot=dict(
            # x=['time', 'set_time'],
            # y=['value', 'set_value'],
            x='time',
            y='value',
        ),
        a_h5web=H5WebAnnotation(axes='time', signal='value', long_name='Pressure')
    )
    m_def = Section(
        a_h5web=H5WebAnnotation(paths=['temperature', 'power']),
    )

    name = Quantity(
        type=str,
        description='The name of the heater',
    )
    temperature = SubSection(
        section_def=HeaterTemperature,
    )

    m_def = Section(
        a_plot=[
            dict(
                label='Pressure and Temperature',
                x=[
                    'sample_parameters/0/substrate_temperature/time',
                    'environment/pressure/time',
                ],
                y=[
                    'sample_parameters/0/substrate_temperature/value',
                    'environment/pressure/value',
                ],
                lines=[
                    dict(
                        mode='lines',
                        line=dict(
                            color='rgb(25, 46, 135)',
                        ),
                    ),
                    dict(
                        mode='lines',
                        line=dict(
                            color='rgb(0, 138, 104)',
                        ),
                    ),
                ],
            ),
            dict(
                x='sources/0/vapor_source/power/time',
                y='sources/0/vapor_source/power/value',
            ),
            dict(
                x='sample_parameters/0/substrate_temperature/time',
                y='sample_parameters/0/substrate_temperature/value',
            ),
            dict(
                x='environment/pressure/time',
                y='environment/pressure/value',
            ),
        ],
    )