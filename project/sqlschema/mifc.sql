-- # Class: "NamedThing" Description: ""
--     * Slot: id Description: 
--     * Slot: laboratory_sample_id Description: A string denoting an identifier of a laboratory sample which was prepared from a food sample.
--     * Slot: laboratory_sample_aliquot_id Description: A string denoting an identifier of a unique aliquot of a laboratory sample which was prepared from a food sample.
--     * Slot: laboratory_sample_batch_id Description: A string denoting an identifier of a batch of laboratory samples analysed together.
-- # Class: "Food" Description: "Metadata about foods analyzed for components of nutritional interest."
--     * Slot: food_id Description: A string denoting the primary identifier for a sample of the class Food. Note that food_id should be unique in a given dataset and should be used to relate Food and Component records via component_id from the Component class.
--     * Slot: food_primary_type Description: A controlled vocabulary term representing the primary food material which was sampled.
--     * Slot: food_primary_type_label Description: A string denoting the label of a controlled vocabulary term representing the primary food material which was sampled.
--     * Slot: food_upc_code Description: An integer denoting a Universal Product Code (UPC) barcode of a food sample.
--     * Slot: food_preservation_state Description: An enumerated set of controlled vocabulary terms representing the preservation state(s) of a food sample (e.g., "raw").
--     * Slot: food_storage_temperature_state Description: An enumerated set of controlled vocabulary terms representing the qualitative temperature state at which a food sample was stored prior to acquisition (e.g., "Refrigerated").
--     * Slot: food_ripeness_state Description: An enumerated set of controlled vocabulary terms representing the qualitative freshness state of a food sample when prepared for analysis.
--     * Slot: food_cooking_method Description: An enumerated set of controlled vocabulary terms representing the any cooking method(s) applied to a food sample prior to analysis (e.g., "baked").
--     * Slot: food_acquisition_city Description: A string denoting the city in which a food sample was acquired.
--     * Slot: food_acquisition_country Description: A string denoting the country code from which a food sample was acquired.
--     * Slot: food_acquisition_country_subdivision Description: A string denoting the country subdivision from which a food sample was acquired (e.g., state or province).
--     * Slot: food_acquisition_date Description: A datetime value representing the date a food sample was acquired.
--     * Slot: food_acquisition_location_type Description: A string describing the type of location from which a food sample was acquired (e.g., a supermarket).
--     * Slot: food_acquisition_latitude Description: A float representing the latitude of the place from which the food sample was acquired.
--     * Slot: food_acquisition_longitude Description: A float representing the longitude of the place from which the food sample was acquired.
--     * Slot: food_acquisition_agent_name Description: A string denoting the name of the agent (person, device or other type of service) that acquired the food sample.
--     * Slot: food_acquisition_organization Description: A string denoting the name of the organization responsible for acquired the food sample.
--     * Slot: food_distributor_city Description: A string denoting the city of a distributor organization from which a food sample was acquired.
--     * Slot: food_distributor_country Description: A string denoting the country code of a distributor organization from which a food sample was acquired.
--     * Slot: food_distributor_country_subdivision Description: A string denoting the country subdivision of a distributor organization from which a food sample was acquired, (e.g., state or province).
--     * Slot: food_expiration_date Description: A datetime value representing the food expiration data as shown on the labeling information of the food sample.
--     * Slot: food_category_label Description: A string or controlled vocabulary denoting the label of the food group or category of the primary food material.
--     * Slot: food_additional_types Description: A list of controlled vocabulary denoting the label(s) of additional food types, not including the food_primary_type that are in a food sample.
--     * Slot: laboratory_sample_id Description: A string denoting an identifier of a laboratory sample which was prepared from a food sample.
--     * Slot: laboratory_sample_aliquot_id Description: A string denoting an identifier of a unique aliquot of a laboratory sample which was prepared from a food sample.
--     * Slot: laboratory_sample_batch_id Description: A string denoting an identifier of a batch of laboratory samples analysed together.
--     * Slot: Container_id Description: Autocreated FK slot
-- # Class: "Component" Description: "Metadata about components of nutritional interest measured from foods."
--     * Slot: id Description: 
--     * Slot: component_id Description: A string denoting the primary identifier for a sample of the class Component. Note that component_id does not need be unique in a given dataset and should be used to relate Food and Component records via food_id from the Food class.
--     * Slot: component_type Description: A controlled vocabulary term representing the type of component of nutritional interest analyzed from a food sample.
--     * Slot: component_type_label Description: A string denoting the label of a controlled vocabulary term representing an analyzed component_type from a food sample.
--     * Slot: component_recorded_value Description: A float representing a recorded value of a component of nutritional interest measured from a laboratory sample derived from a food sample.
--     * Slot: component_measurement_unit Description: A unit code representing the unit of measurement in which a component_recorded_value is measured.
--     * Slot: component_data_points_number Description: An integer representing the number of individual samples that comprise a component sample. 1 if an individual sample >1 if an aggregation of samples.
--     * Slot: component_record_date Description: A datetime value representing recorded date pertaining to an analyzed sample.
--     * Slot: component_analysis_date Description: A datetime value representing the date in which a component of nutritional interest was analyzed.
--     * Slot: component_comment Description: A comment relating to an analyzed component of nutritional interest.
--     * Slot: component_derivation_type Description: A controlled vocabulary term denoting how a component of nutritional interest was generated, (e.g., Analytical or Calculated).
--     * Slot: component_limit_of_quantitation Description: A string representing the lowest analyte concentration likely to be reliably distinguished from the Limit of Blank (LoB) and at which detection is feasible during the analysis of a component of nutritional interest.
--     * Slot: laboratory_sample_aggregation_minimum_measured_compound_value Description: A float representing the minimum measured compound value of an aggregation of samples.
--     * Slot: laboratory_sample_aggregation_maximum_measured_compound_value Description: A float representing the maximum measured compound value of an aggregation of samples.
--     * Slot: laboratory_sample_aggregation_median_measured_compound_value Description: A float representing the median measured compound value of an aggregation of samples.
--     * Slot: laboratory_sample_aggregation_measured_compound_standard_deviation Description: A float representing the standard deviation of a measured compound value of an aggregation of samples.
--     * Slot: compound_analytical_measurement_protocol_doi Description: A string denoting a digital object identifier link to a measurement protocol used to conduct an analytical analysis on a sample.
--     * Slot: compound_analytical_measurement_method Description: A controlled vocabulary term denoting the method used to conduct an analytical analysis on a sample, (e.g., HPLC).
--     * Slot: laboratory_conducting_analytical_analysis Description: A string denoting the name of a laboratory that conducted the analytical analysis of a measured_compound.
--     * Slot: component_quality_control_remeasurement Description: A boolean value denoting TRUE if a component_recorded_value was measured more than once for internal laboratory quality control purposes.
--     * Slot: laboratory_sample_id Description: A string denoting an identifier of a laboratory sample which was prepared from a food sample.
--     * Slot: laboratory_sample_aliquot_id Description: A string denoting an identifier of a unique aliquot of a laboratory sample which was prepared from a food sample.
--     * Slot: laboratory_sample_batch_id Description: A string denoting an identifier of a batch of laboratory samples analysed together.
--     * Slot: Container_id Description: Autocreated FK slot
-- # Class: "Provenance" Description: "Supplemental data about the provenance of a Food and Component dataset collection standardized using MIFC."
--     * Slot: id Description: 
--     * Slot: dataset_label Description: A string corresponding to the labeled name of dataset (e.g., "Standard Reference (SR) Legacy").
--     * Slot: mifc_version_tag Description: A string corresponding to a named MIFC release number (e.g., "v1.0.1").
--     * Slot: contributor_orcid Description: A string corresponding to a "|" delimited list of ORCIDs of people who contributed to a MIFC formatted dataset. See https://orcid.org/.
--     * Slot: organization_name Description: A string corresponding to a "|" delimited list of organizations who created or help to create to a MIFC formatted dataset. E.g., "USDA".
--     * Slot: laboratory_sample_id Description: A string denoting an identifier of a laboratory sample which was prepared from a food sample.
--     * Slot: laboratory_sample_aliquot_id Description: A string denoting an identifier of a unique aliquot of a laboratory sample which was prepared from a food sample.
--     * Slot: laboratory_sample_batch_id Description: A string denoting an identifier of a batch of laboratory samples analysed together.
--     * Slot: Container_id Description: Autocreated FK slot
-- # Class: "Container" Description: ""
--     * Slot: id Description: 

