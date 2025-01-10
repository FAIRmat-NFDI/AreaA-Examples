
from nomad.datamodel.metainfo.annotations import (
    ELNAnnotation,
)
from nomad.datamodel.metainfo.basesections import (
    SectionReference,
)
from nomad.metainfo import (
    Quantity,
    SchemaPackage,
    SubSection,
)


from pdi_nomad_plugin.characterization.schema import (
    Pyrometry,
)


m_package = SchemaPackage()


class PyrometryReference(SectionReference):
    """
    A section used for referencing a pyrometry.
    """

    reference = Quantity(
        type=Pyrometry,
        description='A reference to a NOMAD `Pyrometry` entry.',
        a_eln=ELNAnnotation(
            component='ReferenceEditQuantity',
            label='Pyrometry Reference',
        ),
    )


class PyrometryNest(SectionReference):
    """
    A section used for referencing a pyrometry.
    """

    pyrometry = SubSection(
        section_def=Pyrometry,
        repeats=True,
    )
