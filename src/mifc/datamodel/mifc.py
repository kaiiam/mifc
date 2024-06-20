# Auto generated from mifc.yaml by pythongen.py version: 0.0.1
# Generation date: 2024-06-20T17:37:48
# Schema: mifc
#
# id: https://w3id.org/kaiiam/mifc
# description: A minimum information standard checklist formalizing the description of food composition data and related metadata.
# license: MIT

import dataclasses
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from datetime import date, datetime
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import Boolean, Float, Integer, String
from linkml_runtime.utils.metamodelcore import Bool

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
class FoodFoodSampleId(extended_str):
    pass


class NamedThing(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MIFC["NamedThing"]
    class_class_curie: ClassVar[str] = "mifc:NamedThing"
    class_name: ClassVar[str] = "NamedThing"
    class_model_uri: ClassVar[URIRef] = MIFC.NamedThing


@dataclass
class Food(NamedThing):
    """
    Metadata about foods analyzed for components of nutritional interest.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["Food"]
    class_class_curie: ClassVar[str] = "schema:Food"
    class_name: ClassVar[str] = "Food"
    class_model_uri: ClassVar[URIRef] = MIFC.Food

    food_sample_id: Union[str, FoodFoodSampleId] = None
    food_primary_type: Optional[str] = None
    food_primary_type_label: Optional[str] = None
    food_upc_code: Optional[int] = None
    food_preservation_state: Optional[Union[str, "FoodPreservationState"]] = None
    food_storage_temperature_state: Optional[Union[str, "FoodStorageTemperatureState"]] = None
    food_ripeness_state: Optional[Union[str, "FoodRipenessState"]] = None
    food_cooking_method: Optional[Union[str, "FoodCookingMethod"]] = None
    food_acquisition_city: Optional[str] = None
    food_acquisition_country: Optional[str] = None
    food_acquisition_country_subdivision: Optional[str] = None
    food_acquisition_date: Optional[str] = None
    food_acquisition_location_type: Optional[Union[str, "FoodAcquisitionLocationType"]] = None
    food_acquisition_latitude: Optional[float] = None
    food_acquisition_longitude: Optional[float] = None
    food_acquisition_agent_name: Optional[str] = None
    food_acquisition_organization: Optional[str] = None
    food_distributor_city: Optional[str] = None
    food_distributor_country: Optional[str] = None
    food_distributor_country_subdivision: Optional[str] = None
    food_expiration_date: Optional[str] = None
    food_category_label: Optional[str] = None
    food_additional_types: Optional[str] = None
    food_laboratory_sample_id: Optional[str] = None
    food_laboratory_sample_aliquot_id: Optional[str] = None
    food_laboratory_sample_batch_id: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.food_sample_id):
            self.MissingRequiredField("food_sample_id")
        if not isinstance(self.food_sample_id, FoodFoodSampleId):
            self.food_sample_id = FoodFoodSampleId(self.food_sample_id)

        if self.food_primary_type is not None and not isinstance(self.food_primary_type, str):
            self.food_primary_type = str(self.food_primary_type)

        if self.food_primary_type_label is not None and not isinstance(self.food_primary_type_label, str):
            self.food_primary_type_label = str(self.food_primary_type_label)

        if self.food_upc_code is not None and not isinstance(self.food_upc_code, int):
            self.food_upc_code = int(self.food_upc_code)

        if self.food_preservation_state is not None and not isinstance(self.food_preservation_state, FoodPreservationState):
            self.food_preservation_state = FoodPreservationState(self.food_preservation_state)

        if self.food_storage_temperature_state is not None and not isinstance(self.food_storage_temperature_state, FoodStorageTemperatureState):
            self.food_storage_temperature_state = FoodStorageTemperatureState(self.food_storage_temperature_state)

        if self.food_ripeness_state is not None and not isinstance(self.food_ripeness_state, FoodRipenessState):
            self.food_ripeness_state = FoodRipenessState(self.food_ripeness_state)

        if self.food_cooking_method is not None and not isinstance(self.food_cooking_method, FoodCookingMethod):
            self.food_cooking_method = FoodCookingMethod(self.food_cooking_method)

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

        if self.food_acquisition_agent_name is not None and not isinstance(self.food_acquisition_agent_name, str):
            self.food_acquisition_agent_name = str(self.food_acquisition_agent_name)

        if self.food_acquisition_organization is not None and not isinstance(self.food_acquisition_organization, str):
            self.food_acquisition_organization = str(self.food_acquisition_organization)

        if self.food_distributor_city is not None and not isinstance(self.food_distributor_city, str):
            self.food_distributor_city = str(self.food_distributor_city)

        if self.food_distributor_country is not None and not isinstance(self.food_distributor_country, str):
            self.food_distributor_country = str(self.food_distributor_country)

        if self.food_distributor_country_subdivision is not None and not isinstance(self.food_distributor_country_subdivision, str):
            self.food_distributor_country_subdivision = str(self.food_distributor_country_subdivision)

        if self.food_expiration_date is not None and not isinstance(self.food_expiration_date, str):
            self.food_expiration_date = str(self.food_expiration_date)

        if self.food_category_label is not None and not isinstance(self.food_category_label, str):
            self.food_category_label = str(self.food_category_label)

        if self.food_additional_types is not None and not isinstance(self.food_additional_types, str):
            self.food_additional_types = str(self.food_additional_types)

        if self.food_laboratory_sample_id is not None and not isinstance(self.food_laboratory_sample_id, str):
            self.food_laboratory_sample_id = str(self.food_laboratory_sample_id)

        if self.food_laboratory_sample_aliquot_id is not None and not isinstance(self.food_laboratory_sample_aliquot_id, str):
            self.food_laboratory_sample_aliquot_id = str(self.food_laboratory_sample_aliquot_id)

        if self.food_laboratory_sample_batch_id is not None and not isinstance(self.food_laboratory_sample_batch_id, str):
            self.food_laboratory_sample_batch_id = str(self.food_laboratory_sample_batch_id)

        super().__post_init__(**kwargs)


@dataclass
class Component(NamedThing):
    """
    Metadata about components of nutritional interest measured from foods.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["Component"]
    class_class_curie: ClassVar[str] = "schema:Component"
    class_name: ClassVar[str] = "Component"
    class_model_uri: ClassVar[URIRef] = MIFC.Component

    component_sample_id: str = None
    component_type: Optional[str] = None
    component_type_label: Optional[str] = None
    component_recorded_value: Optional[float] = None
    component_measurement_unit: Optional[str] = None
    component_data_points_number: Optional[int] = None
    component_record_date: Optional[str] = None
    component_analysis_date: Optional[str] = None
    component_comment: Optional[str] = None
    component_derivation_type: Optional[str] = None
    component_limit_of_quantitation: Optional[str] = None
    laboratory_sample_aggregation_minimum_measured_compound_value: Optional[float] = None
    laboratory_sample_aggregation_maximum_measured_compound_value: Optional[float] = None
    laboratory_sample_aggregation_median_measured_compound_value: Optional[float] = None
    laboratory_sample_aggregation_measured_compound_standard_deviation: Optional[float] = None
    compound_analytical_measurement_protocol_doi: Optional[str] = None
    compound_analytical_measurement_method: Optional[Union[str, "AnalyticalMeasurementMethod"]] = None
    compound_analytical_laboratory_name: Optional[str] = None
    component_quality_control_remeasurement: Optional[Union[bool, Bool]] = None
    food_laboratory_sample_id: Optional[str] = None
    food_laboratory_sample_aliquot_id: Optional[str] = None
    food_laboratory_sample_batch_id: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.component_sample_id):
            self.MissingRequiredField("component_sample_id")
        if not isinstance(self.component_sample_id, str):
            self.component_sample_id = str(self.component_sample_id)

        if self.component_type is not None and not isinstance(self.component_type, str):
            self.component_type = str(self.component_type)

        if self.component_type_label is not None and not isinstance(self.component_type_label, str):
            self.component_type_label = str(self.component_type_label)

        if self.component_recorded_value is not None and not isinstance(self.component_recorded_value, float):
            self.component_recorded_value = float(self.component_recorded_value)

        if self.component_measurement_unit is not None and not isinstance(self.component_measurement_unit, str):
            self.component_measurement_unit = str(self.component_measurement_unit)

        if self.component_data_points_number is not None and not isinstance(self.component_data_points_number, int):
            self.component_data_points_number = int(self.component_data_points_number)

        if self.component_record_date is not None and not isinstance(self.component_record_date, str):
            self.component_record_date = str(self.component_record_date)

        if self.component_analysis_date is not None and not isinstance(self.component_analysis_date, str):
            self.component_analysis_date = str(self.component_analysis_date)

        if self.component_comment is not None and not isinstance(self.component_comment, str):
            self.component_comment = str(self.component_comment)

        if self.component_derivation_type is not None and not isinstance(self.component_derivation_type, str):
            self.component_derivation_type = str(self.component_derivation_type)

        if self.component_limit_of_quantitation is not None and not isinstance(self.component_limit_of_quantitation, str):
            self.component_limit_of_quantitation = str(self.component_limit_of_quantitation)

        if self.laboratory_sample_aggregation_minimum_measured_compound_value is not None and not isinstance(self.laboratory_sample_aggregation_minimum_measured_compound_value, float):
            self.laboratory_sample_aggregation_minimum_measured_compound_value = float(self.laboratory_sample_aggregation_minimum_measured_compound_value)

        if self.laboratory_sample_aggregation_maximum_measured_compound_value is not None and not isinstance(self.laboratory_sample_aggregation_maximum_measured_compound_value, float):
            self.laboratory_sample_aggregation_maximum_measured_compound_value = float(self.laboratory_sample_aggregation_maximum_measured_compound_value)

        if self.laboratory_sample_aggregation_median_measured_compound_value is not None and not isinstance(self.laboratory_sample_aggregation_median_measured_compound_value, float):
            self.laboratory_sample_aggregation_median_measured_compound_value = float(self.laboratory_sample_aggregation_median_measured_compound_value)

        if self.laboratory_sample_aggregation_measured_compound_standard_deviation is not None and not isinstance(self.laboratory_sample_aggregation_measured_compound_standard_deviation, float):
            self.laboratory_sample_aggregation_measured_compound_standard_deviation = float(self.laboratory_sample_aggregation_measured_compound_standard_deviation)

        if self.compound_analytical_measurement_protocol_doi is not None and not isinstance(self.compound_analytical_measurement_protocol_doi, str):
            self.compound_analytical_measurement_protocol_doi = str(self.compound_analytical_measurement_protocol_doi)

        if self.compound_analytical_measurement_method is not None and not isinstance(self.compound_analytical_measurement_method, AnalyticalMeasurementMethod):
            self.compound_analytical_measurement_method = AnalyticalMeasurementMethod(self.compound_analytical_measurement_method)

        if self.compound_analytical_laboratory_name is not None and not isinstance(self.compound_analytical_laboratory_name, str):
            self.compound_analytical_laboratory_name = str(self.compound_analytical_laboratory_name)

        if self.component_quality_control_remeasurement is not None and not isinstance(self.component_quality_control_remeasurement, Bool):
            self.component_quality_control_remeasurement = Bool(self.component_quality_control_remeasurement)

        if self.food_laboratory_sample_id is not None and not isinstance(self.food_laboratory_sample_id, str):
            self.food_laboratory_sample_id = str(self.food_laboratory_sample_id)

        if self.food_laboratory_sample_aliquot_id is not None and not isinstance(self.food_laboratory_sample_aliquot_id, str):
            self.food_laboratory_sample_aliquot_id = str(self.food_laboratory_sample_aliquot_id)

        if self.food_laboratory_sample_batch_id is not None and not isinstance(self.food_laboratory_sample_batch_id, str):
            self.food_laboratory_sample_batch_id = str(self.food_laboratory_sample_batch_id)

        super().__post_init__(**kwargs)


