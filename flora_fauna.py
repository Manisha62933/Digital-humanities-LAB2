"""
Bengali Literary Corpus: Flora and Fauna Extraction
Digital Humanities RAG Project

This file presents preliminary flora and fauna references
retrieved from three Bengali literary works:

1. Ichamati
2. Nilkantha Pakhir Khoje
3. Aranyak

The extraction preserves the source and chunk reference.
OCR-uncertain entries require verification against the
original literary text.
"""

import json
import os

EXTRACTED_ELEMENTS = [{'name': 'মাদারগাছ', 'category': 'Flora', 'source': 'Ichamati', 'chunk_id': 335, 'context': 'A tree mentioned in a childhood memory; its fruit is described as sweet.', 'verification': 'Needs OCR and source-text verification'}, {'name': 'আম', 'category': 'Flora', 'source': 'Ichamati', 'chunk_id': 335, 'context': 'Fruit mentioned in the passage.', 'verification': 'Candidate identified'}, {'name': 'বনকলমি ফুল', 'category': 'Flora', 'source': 'Ichamati', 'chunk_id': 366, 'context': 'Flowers growing near water in the bushes.', 'verification': 'Candidate identified'}, {'name': 'ঘাসবন', 'category': 'Flora', 'source': 'Ichamati', 'chunk_id': 366, 'context': 'Grassland mentioned in the passage.', 'verification': 'Candidate identified'}, {'name': 'বাঁশঝাড়', 'category': 'Flora', 'source': 'Ichamati', 'chunk_id': 366, 'context': 'A dense bamboo grove.', 'verification': 'Candidate identified'}, {'name': 'হিজল গাছ', 'category': 'Flora', 'source': 'Nilkantha_Pakhir_Khoje', 'chunk_id': 88, 'context': 'A hijal tree visible from a particular location.', 'verification': 'Candidate identified'}, {'name': 'বেতপাতা', 'category': 'Flora', 'source': 'Nilkantha_Pakhir_Khoje', 'chunk_id': 7, 'context': 'Leaves hanging in a room.', 'verification': 'Candidate identified'}, {'name': 'মটকিলা গাছ', 'category': 'Flora', 'source': 'Nilkantha_Pakhir_Khoje', 'chunk_id': 7, 'context': 'A branch placed at the doorway; OCR spelling needs checking.', 'verification': 'Needs OCR and source-text verification'}, {'name': 'বুনো তেউড়ি ফুল', 'category': 'Flora', 'source': 'Aranyak', 'chunk_id': 276, 'context': 'Wild flowers blooming in the forest.', 'verification': 'Candidate identified'}, {'name': 'ঘেঁটুবন', 'category': 'Flora', 'source': 'Ichamati', 'chunk_id': 420, 'context': 'Flowering vegetation in an open field.', 'verification': 'Needs OCR and source-text verification'}, {'name': 'অর্জুন', 'category': 'Flora', 'source': 'Aranyak', 'chunk_id': 151, 'context': 'Plant name appearing in a forest description.', 'verification': 'Needs OCR and source-text verification'}, {'name': 'পিয়াল', 'category': 'Flora', 'source': 'Aranyak', 'chunk_id': 151, 'context': 'Plant name appearing in a forest description.', 'verification': 'Needs OCR and source-text verification'}, {'name': 'বাঘ', 'category': 'Fauna', 'source': 'Ichamati', 'chunk_id': 335, 'context': 'A wild animal mentioned in a forest.', 'verification': 'Candidate identified'}, {'name': 'সাপ', 'category': 'Fauna', 'source': 'Ichamati', 'chunk_id': 335, 'context': 'A wild animal mentioned in a forest.', 'verification': 'Candidate identified'}, {'name': 'বসন্তবৌরি পাখি', 'category': 'Fauna', 'source': 'Ichamati', 'chunk_id': 366, 'context': 'A bird described by its yellow-coloured body.', 'verification': 'OCR spelling requires verification'}, {'name': 'পাখি', 'category': 'Fauna', 'source': 'Ichamati', 'chunk_id': 309, 'context': 'A bird shown to a child.', 'verification': 'Generic animal reference'}, {'name': 'প্রজাপতি', 'category': 'Fauna', 'source': 'Nilkantha_Pakhir_Khoje', 'chunk_id': 244, 'context': 'A butterfly caught for a character.', 'verification': 'Candidate identified'}, {'name': 'শিঙি মাছ', 'category': 'Fauna', 'source': 'Nilkantha_Pakhir_Khoje', 'chunk_id': 244, 'context': 'A fish being prepared for cooking.', 'verification': 'Candidate identified'}, {'name': 'মাছ', 'category': 'Fauna', 'source': 'Ichamati', 'chunk_id': 461, 'context': 'Fish and fishing practices are discussed.', 'verification': 'Generic animal reference'}, {'name': 'হরিণ', 'category': 'Fauna', 'source': 'Aranyak', 'chunk_id': 198, 'context': 'A deer mentioned in a passage containing bird references.', 'verification': 'Candidate identified'}, {'name': 'ভালুক', 'category': 'Fauna', 'source': 'Aranyak', 'chunk_id': 151, 'context': 'A wild animal mentioned in a forest description.', 'verification': 'Candidate identified'}, {'name': 'শ্যামা', 'category': 'Fauna', 'source': 'Aranyak', 'chunk_id': 198, 'context': 'Bird name appearing in a list of birds.', 'verification': 'OCR spelling requires verification'}, {'name': 'শালিক', 'category': 'Fauna', 'source': 'Aranyak', 'chunk_id': 198, 'context': 'Bird name appearing in a list of birds.', 'verification': 'Candidate identified'}, {'name': 'ঘুঘু', 'category': 'Fauna', 'source': 'Aranyak', 'chunk_id': 198, 'context': 'Bird name appearing in a list of birds.', 'verification': 'Candidate identified'}, {'name': 'হরিয়াল', 'category': 'Fauna', 'source': 'Aranyak', 'chunk_id': 198, 'context': 'Bird name appearing in a list of birds.', 'verification': 'Candidate identified'}, {'name': 'চিল', 'category': 'Fauna', 'source': 'Aranyak', 'chunk_id': 198, 'context': 'Bird name appearing in a list of birds.', 'verification': 'Candidate identified'}, {'name': 'বক', 'category': 'Fauna', 'source': 'Aranyak', 'chunk_id': 198, 'context': 'Bird name appearing in a list of birds.', 'verification': 'Candidate identified'}, {'name': 'রাঙাহাঁস', 'category': 'Fauna', 'source': 'Aranyak', 'chunk_id': 198, 'context': 'Bird name appearing in a list of birds.', 'verification': 'OCR spelling requires verification'}]

def display_elements(category=None):
    """Display extracted flora and fauna references."""

    for item in EXTRACTED_ELEMENTS:
        if category is None or item["category"].lower() == category.lower():
            print(
                item["name"],
                "|", item["category"],
                "|", item["source"],
                "| Chunk:", item["chunk_id"],
                "|", item["verification"]
            )


def save_results(filename="bengali_flora_fauna.json"):
    """Save the extraction as a JSON file."""

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(
            EXTRACTED_ELEMENTS,
            file,
            ensure_ascii=False,
            indent=4
        )

    print("Results saved to:", filename)


if __name__ == "__main__":
    print("BENGALI FLORA AND FAUNA EXTRACTION")
    print("=" * 50)

    print("\\nFLORA")
    display_elements("Flora")

    print("\\nFAUNA")
    display_elements("Fauna")

    print("\\nTotal extracted references:", len(EXTRACTED_ELEMENTS))
