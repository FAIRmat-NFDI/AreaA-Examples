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

import plotly.graph_objects as go

from nomad.datamodel.metainfo.annotations import (
    ELNAnnotation,
)
from nomad.metainfo import Section


if TYPE_CHECKING:
    pass


from nomad.datamodel.data import (
    ArchiveSection,
)
from nomad.metainfo import (
    Quantity,
    SubSection,
)


from typing import (
    TYPE_CHECKING,
)

from nomad.datamodel.data import EntryData

from nomad.datamodel.metainfo.plot import (
    PlotlyFigure,
    PlotSection,
)

if TYPE_CHECKING:
    pass


class MyClassOne(PlotSection, EntryData):
    m_def = Section(
        a_plotly_express={
            "method": "line",
            "x": "#my_value",
            "y": "#my_time",
            "label": "Example Express Plot",
            "index": 0,
            "layout": {
                "title": {"text": "Example Express Plot"},
                "xaxis": {"title": {"text": "x axis"}},
                "yaxis": {"title": {"text": "y axis"}},
            },
        },
    )

    my_name = Quantity(
        type=str,
        a_eln=ELNAnnotation(
            component="StringEditQuantity",
        ),
    )

    my_value = Quantity(
        type=float,
        shape=["*"],
        a_eln=ELNAnnotation(
            component="NumberEditQuantity",
        ),
    )

    my_time = Quantity(
        type=float,
        shape=["*"],
        a_eln=ELNAnnotation(
            component="NumberEditQuantity",
        ),
    )


class MyClassTwo(EntryData, ArchiveSection):
    """
    An example class
    """

    m_def = Section(
        a_plot=[
            dict(
                label="Pressure and Temperature",
                x=[
                    "my_class_one/0/my_time",
                ],
                y=[
                    "my_class_one/0/my_value",
                ],
                lines=[
                    dict(
                        mode="lines",
                        line=dict(
                            color="rgb(25, 46, 135)",
                        ),
                    ),
                    dict(
                        mode="lines",
                        line=dict(
                            color="rgb(0, 138, 104)",
                        ),
                    ),
                ],
            ),
            # dict(
            #     x='sources/0/vapor_source/power/time',
            #     y='sources/0/vapor_source/power/value',
            # ),
        ],
    )

    my_name = Quantity(
        type=str,
        a_eln=ELNAnnotation(
            component="StringEditQuantity",
        ),
    )

    my_class_one = SubSection(
        section_def=MyClassOne,
        repeats=True,
    )


class MyClassThree(EntryData, ArchiveSection):
    """
    An example class
    """

    m_def = Section(
        a_plotly_graph_object=[
            {
                "label": "shaft temperature",
                "index": 0,
                "dragmode": "pan",
                "data": {
                    "type": "scattergl",
                    "line": {"width": 2},
                    "marker": {"size": 6},
                    "mode": "lines+markers",
                    "name": "Temperature",
                    "x": "#my_time",
                    "y": "#my_value",
                },
                "layout": {
                    "title": {"text": "Shaft Temperature"},
                    "xaxis": {
                        "showticklabels": True,
                        "fixedrange": True,
                        "ticks": "",
                        "title": {"text": "Process time [min]"},
                        "showline": True,
                        "linewidth": 1,
                        "linecolor": "black",
                        "mirror": True,
                    },
                    "yaxis": {
                        "showticklabels": True,
                        "fixedrange": True,
                        "ticks": "",
                        "title": {"text": "Temperature [°C]"},
                        "showline": True,
                        "linewidth": 1,
                        "linecolor": "black",
                        "mirror": True,
                    },
                    "showlegend": False,
                },
                "config": {
                    "displayModeBar": False,
                    "scrollZoom": False,
                    "responsive": False,
                    "displaylogo": False,
                    "dragmode": False,
                },
            },
            # {
            #     ...
            # },
        ],
    )
    name = Quantity(
        type=str,
        description="""
        Sample name.
        """,
        a_eln=ELNAnnotation(
            component="StringEditQuantity",
        ),
    )
    my_value = Quantity(
        type=float,
        shape=["*"],
        a_eln=ELNAnnotation(
            component="NumberEditQuantity",
        ),
    )

    my_time = Quantity(
        type=float,
        shape=["*"],
        a_eln=ELNAnnotation(
            component="NumberEditQuantity",
        ),
    )


class MyClassFour(PlotSection, EntryData):
    """
    Class autogenerated from yaml schema.
    """

    my_value = Quantity(
        type=float,
        shape=["*"],
        a_eln=ELNAnnotation(
            component="NumberEditQuantity",
        ),
    )

    my_time = Quantity(
        type=float,
        shape=["*"],
        a_eln=ELNAnnotation(
            component="NumberEditQuantity",
        ),
    )
    my_value_bis = Quantity(
        type=float,
        shape=["*"],
        a_eln=ELNAnnotation(
            component="NumberEditQuantity",
        ),
    )

    my_time_bis = Quantity(
        type=float,
        shape=["*"],
        a_eln=ELNAnnotation(
            component="NumberEditQuantity",
        ),
    )

    def normalize(self, archive, logger):
        # plotly figure
        fig = go.Figure()
        fig.add_trace(
            go.Scatter(
                x=self.my_time,
                y=self.my_value,
                name="Sub Temp",
                line=dict(color="#2A4CDF", width=4),
                yaxis="y",
            ),
        )
        fig.add_trace(
            go.Scatter(
                x=self.my_time_bis,
                y=self.my_value_bis,
                name="Pyro Temp",
                line=dict(color="#90002C", width=2),
                yaxis="y",
            ),
        )
        fig.update_layout(
            template="plotly_white",
            dragmode="zoom",
            xaxis=dict(
                fixedrange=False,
                autorange=True,
                title="Process time / s",
                mirror="all",
                showline=True,
                gridcolor="#EAEDFC",
            ),
            yaxis=dict(
                fixedrange=False,
                title="Temperature / °C",
                tickfont=dict(color="#2A4CDF"),
                gridcolor="#EAEDFC",
            ),
            showlegend=True,
        )
        self.figures = [PlotlyFigure(label="my figure 1", figure=fig.to_plotly_json())]
