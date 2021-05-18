MUSCO - Multimodal Descriptions of Social Concepts
===============

## Automatic Modeling of (Highly Abstract) Social Concepts evoked by Art Images

This project aims to **investigate, model, and experiment with how and why social concepts** (such as *violence, power, peace*, or *destruction*) **are modeled and detected by humans and machines in images**. It specifically focuses on the detection of social concepts referring to non-physical objects in (visual) art images, as these concepts are powerful tools for visual data management, especially in the Cultural Heritage field (present in resources such Iconclass and Getty Vocabularies). The hypothesis underlying this research is that we can formulate a description of a social concept as a multimodal frame, starting from a set of observations (in this case, image annotations). We believe thaat even with no explicit definition of the concepts,  a “common sense” description can be (approximately) derived from observations of their use.

Goals of this work include:
* Identification of a set of social concepts that is consistently used to tag the non-concrete content of (art) images.
* Creation of a dataset of art images and social concepts evoked by them.
* Creation of an Social Concepts Knowledge Graph (KG).
* Identification of common features of art images tagged by experts with the same social concepts.
* Automatic detection of social concepts in previously unseen art images.
* Automatic generation of new art images that evoke specific social concepts.

The approach proposed is to automatically model social concepts based on extraction and integration of multimodal features. Specifically, on sensory-perceptual data, such as pervasive visual features of images which evoke them, along with distributional linguistic patterns of social concept usage. To do so, we have defined the **MUSCO (Multimodal Descriptions of Social Concepts) Ontology**, which uses the Descriptions and Situations (Gangemi & Mika 2003) pattern modularly. It considers the image annotation process a situation representing the state of affairs of all related data (actual multimedia data as well as metadata), whose descriptions give meaning to specific annotation structures and results. It also considers social concepts as entities defined in multimodal description frames. 

The starting point of this project is one of the richest datasets that include **social concepts referring to non-physical objects** as tags for the content of visual artworks: the [metadata released by The Tate Collection](https://github.com/tategallery/collection) on Github in 2014. This dataset includes the metadata for around 70,000 artworks that [Tate](http://www.tate.org.uk/) owns or jointly owns with the [National Galleries of Scotland](http://www.nationalgalleries.org) as part of [ARTIST ROOMS](http://www.tate.org.uk/artist-rooms). To tag the content of the artworks in their collection, the Tate uses a [subject taxonomy](https://github.com/tategallery/collection/tree/master/processed/subjects) with three levels (0, 1, and 2) of increasing specificity to provide a hierarchy of subject tags (for example; 0 religion and belief, 1 universal religious imagery, 2 blessing). 

This repository holds the `functions.py` file, which defines functions for 

* Preprocessing the Tate Gallery metadata as input source (`create_newdict()`, `get_topConcepts()`, and `get_parent_rels()`)
* Reconstruction and formalization of the the Tate subject taxonomy (`get_tatetaxonomy_ttl()`)
* Visualization of the Tate subject taxonomy, allowing manual inspection (`get_all_edges()`, and `get_gv_pdf()`)
* Identification of social concepts from the Tate taxonomy (`get_sc_dict()`, and `get_narrow_sc_dict()`)
* Formalization of taxonomic relations between social concepts (`get_sc_tate_taxonomy_ttl()`)
* Gathering specific artwork details relevant to the tasks proposed in this project (`get_artworks_filenames()`, `get_all_artworks_tags()`, and `get_all_artworks_details()`)
* Corpus creation: matching social concept to art images (`get_sc_artworks_dict()` and `get_match_details(input_sc)`)
* Co-occuring tag collection and analysis (`get_all_scs_tag_ids()`, `get_objects_and_actions_dict(input_sc)`, and `get_match_stats()`)
* Image dominant color analyses (`get_dom_colors()` and `get_avg_sc_contrast()`)

In order to understand the breadth, abstraction level, and hierarchy of subject tags, I reconstructed the hierarchy of the [Tate subject data](https://github.com/tategallery/collection/tree/master/processed/subjects) by transforming it into a `RDF` file in Turtle `.ttl` format with the MUSCO ontology. [SKOS](https://www.w3.org/TR/skos-primer/#sechierarchy) was used as an initial step because of its simple way to assert that one concept is broader in meaning (i.e. more general) than another, with the skos:broader property. Additionally, I used the `Graphviz` module in order to visualize the hierchy.

Next steps include:
* Automatic population of a KG with the extracted data
* Disambiguating the terms, expanding the terminology by leveraging lexical resources such as WordNet, VerbNet, and FrameNet, and studying the terms’ distributional linguistic features.
* MUSCO’s modular infrastructure allows expansion of types of integrated data (potentially including: other co-occurring social concepts, contrast measures, common shapes, repetition, and other visual patterns, other senses (e.g., sound), facial recognition analysis, distributional semantics information)
* Refine initial social concepts list, through alignment with the latest cognitive science research as well as through user-based studies.
* Enlarge and diversify art image corpus after a survey of additional catalogues and collections.
* Distinguishing artwork medium types

The use of Tate images in the context of this non-commercial, educational research project falls within the within the [Tate Images Terms of use](https://www.tate.org.uk/about-us/policies-and-procedures/website-terms-use): "Website content that is Tate copyright may be reproduced for the non-commercial purposes of research, private study, criticism and review, or for limited circulation within an educational establishment (such as a school, college or university)."