@dataclass
class Provenance(NamedThing):
    """
    Supplemental data about the provenance of a Food and Component dataset collection standardized using MIFC.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["Provenance"]
    class_class_curie: ClassVar[str] = "schema:Provenance"
    class_name: ClassVar[str] = "Provenance"
    class_model_uri: ClassVar[URIRef] = MIFC.Provenance

    dataset_label: Optional[str] = None
    mifc_version_tag: Optional[str] = None
    contributor_orcid: Optional[str] = None
    organization_name: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.dataset_label is not None and not isinstance(self.dataset_label, str):
            self.dataset_label = str(self.dataset_label)

        if self.mifc_version_tag is not None and not isinstance(self.mifc_version_tag, str):
            self.mifc_version_tag = str(self.mifc_version_tag)

        if self.contributor_orcid is not None and not isinstance(self.contributor_orcid, str):
            self.contributor_orcid = str(self.contributor_orcid)

        if self.organization_name is not None and not isinstance(self.organization_name, str):
            self.organization_name = str(self.organization_name)

        super().__post_init__(**kwargs)


@dataclass
class Container(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MIFC["Container"]
    class_class_curie: ClassVar[str] = "mifc:Container"
    class_name: ClassVar[str] = "Container"
    class_model_uri: ClassVar[URIRef] = MIFC.Container

    foods: Optional[Union[Dict[Union[str, FoodFoodSampleId], Union[dict, Food]], List[Union[dict, Food]]]] = empty_dict()
    components: Optional[Union[Union[dict, Component], List[Union[dict, Component]]]] = empty_list()
    provenances: Optional[Union[Union[dict, Provenance], List[Union[dict, Provenance]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_list(slot_name="foods", slot_type=Food, key_name="food_sample_id", keyed=True)

        if not isinstance(self.components, list):
            self.components = [self.components] if self.components is not None else []
        self.components = [v if isinstance(v, Component) else Component(**as_dict(v)) for v in self.components]

        if not isinstance(self.provenances, list):
            self.provenances = [self.provenances] if self.provenances is not None else []
        self.provenances = [v if isinstance(v, Provenance) else Provenance(**as_dict(v)) for v in self.provenances]

        super().__post_init__(**kwargs)


# Enumerations
class AnalyticalMeasurementMethod(EnumDefinitionImpl):

    HPLC = PermissibleValue(
        text="HPLC",
        description="High performance liquid chromotography",
        meaning=OBI["0002116"])
    GLC = PermissibleValue(
        text="GLC",
        description="gas-liquid chromatography")
    GC = PermissibleValue(text="GC")
    Nephelometry = PermissibleValue(text="Nephelometry")
    Gravimetric = PermissibleValue(text="Gravimetric")
    Fluorometric = PermissibleValue(text="Fluorometric")
    Kjeldahl = PermissibleValue(text="Kjeldahl")

    _defn = EnumDefinition(
        name="AnalyticalMeasurementMethod",
    )

class FoodPreservationState(EnumDefinitionImpl):

    brined = PermissibleValue(text="brined")
    candied = PermissibleValue(text="candied")
    canned = PermissibleValue(text="canned")
    cured = PermissibleValue(text="cured")
    dried = PermissibleValue(text="dried")
    fermented = PermissibleValue(text="fermented")
    fresh = PermissibleValue(text="fresh")
    irradiated = PermissibleValue(text="irradiated")
    jellied = PermissibleValue(text="jellied")
    kippered = PermissibleValue(text="kippered")
    pasteurized = PermissibleValue(text="pasteurized")
    pickled = PermissibleValue(text="pickled")
    raw = PermissibleValue(text="raw")

    _defn = EnumDefinition(
        name="FoodPreservationState",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "air-dried",
            PermissibleValue(text="air-dried"))
        setattr(cls, "artificially dried",
            PermissibleValue(text="artificially dried"))
        setattr(cls, "freeze-dried",
            PermissibleValue(text="freeze-dried"))
        setattr(cls, "heat treated",
            PermissibleValue(text="heat treated"))
        setattr(cls, "naturally dried",
            PermissibleValue(text="naturally dried"))
        setattr(cls, "shelf stable",
            PermissibleValue(text="shelf stable"))
        setattr(cls, "sun-dried",
            PermissibleValue(text="sun-dried"))
        setattr(cls, "ultraviolet light exposed",
            PermissibleValue(text="ultraviolet light exposed"))

class FoodStorageTemperatureState(EnumDefinitionImpl):

    chilled = PermissibleValue(text="chilled")
    frozen = PermissibleValue(text="frozen")
    refrigerated = PermissibleValue(text="refrigerated")

    _defn = EnumDefinition(
        name="FoodStorageTemperatureState",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "foodsafe chilled",
            PermissibleValue(text="foodsafe chilled"))

class FoodRipenessState(EnumDefinitionImpl):

    ripe = PermissibleValue(text="ripe")
    overripe = PermissibleValue(text="overripe")
    unripe = PermissibleValue(text="unripe")

    _defn = EnumDefinition(
        name="FoodRipenessState",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "slightly ripe",
            PermissibleValue(text="slightly ripe"))

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
            PermissibleValue(text="fresh market"))
        setattr(cls, "small grocery",
            PermissibleValue(text="small grocery"))

class FoodCookingMethod(EnumDefinitionImpl):

    baked = PermissibleValue(text="baked")
    blanched = PermissibleValue(text="blanched")
    boiled = PermissibleValue(text="boiled")
    braised = PermissibleValue(text="braised")
    broiled = PermissibleValue(text="broiled")
    cooked = PermissibleValue(text="cooked")
    fried = PermissibleValue(text="fried")
    grilled = PermissibleValue(text="grilled")
    heated = PermissibleValue(text="heated")
    microwaved = PermissibleValue(text="microwaved")
    parboiled = PermissibleValue(text="parboiled")
    poached = PermissibleValue(text="poached")
    precooked = PermissibleValue(text="precooked")
    refried = PermissibleValue(text="refried")
    roasted = PermissibleValue(text="roasted")
    sauteed = PermissibleValue(text="sauteed")
    simmered = PermissibleValue(text="simmered")
    smoked = PermissibleValue(text="smoked")
    steamed = PermissibleValue(text="steamed")
    stewed = PermissibleValue(text="stewed")
    toasted = PermissibleValue(text="toasted")
    uncooked = PermissibleValue(text="uncooked")
    unheated = PermissibleValue(text="unheated")

    _defn = EnumDefinition(
        name="FoodCookingMethod",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "dry-heat cooked",
            PermissibleValue(text="dry-heat cooked"))
        setattr(cls, "dry-roasted",
            PermissibleValue(text="dry-roasted"))
        setattr(cls, "moist-heat cooked",
            PermissibleValue(text="moist-heat cooked"))
        setattr(cls, "oil-roasted",
            PermissibleValue(text="oil-roasted"))
        setattr(cls, "pan-broiled",
            PermissibleValue(text="pan-broiled"))
        setattr(cls, "pan-browned",
            PermissibleValue(text="pan-browned"))
        setattr(cls, "pan-fried",
            PermissibleValue(text="pan-fried"))
        setattr(cls, "partially fried",
            PermissibleValue(text="partially fried"))
        setattr(cls, "slow-roasted",
            PermissibleValue(text="slow-roasted"))
        setattr(cls, "spit-roasted",
            PermissibleValue(text="spit-roasted"))
        setattr(cls, "stir-fried",
            PermissibleValue(text="stir-fried"))

# Slots
class slots:
    pass

slots.food_sample_id = Slot(uri=MIFC.food_sample_id, name="food_sample_id", curie=MIFC.curie('food_sample_id'),
                   model_uri=MIFC.food_sample_id, domain=None, range=URIRef)

slots.food_primary_type = Slot(uri=SCHEMA.name, name="food_primary_type", curie=SCHEMA.curie('name'),
                   model_uri=MIFC.food_primary_type, domain=None, range=Optional[str])

slots.food_primary_type_label = Slot(uri=MIFC.food_primary_type_label, name="food_primary_type_label", curie=MIFC.curie('food_primary_type_label'),
                   model_uri=MIFC.food_primary_type_label, domain=None, range=Optional[str])

slots.food_upc_code = Slot(uri=MIFC.food_upc_code, name="food_upc_code", curie=MIFC.curie('food_upc_code'),
                   model_uri=MIFC.food_upc_code, domain=None, range=Optional[int])

slots.food_preservation_state = Slot(uri=MIFC.food_preservation_state, name="food_preservation_state", curie=MIFC.curie('food_preservation_state'),
                   model_uri=MIFC.food_preservation_state, domain=None, range=Optional[Union[str, "FoodPreservationState"]])

slots.food_storage_temperature_state = Slot(uri=MIFC.food_storage_temperature_state, name="food_storage_temperature_state", curie=MIFC.curie('food_storage_temperature_state'),
                   model_uri=MIFC.food_storage_temperature_state, domain=None, range=Optional[Union[str, "FoodStorageTemperatureState"]])

slots.food_ripeness_state = Slot(uri=MIFC.food_ripeness_state, name="food_ripeness_state", curie=MIFC.curie('food_ripeness_state'),
                   model_uri=MIFC.food_ripeness_state, domain=None, range=Optional[Union[str, "FoodRipenessState"]])

slots.food_cooking_method = Slot(uri=MIFC.food_cooking_method, name="food_cooking_method", curie=MIFC.curie('food_cooking_method'),
                   model_uri=MIFC.food_cooking_method, domain=None, range=Optional[Union[str, "FoodCookingMethod"]])

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

slots.food_acquisition_agent_name = Slot(uri=MIFC.food_acquisition_agent_name, name="food_acquisition_agent_name", curie=MIFC.curie('food_acquisition_agent_name'),
                   model_uri=MIFC.food_acquisition_agent_name, domain=None, range=Optional[str])

slots.food_acquisition_organization = Slot(uri=MIFC.food_acquisition_organization, name="food_acquisition_organization", curie=MIFC.curie('food_acquisition_organization'),
                   model_uri=MIFC.food_acquisition_organization, domain=None, range=Optional[str])

slots.food_distributor_city = Slot(uri=MIFC.food_distributor_city, name="food_distributor_city", curie=MIFC.curie('food_distributor_city'),
                   model_uri=MIFC.food_distributor_city, domain=None, range=Optional[str])

slots.food_distributor_country = Slot(uri=MIFC.food_distributor_country, name="food_distributor_country", curie=MIFC.curie('food_distributor_country'),
                   model_uri=MIFC.food_distributor_country, domain=None, range=Optional[str])

slots.food_distributor_country_subdivision = Slot(uri=MIFC.food_distributor_country_subdivision, name="food_distributor_country_subdivision", curie=MIFC.curie('food_distributor_country_subdivision'),
                   model_uri=MIFC.food_distributor_country_subdivision, domain=None, range=Optional[str])

slots.food_expiration_date = Slot(uri=MIFC.food_expiration_date, name="food_expiration_date", curie=MIFC.curie('food_expiration_date'),
                   model_uri=MIFC.food_expiration_date, domain=None, range=Optional[str])

slots.food_category_label = Slot(uri=MIFC.food_category_label, name="food_category_label", curie=MIFC.curie('food_category_label'),
                   model_uri=MIFC.food_category_label, domain=None, range=Optional[str])

slots.food_additional_types = Slot(uri=MIFC.food_additional_types, name="food_additional_types", curie=MIFC.curie('food_additional_types'),
                   model_uri=MIFC.food_additional_types, domain=None, range=Optional[str])

slots.component_sample_id = Slot(uri=MIFC.component_sample_id, name="component_sample_id", curie=MIFC.curie('component_sample_id'),
                   model_uri=MIFC.component_sample_id, domain=None, range=str)

slots.component_type = Slot(uri=MIFC.component_type, name="component_type", curie=MIFC.curie('component_type'),
                   model_uri=MIFC.component_type, domain=None, range=Optional[str])

slots.component_type_label = Slot(uri=MIFC.component_type_label, name="component_type_label", curie=MIFC.curie('component_type_label'),
                   model_uri=MIFC.component_type_label, domain=None, range=Optional[str])

slots.component_recorded_value = Slot(uri=MIFC.component_recorded_value, name="component_recorded_value", curie=MIFC.curie('component_recorded_value'),
                   model_uri=MIFC.component_recorded_value, domain=None, range=Optional[float])

slots.component_measurement_unit = Slot(uri=MIFC.component_measurement_unit, name="component_measurement_unit", curie=MIFC.curie('component_measurement_unit'),
                   model_uri=MIFC.component_measurement_unit, domain=None, range=Optional[str])

slots.component_data_points_number = Slot(uri=MIFC.component_data_points_number, name="component_data_points_number", curie=MIFC.curie('component_data_points_number'),
                   model_uri=MIFC.component_data_points_number, domain=None, range=Optional[int])

slots.component_record_date = Slot(uri=MIFC.component_record_date, name="component_record_date", curie=MIFC.curie('component_record_date'),
                   model_uri=MIFC.component_record_date, domain=None, range=Optional[str])

slots.component_analysis_date = Slot(uri=MIFC.component_analysis_date, name="component_analysis_date", curie=MIFC.curie('component_analysis_date'),
                   model_uri=MIFC.component_analysis_date, domain=None, range=Optional[str])

slots.component_comment = Slot(uri=MIFC.component_comment, name="component_comment", curie=MIFC.curie('component_comment'),
                   model_uri=MIFC.component_comment, domain=None, range=Optional[str])

slots.component_derivation_type = Slot(uri=MIFC.component_derivation_type, name="component_derivation_type", curie=MIFC.curie('component_derivation_type'),
                   model_uri=MIFC.component_derivation_type, domain=None, range=Optional[str])

slots.component_limit_of_quantitation = Slot(uri=MIFC.component_limit_of_quantitation, name="component_limit_of_quantitation", curie=MIFC.curie('component_limit_of_quantitation'),
                   model_uri=MIFC.component_limit_of_quantitation, domain=None, range=Optional[str])

slots.laboratory_sample_aggregation_minimum_measured_compound_value = Slot(uri=MIFC.laboratory_sample_aggregation_minimum_measured_compound_value, name="laboratory_sample_aggregation_minimum_measured_compound_value", curie=MIFC.curie('laboratory_sample_aggregation_minimum_measured_compound_value'),
                   model_uri=MIFC.laboratory_sample_aggregation_minimum_measured_compound_value, domain=None, range=Optional[float])

slots.laboratory_sample_aggregation_maximum_measured_compound_value = Slot(uri=MIFC.laboratory_sample_aggregation_maximum_measured_compound_value, name="laboratory_sample_aggregation_maximum_measured_compound_value", curie=MIFC.curie('laboratory_sample_aggregation_maximum_measured_compound_value'),
                   model_uri=MIFC.laboratory_sample_aggregation_maximum_measured_compound_value, domain=None, range=Optional[float])

slots.laboratory_sample_aggregation_median_measured_compound_value = Slot(uri=MIFC.laboratory_sample_aggregation_median_measured_compound_value, name="laboratory_sample_aggregation_median_measured_compound_value", curie=MIFC.curie('laboratory_sample_aggregation_median_measured_compound_value'),
                   model_uri=MIFC.laboratory_sample_aggregation_median_measured_compound_value, domain=None, range=Optional[float])

slots.laboratory_sample_aggregation_measured_compound_standard_deviation = Slot(uri=MIFC.laboratory_sample_aggregation_measured_compound_standard_deviation, name="laboratory_sample_aggregation_measured_compound_standard_deviation", curie=MIFC.curie('laboratory_sample_aggregation_measured_compound_standard_deviation'),
                   model_uri=MIFC.laboratory_sample_aggregation_measured_compound_standard_deviation, domain=None, range=Optional[float])

slots.compound_analytical_measurement_protocol_doi = Slot(uri=MIFC.compound_analytical_measurement_protocol_doi, name="compound_analytical_measurement_protocol_doi", curie=MIFC.curie('compound_analytical_measurement_protocol_doi'),
                   model_uri=MIFC.compound_analytical_measurement_protocol_doi, domain=None, range=Optional[str])

slots.compound_analytical_measurement_method = Slot(uri=MIFC.compound_analytical_measurement_method, name="compound_analytical_measurement_method", curie=MIFC.curie('compound_analytical_measurement_method'),
                   model_uri=MIFC.compound_analytical_measurement_method, domain=None, range=Optional[Union[str, "AnalyticalMeasurementMethod"]])

slots.compound_analytical_laboratory_name = Slot(uri=MIFC.compound_analytical_laboratory_name, name="compound_analytical_laboratory_name", curie=MIFC.curie('compound_analytical_laboratory_name'),
                   model_uri=MIFC.compound_analytical_laboratory_name, domain=None, range=Optional[str])

slots.component_quality_control_remeasurement = Slot(uri=MIFC.component_quality_control_remeasurement, name="component_quality_control_remeasurement", curie=MIFC.curie('component_quality_control_remeasurement'),
                   model_uri=MIFC.component_quality_control_remeasurement, domain=None, range=Optional[Union[bool, Bool]])

slots.dataset_label = Slot(uri=MIFC.dataset_label, name="dataset_label", curie=MIFC.curie('dataset_label'),
                   model_uri=MIFC.dataset_label, domain=None, range=Optional[str])

slots.mifc_version_tag = Slot(uri=MIFC.mifc_version_tag, name="mifc_version_tag", curie=MIFC.curie('mifc_version_tag'),
                   model_uri=MIFC.mifc_version_tag, domain=None, range=Optional[str])

slots.contributor_orcid = Slot(uri=MIFC.contributor_orcid, name="contributor_orcid", curie=MIFC.curie('contributor_orcid'),
                   model_uri=MIFC.contributor_orcid, domain=None, range=Optional[str])

slots.organization_name = Slot(uri=MIFC.organization_name, name="organization_name", curie=MIFC.curie('organization_name'),
                   model_uri=MIFC.organization_name, domain=None, range=Optional[str])

slots.food_laboratory_sample_id = Slot(uri=MIFC.food_laboratory_sample_id, name="food_laboratory_sample_id", curie=MIFC.curie('food_laboratory_sample_id'),
                   model_uri=MIFC.food_laboratory_sample_id, domain=None, range=Optional[str])

slots.food_laboratory_sample_aliquot_id = Slot(uri=MIFC.food_laboratory_sample_aliquot_id, name="food_laboratory_sample_aliquot_id", curie=MIFC.curie('food_laboratory_sample_aliquot_id'),
                   model_uri=MIFC.food_laboratory_sample_aliquot_id, domain=None, range=Optional[str])

slots.food_laboratory_sample_batch_id = Slot(uri=MIFC.food_laboratory_sample_batch_id, name="food_laboratory_sample_batch_id", curie=MIFC.curie('food_laboratory_sample_batch_id'),
                   model_uri=MIFC.food_laboratory_sample_batch_id, domain=None, range=Optional[str])

slots.container__foods = Slot(uri=MIFC.foods, name="container__foods", curie=MIFC.curie('foods'),
                   model_uri=MIFC.container__foods, domain=None, range=Optional[Union[Dict[Union[str, FoodFoodSampleId], Union[dict, Food]], List[Union[dict, Food]]]])

slots.container__components = Slot(uri=MIFC.components, name="container__components", curie=MIFC.curie('components'),
                   model_uri=MIFC.container__components, domain=None, range=Optional[Union[Union[dict, Component], List[Union[dict, Component]]]])

slots.container__provenances = Slot(uri=MIFC.provenances, name="container__provenances", curie=MIFC.curie('provenances'),
                   model_uri=MIFC.container__provenances, domain=None, range=Optional[Union[Union[dict, Provenance], List[Union[dict, Provenance]]]])