CREATE TABLE "NamedThing" (
	id INTEGER NOT NULL, 
	laboratory_sample_id TEXT, 
	laboratory_sample_aliquot_id TEXT, 
	laboratory_sample_batch_id TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Container" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "Food" (
	food_id TEXT NOT NULL, 
	food_primary_type TEXT, 
	food_primary_type_label TEXT, 
	food_upc_code INTEGER, 
	food_preservation_state VARCHAR(25), 
	food_storage_temperature_state VARCHAR(16), 
	food_ripeness_state VARCHAR(13), 
	food_cooking_method VARCHAR(17), 
	food_acquisition_city TEXT, 
	food_acquisition_country TEXT, 
	food_acquisition_country_subdivision TEXT, 
	food_acquisition_date TEXT, 
	food_acquisition_location_type VARCHAR(13), 
	food_acquisition_latitude FLOAT, 
	food_acquisition_longitude FLOAT, 
	food_acquisition_agent_name TEXT, 
	food_acquisition_organization TEXT, 
	food_distributor_city TEXT, 
	food_distributor_country TEXT, 
	food_distributor_country_subdivision TEXT, 
	food_expiration_date TEXT, 
	food_category_label TEXT, 
	food_additional_types TEXT, 
	laboratory_sample_id TEXT, 
	laboratory_sample_aliquot_id TEXT, 
	laboratory_sample_batch_id TEXT, 
	"Container_id" INTEGER, 
	PRIMARY KEY (food_id), 
	FOREIGN KEY("Container_id") REFERENCES "Container" (id)
);
CREATE TABLE "Component" (
	id INTEGER NOT NULL, 
	component_id TEXT NOT NULL, 
	component_type TEXT, 
	component_type_label TEXT, 
	component_recorded_value FLOAT, 
	component_measurement_unit TEXT, 
	component_data_points_number INTEGER, 
	component_record_date TEXT, 
	component_analysis_date TEXT, 
	component_comment TEXT, 
	component_derivation_type TEXT, 
	component_limit_of_quantitation TEXT, 
	laboratory_sample_aggregation_minimum_measured_compound_value FLOAT, 
	laboratory_sample_aggregation_maximum_measured_compound_value FLOAT, 
	laboratory_sample_aggregation_median_measured_compound_value FLOAT, 
	laboratory_sample_aggregation_measured_compound_standard_deviation FLOAT, 
	compound_analytical_measurement_protocol_doi TEXT, 
	compound_analytical_measurement_method VARCHAR(12), 
	laboratory_conducting_analytical_analysis TEXT, 
	component_quality_control_remeasurement BOOLEAN, 
	laboratory_sample_id TEXT, 
	laboratory_sample_aliquot_id TEXT, 
	laboratory_sample_batch_id TEXT, 
	"Container_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("Container_id") REFERENCES "Container" (id)
);
CREATE TABLE "Provenance" (
	id INTEGER NOT NULL, 
	dataset_label TEXT, 
	mifc_version_tag TEXT, 
	contributor_orcid TEXT, 
	organization_name TEXT, 
	laboratory_sample_id TEXT, 
	laboratory_sample_aliquot_id TEXT, 
	laboratory_sample_batch_id TEXT, 
	"Container_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("Container_id") REFERENCES "Container" (id)
);