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

from nomad.metainfo import Section

from nomad.datamodel.metainfo.annotations import (
    H5WebAnnotation,
)

from nomad.datamodel.data import (
    ArchiveSection,
)
from nomad.datamodel.hdf5 import HDF5Reference
from nomad.metainfo import (
    Quantity,
    SubSection,
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
        label="IKZ Pulsed Laser Deposition", categories=[EntryDataCategory]
    )


class ImpingingFlux(ArchiveSection):
    """
    The flux that impinges the surface of the substrate.
    It is calculated from the effusion cell heater temperature as the following:

    bep_to_flux * np.exp(a_parameter) * np.exp(t_0_parameter / temperature[:])

    """

    m_def = Section(a_h5web=H5WebAnnotation(axes="time", signal="value"))
    bep_to_flux = Quantity(
        type=float,
        description="The conversion factor from Beam Equivalent Pressure (BEP) to the flux.",
        unit="meter ** -2 * second ** -1 * pascal ** -1",
    )
    value = Quantity(
        type=HDF5Reference,
        shape=[],
    )
    time = Quantity(
        type=HDF5Reference,
        description="The process time when each of the values were recorded.",
        shape=[],
    )


class EffusionCellSourcePDI(ArchiveSection):
    """
    A thermal evaporation source is a device that heats a material
    to the point of evaporation.
    """

    m_def = Section(
        a_h5web=H5WebAnnotation(paths=["impinging_flux/0"]),
    )

    impinging_flux = SubSection(
        section_def=ImpingingFlux,
        description="""
        The deposition rate of the material onto the substrate (mol/area/time).
        """,
        repeats=True,
    )
