# Auto generated from mifc.yaml by pythongen.py version: 0.9.0
# Generation date: 2023-09-12T15:39:28
# Schema: mifc
#
# id: https://w3id.org/kaiiam/mifc
# description: A minimum information standard checklist formalizing the description of food composition data and
#              related metadata.
# license: MIT

import dataclasses
import sys
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import Float, Integer, String

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
FDC = CurieNamespace('FDC', 'https://fdc.nal.usda.gov/')
OBI = CurieNamespace('OBI', 'http://purl.obolibrary.org/obo/OBI_')
PATO = CurieNamespace('PATO', 'http://purl.obolibrary.org/obo/PATO_')
PTFI = CurieNamespace('PTFI', 'https://foodperiodictable.org/')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/')
EXAMPLE = CurieNamespace('example', 'https://example.org/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
MIFC = CurieNamespace('mifc', 'https://w3id.org/kaiiam/mifc/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
DEFAULT_ = MIFC


# Types

# Class references



@dataclass
class NamedThing(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MIFC.NamedThing
    class_class_curie: ClassVar[str] = "mifc:NamedThing"
    class_name: ClassVar[str] = "NamedThing"
    class_model_uri: ClassVar[URIRef] = MIFC.NamedThing

    id: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.id is not None and not isinstance(self.id, str):
            self.id = str(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Food(NamedThing):
    """
    Metadata about foods
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA.Food
    class_class_curie: ClassVar[str] = "schema:Food"
    class_name: ClassVar[str] = "Food"
    class_model_uri: ClassVar[URIRef] = MIFC.Food

    primary_food_type: Optional[str] = None
    primary_food_type_label: Optional[str] = None
    primary_food_type_upc_code: Optional[int] = None
    food_preparation_state: Optional[Union[str, "FoodPreparationState"]] = None
    food_acquisition_city: Optional[str] = None
    food_acquisition_country: Optional[str] = None
    food_acquisition_country_subdivision: Optional[str] = None
    food_acquisition_date: Optional[str] = None
    food_acquisition_location_type: Optional[Union[str, "FoodAcquisitionLocationType"]] = None
    food_acquisition_latitude: Optional[float] = None
    food_acquisition_longitude: Optional[float] = None
    food_distributor_city: Optional[str] = None
    food_distributor_country: Optional[str] = None
    food_distributor_country_subdivision: Optional[str] = None
    food_expiration_date: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.primary_food_type is not None and not isinstance(self.primary_food_type, str):
            self.primary_food_type = str(self.primary_food_type)

        if self.primary_food_type_label is not None and not isinstance(self.primary_food_type_label, str):
            self.primary_food_type_label = str(self.primary_food_type_label)

        if self.primary_food_type_upc_code is not None and not isinstance(self.primary_food_type_upc_code, int):
            self.primary_food_type_upc_code = int(self.primary_food_type_upc_code)

        if self.food_preparation_state is not None and not isinstance(self.food_preparation_state, FoodPreparationState):
            self.food_preparation_state = FoodPreparationState(self.food_preparation_state)

        if self.food_acquisition_city is not None and not isinstance(self.food_acquisition_city, str):
            self.food_acquisition_city = str(self.food_acquisition_city)

        if self.food_acquisition_country is not None and not isinstance(self.food_acquisition_country, str):
            self.food_acquisition_country = str(self.food_acquisition_country)

        if self.food_acquisition_country_subdivision is not None and not isinstance(self.food_acquisition_country_subdivision, str):
            self.food_acquisition_country_subdivision = str(self.food_acquisition_country_subdivision)

        if self.food_acquisition_date is not None and not isinstance(self.food_acquisition_date, str):
            self.food_acquisition_date = str(self.food_acquisition_date)

        if self.food_acquisition_location_type is not None and not isinstance(self.food_acquisition_location_type, FoodAcquisitionLocationType):
            self.food_acquisition_location_type = FoodAcquisitionLocationType(self.food_acquisition_location_type)

        if self.food_acquisition_latitude is not None and not isinstance(self.food_acquisition_latitude, float):
            self.food_acquisition_latitude = float(self.food_acquisition_latitude)

        if self.food_acquisition_longitude is not None and not isinstance(self.food_acquisition_longitude, float):
            self.food_acquisition_longitude = float(self.food_acquisition_longitude)

        if self.food_distributor_city is not None and not isinstance(self.food_distributor_city, str):
            self.food_distributor_city = str(self.food_distributor_city)

        if self.food_distributor_country is not None and not isinstance(self.food_distributor_country, str):
            self.food_distributor_country = str(self.food_distributor_country)

        if self.food_distributor_country_subdivision is not None and not isinstance(self.food_distributor_country_subdivision, str):
            self.food_distributor_country_subdivision = str(self.food_distributor_country_subdivision)

        if self.food_expiration_date is not None and not isinstance(self.food_expiration_date, str):
            self.food_expiration_date = str(self.food_expiration_date)

        super().__post_init__(**kwargs)


@dataclass
class Component(NamedThing):
    """
    Metadata about measured components of nutritional interest
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA.Component
    class_class_curie: ClassVar[str] = "schema:Component"
    class_name: ClassVar[str] = "Component"
    class_model_uri: ClassVar[URIRef] = MIFC.Component

    measured_compound: Optional[str] = None
    measured_compound_value: Optional[float] = None
    measured_compound_unit: Optional[str] = None
    measured_compound_denominator_value: Optional[float] = None
    measured_compound_denominator_unit: Optional[str] = None
    measured_compound_data_points_number: Optional[int] = None
    measured_compound_record_date: Optional[str] = None
    measured_compound_analysis_date: Optional[str] = None
    measured_compound_comment: Optional[str] = None
    measured_compound_derivation_type: Optional[str] = None
    measured_compound_limit_of_quantitation: Optional[str] = None
    laboratory_sample_aggregation_minimum_measured_compound_value: Optional[float] = None
    laboratory_sample_aggregation_maximum_measured_compound_value: Optional[float] = None
    laboratory_sample_aggregation_median_measured_compound_value: Optional[float] = None
    laboratory_sample_aggregation_measured_compound_standard_deviation: Optional[float] = None
    analytical_analysis_measurement_protocol_doi: Optional[str] = None
    analytical_analysis_measurement_method: Optional[Union[str, "AnalyticalMeasurementMethod"]] = None
    laboratory_conducting_analytical_analysis: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.measured_compound is not None and not isinstance(self.measured_compound, str):
            self.measured_compound = str(self.measured_compound)

        if self.measured_compound_value is not None and not isinstance(self.measured_compound_value, float):
            self.measured_compound_value = float(self.measured_compound_value)

        if self.measured_compound_unit is not None and not isinstance(self.measured_compound_unit, str):
            self.measured_compound_unit = str(self.measured_compound_unit)

        if self.measured_compound_denominator_value is not None and not isinstance(self.measured_compound_denominator_value, float):
            self.measured_compound_denominator_value = float(self.measured_compound_denominator_value)

        if self.measured_compound_denominator_unit is not None and not isinstance(self.measured_compound_denominator_unit, str):
            self.measured_compound_denominator_unit = str(self.measured_compound_denominator_unit)

        if self.measured_compound_data_points_number is not None and not isinstance(self.measured_compound_data_points_number, int):
            self.measured_compound_data_points_number = int(self.measured_compound_data_points_number)

        if self.measured_compound_record_date is not None and not isinstance(self.measured_compound_record_date, str):
            self.measured_compound_record_date = str(self.measured_compound_record_date)

        if self.measured_compound_analysis_date is not None and not isinstance(self.measured_compound_analysis_date, str):
            self.measured_compound_analysis_date = str(self.measured_compound_analysis_date)

        if self.measured_compound_comment is not None and not isinstance(self.measured_compound_comment, str):
            self.measured_compound_comment = str(self.measured_compound_comment)

        if self.measured_compound_derivation_type is not None and not isinstance(self.measured_compound_derivation_type, str):
            self.measured_compound_derivation_type = str(self.measured_compound_derivation_type)

        if self.measured_compound_limit_of_quantitation is not None and not isinstance(self.measured_compound_limit_of_quantitation, str):
            self.measured_compound_limit_of_quantitation = str(self.measured_compound_limit_of_quantitation)

        if self.laboratory_sample_aggregation_minimum_measured_compound_value is not None and not isinstance(self.laboratory_sample_aggregation_minimum_measured_compound_value, float):
            self.laboratory_sample_aggregation_minimum_measured_compound_value = float(self.laboratory_sample_aggregation_minimum_measured_compound_value)

        if self.laboratory_sample_aggregation_maximum_measured_compound_value is not None and not isinstance(self.laboratory_sample_aggregation_maximum_measured_compound_value, float):
            self.laboratory_sample_aggregation_maximum_measured_compound_value = float(self.laboratory_sample_aggregation_maximum_measured_compound_value)

        if self.laboratory_sample_aggregation_median_measured_compound_value is not None and not isinstance(self.laboratory_sample_aggregation_median_measured_compound_value, float):
            self.laboratory_sample_aggregation_median_measured_compound_value = float(self.laboratory_sample_aggregation_median_measured_compound_value)

        if self.laboratory_sample_aggregation_measured_compound_standard_deviation is not None and not isinstance(self.laboratory_sample_aggregation_measured_compound_standard_deviation, float):
            self.laboratory_sample_aggregation_measured_compound_standard_deviation = float(self.laboratory_sample_aggregation_measured_compound_standard_deviation)

        if self.analytical_analysis_measurement_protocol_doi is not None and not isinstance(self.analytical_analysis_measurement_protocol_doi, str):
            self.analytical_analysis_measurement_protocol_doi = str(self.analytical_analysis_measurement_protocol_doi)

        if self.analytical_analysis_measurement_method is not None and not isinstance(self.analytical_analysis_measurement_method, AnalyticalMeasurementMethod):
            self.analytical_analysis_measurement_method = AnalyticalMeasurementMethod(self.analytical_analysis_measurement_method)

        if self.laboratory_conducting_analytical_analysis is not None and not isinstance(self.laboratory_conducting_analytical_analysis, str):
            self.laboratory_conducting_analytical_analysis = str(self.laboratory_conducting_analytical_analysis)

        super().__post_init__(**kwargs)


@dataclass
class Container(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MIFC.Container
    class_class_curie: ClassVar[str] = "mifc:Container"
    class_name: ClassVar[str] = "Container"
    class_model_uri: ClassVar[URIRef] = MIFC.Container

    foods: Optional[Union[Union[dict, Food], List[Union[dict, Food]]]] = empty_list()
    components: Optional[Union[Union[dict, Component], List[Union[dict, Component]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.foods, list):
            self.foods = [self.foods] if self.foods is not None else []
        self.foods = [v if isinstance(v, Food) else Food(**as_dict(v)) for v in self.foods]

        if not isinstance(self.components, list):
            self.components = [self.components] if self.components is not None else []
        self.components = [v if isinstance(v, Component) else Component(**as_dict(v)) for v in self.components]

        super().__post_init__(**kwargs)


# Enumerations
class AnalyticalMeasurementMethod(EnumDefinitionImpl):

    HPLC = PermissibleValue(text="HPLC",
                               description="High performance liquid chromotography",
                               meaning=OBI["0002116"])
    GLC = PermissibleValue(text="GLC",
                             description="gas-liquid chromatography")
    GC = PermissibleValue(text="GC")
    Nephelometry = PermissibleValue(text="Nephelometry")
    Gravimetric = PermissibleValue(text="Gravimetric")
    Fluorometric = PermissibleValue(text="Fluorometric")
    Kjeldahl = PermissibleValue(text="Kjeldahl")

    _defn = EnumDefinition(
        name="AnalyticalMeasurementMethod",
    )

class FoodPreparationState(EnumDefinitionImpl):

    raw = PermissibleValue(text="raw")
    fresh = PermissibleValue(text="fresh")
    chilled = PermissibleValue(text="chilled")
    frozen = PermissibleValue(text="frozen")
    unripe = PermissibleValue(text="unripe")
    ripe = PermissibleValue(text="ripe")
    overripe = PermissibleValue(text="overripe")
    dried = PermissibleValue(text="dried")
    irradiated = PermissibleValue(text="irradiated")

    _defn = EnumDefinition(
        name="FoodPreparationState",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "foodsafe chilled",
                PermissibleValue(text="foodsafe chilled") )
        setattr(cls, "fresh chilled",
                PermissibleValue(text="fresh chilled") )
        setattr(cls, "fresh frozen",
                PermissibleValue(text="fresh frozen") )
        setattr(cls, "slightly ripe",
                PermissibleValue(text="slightly ripe") )
        setattr(cls, "naturally dried",
                PermissibleValue(text="naturally dried") )
        setattr(cls, "artificially dried",
                PermissibleValue(text="artificially dried") )
        setattr(cls, "heat treated",
                PermissibleValue(text="heat treated") )

class FoodAcquisitionLocationType(EnumDefinitionImpl):

    field = PermissibleValue(text="field")
    supermarket = PermissibleValue(text="supermarket")
    biobank = PermissibleValue(text="biobank")
    unknown = PermissibleValue(text="unknown")
    other = PermissibleValue(text="other")

    _defn = EnumDefinition(
        name="FoodAcquisitionLocationType",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "fresh market",
                PermissibleValue(text="fresh market") )
        setattr(cls, "small grocery",
                PermissibleValue(text="small grocery") )

# Slots
class slots:
    pass

slots.id = Slot(uri=MIFC.id, name="id", curie=MIFC.curie('id'),
                   model_uri=MIFC.id, domain=None, range=Optional[str])

slots.primary_food_type = Slot(uri=SCHEMA.name, name="primary_food_type", curie=SCHEMA.curie('name'),
                   model_uri=MIFC.primary_food_type, domain=None, range=Optional[str])

slots.primary_food_type_label = Slot(uri=MIFC.primary_food_type_label, name="primary_food_type_label", curie=MIFC.curie('primary_food_type_label'),
                   model_uri=MIFC.primary_food_type_label, domain=None, range=Optional[str])

slots.primary_food_type_upc_code = Slot(uri=MIFC.primary_food_type_upc_code, name="primary_food_type_upc_code", curie=MIFC.curie('primary_food_type_upc_code'),
                   model_uri=MIFC.primary_food_type_upc_code, domain=None, range=Optional[int])

slots.food_preparation_state = Slot(uri=MIFC.food_preparation_state, name="food_preparation_state", curie=MIFC.curie('food_preparation_state'),
                   model_uri=MIFC.food_preparation_state, domain=None, range=Optional[Union[str, "FoodPreparationState"]])

slots.food_acquisition_city = Slot(uri=MIFC.food_acquisition_city, name="food_acquisition_city", curie=MIFC.curie('food_acquisition_city'),
                   model_uri=MIFC.food_acquisition_city, domain=None, range=Optional[str])

slots.food_acquisition_country = Slot(uri=MIFC.food_acquisition_country, name="food_acquisition_country", curie=MIFC.curie('food_acquisition_country'),
                   model_uri=MIFC.food_acquisition_country, domain=None, range=Optional[str])

slots.food_acquisition_country_subdivision = Slot(uri=MIFC.food_acquisition_country_subdivision, name="food_acquisition_country_subdivision", curie=MIFC.curie('food_acquisition_country_subdivision'),
                   model_uri=MIFC.food_acquisition_country_subdivision, domain=None, range=Optional[str])

slots.food_acquisition_date = Slot(uri=MIFC.food_acquisition_date, name="food_acquisition_date", curie=MIFC.curie('food_acquisition_date'),
                   model_uri=MIFC.food_acquisition_date, domain=None, range=Optional[str])

slots.food_acquisition_location_type = Slot(uri=MIFC.food_acquisition_location_type, name="food_acquisition_location_type", curie=MIFC.curie('food_acquisition_location_type'),
                   model_uri=MIFC.food_acquisition_location_type, domain=None, range=Optional[Union[str, "FoodAcquisitionLocationType"]])

slots.food_acquisition_latitude = Slot(uri=MIFC.food_acquisition_latitude, name="food_acquisition_latitude", curie=MIFC.curie('food_acquisition_latitude'),
                   model_uri=MIFC.food_acquisition_latitude, domain=None, range=Optional[float])

slots.food_acquisition_longitude = Slot(uri=MIFC.food_acquisition_longitude, name="food_acquisition_longitude", curie=MIFC.curie('food_acquisition_longitude'),
                   model_uri=MIFC.food_acquisition_longitude, domain=None, range=Optional[float])

slots.food_distributor_city = Slot(uri=MIFC.food_distributor_city, name="food_distributor_city", curie=MIFC.curie('food_distributor_city'),
                   model_uri=MIFC.food_distributor_city, domain=None, range=Optional[str])

slots.food_distributor_country = Slot(uri=MIFC.food_distributor_country, name="food_distributor_country", curie=MIFC.curie('food_distributor_country'),
                   model_uri=MIFC.food_distributor_country, domain=None, range=Optional[str])

slots.food_distributor_country_subdivision = Slot(uri=MIFC.food_distributor_country_subdivision, name="food_distributor_country_subdivision", curie=MIFC.curie('food_distributor_country_subdivision'),
                   model_uri=MIFC.food_distributor_country_subdivision, domain=None, range=Optional[str])

slots.food_expiration_date = Slot(uri=MIFC.food_expiration_date, name="food_expiration_date", curie=MIFC.curie('food_expiration_date'),
                   model_uri=MIFC.food_expiration_date, domain=None, range=Optional[str])

slots.measured_compound = Slot(uri=MIFC.measured_compound, name="measured_compound", curie=MIFC.curie('measured_compound'),
                   model_uri=MIFC.measured_compound, domain=None, range=Optional[str])

slots.measured_compound_value = Slot(uri=MIFC.measured_compound_value, name="measured_compound_value", curie=MIFC.curie('measured_compound_value'),
                   model_uri=MIFC.measured_compound_value, domain=None, range=Optional[float])

slots.measured_compound_unit = Slot(uri=MIFC.measured_compound_unit, name="measured_compound_unit", curie=MIFC.curie('measured_compound_unit'),
                   model_uri=MIFC.measured_compound_unit, domain=None, range=Optional[str])

slots.measured_compound_denominator_value = Slot(uri=MIFC.measured_compound_denominator_value, name="measured_compound_denominator_value", curie=MIFC.curie('measured_compound_denominator_value'),
                   model_uri=MIFC.measured_compound_denominator_value, domain=None, range=Optional[float])

slots.measured_compound_denominator_unit = Slot(uri=MIFC.measured_compound_denominator_unit, name="measured_compound_denominator_unit", curie=MIFC.curie('measured_compound_denominator_unit'),
                   model_uri=MIFC.measured_compound_denominator_unit, domain=None, range=Optional[str])

slots.measured_compound_data_points_number = Slot(uri=MIFC.measured_compound_data_points_number, name="measured_compound_data_points_number", curie=MIFC.curie('measured_compound_data_points_number'),
                   model_uri=MIFC.measured_compound_data_points_number, domain=None, range=Optional[int])

slots.measured_compound_record_date = Slot(uri=MIFC.measured_compound_record_date, name="measured_compound_record_date", curie=MIFC.curie('measured_compound_record_date'),
                   model_uri=MIFC.measured_compound_record_date, domain=None, range=Optional[str])

slots.measured_compound_analysis_date = Slot(uri=MIFC.measured_compound_analysis_date, name="measured_compound_analysis_date", curie=MIFC.curie('measured_compound_analysis_date'),
                   model_uri=MIFC.measured_compound_analysis_date, domain=None, range=Optional[str])

slots.measured_compound_comment = Slot(uri=MIFC.measured_compound_comment, name="measured_compound_comment", curie=MIFC.curie('measured_compound_comment'),
                   model_uri=MIFC.measured_compound_comment, domain=None, range=Optional[str])

slots.measured_compound_derivation_type = Slot(uri=MIFC.measured_compound_derivation_type, name="measured_compound_derivation_type", curie=MIFC.curie('measured_compound_derivation_type'),
                   model_uri=MIFC.measured_compound_derivation_type, domain=None, range=Optional[str])

slots.measured_compound_limit_of_quantitation = Slot(uri=MIFC.measured_compound_limit_of_quantitation, name="measured_compound_limit_of_quantitation", curie=MIFC.curie('measured_compound_limit_of_quantitation'),
                   model_uri=MIFC.measured_compound_limit_of_quantitation, domain=None, range=Optional[str])

slots.laboratory_sample_aggregation_minimum_measured_compound_value = Slot(uri=MIFC.laboratory_sample_aggregation_minimum_measured_compound_value, name="laboratory_sample_aggregation_minimum_measured_compound_value", curie=MIFC.curie('laboratory_sample_aggregation_minimum_measured_compound_value'),
                   model_uri=MIFC.laboratory_sample_aggregation_minimum_measured_compound_value, domain=None, range=Optional[float])

slots.laboratory_sample_aggregation_maximum_measured_compound_value = Slot(uri=MIFC.laboratory_sample_aggregation_maximum_measured_compound_value, name="laboratory_sample_aggregation_maximum_measured_compound_value", curie=MIFC.curie('laboratory_sample_aggregation_maximum_measured_compound_value'),
                   model_uri=MIFC.laboratory_sample_aggregation_maximum_measured_compound_value, domain=None, range=Optional[float])

slots.laboratory_sample_aggregation_median_measured_compound_value = Slot(uri=MIFC.laboratory_sample_aggregation_median_measured_compound_value, name="laboratory_sample_aggregation_median_measured_compound_value", curie=MIFC.curie('laboratory_sample_aggregation_median_measured_compound_value'),
                   model_uri=MIFC.laboratory_sample_aggregation_median_measured_compound_value, domain=None, range=Optional[float])

slots.laboratory_sample_aggregation_measured_compound_standard_deviation = Slot(uri=MIFC.laboratory_sample_aggregation_measured_compound_standard_deviation, name="laboratory_sample_aggregation_measured_compound_standard_deviation", curie=MIFC.curie('laboratory_sample_aggregation_measured_compound_standard_deviation'),
                   model_uri=MIFC.laboratory_sample_aggregation_measured_compound_standard_deviation, domain=None, range=Optional[float])

slots.analytical_analysis_measurement_protocol_doi = Slot(uri=MIFC.analytical_analysis_measurement_protocol_doi, name="analytical_analysis_measurement_protocol_doi", curie=MIFC.curie('analytical_analysis_measurement_protocol_doi'),
                   model_uri=MIFC.analytical_analysis_measurement_protocol_doi, domain=None, range=Optional[str])

slots.analytical_analysis_measurement_method = Slot(uri=MIFC.analytical_analysis_measurement_method, name="analytical_analysis_measurement_method", curie=MIFC.curie('analytical_analysis_measurement_method'),
                   model_uri=MIFC.analytical_analysis_measurement_method, domain=None, range=Optional[Union[str, "AnalyticalMeasurementMethod"]])

slots.laboratory_conducting_analytical_analysis = Slot(uri=MIFC.laboratory_conducting_analytical_analysis, name="laboratory_conducting_analytical_analysis", curie=MIFC.curie('laboratory_conducting_analytical_analysis'),
                   model_uri=MIFC.laboratory_conducting_analytical_analysis, domain=None, range=Optional[str])

slots.container__foods = Slot(uri=MIFC.foods, name="container__foods", curie=MIFC.curie('foods'),
                   model_uri=MIFC.container__foods, domain=None, range=Optional[Union[Union[dict, Food], List[Union[dict, Food]]]])

slots.container__components = Slot(uri=MIFC.components, name="container__components", curie=MIFC.curie('components'),
                   model_uri=MIFC.container__components, domain=None, range=Optional[Union[Union[dict, Component], List[Union[dict, Component]]]])