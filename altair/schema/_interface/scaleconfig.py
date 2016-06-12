# This file auto-generated by `generate_schema_interface.py`.
# Do not modify this file directly.

import traitlets as T
from ..baseobject import BaseObject


class ScaleConfig(BaseObject):
    """Wrapper for Vega-Lite ScaleConfig definition.
    
    Attributes
    ----------
    bandSize: CFloat
        Default band size for (1) `y` ordinal scale, and (2) `x` ordinal scale when the mark is not `text`.
    barSizeRange: List(CFloat)
        Default range for bar size scale.
    fontSizeRange: List(CFloat)
        Default range for font size scale.
    nominalColorRange: Union(Unicode, List(Unicode))
        Default range for nominal color scale.
    opacity: List(CFloat)
        Default range for opacity.
    padding: CFloat
        Default padding for `x` and `y` ordinal scales.
    pointSizeRange: List(CFloat)
        Default range for bar size scale.
    round: Bool
        If true, rounds numeric output values to integers.
    ruleSizeRange: List(CFloat)
        Default range for rule stroke widths.
    sequentialColorRange: Union(Unicode, List(Unicode))
        Default range for ordinal / continuous color scale.
    shapeRange: Union(Unicode, List(Unicode))
        Default range for shape.
    textBandWidth: CFloat
        Default band width for `x` ordinal scale when is mark is `text`.
    tickSizeRange: List(CFloat)
        Default range for tick spans.
    useRawDomain: Bool
        Uses the source data range as scale domain instead of aggregated data for aggregate axis.
    """
    bandSize = T.CFloat(allow_none=True, default_value=None, min=0, help="""Default band size for (1) `y` ordinal scale, and (2) `x` ordinal scale when the mark is not `text`.""")
    barSizeRange = T.List(T.CFloat(allow_none=True, default_value=None), allow_none=True, default_value=None, help="""Default range for bar size scale.""")
    fontSizeRange = T.List(T.CFloat(allow_none=True, default_value=None), allow_none=True, default_value=None, help="""Default range for font size scale.""")
    nominalColorRange = T.Union([T.Unicode(allow_none=True, default_value=None), T.List(T.Unicode(allow_none=True, default_value=None), allow_none=True, default_value=None)])
    opacity = T.List(T.CFloat(allow_none=True, default_value=None), allow_none=True, default_value=None, help="""Default range for opacity.""")
    padding = T.CFloat(allow_none=True, default_value=None, help="""Default padding for `x` and `y` ordinal scales.""")
    pointSizeRange = T.List(T.CFloat(allow_none=True, default_value=None), allow_none=True, default_value=None, help="""Default range for bar size scale.""")
    round = T.Bool(allow_none=True, default_value=None, help="""If true, rounds numeric output values to integers.""")
    ruleSizeRange = T.List(T.CFloat(allow_none=True, default_value=None), allow_none=True, default_value=None, help="""Default range for rule stroke widths.""")
    sequentialColorRange = T.Union([T.Unicode(allow_none=True, default_value=None), T.List(T.Unicode(allow_none=True, default_value=None), allow_none=True, default_value=None)])
    shapeRange = T.Union([T.Unicode(allow_none=True, default_value=None), T.List(T.Unicode(allow_none=True, default_value=None), allow_none=True, default_value=None)])
    textBandWidth = T.CFloat(allow_none=True, default_value=None, min=0, help="""Default band width for `x` ordinal scale when is mark is `text`.""")
    tickSizeRange = T.List(T.CFloat(allow_none=True, default_value=None), allow_none=True, default_value=None, help="""Default range for tick spans.""")
    useRawDomain = T.Bool(allow_none=True, default_value=None, help="""Uses the source data range as scale domain instead of aggregated data for aggregate axis.""")
    
    def __init__(self, bandSize=None, barSizeRange=None, fontSizeRange=None, nominalColorRange=None, opacity=None, padding=None, pointSizeRange=None, round=None, ruleSizeRange=None, sequentialColorRange=None, shapeRange=None, textBandWidth=None, tickSizeRange=None, useRawDomain=None, **kwargs):
        kwds = dict(bandSize=bandSize, barSizeRange=barSizeRange, fontSizeRange=fontSizeRange, nominalColorRange=nominalColorRange, opacity=opacity, padding=padding, pointSizeRange=pointSizeRange, round=round, ruleSizeRange=ruleSizeRange, sequentialColorRange=sequentialColorRange, shapeRange=shapeRange, textBandWidth=textBandWidth, tickSizeRange=tickSizeRange, useRawDomain=useRawDomain)
        kwargs.update({k:v for k, v in kwds.items() if v is not None})
        super(ScaleConfig, self).__init__(**kwargs)