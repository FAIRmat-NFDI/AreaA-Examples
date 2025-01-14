from nomad.datamodel.metainfo.annotations import (
    ELNAnnotation,
)
from nomad.metainfo import (
    Quantity,
    SchemaPackage,
    SubSection,
)
from nomad.datamodel.data import (
    ArchiveSection,
)

from nomad.datamodel.metainfo.basesections import (
    SectionReference,
)

# copy the code from here: https://github.com/PDI-Berlin/pdi-nomad-plugin/blob/main/src/pdi_nomad_plugin
from pdi_nomad_plugin.characterization.schema import (
    Pyrometry,
)

m_package = SchemaPackage()


class PyrometryReference(SectionReference): # SectionReference is a besesection contained in packages/nomad-FAIR/nomad/datamodel/metainfo/basesections.py
    """
    A section used for referencing a pyrometry.
    """

    # this property is a Quantity with a special annotation for the ELN component to make it a Reference from another file
    reference = Quantity(
        type=Pyrometry,
        description="A reference to a NOMAD `Pyrometry` entry.",
        a_eln=ELNAnnotation(
            component="ReferenceEditQuantity",
            label="Pyrometry Reference",
        ),
    )


class PyrometryNest(ArchiveSection):
    """
    A section used for referencing a pyrometry.
    """

    # this property is a SubSection containing a pirometry COMPOSED in the same file
    pyrometry = SubSection(
        section_def=Pyrometry,
        repeats=True,
    )
