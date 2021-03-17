Highly Abstract
===============

## Modeling and playing with High Level Abstract Concepts (HLACs) evoked by images

This project aims to **investigate, model, and experiment with how HLACs** (such as violence, power, peace, or destruction) **are detected by humans and machines in images**. It specifically focuses on the detection of such concepts in (visual) art images. Goals of this work include:
* Identification of a set of HLACs that is used to tag the non-concrete content of (art) images.
* Creation of a dataset of images and HLACs evoked by them.
* For (art) images tagged by experts with the same HLACs, identification of common features.
* Automatic detection of highly abstract concepts in previously unseen (art) images.
* Automatic generation of new images that evoke specific highly abstract concepts.

The starting point is one of the richest datasets that include abstract concepts as tags for the content of visual artworks: the [metadata released by The Tate Collection](https://github.com/tategallery/collection) on Github in 2014. This dataset includes the metadata for around 70,000 artworks that [Tate](http://www.tate.org.uk/) owns or jointly owns with the [National Galleries of Scotland](http://www.nationalgalleries.org) as part of [ARTIST ROOMS](http://www.tate.org.uk/artist-rooms). To tag the content of the artworks in their collection, the Tate uses three levels (0, 1, and 2) of increasing specificity to provide a hierarchy of subject tags (for example; 0 religion and belief, 1 universal religious imagery, 2 blessing). 

In order to understand the breadth, abstraction level, and hierarchy of subject tags, I reconstructed the hierarchy of the [Tate subject data](https://github.com/tategallery/collection/tree/master/processed/subjects) by transforming it into a skos-based `RDF` file in Turtle `.ttl` format. [SKOS](https://www.w3.org/TR/skos-primer/#sechierarchy) was used as an initial step because of its simple way to assert that one concept is broader in meaning (i.e. more general) than another, with the skos:broader property. The skos:narrower property is used to assert the inverse, namely when one concept is narrower in meaning (i.e. more specific) than another. Additionally, I used the `Graphviz` module in order to visualize the hierchy. All code used to create the `.ttl` files as well as the graphviz style edges is available in `functions.py`.

Next steps include:
* Formalization of the namespace for the RDF resources create in the context of this project (potentially within ArCo).
* Selecting a set of HLACs to begin the study. 
* Collection of images of Tate artworks tagged with selected HLACs.
* Collection of images from other datasets, including the Catalogue of Cultural Heritage of the Italian Government, tagged with selected HLACs.


The use of Tate images in the context of this non-commercial, educational research falls within the within the [Tate Images Terms of use](https://www.tate.org.uk/about-us/policies-and-procedures/website-terms-use): "Website content that is Tate copyright may be reproduced for the non-commercial purposes of research, private study, criticism and review, or for limited circulation within an educational establishment (such as a school, college or university)."

