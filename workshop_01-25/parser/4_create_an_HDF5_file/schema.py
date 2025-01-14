from typing import (
    TYPE_CHECKING,
)

if TYPE_CHECKING:
    pass

from nomad.datamodel.data import (
    ArchiveSection,
)

from nomad.datamodel.hdf5 import HDF5Reference
from nomad.datamodel.metainfo.annotations import ELNAnnotation, H5WebAnnotation
from nomad.metainfo import Quantity, SchemaPackage
from nomad.datamodel.data import EntryData
from nomad.metainfo import (
    SubSection,
    Section,
)

m_package = SchemaPackage()


class MyClassOneHDF5(EntryData, ArchiveSection):
    """
    A test class for HDF5 data.
    """

    m_def = Section(a_h5web=H5WebAnnotation(axes="my_time", signal="my_value"))

    my_name = Quantity(
        type=str,
        a_eln=ELNAnnotation(
            component="StringEditQuantity",
        ),
    )

    my_value = Quantity(
        type=HDF5Reference,
        shape=[],
    )

    my_time = Quantity(
        type=HDF5Reference,
        shape=[],
    )


class MyClassTwoHDF5(EntryData, ArchiveSection):
    """
    An example class for hdf5 files
    """

    m_def = Section(
        a_h5web=H5WebAnnotation(
            paths=[
                "my_class_one/*",
            ]
        ),
    )

    my_name = Quantity(
        type=str,
        a_eln=ELNAnnotation(
            component="StringEditQuantity",
        ),
    )

    my_class_one = SubSection(
        section_def=MyClassOneHDF5,
        repeats=True,
    )


m_package.__init_metainfo__()
